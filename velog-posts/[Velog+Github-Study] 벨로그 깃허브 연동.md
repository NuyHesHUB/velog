<h1 id="veloggithub-study-벨로그-깃허브-연동-test">[Velog+Github-Study] 벨로그 깃허브 연동 test</h1>
<hr />
<p>🕵️ <code>Velog</code>에 글을 작성하면 <code>GitHub</code>에 업로드가 되게 하고 싶었다.</p>
<hr />
<h2 id="연동-방법-순서">연동 방법 순서</h2>
<blockquote>
<h4 id="📂-폴더-구조">📂 폴더 구조</h4>
<pre><code>📁 프로젝트 루트 
├── 📁 .github 
│ └── 📁 workflows 
│ └── python-workflow.yml # GitHub Actions 워크플로우 정의 파일 
├── 📁 scripts 
│ └── my_script.py # 실행할 Python 스크립트 파일 
└── README.md</code></pre></blockquote>
<pre><code>
### 1. Github 리포지토리 생성

### 2. 로컬 폴더에서 Git 초기화 및 리포지토리 연결
</code></pre><p>echo "# velog" &gt;&gt; README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin <a href="https://github.com/NuyHesHUB/velog.git">https://github.com/NuyHesHUB/velog.git</a>
git push -u origin main</p>
<pre><code>
### 3. update_velog.yml 파일 생성

해당 로컬 디렉토리에서 입력하여 .github/workflows 폴더를 생성한다.

