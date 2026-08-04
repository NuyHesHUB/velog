<blockquote>
<p>🕵️‍♀️ 리눅스/우분투 환경에서 안전하게 파일을 삭제하고 싶었다.</p>
</blockquote>
<hr />
<h2 id="1-trash-cli-설치하기">1. trash-cli 설치하기</h2>
<blockquote>
<p>우분투의 기본 패키지 관리자인 <code>apt</code>를 사용하여 간편하게 설치할 수 있다.</p>
</blockquote>
<p><strong>apt 업데이트</strong></p>
<pre><code class="language-shell">sudo apt update</code></pre>
<p><strong>trash-cli 설치</strong></p>
<pre><code class="language-shell">sudo apt install trash-cli</code></pre>
<hr />
<h2 id="2-사용자-편의를-위한-alias-설정">2. 사용자 편의를 위한 Alias 설정</h2>
<p><code>trash-put</code>이라는 명령어가 길게 느껴질 수 있으므로 짧은 별칭을 설정하는 것이 좋다. 또한 <code>rm</code>을 직접 사용하는 실수를 방지하기 위한 안전장치도 함께 추가한다.</p>
<hr />
<p><strong>1. 사용 중인 쉘 설정 파일을 연다</strong></p>
<pre><code class="language-shell">nano ~/.bashrc</code></pre>
<hr />
<p><strong>2. 해당 파일 맨 아래에 다음 내용을 추가한다</strong></p>
<pre><code class="language-shell"># trash-cli 별칭 설정
alias tp='trash-put'      # 파일 삭제 (휴지통으로)
alias tl='trash-list'     # 휴지통 목록 확인
alias tr='trash-restore'  # 파일 복구
alias te='trash-empty'    # 휴지통 비우기

# rm 명령어 사용 시 경고 메시지 (선택 사항)
alias rm='echo &quot;rm 대신 tp (trash-put)를 사용하세요. 정말 삭제하려면 \rm을 입력하세요.&quot;'</code></pre>
<hr />
<p><strong>3. <code>Ctrl + O</code> (저장) -&gt; <code>Enter</code> -&gt; <code>Ctrl + X</code> (종료) 순으로 누른 뒤 설정을 적용</strong></p>
<pre><code class="language-shell">source ~/.bashrc</code></pre>
<hr />
<h2 id="3-주요-명령어-사용법">3. 주요 명령어 사용법</h2>
<table>
<thead>
<tr>
<th>기능</th>
<th>명령어</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td>삭제</td>
<td><code>tp 파일명</code></td>
<td>파일을 휴지통으로 이동시킨다. (trash-put)</td>
</tr>
<tr>
<td>목록</td>
<td><code>tl</code></td>
<td>휴지통에 있는 파일들과 삭제된 시간을 보여준다.</td>
</tr>
<tr>
<td>복구</td>
<td><code>tr</code></td>
<td>번호를 선택하여 파일을 원래 위치로 복구한다.</td>
</tr>
<tr>
<td>비우기</td>
<td><code>te 30</code></td>
<td>휴지통에서 30일 이상 된 파일만 삭제한다.</td>
</tr>
<tr>
<td>전체 비우기</td>
<td><code>te</code></td>
<td>휴지통의 모든 내용을 완전히 삭제한다.</td>
</tr>
</tbody></table>
<hr />
<h2 id="4-사용-방법">4. 사용 방법</h2>
<blockquote>
<p>ex ) <code>~/projects/code/TEST</code> 폴더를 삭제한다는 가정</p>
</blockquote>
<h3 id="1-해당-경로-내부에서-삭제할-때">1. 해당 경로 내부에서 삭제할 때</h3>
<p>현재 위치가 <code>~/projects/code</code>라면 폴더명만 입력하면 된다.</p>
<p><strong>명령어:</strong></p>
<pre><code class="language-shell">tp TEST/
# (참고: 뒤에 `/`는 붙여도 되고 안 붙여도 무방)</code></pre>
<hr />
<h3 id="2-경로-외부에서-삭제할-때-예제">2. 경로 외부에서 삭제할 때 (예제)</h3>
<p>현재 위치가 홈 디렉토리(<code>~</code>)나 다른 곳에 있을 때는 <strong>상대 경로</strong> 또는 <strong>절대 경로</strong>를 사용해야 한다.</p>
<h4 id="a-상대-경로-사용-현재-내-위치-기준">A. 상대 경로 사용 (현재 내 위치 기준)</h4>
<p>만약 현재 내 위치가 <code>~</code> (홈) 이라면:</p>
<pre><code class="language-shell">tp projects/code/TEST/</code></pre>
<h4 id="b-절대-경로-사용-가장-확실한-방법">B. 절대 경로 사용 (가장 확실한 방법)</h4>
<p>내가 어디에 있든 상관없이 삭제하고 싶을 때 사용한다.</p>
<pre><code class="language-shell">tp ~/projects/code/TEST/</code></pre>
<hr />
<h3 id="3-제대로-삭제되었는지-확인-및-복구-연습">3. 제대로 삭제되었는지 확인 및 복구 연습</h3>
<p>삭제 명령을 내린 후 다음 단계로 확인</p>
<p><strong>1. 목록 확인: <code>tl</code> (trash-list) 명령어를 친다</strong></p>
<pre><code class="language-shell">tl
# 출력 예시: 2026-05-15 14:05:00 /home/jaiden-linux/projects/code/TEST</code></pre>
<p><strong>2. 복구 테스트: 만약 잘못 지웠다면 tr (trash-restore) 명령어를 친다</strong></p>
<pre><code class="language-shell">tr
# 그 후 화면에 뜨는 번호(예: `0`, `1` 등)를 입력하면 `TEST` 폴더가 다시 `~/projects/code/` 위치로 돌아온다.</code></pre>
<blockquote>
<p>💡 팁: 여러 개를 한 번에 지우고 싶다면?</p>
</blockquote>
<pre><code class="language-shell"># 띄어쓰기로 구분해서 나열하면 된다
tp file1.txt file2.txt TEST_FOLDER/</code></pre>
<hr />