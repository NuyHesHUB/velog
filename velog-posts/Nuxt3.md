<h1 id="튜토리얼-nuxt3-시작">[튜토리얼] Nuxt3 시작</h1>
<h3 id="nuxtjs로-프로젝트생성">Nuxt.js로 프로젝트생성</h3>
<blockquote>
<ol>
<li><code>npx nuxi@latest init project-name</code></li>
</ol>
</blockquote>
<blockquote>
<ol start="2">
<li><code>✔ Are you interested in participating?</code> y | n 선택</li>
</ol>
</blockquote>
<blockquote>
<ol start="3">
<li><code>✔ Initialize git repository?</code> y | n 선택</li>
</ol>
</blockquote>
<blockquote>
<ol start="4">
<li>해당 디렉토리 이동 <code>cd 프로젝트명</code></li>
</ol>
</blockquote>
<blockquote>
<ol start="5">
<li><code>npm run dev</code></li>
</ol>
</blockquote>
<blockquote>
<ol start="6">
<li>실행 화면
<img alt="" src="https://velog.velcdn.com/images/nuyhes/post/2d848788-a81b-4343-b7b1-6a85e385a16e/image.png" /></li>
</ol>
</blockquote>
<hr />

<h3 id="🕵️are-you-interested-in-participating-이란">🕵️Are you interested in participating 이란?</h3>
<p>출처: <a href="https://ordinary-code.tistory.com/55">https://ordinary-code.tistory.com/55</a> [김평범's OrdinaryCode:티스토리]</p>
<p>위의 내용에 따라 보면 NuxtJS의 경우 익명의 원격 측정 데이터를 수집하여 
지속적으로 개선하는데 노력하니 원격으로 데이터를 수집하길 참여해달라는 내용이다.
 
들어가 보니 수집되는 항목은 아래와 같다</p>
<p>호출하는 명령어(nuxt dev, nuxt Build 등)</p>
<ul>
<li>Nuxt.js, Node.js 버전</li>
<li>일반적인 시스템 정보(OS 및 CI)</li>
<li>webpack 빌드 기간 및 애플리케이션 크기 </li>
<li>Nuxt modules </li>
</ul>
<h4 id="are-you-interested-in-participating-문구-안-뜨도록-설정하는-방법">Are you interested in participating 문구 안 뜨도록 설정하는 방법</h4>
<blockquote>
<p>nuxt.config.js 설정하기</p>
</blockquote>
<p>nuxt.config.js 중 telemetry 속성을 이용하면 서버를 돌릴 때마다 나타난 저런 문구가 사라진다.</p>
<p>telemetry는 true, false를 선택해서 사용이 가능하다.</p>
<pre><code class="language-js">//nuxt.config.js
module.exports = {
  ...
  telemetry: true,
  ...
}</code></pre>
<hr />