<h2 id="wsl2-기본-배포판-변경">WSL2 기본 배포판 변경</h2>
<p><code>wsl -l -v</code> 또는 <code>wsl --list -verbose</code>로 리눅스 배포판 목록을 조회하면</p>
<pre><code class="language-bash">출력 예시
  NAME                STATE   VERSION 
  Ubuntu-22.04        Running 2 
* docker-desktop      Running 2 
  docker-desktop-data Stopped 2</code></pre>
<p>로 <code>*</code>표시로 기본 배포판이 설정되어있다.</p>
<p>기본 배포판을 <code>Ubuntu-22.04</code>로 변경하거나 다른 배포판을 기본으로 설정하고 싶다면</p>
<pre><code>wsl --set-default Ubuntu-24.04

또는

wsl --set-default &lt;NAME&gt;</code></pre><p>을 입력하여 기본 배포판을 설정한다.</p>
<p><strong>변경 후 테스트</strong></p>
<p><code>cmd</code>에서 <code>wsl</code>을 입력하면 바로 기본 배포판 설정된 경로로 들어간다.</p>
<hr />