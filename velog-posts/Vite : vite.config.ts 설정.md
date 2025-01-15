<hr />

<p>기존에는 vue.config.js 에서 CommonJS 방식으로 설정을 배웠고 해왔다.</p>
<p><code>vite</code>를 사용해보고자 사용하는데 ESmodule 방식으로 설정을 하는데 좀 어려웠다</p>
<h2 id="기본-세팅-viteconfigts-파일">기본 세팅 vite.config.ts 파일</h2>
<pre><code class="language-ts">import react from '@vitejs/plugin-react'
import { defineConfig } from 'vite'

// https://vite.dev/config/
export default defineConfig({
    plugins: [react()],
})</code></pre>
<p>여기에서 나는 <code>resolve alias</code> 를 설정하고 <code>server proxy</code>를 환경벌로 설정하고 싶었다.</p>
<p>우선 환경별로 설정하기전 <code>dotenv</code> 라이브러리를 설치한다.</p>
<hr />

<p><a href="https://ko.vite.dev/guide/env-and-mode" rel="noopener noreferrer" target="_blank">VITE 환경변수 - 공식문서</a></p>
<hr />

<p>VITE 환경변수 - 공식문서 일부</p>
<p>.env 파일들</p>
<p>Vite는 dotenv를 이용해 환경 변수가 저장된 디렉터리 내 아래의 파일에서 환경 변수를 가져옵니다.</p>
<pre><code>.env                # 모든 상황에서 사용될 환경 변수
.env.local          # 모든 상황에서 사용되나, 로컬 개발 환경에서만 사용될(Git에 의해 무시될) 환경 변수
.env.[mode]         # 특정 모드에서만 사용될 환경 변수
.env.[mode].local   # 특정 모드에서만 사용되나, 로컬 개발 환경에서만 사용될(Git에 의해 무시될) 환경 변수</code></pre><hr />

<h2 id="dotenv-사용하여-환경변수-설정">dotenv 사용하여 환경변수 설정</h2>
<h3 id="1-dotenv-설치">1. dotenv 설치</h3>
<blockquote>
<p><code>npm i dotenv</code></p>
</blockquote>
<hr />

<h3 id="2-환경-변수-파일-생성">2. 환경 변수 파일 생성</h3>
<p>루트 디렉토리에 <code>$ .env.[환경명]</code> ex ) <code>.env.dev</code> , <code>.env.prd</code> 을 생성한다.</p>
<hr />

<h3 id="3-env환경명-파일-환경-변수-설정">3. .env.[환경명] 파일 환경 변수 설정</h3>
<p>VITE_APP_ENVIRONMENT=DEV
VITE_APP_SERVER=<a href="https://abc.com">https://abc.com</a></p>
<hr />

<h3 id="🕵️-참고로-vite에서-접근-가능한-환경-변수는-일반-환경-변수와-구분을-위해-vite_-라는-접두사를-붙여-나타낸다">🕵️ 참고로, Vite에서 접근 가능한 환경 변수는 일반 환경 변수와 구분을 위해 VITE_ 라는 접두사를 붙여 나타낸다.</h3>
<blockquote>
<p>ex ) VITE_APP_ENVIRONMENT=DEV</p>
</blockquote>
<hr />

<h2 id="packagejson-에서-모드-설정">package.json 에서 모드 설정</h2>
<h3 id="1-packagejson-에서-scripts-에-실행할-환경을-설정한다">1. package.json 에서 scripts 에 실행할 환경을 설정한다</h3>
<p>ex ) npm run <code>실행명(start-dev, dev)</code> </p>
<p>그리고 "vite <code>--mode</code> <code>dev</code>" 를 적어준다.</p>
<p>local일 경우 --mode local 은 viet에서 <code>.local</code> 접미사를 가진 환경 파일을 특별하게 처리를 한다고 한다.</p>
<hr />

<h3 id="🕵️---mode-local을-쓰면">🕵️ --mode local을 쓰면</h3>
<blockquote>
<p>⚠️ error when starting dev server: Error: "local" cannot be used as a mode name because it conflicts with the .local postfix for .env files. at loadEnv</p>
</blockquote>
<p>Vite는 <code>.env.[mode]</code> 형식의 파일을 로드할 때, <code>.env.local</code> 파일을 항상 특별히 처리한다고 한다. local을 모드 이름으로 지정하면 <code>.local</code> 접미사와 충돌하여 이와 같은 에러가 발생한다.</p>
<p>음 .. 웬만하면 local 보다는 다른명으로 하는게 낫겠다.</p>
<hr />

<pre><code class="language-js">"scripts": {
    "start-dev": "vite --mode dev",
    "start-local": "vite --mode 🔴mylocal 또는 test 등등",
    "build": "tsc -b &amp;&amp; vite build",
    "lint": "eslint .",
    "preview": "vite preview"
  },</code></pre>
<h2 id="vueconfigts-설정">vue.config.ts 설정</h2>
<pre><code class="language-ts">import react from '@vitejs/plugin-react'
import { defineConfig } from 'vite'

