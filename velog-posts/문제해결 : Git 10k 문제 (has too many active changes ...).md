<hr />

<blockquote>
<p>🔴 The git repository at 'C\Users.....' 
has too many active changes, only a subset of Git features will be enabled</p>
</blockquote>
<p>Visual Studio Code를 사용하는데 갑자기 위와 같은 경고가 뜨면서 Git change가 무려 10k 를 넘어갔다.</p>
<p><img alt="" src="https://velog.velcdn.com/images/nuyhes/post/1e875ae2-5a26-46c0-8efe-dc18b8c8b27a/image.png" /></p>
<p>방법은 여러 곳을 검색해보았고 <a href="https://seanlion.github.io/blog/25">https://seanlion.github.io/blog/25</a> 이 분의 도움으로 문제를 해결했다. (감사합니다)</p>
<h3 id="해결방법">해결방법</h3>
<blockquote>
<p>출처 : <a href="https://seanlion.github.io/blog/25">https://seanlion.github.io/blog/25</a></p>
</blockquote>
<h4 id="문제의-원인">문제의 원인</h4>
<p>Desktop 같은 파일이 많고 복잡한 디렉토리에 실수로 <code>.git</code> 폴더를 생성한 경우, Git은 해당 디렉토리를 저장소로 간주하고 모든 파일을 추적하려 시도한다. 그 결과, 과도한 변경 사항이 감지되어 경고 메시지가 출력된다.</p>
<hr />

<h4 id="문제-해결-방법">문제 해결 방법</h4>
<p><strong>1️⃣ Git 저장소 루트 확인</strong></p>
<p>현재 사용 중인 Git 저장소의 루트 디렉토리가 어디인지 확인한다.</p>
<p>아래 명령어를 입력한다.</p>
<blockquote>
<p><code>git rev-parse --show-toplevel</code></p>
</blockquote>
<p>이 명령어는 현재 Git 저장소의 최상위 디렉토리 경로를 출력한다. </p>
<blockquote>
<p>ex ) <code>C/Users/...</code></p>
</blockquote>
<hr />

<p><strong>2️⃣Git 저장소 루트로 이동 (위에서 확인한 경로로 이동한다)</strong></p>
<blockquote>
<p>ex ) <code>cd /Users/...</code></p>
</blockquote>
<hr />

<p><strong>3️⃣.git 폴더 확인</strong></p>
<p>이 디렉토리에서 .git 폴더가 있는지 확인한다. 숨김 파일을 포함하여 디렉토리를 나열하려면 </p>
<blockquote>
<p><code>ls -a</code> 를 입력한다.</p>
</blockquote>
<p>출력 결과에 .git 폴더가 보인다면, 이 디렉토리가 Git 저장소로 설정되어 있는 상태이다.</p>
<hr />

<p><strong>4️⃣.git 폴더 삭제</strong></p>
<p>.git 폴더를 삭제하면 해당 디렉토리가 더 이상 Git 저장소로 인식되지 않는다. </p>
<blockquote>
<p><code>rm -r -f .git</code> 를 이용하여 강제 삭제한다.</p>
</blockquote>
<p>⚠️ 주의 <code>-f</code> 옵션은 강제 삭제(force)를 의미하므로, 꼭 삭제 대상이 .git 폴더인지 확인해야한다.</p>
<hr />

<p><strong>5️⃣문제 해결 확인</strong></p>
<p>이제 Visual Studio Code에서 작업 디렉토리를 다시 확인하면 더 이상 이 많은 git 변경 사항이 나타나지 않을 것이다.</p>
<hr />

<p>👍 깔끔해진 모습</p>
<p><img alt="" src="https://velog.velcdn.com/images/nuyhes/post/a934c854-7dc9-44b0-a7fd-8cc145e0c1e7/image.png" /></p>
<hr />


<h4 id="🕵️추가-팁-안전하게-git-정리하기">🕵️추가 팁: 안전하게 Git 정리하기</h4>
<p>강제 삭제 명령어를 사용할 때 주의
<code>git clean -f -d</code> 같은 명령어는 강제로 파일을 삭제하며 복구가 어려울 수 있다.</p>
<p>파일 삭제가 어떤 영향을 미칠지 사전에 확인하려면 아래 명령어를 먼저 사용하는게 좋다</p>
<blockquote>
<p><code>git clean -d -n</code></p>
</blockquote>
<p>이 명령어는 실제 삭제 없이 삭제될 항목만 미리 보여준다.</p>
<hr />