```shell
# terminal
mkdir -p .github/workflows</code></pre><p>.github/workflows 폴더 생성 후 <code>update_velog.yml</code> 파일 생성하고 yml 설정코드를  작성한다.</p>
<hr />
<h3 id="🕵️-github-actions-이란">🕵️ Github Actions 이란?</h3>
<p><a href="https://docs.github.com/ko/actions/about-github-actions/understanding-github-actions">Github-Actions 문서</a></p>
<p><code>GitHub Actions</code>는 빌드, 테스트 및 배포 파이프라인을 자동화할 수 있는 CI/CD(연속 통합 및 지속적인 업데이트) 플랫폼입니다. 리포지토리에 대한 모든 끌어오기 요청을 빌드 및 테스트하거나 병합된 끌어오기 요청을 프로덕션에 배포하는 워크플로를 만들 수 있습니다.</p>
<p>GitHub Actions은(는) 단순한 DevOps 수준을 넘어 리포지토리에서 다른 이벤트가 발생할 때 워크플로를 실행할 수 있도록 합니다. 예를 들어 누군가가 리포지토리에서 새 이슈를 만들 때마다 워크플로를 실행하여 적절한 레이블을 자동으로 추가할 수 있습니다.</p>
<p>GitHub에서 워크플로를 실행할 Linux, Windows, macOS 가상 머신을 제공하거나, 사용자 고유의 데이터 센터 또는 클라우드 인프라에서 자체 호스트형 실행기를 호스트할 수 있습니다.</p>
<h4 id="주요기능">주요기능</h4>
<p>자동화된 워크플로우</p>
<ul>
<li>코드 변경 시 빌드, 테스트, 배포 등의 작업을 자동으로 실행할 수 있습니다.</li>
<li>워크플로우는 <code>.github/workflows</code> 디렉토리 아래에 작성된 <code>YAML</code>파일로 정의됩니다.</li>
</ul>
<p>이벤트 기반 실행</p>
<ul>
<li><code>Github Actions</code>는 다양한 이벤트를 트리거로 실행됩니다. 예 ) <code>main</code> 브랜치에 코드가 푸시되면 자동으로 테스트를 실행 등</li>
</ul>
<p>멀티 플랫폼 지원</p>
<ul>
<li><code>Linux</code>, <code>macOS</code>, <code>Windows</code> 환경에서 작업을 실행할 수 있습니다.</li>
</ul>
<p>직접 작성 가능한 커스텀 작업</p>
<ul>
<li>GitHub Actions에서 제공하는 기본 작업 외에도 사용자가 JavaScript 또는 Docker 기반으로 커스텀 작업을 작성할 수 있습니다.</li>
</ul>
<p>시크릿 및 환경 변수 관리</p>
<ul>
<li>민감한 데이터(예: API 키, 토큰)는 GitHub Secrets로 안전하게 저장하고, Actions에서 사용할 수 있습니다.</li>
</ul>
<p>다양한 마켓플레이스</p>
<ul>
<li>GitHub Actions 마켓플레이스에서 다양한 사전 정의된 액션(예: AWS 배포, Docker 빌드 등)을 사용할 수 있습니다.</li>
</ul>
<hr />
<h3 id="4-📂githubworkflows📄update_velogyml-코드-작성">4. 📂.github/workflows/📄update_velog.yml 코드 작성</h3>
<p><img alt="" src="https://velog.velcdn.com/images/nuyhes/post/54bcb1d5-fd3f-4679-bf2e-24cb897fde41/image.png" /></p>
<blockquote>
<p>코드</p>
</blockquote>
<pre><code class="language-yml">name: Update Velog

on:
    push:
        branches:
            - master
    schedule:
        - cron: '0 0 * * *'

jobs:
    update_velog:
        runs-on: ubuntu-latest
        steps:
            - name: Checkout
              uses: actions/checkout@v2
              
            - name: Push changes
              run: |
                git config --global user.name 'github-actions[bot]'
                git config --global user.email 'github-actions[bot]@user.noreply.github.com'
                git push https://${{ secrets.GH_PAT }}@github.com/🟢깃허브ID🟢/velog.git
                
            - name: Set up Python
              uses: actions/setup-python@v2
              with:
                python-version: '3.x'
                
            - name: Install dependencies
              run: |
                pip install feedparser gitpython

            - name: Run script
              run: python scripts/update_velog.py</code></pre>
<hr />
<h4 id="🕵️-secretsgh_pat-변수">🕵️ secrets.GH_PAT 변수</h4>
<p><code>git push https://${{ secrets.GH_PAT }}@github.com/🟢깃허브ID🟢/velog.git</code> 에서 </p>
<p>변수 sercrets.GH_PAT 은 잠시 PAT 생성한는 NAME과 동일하게 한다.</p>
<hr />
<h3 id="5--📂scripts📄update_velogpy-파일-생성--코드">5.  📂scripts/📄update_velog.py 파일 생성 &amp; 코드</h3>
<p><code>벨로그</code> RSS 피드를 파싱하여 새로운 글을 로컬 깃 저장소에 마크다운 파일로 저장하고, 이를 커밋 및 푸시하는 스크립트다. </p>
<ol>
<li>필요한 라이브러리(<a href="https://api.velog.io/rss/@nuyhes">feedparser</a>, <a href="https://api.velog.io/rss/@nuyhes">git</a>, <a href="https://api.velog.io/rss/@nuyhes">os</a>)를 임포트한다.</li>
<li>벨로그 RSS 피드 URL과 깃허브 레포지토리 경로를 설정한다.</li>
<li><code>velog-posts</code> 폴더 경로를 설정하고, 폴더가 없으면 생성한다.</li>
<li>로컬 깃 저장소를 로드한다.</li>
<li>RSS 피드를 파싱하여 각 글을 가져온다.</li>
<li>각 글을 파일로 저장하고 커밋한다:<ul>
<li>글 제목을 파일 이름으로 사용하며, 파일 이름에 유효하지 않은 문자를 제거하거나 대체한다.</li>
<li>파일 경로를 설정하고, 파일이 존재하지 않으면 새 파일을 생성하여 글 내용을 저장한다.</li>
<li>파일을 깃에 추가하고 커밋 메시지를 작성하여 커밋한다.</li>
</ul>
</li>
<li>변경 사항을 원격 저장소에 푸시한다.</li>
</ol>
<hr />
<p><img alt="" src="https://velog.velcdn.com/images/nuyhes/post/9a2f2281-f773-42cc-a151-ca0cf8e8f9ae/image.png" /></p>
<blockquote>
<p>코드</p>
</blockquote>
<pre><code class="language-python">import feedparser
import git
import os

# 벨로그 RSS 피드 URL
rss_url = 'https://api.velog.io/rss/@nuyhes'

# 깃허브 레포지토리 경로
repo_path = '.'

# 'velog-posts' 폴더 경로
posts_dir = os.path.join(repo_path, 'velog-posts')

# 'velog-posts' 폴더가 없으면 생성
if not os.path.exists(posts_dir):
    os.makedirs(posts_dir)

# 레포지토리 로드
repo = git.Repo(repo_path)

# RSS 피드 파싱
feed = feedparser.parse(rss_url)

# 각 글을 파일로 저장하고 커밋
for entry in feed.entries:
    # 파일 이름에서 유효하지 않은 문자 제거 또는 대체
    file_name = entry.title
    file_name = file_name.replace('/', '-') # 슬래시는 하위 폴더로 인식되므로 대시로 대체
    file_name = file_name.replace('\\', '') # 역슬래시는 파일 이름에 사용할 수 없으므로 제거
    file_name += '.md' # 마크다운 파일 확장자 추가
    file_path = os.path.join(posts_dir, file_name) # 파일 경로

    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(entry.discription) # 글 내용을 파일에 쓰기
        repo.git.add(file_path) # 깃에 파일 추가
        repo.git.commit('-m', f'Add post: {entry.title}') # 커밋

# 푸시

repo.git.push()</code></pre>
<hr />
<h3 id="6-pat-권한-받기">6. PAT 권한 받기</h3>
<p>1️⃣ Github 계정
2️⃣ Settings
3️⃣ Developer Settings
4️⃣ Personal access tokens
5️⃣ Tokens(classic)
<img alt="" src="https://velog.velcdn.com/images/nuyhes/post/872031fc-b154-4ab8-9062-0a3884aefdbe/image.png" /></p>
<p>6️⃣ Generate New Token 버튼 클릭
1️⃣ Note에 토큰 이름을 적는다
2️⃣ repo 체크 , workflow 체크
3️⃣ Generate Token 버튼 클릭
<img alt="" src="https://velog.velcdn.com/images/nuyhes/post/72c50e53-7755-4992-864b-328ac7ba3051/image.png" /></p>
<p>4️⃣ 토큰 값 복사 (토큰 값은 메모해둔다)
<img alt="" src="https://velog.velcdn.com/images/nuyhes/post/d0b9e9da-137d-4c98-a5d3-afa7493093ef/image.png" /></p>
<hr />
<blockquote>
<p>velog 레포지토리 이동</p>
</blockquote>
<p>1️⃣ Settings
2️⃣ Security 목록 &gt; Secret and variables &gt; Actions
<img alt="" src="https://velog.velcdn.com/images/nuyhes/post/67b5240e-4473-4efa-b2b3-cb2d65594c04/image.png" /></p>
<p>3️⃣ Secrets 탭 &gt; Repository secrets &gt; New repository secret 버튼 클릭</p>
<p><img alt="" src="https://velog.velcdn.com/images/nuyhes/post/ffabc562-7375-4adb-af7a-737ef8058da4/image.png" /></p>
<p>4️⃣ Name 이름 작성 (yml 변수에 넣은 이름) <code>GH_PAT_이름</code> / Secret 란 토큰 값 입력</p>
<hr />
<blockquote>
<p>레포지토리 외부 권한 부여</p>
</blockquote>
<pre><code>1️⃣ 해당 레포지토리 &gt; Settings
2️⃣ Actions &gt; General
3️⃣ Actions permissions &gt; 첫번째 Allow all actions and reusable workflows 체크
4️⃣ Approval for running fork pull request workflows from contributors &gt; 세번째 Require approval for all external contributors 체크
5️⃣ Workflow permissions &gt; 첫번째 Read and write permissions 체크
6️⃣ Allow GitHub Actions to create and approve pull requests 활성화</code></pre><p><img alt="" src="https://velog.velcdn.com/images/nuyhes/post/68b0b80c-4419-4d6e-91d8-fa7a2b61e54a/image.png" /></p>
<hr />
<h3 id="테스트-실패">테스트 실패</h3>
<blockquote>
<p>Actions 확인</p>
</blockquote>
<pre><code>1️⃣ 해당 레포지토리 &gt; Actions &gt; jobs
2️⃣ Run script 부분에서 에러가 발생했다.</code></pre><blockquote>
<p>에러 로그</p>
</blockquote>
<pre><code>Run python scripts/update_velog.py

[7](https://github.com/NuyHesHUB/velog/actions/runs/12578392936/job/35057054076#step:6:8)Traceback (most recent call last):
[8](https://github.com/NuyHesHUB/velog/actions/runs/12578392936/job/35057054076#step:6:9) File "/opt/hostedtoolcache/Python/3.12.8/x64/lib/python3.12/site-packages/feedparser/util.py", line 156, in __getattr__
[9](https://github.com/NuyHesHUB/velog/actions/runs/12578392936/job/35057054076#step:6:10) return self.__getitem__(key)
[10](https://github.com/NuyHesHUB/velog/actions/runs/12578392936/job/35057054076#step:6:11) ^^^^^^^^^^^^^^^^^^^^^
[11](https://github.com/NuyHesHUB/velog/actions/runs/12578392936/job/35057054076#step:6:12) File "/opt/hostedtoolcache/Python/3.12.8/x64/lib/python3.12/site-packages/feedparser/util.py", line 113, in __getitem__
[12](https://github.com/NuyHesHUB/velog/actions/runs/12578392936/job/35057054076#step:6:13) return dict.__getitem__(self, key)
[13](https://github.com/NuyHesHUB/velog/actions/runs/12578392936/job/35057054076#step:6:14) ^^^^^^^^^^^^^^^^^^^^^^^^^^^
[14](https://github.com/NuyHesHUB/velog/actions/runs/12578392936/job/35057054076#step:6:15)KeyError: 'discription'
[15](https://github.com/NuyHesHUB/velog/actions/runs/12578392936/job/35057054076#step:6:16)
[16](https://github.com/NuyHesHUB/velog/actions/runs/12578392936/job/35057054076#step:6:17)During handling of the above exception, another exception occurred:
[17](https://github.com/NuyHesHUB/velog/actions/runs/12578392936/job/35057054076#step:6:18)
[18](https://github.com/NuyHesHUB/velog/actions/runs/12578392936/job/35057054076#step:6:19)Traceback (most recent call last):
[19](https://github.com/NuyHesHUB/velog/actions/runs/12578392936/job/35057054076#step:6:20) File "/home/runner/work/velog/velog/scripts/update_velog.py", line 35, in &lt;module&gt;
[20](https://github.com/NuyHesHUB/velog/actions/runs/12578392936/job/35057054076#step:6:21) file.write(entry.discription) # 글 내용을 파일에 쓰기
[21](https://github.com/NuyHesHUB/velog/actions/runs/12578392936/job/35057054076#step:6:22) ^^^^^^^^^^^^^^^^^
[22](https://github.com/NuyHesHUB/velog/actions/runs/12578392936/job/35057054076#step:6:23) File "/opt/hostedtoolcache/Python/3.12.8/x64/lib/python3.12/site-packages/feedparser/util.py", line 158, in __getattr__
[23](https://github.com/NuyHesHUB/velog/actions/runs/12578392936/job/35057054076#step:6:24) raise AttributeError("object has no attribute '%s'" % key)
[24](https://github.com/NuyHesHUB/velog/actions/runs/12578392936/job/35057054076#step:6:25)AttributeError: object has no attribute 'discription'
[25](https://github.com/NuyHesHUB/velog/actions/runs/12578392936/job/35057054076#step:6:26)Error: Process completed with exit code 1.</code></pre><blockquote>
<p>📄update_velog.py</p>
</blockquote>
<pre><code class="language-python">if not os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            🔴file.write(entry.description) # 글 내용을 파일에 쓰기
            
        repo.git.add(file_path) # 깃에 파일 추가
        repo.git.commit('-m', f'Add post: {entry.title}') # 커밋</code></pre>
<p>🔴부분 : <code>entry.discription</code> 오타가 있었다. <code>entry.description</code>로 수정 </p>
<hr />
<h3 id="성공">성공</h3>
<p><img alt="" src="https://velog.velcdn.com/images/nuyhes/post/30c3681c-5ee1-4806-bb78-fe6b8cc27aff/image.png" /></p>
<hr />
<blockquote>
<p>참고</p>
</blockquote>
<ul>
<li><a href="https://velog.io/@ryuneng2/GitHub-velog%EC%99%80-GitHub-%EC%97%B0%EB%8F%99%ED%95%98%EA%B8%B0-velog-%EA%B8%80-%EC%9E%91%EC%84%B1-%EC%8B%9C-%EC%9E%90%EB%8F%99%EC%9C%BC%EB%A1%9C-%EA%B9%83%ED%97%88%EB%B8%8C%EC%97%90-%EC%BB%A4%EB%B0%8B%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95">https://velog.io/@ryuneng2</a></li>
</ul>
<hr />