// https://vite.dev/config/
export default defineConfig({
    plugins: [react()],
})</code></pre>
<p>위 기본세팅에서 이제 설정한 환경파일과 환경변수를 server proxy 설정을 한다.</p>
<h3 id="1-export-default-defineconfig-에-매개변수-사용">1. export default defineConfig 에 매개변수 사용</h3>
<p>package.json 에서 --mode 를 설정했었다. </p>
<p>해당 모드를 동적으로 defineConfig에서 설정하기 위해 매개변수를 받아오는 코드로 바꾼다.</p>
<pre><code class="language-js">// 변경전
export default defineConfig({
    plugins: [react()],
})

// 변경후
export default defineConfig(({ mode }) =&gt; {
    return {
        plugins: [react()]
    }
})</code></pre>
<p>Vite는 해당 모드를 defineConfig 함수의 매개변수로 전달한다. 이를 통해 Vite 설정 파일에서 모드에 따라 다른 설정을 적용할 수 있다.</p>
<hr />

<h3 id="🕵️-packagejson-에서-설정한---mode-dev-매개변수로-mode를-전달받는-형태로-만들어-준다">🕵️ <code>package.json</code> 에서 설정한 <code>--mode dev</code> 매개변수로 mode를 전달받는 형태로 만들어 준다.</h3>
<hr />

<h3 id="2-해당-mode를-동적으로-전달받아-루트디렉토리에-있는-환경파일-경로-변수-생성">2. 해당 mode를 동적으로 전달받아 루트디렉토리에 있는 환경파일 경로 변수 생성</h3>
<pre><code class="language-ts">export default defineConfig(({ mode }) =&gt; {
  🟢const envPath = path.resolve(new URL(import.meta.url).pathname, `.env.${mode}`)
    •••••

    return {
        •••••

        •••••
    }
    •••••
})</code></pre>
<p><code>envPath</code> 변수를 생성한다. <code>defineConfig</code>에서 전달받은 매개변수 <code>mode</code>를 동적으로 받아 루트디렉토리에 있는 환경파일들의 파일경로를 담는다.</p>
<h3 id="3-dotenv-환경-변수-파일-로드">3. dotenv 환경 변수 파일 로드</h3>
<pre><code class="language-ts">export default defineConfig(({ mode }) =&gt; {
   const envPath = path.resolve(new URL(import.meta.url).pathname, `.env.${mode}`)
   🟢dotenv.config({ path: envPath })
    •••••

    return {
        •••••

        •••••
    }
    •••••
})</code></pre>
<p><code>dotenv</code> 패키지를 사용하여 지정된 경로에 있는 환경 변수 파일을 로드하는 기능을 한다. 이 코드를 통해 환경 변수 파일에 정의된 변수들을 process.env에 설정할 수 있다.</p>
<h3 id="4-vite-loadenv-함수를-사용하여-환경-변수를-로드">4. vite loadEnv 함수를 사용하여 환경 변수를 로드</h3>
<pre><code class="language-ts">import { defineConfig, 🟢loadEnv } from 'vite'

export default defineConfig(({ mode }) =&gt; {
  const envPath = path.resolve(new URL(import.meta.url).pathname, `.env.${mode}`)
  dotenv.config({ path: envPath })
  🟢const env = loadEnv(mode, process.cwd(), '')    
    •••••

    return {
        •••••

        •••••
    }
    •••••
})</code></pre>
<hr />

<blockquote>
<p><span style="font-size: 25px;">loadEnv 함수</span></p>
</blockquote>
<p><a href="https://vite.dev/guide/api-javascript.html#loadenv">VITE loadEnv() 함수 문서</a></p>
<pre><code class="language-ts">function loadEnv(
  mode: string,
  envDir: string,
  prefixes: string | string[] = 'VITE_',
): Record&lt;string, string&gt;</code></pre>
<p>관련: <code>.env파일</code></p>
<p>Vite에서는 <code>envDir(환경 파일 디렉터리)</code> 안에 있는 <code>.env</code> 파일들을 로드한다. 이 때, 기본적으로 <code>VITE_</code>로 시작하는 환경 변수만 로드된다.</p>
<hr />

<p>⚠️ 단, 이 동작은 설정에서 prefixes 값을 변경하면 수정할 수 있다.</p>
<hr />

<p>Vite는 envDir 디렉터리(기본값: 프로젝트 루트)에 있는 .env 파일들을 읽는다.</p>
<p>환경 변수 이름이 VITE_로 시작해야 Vite가 이를 인식하고 사용할 수 있다.</p>
<hr />

<pre><code>🟢사용가능
VITE_API_URL=https://example.com
VITE_APP_NAME=MyApp

위 변수들은 Vite에서 사용할 수 있다.</code></pre><hr />

<pre><code>🔴다른 접두사 사용

prefixes 설정을 수정하면 VITE_ 외의 접두사도 사용할 수 있다.

import { defineConfig } from 'vite';

