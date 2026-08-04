<h1 id="로컬-개발-환경에서-모바일-ngrok-hmr-붙여서-개발하기">로컬 개발 환경에서 모바일 ngrok, HMR 붙여서 개발하기</h1>
<p>회사 노트북(Windows 11 + WSL2 Ubuntu)에서 Next.js 프로젝트를 돌리다가, 아이폰 Safari로 실시간 화면을 확인하면서 개발해야 하는 상황이 생겼다. 서브 노트북에서 SSH로 붙어 작업할 때도 있고, 반응형 레이아웃을 실기기에서 바로 확인하고 싶을 때도 있었기 때문이다.</p>
<p>처음에는 단순하게 생각했다. <code>next dev -H 0.0.0.0</code>으로 띄우고 같은 Wi-Fi에 물린 아이폰에서 내부 IP로 접속하면 되겠지, 라고. 실제로는 그렇게 간단하지 않았다.</p>
<h2 id="1-왜-내부-ip로는-접속이-안-될까">1. 왜 내부 IP로는 접속이 안 될까</h2>
<p>서버를 띄우면 터미널에 이렇게 뜬다.</p>
<p>bash</p>
<pre><code class="language-bash">▲ Next.js
- Local:   http://localhost:3000
- Network: http://0.0.0.0:3000</code></pre>
<p><code>0.0.0.0:3000</code>을 보고 &quot;아, 이 주소로 접속하면 되는구나&quot;라고 착각했는데, 이건 실제 접속 주소가 아니라 <strong>모든 인터페이스의 요청을 받겠다는 선언</strong>일 뿐이었다. 그래서 Windows의 내부 IP(<code>192.168.0.15:3000</code>)로 아이폰에서 접속을 시도했지만 계속 실패했다.</p>
<h3 id="첫-번째-문제-원인이-한두-개가-아니었다">첫 번째 문제: 원인이 한두 개가 아니었다</h3>
<p>막히는 지점을 하나씩 따라가보니 원인이 겹쳐 있었다.</p>
<ol>
<li>WSL2는 Windows 호스트와 분리된 Hyper-V 가상 머신이라 네트워크 경로가 한 겹 더 있다.</li>
<li>사내 Wi-Fi에 AP Isolation이 걸려 있어서 같은 네트워크의 기기끼리 통신 자체가 차단된다.</li>
<li>Windows 방화벽 인바운드 규칙이 3000번 포트를 막고 있다.</li>
</ol>
<p>IP 대역을 맞추고 방화벽 규칙을 하나씩 뚫는 방법도 있었지만, 어차피 카페나 외부 Wi-Fi에서도 똑같은 문제를 반복해서 겪을 게 뻔했다. 그래서 방향을 아예 바꿔서 <strong><code>ngrok</code> 터널링</strong>으로 우회하기로 했다. IP나 방화벽 설정에 의존하지 않고 어디서든 접속되는 URL을 하나 만드는 쪽이 훨씬 마음이 편했다.</p>
<h2 id="2-wsl2-안에-ngrok-설치하기">2. WSL2 안에 ngrok 설치하기</h2>
<p>여기서 한 가지 정해둔 원칙은, ngrok을 <strong>Windows 호스트가 아니라 WSL2(Ubuntu) 안에</strong> 직접 설치한다는 것이었다. 어차피 Next.js 서버도 WSL2 안에서 돌고 있으니 같은 위치에서 터널을 열어야 경로가 단순해진다.</p>
<p>bash</p>
<pre><code class="language-bash">curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc &gt;/dev/null
echo &quot;deb https://ngrok-agent.s3.amazonaws.com buster main&quot; | sudo tee /etc/apt/sources.list.d/ngrok.list
sudo apt update
sudo apt install ngrok</code></pre>
<p>ngrok 공식 사이트에서 회원가입하고 대시보드에서 Authtoken을 복사한 뒤, WSL2 터미널에 최초 1회 등록해준다.</p>
<p>bash</p>
<pre><code class="language-bash">ngrok config add-authtoken &lt;YOUR_NGROK_AUTHTOKEN&gt;</code></pre>
<p>여기까지는 순조로웠다. 문제는 다음 단계에서 터졌다.</p>
<h2 id="3-화면은-뜨는데-코드를-고쳐도-반영이-안-된다">3. 화면은 뜨는데 코드를 고쳐도 반영이 안 된다</h2>
<p>ngrok으로 외부 도메인(<code>https://xxxx.ngrok-free.dev</code>)을 열어서 아이폰으로 접속하니 화면 자체는 잘 나왔다. 그런데 컴포넌트나 스타일을 고쳐서 저장해도 아이폰 화면이 그대로였다. 수동으로 새로고침을 해야만 반영이 됐다.</p>
<h3 id="두-번째-문제-hmr-웹소켓이-조용히-죽어-있었다">두 번째 문제: HMR 웹소켓이 조용히 죽어 있었다</h3>
<p>아이폰 Safari 개발자 콘솔을 열어보니 이런 에러가 찍혀 있었다.</p>
<p>text</p>
<pre><code class="language-text">web-socket.ts:50 WebSocket connection to 'wss://xxxx.ngrok-free.dev/_next/webpack-hmr?id=...' failed:</code></pre>
<p>원인을 찾아보니, Next.js 15+ 최신 버전부터 보안 정책이 강화되면서 <code>localhost</code>가 아닌 외부 도메인에서 들어오는 HMR 웹소켓(<code>wss://.../_next/webpack-hmr</code>) 연결을 기본적으로 막아버린다는 걸 알게 됐다. ngrok 터널 자체는 문제가 없었고, Next.js가 &quot;낯선 도메인에서 온 웹소켓&quot;을 신뢰하지 않은 것이었다.</p>
<h3 id="해결책-nextconfigts에-alloweddevorigins-추가">해결책: <code>next.config.ts</code>에 <code>allowedDevOrigins</code> 추가</h3>
<p>허용할 도메인 패턴을 최상위 설정에 명시하면 된다.</p>
<p>typescript</p>
<pre><code class="language-typescript">// next.config.ts
import type { NextConfig } from &quot;next&quot;;

const nextConfig: NextConfig = {
  reactCompiler: true,

  // 💡 ngrok 외부 도메인의 HMR/Fast Refresh 웹소켓 접속 허용
  allowedDevOrigins: [
    &quot;*.ngrok-free.app&quot;,
    &quot;*.ngrok-free.dev&quot;,
    &quot;localhost:3000&quot;,
  ],

  experimental: {
    viewTransition: true,
  },
};

export default nextConfig;</code></pre>
<p>이걸 처음 <code>experimental</code> 객체 안에 넣었다가 TypeScript 타입 에러(TS2353)를 만났다. <code>allowedDevOrigins</code>는 실험적 옵션이 아니라 <strong><code>NextConfig</code>의 최상위 속성</strong>으로 옮겨야 인식됐다. 이름만 보면 experimental에 있을 것 같아서 여기서 시간을 좀 썼다.</p>
<h2 id="4-실제로-붙여서-확인하기">4. 실제로 붙여서 확인하기</h2>
<p>설정을 고치고 나서 순서대로 다시 실행해봤다.</p>
<p><strong>Step 1. WSL2에서 Next.js 서버 실행</strong></p>
<p>bash</p>
<pre><code class="language-bash">pnpm dev</code></pre>
<p><strong>Step 2. WSL2 터미널 하나를 더 열어서 ngrok 실행</strong></p>
<p>bash</p>
<pre><code class="language-bash">ngrok http 3000 --host-header=rewrite</code></pre>
<p>text</p>
<pre><code class="language-text">Session Status        online
Forwarding            https://fling-android-appear.ngrok-free.dev -&gt; http://localhost:3000</code></pre>
<p><strong>Step 3. 아이폰 Safari로 접속</strong></p>
<p>출력된 ngrok URL을 아이폰 Safari에 입력하고, 최초 접속시 뜨는 안내 페이지에서 [Visit Site]를 눌러줬다. 그다음 VS Code에서 컴포넌트를 하나 고쳐서 저장했는데, <strong>수동 새로고침 없이 아이폰 화면이 바로 바뀌는 걸</strong> 확인했다. 이 순간이 제일 반가웠다.</p>
<h2 id="삽질하면서-배운-점">삽질하면서 배운 점</h2>
<p><strong><code>0.0.0.0</code>은 접속 주소가 아니라 대기 상태 표시다</strong> 처음에 이걸 실제 IP처럼 취급해서 시간을 버렸다. 저 값 자체로 접속을 시도하는 게 아니라, 서버가 모든 인터페이스를 듣고 있다는 뜻으로만 이해하면 된다.</p>
<p><strong>네트워크 우회보다 터널링이 더 오래 간다</strong> 방화벽 규칙이나 Wi-Fi AP Isolation은 장소가 바뀔 때마다 다시 부딪힌다. ngrok으로 한 번 세팅해두면 사내망이든 카페든 신경 쓸 일이 없어졌다.</p>
<p><strong>같은 문제라도 레이어가 다를 수 있다</strong> 접속 자체가 안 되는 문제(네트워크)와, 접속은 되는데 HMR만 안 되는 문제(Next.js 보안 정책)는 원인이 완전히 달랐다. 화면이 뜬다고 안심하지 않고 콘솔 로그를 먼저 확인한 게 원인을 좁히는 데 도움이 됐다.</p>
<p><strong>설정 옵션의 &quot;위치&quot;도 스펙의 일부다</strong> <code>allowedDevOrigins</code>처럼 이름만 봐서는 실험적 기능 같아 보이는 옵션도, 실제로는 최상위 속성으로 옮겨야 하는 경우가 있다. 공식 문서나 타입 정의를 한 번 더 확인하는 습관이 필요하다는 걸 느꼈다.</p>
<h2 id="마무리">마무리</h2>
<p>정리하면 핵심은 두 가지였다.</p>
<ol>
<li>ngrok을 WSL2 내부에서 직접 실행할 것</li>
<li><code>next.config.ts</code> 최상위에 <code>allowedDevOrigins</code>를 정의할 것</li>
</ol>
<p>이 두 가지만 기억해두면, 이후로는 어떤 네트워크 환경에서도 아이폰으로 실시간 HMR을 확인하면서 개발할 수 있다. 다음에 비슷한 상황이 오면 이번처럼 헤매지 않고 바로 적용할 수 있을 것 같다.</p>
<hr />