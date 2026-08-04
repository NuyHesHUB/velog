<hr />
<h2 id="1-옵시디언-폴더-찾기">1. 옵시디언 폴더 찾기</h2>
<h3 id="1-gitignore-세팅">1. .gitignore 세팅</h3>
<p>옵시디언 폴더(볼트)위치</p>
<pre><code class="language-shell"># C:\Users\&lt;사용자명&gt;\Documents\obsidian </code></pre>
<p>폴더 내부에 <code>.gitignore</code> 생성하여 <code>.obsidian</code>폴더 내부의 <code>json</code>파일을 제외시킨다.</p>
<pre><code class="language-shell">.obsidian/
.obsidian/app.json
.obsidian/workspace.json</code></pre>
<hr />
<blockquote>
<p>🕵️ <strong><code>.obsidian</code>폴더내 <code>json</code>파일</strong></p>
</blockquote>
<ul>
<li><code>app.json</code>: 주로 앱 전역 설정이라 일부는 공유해도 되지만 기기별 UI 상태가 섞일 수 있어 조심하는 편이 좋습니다.</li>
<li><code>appearance.json</code>: 테마, 모양 같은 <strong>공통 설정</strong> 성격이라 여러 기기에서 공유해도 비교적 무난합니다</li>
<li><code>core-plugin.json</code>: 코어 플러그인 활성화 상태라서, 여러 기기에서 같은 작업 환경이면 공유해도 괜찮습니다.</li>
<li><code>workspace.json</code>: 이건 현재 창 배치, 열어둔 탭 같은 <strong>기기/세션 상태</strong>가 들어가서 보통은 공유하지 않는 편이 좋습니다.</li>
</ul>
<hr />
<h2 id="2-github-리포지토리-생성">2. Github 리포지토리 생성</h2>
<p>먼저 메모가 저장될 원격 저장소를 생성해야 합니다.</p>
<ol>
<li><strong>GitHub</strong>에 로그인 후 <strong>New Repository</strong>를 클릭</li>
<li><strong>Repository name</strong>을 입력 (예: <code>my-obsidian-vault</code>).</li>
<li><strong>Public/Private</strong> 중 반드시 <strong>Private</strong>을 선택 (개인 메모 보안)</li>
<li><code>Initialize this repository with a README</code>는 체크하지 않은 상태로 <strong>Create repository</strong> 클릭 생성</li>
</ol>
<hr />
<h2 id="3-옵시디언-플러그인-설치-및-설정">3. 옵시디언 플러그인 설치 및 설정</h2>
<ol>
<li>옵시디언 &gt; Setting &gt; 커뮤니티 플러그인 &gt; 탐색 &gt; &quot;Git&quot;으로 검색한다.</li>
<li><code>Git(Obsidian Git Plugin)</code>이라는 플러그인을 설치 및 활성화 처리</li>
<li>옵시디언 &gt; Setting 탭 하단 &gt; 커뮤니티 플러그인 &gt; Git 확인 및 이동</li>
</ol>
<hr />
<blockquote>
<p>🕵️ Git 플러그인 영역별 주요 옵션</p>
</blockquote>
<p><strong>History view</strong> (주로 옵시디언 내에서 Git의 상태를 어떻게 보여줄지 결정하는 영역)</p>
<pre><code>1. Show Author : Git 기록을 볼 때 작성자 표시 여부
2. Show Date   : Git 기록을 볼 때 날짜 표시 여부</code></pre><p><strong>Source control view</strong></p>
<pre><code>1. Automatically refresh source control view on file changes: 파일이 변경될 때 마다 Git 소스 제어창을 자동으로 새로고침
2. Source control view refresh interval: 파일을 수정한 후 옵시디언 내 Git 관리 창에 그 변화가 반영될 때까지 기다리는 대기 시간</code></pre><p><strong>Miscellaneous</strong> (기타 설정)</p>
<pre><code>1. Diff view style (기본값: Split): 수정 전후의 차이점을 어떻게 보여줄지 정한다
2. Disable informative notifications: &quot;백업 성공&quot;, &quot;푸시 완료&quot; 같은 단순 정보성 알림
3. Disable error notifications: 에러 알림을 포함한 모든 알림
4. Hide notifications for no changes: 커밋이나 푸시를 실행했는데 변경 사항이 없을 때 뜨는 &quot;변경 사항 없음&quot; 알림을 숨김
5. Show status bar: Git의 전반적인 상태(동기화 중, 대기 중 등)를 하단 바에 표시
6. File menu integration: 추천 옵션 파일 탐색기에서 마우스 우클릭을 했을 때 Git 관련 메뉴를 추가해준다.
7. Show branch status bar: 현재 내가 어떤 브랜치(기본은 `main`)에서 작업 중인지 표시
8. Show the count of modified files in the status bar: 현재 커밋되지 않은 즉 수정된 파일이 몇 개인지 숫자로 보여줌</code></pre><p>Advanced (고급 설정)</p>
<pre><code>1. Update submodules: 내 볼트 안에 또 다른 Git 저장소(Submodule)가 포함되어 있을 경우 메인 볼트를 동기화할 때 이 하위 저장소들도 같이 업데이트할지 결정
2. Custom Git binary path: 보통은 'git'이라고만 적혀 있으면 시스템이 알아서 찾는다.
3. Additional environment variables / PATH:: Git 실행 시 필요한 특수한 시스템 변수나 경로를 추가할 때 쓴다 (일반 유저는 비워둠)
4. Reload with new environment variables: 위에서 환경 변수를 수정했다면 프로그램을 껐다 켜지 않고 이 버튼을 눌러 즉시 적용
5. Custom base path (Git repository path): 보통은 옵시디언 볼트 폴더 자체가 Git 저장소이다. 하지만 볼트 안의 특정 하위 폴더만 Git으로 관리하고 싶을 때 그 경로를 적어준다.
(윈도우는 '/' 대신 '₩'를 써야 함)
6. Custom Git directory path (Instead of '.git'): Git은 보통 '.git'이라는 숨김 폴더에 모든 이력을 저장한다. 만약 이 폴더 이름을 다른 것으로 바꿨다면 여기서 지정한다. (거의 쓰이지 않음)
7. Disable on this device: 이 기기에서 비활성화 옵시디언 설정 파일('.obsidian' 폴더)까지 GitHub에 올릴 경우 다른 모든 기기에서 이 플러그인이 켜지게 된다. 만약 &quot;내 회사 컴퓨터에서는 보안상 Git 동기화를 쓰면 안 돼&quot; 할 때 이 옵션을 켜면 해당 기기에서만 플러그인이 작동하지 않는다.</code></pre><hr />
<h2 id="로컬-폴더와-github-연결">로컬 폴더와 GitHub 연결</h2>
<blockquote>
<p>🕵️ 처음 한 번은 터미널(또는 CMD)을 통해 볼트 폴더와 GitHub를 연결해줘야 한다.</p>
</blockquote>
<ol>
<li>옵시디언 볼트 폴더로 이동</li>
<li>해당 폴더에서 터미널을 열고 다음 명령어를 순서대로 입력한다:</li>
</ol>
<pre><code>git init
git add README.md
git commit -m &quot;first commit&quot;
git branch -M main
git remote add origin https://github.com/&lt;사용자아이디&gt;/&lt;저장소이름&gt;.git
git push -u origin main</code></pre><hr />
<h2 id="작업한-내용-git-관리">작업한 내용 Git 관리</h2>
<ol>
<li>단축키 <code>Ctrl</code> + <code>P</code> (Mac <code>Cmd</code> + <code>P</code>)를 눌러 명령어 팔레트 오픈</li>
<li><code>Git Commit</code> 후 <code>Git Push</code> 반영</li>
</ol>
<p>또는 <code>Vault backup interval (minutes)</code>로 분 단위 자동 처리</p>
<hr />
<h2 id="다른-pc에서-가져오기">다른 PC에서 가져오기</h2>
<hr />
<blockquote>
<p>방법 1</p>
</blockquote>
<p>가장 권장하는 방법 빈 폴더를 하나 만들고 GitHub에 있는 내용을 그대로 복제(Clone)해오는 방식</p>
<ol>
<li><strong>Git 설치:</strong> 새 컴퓨터에도 <a href="https://git-scm.com/">git-scm.com</a>에서 Git이 설치되어 있어야 한다.</li>
<li><strong>폴더 생성:</strong> 메모를 저장할 빈 폴더를 만든다.</li>
<li><strong>터미널 열기:</strong> 해당 폴더에서 터미널(또는 CMD)을 연다.</li>
<li><strong>복제 명령어 입력:</strong><pre><code class="language-bash">git clone https://github.com/사용자아이디/저장소이름.git .</code></pre>
</li>
</ol>
<ul>
<li>(주의: 맨 끝에 한 칸 띄우고 마침표(<code>.</code>)*_를 찍으면 현재 폴더에 바로 풀림)</li>
</ul>
<ol start="5">
<li><strong>로그인:</strong> GitHub 아이디/비번 혹은 Personal Access Token을 요구하면 입력한다.</li>
<li><strong>옵시디언에서 열기:</strong> 옵시디언을 실행하고 &quot;Open folder as vault&quot;를 선택해 해당 폴더를 선택한다.</li>
<li><strong>플러그인 확인:</strong> <code>.obsidian</code> 폴더까지 동기화했다면 'Obsidian Git' 플러그인이 이미 설치되어 있을 것 만약 안 보인다면 커뮤니티 플러그인에서 다시 설치하고 활성화해주면 설정값이 그대로 살아난다.</li>
</ol>
<hr />
<blockquote>
<p>방법 2</p>
</blockquote>
<p>터미널 사용이 어렵다면 플러그인의 기능을 활용할 수 있다.</p>
<ol>
<li><strong>빈 볼트 생성:</strong> 옵시디언에서 새로운 빈 볼트를 하나 만든다.</li>
<li><strong>플러그인 설치:</strong> <code>Obsidian Git</code> 플러그인을 설치하고 활성화한다.</li>
<li><strong>명령어 팔레트 실행:</strong> <code>Ctrl + P</code> (맥은 <code>Cmd + P</code>)를 누르고 <code>Git: Clone</code>을 검색하여 실행한다.</li>
<li><strong>정보 입력</strong>:<ul>
<li>GitHub 저장소 URL을 입력한다.</li>
<li>나머지 절차에 따라 인증을 완료하면 GitHub의 파일들이 현재 볼트로 다운로드된다.</li>
</ul>
</li>
</ol>
<hr />