export default defineConfig({
  envPrefix: ['VITE_', 'APP_']
});
이렇게 하면 APP_으로 시작하는 변수도 로드된다.</code></pre><p>ex ) <code>APP_SECRET_KEY=abcdef12345</code></p>
<hr />

<p><span style="font-size: 25px;">loadEnv 함수 코드</span></p>
<pre><code class="language-ts">📂 node_modules &gt; vite &gt; dist &gt; node &gt; index.d.ts 

declare function loadEnv(mode: string, envDir: string, prefixes?: string | string[]): Record&lt;string, string&gt;;</code></pre>
<p>1️⃣ <code>mode</code> : Vite가 실행되는 모드를 나타내는 문자열이다. 실행환경 ex ) dev, 
prod 등이 될 수 있다.</p>
<p>2️⃣ <code>envDir</code> : 환경 변수 파일이 위치한 디렉토리의 경로이다. 일반적으로 process.cwd()를 사용하여 현재 작업 디렉토리를 지정한다.</p>
<p>ex ) <code>C:\Users\...\...\...\vite.config.ts\.env.dev</code></p>
<p>3️⃣ <code>prefixes</code> : 로드할 환경 변수의 접두사를 지정하는 문자열 또는 문자열 배열다. 빈 문자열('')을 사용하면 모든 환경 변수를 로드한다.</p>
<blockquote>
<p>💡 빈 문자일 경우 모든 환경 변수를 로드한다</p>
</blockquote>
<pre><code>{
  VITE_APP_ENVIRONMENT: 'DEV',
  VITE_APP_SERVER: 'https://abc.abc.com',
  ALLUSERSPROFILE: 'C:\\ProgramData',
  APPDATA: 'C:\\Users\\AppData\\Roaming',
  CHROME_CRASHPAD_PIPE_NAME: '\\\\.\\pipe\\crashpad_5276_XOTRGHZMDFBHYJKD',
  COLOR: '1',
  COLORTERM: 'truecolor',
  CommonProgramFiles: 'C:\\Program Files\\Common Files',
  'CommonProgramFiles(x86)': 'C:\\Program Files (x86)\\Common Files',
}</code></pre><blockquote>
</blockquote>
<p>🕵️ 그래서 환경 변수명만 불러오고 싶을 땐 </p>
<pre><code class="language-js"> const env = loadEnv(mode, process.cwd(), 'VITE_')</code></pre>
<blockquote>
</blockquote>
<p>세번째 인자에 'VITE_' 를 넣어준다.</p>
<pre><code> {
  VITE_APP_ENVIRONMENT: 'DEV',
  VITE_APP_SERVER: 'https://abc.abc.com'
}</code></pre><h3 id="5-server-proxy-설정">5. server proxy 설정</h3>
<pre><code class="language-ts"> export default defineConfig(({ mode }) =&gt; {
   const envPath = path.resolve(new URL(import.meta.url).pathname, `.env.${mode}`)
   dotenv.config({ path: envPath })
   const env = loadEnv(mode, process.cwd(), 'VITE_')
    •••••

    return {
        •••••
        🟢server: {
            proxy: {
                '/api': {
                    target: env.VITE_APP_SERVER,
                    changeOrigin: true,
                    rewrite: (path) =&gt; path.replace(/^\/api/, ''),
                },
            },
        },
        •••••
    }
    •••••
 })</code></pre>
<p>1️⃣ target : 프록시 요청을 보낼 대상 서버의 URL을 지정한다.</p>
<ul>
<li><p>ex ) <code>target: env.VITE_APP_SERVER</code>는 프록시 요청을 <code>env.VITE_APP_SERVER</code>에 지정된 서버로 보낸다.</p>
</li>
<li><p>사용 : 클라이언트 코드에서 <code>/api</code>로 시작하는 요청을 프록시 서버를 통해 실제 API 서버로 전달할 때 사용한다.</p>
</li>
</ul>
<p>2️⃣ changeOrigin : 프록시 요청을 보낼 때 원본 요청의 호스트 헤더를 대상 서버의 호스트 헤더로 변경할지 여부를 지정한다.</p>
<ul>
<li><p>ex ) <code>changeOrigin: true</code>는 원본 요청의 호스트 헤더를 대상 서버의 호스트 헤더로 변경한다.</p>
</li>
<li><p>사용 : 대상 서버가 호스트 헤더를 기반으로 요청을 처리하는 경우 유용하다.</p>
</li>
</ul>
<p>3️⃣ rewrite : 프록시 요청의 경로를 재작성하는 함수다. 경로를 변경하여 대상 서버에 전달할 수 있다.</p>
<ul>
<li><p>ex ) <code>rewrite: (path) =&gt; path.replace(/^\/api/, '')</code>는 /api로 시작하는 경로를 빈 문자열로 대체하여 대상 서버에 전달한다.</p>
</li>
<li><p>사용 : 클라이언트 코드에서 <code>/api</code>로 시작하는 경로를 대상 서버의 실제 경로로 변경할 때 사용한다.</p>
</li>
</ul>
<hr />