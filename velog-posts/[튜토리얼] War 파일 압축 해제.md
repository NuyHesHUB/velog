<h1 id="war-파일-압축-해제">.War 파일 압축 해제</h1>
<hr />

<h3 id="방법1--tar-명령어-사용">방법1 : tar 명령어 사용</h3>
<p><code>tar</code> 명령어 사용</p>
<p>Windows 10 버전 1803 이후에는 tar 명령어가 기본적으로 지원됩니다. 이 명령어를 사용하여 .war 파일을 압축 해제할 수 있습니다.</p>
<blockquote>
<ol>
<li>명령 프롬프트 열기</li>
</ol>
</blockquote>
<p><code>windows</code> + <code>R</code>을 눌러 <code>실행</code> 대화상자를 열고, <code>cmd</code>를 입력한 후 <code>Enter</code>를 누릅니다.</p>
<blockquote>
<ol start="2">
<li><code>tar</code> 명령어로 압축 해제하기</li>
</ol>
</blockquote>
<pre><code>tar -xf C:\Users\...\"파일이름".war -C C:\Users\...\"압축 풀 폴더이름"</code></pre><p>여기서 -C 옵션은 압축을 풀 디렉토리를 지정합니다. 폴더가 없다면 자동으로 생성됩니다.</p>
<hr />

<h3 id="방법2--7-zip-사용">방법2 : 7-Zip 사용</h3>
<p>7-Zip은 다양한 파일 형식을 지원하는 압축 도구로, .war 파일의 압축을 해제할 수 있습니다. 명령줄에서 7z 명령어를 사용할 수 있습니다.</p>
<blockquote>
<ol>
<li>7-Zip 설치</li>
</ol>
</blockquote>
<p>[7-Zip 공식 웹사이트] <a href="https://www.7-zip.org/">https://www.7-zip.org/</a> 에서 7-Zip을 다운로드하여 설치합니다.</p>
<blockquote>
<ol start="2">
<li>명령 프롬프트 열기</li>
</ol>
</blockquote>
<p><code>windows</code> + <code>R</code>을 눌러 <code>실행</code> 대화상자를 열고, <code>cmd</code>를 입력한 후 <code>Enter</code>를 누릅니다.</p>
<blockquote>
<ol start="3">
<li>7-Zip으로 압축 해제하기</li>
</ol>
</blockquote>
<p><code>.war</code> 파일이 있는 디렉토리로 이동한 후, 다음 명령어를 입력합니다</p>
<pre><code>"C:\Program Files\7-Zip\7z.exe" x C:\Users\...\"파일이름".war -oC:\Users\...\"압축 풀 폴더이름"</code></pre><p>여기서 <code>-o</code> 옵션은 압축을 풀 디렉토리를 지정합니다.</p>
<hr />

<h3 id="방법-3-7-zip-gui-사용">방법 3: 7-Zip GUI 사용</h3>
<blockquote>
<ol>
<li>7-Zip GUI 열기</li>
</ol>
</blockquote>
<p><code>windows</code> + <code>R</code>을 눌러 <code>실행</code> 대화상자를 열고, <code>7zFM</code>을 입력하여 7-Zip 파일 관리자를 엽니다.</p>
<blockquote>
<ol start="2">
<li>파일 열기</li>
</ol>
</blockquote>
<p>7-Zip 파일 관리자에서 .war 파일이 위치한 디렉토리로 이동하고, 해당 파일을 선택한 후 압축 해제 버튼을 클릭합니다.</p>
<hr />