<blockquote>
<p>🕵️ 문제점</p>
</blockquote>
<p>WSL 환경에서 Git 작업을 하면 매번 인증 처리를 요구한다.
그래서 찾아봤더니 윈도우와 인증 처리 방식이 다르기 때문이라고 한다.</p>
<hr />
<p><strong>차이점</strong></p>
<p><code>Windows Git</code></p>
<ul>
<li>Git Credential Manager(GCM) 자동설치</li>
<li>Windows 자격 증명 관리자에 비밀번호 저장</li>
<li>한 번 입력하면 계속 사용</li>
</ul>
<p><code>WSL Git</code></p>
<ul>
<li>독립적인 Linux 환경</li>
<li>기본적으로 credential helper 없음</li>
<li>매번 인증정보 요구</li>
</ul>
<hr />
<h2 id="https-방식-글로벌-credential-도메인별-등록">HTTPS 방식 글로벌 Credential 도메인별 등록</h2>
<p><strong><code>Linux</code>의 <code>Git Credential Manager</code>를 사용</strong></p>
<p>해당 Git 서버의 credential을 각 저장소 별로 처리하게 되면 각 저장소 마다 설정을 해야해서 비효율적이다. 특정 서버를 글로벌 설정을 적용하여 모든 저장소에서 해당 인증정보를 사용하기 위해 아래와 같이 설정했다.</p>
<pre><code class="language-shell"># 특정 Git 서버에 대한 글로벌 credential helper 설정
git config --global credential.https://gitlab.example.com.helper store

# 이후 해당 서버에 처음 접근할 때 한 번만 인증 정보를 입력하면 됨
UserName for 'https://gitlab.example.com': your_username
Password for 'https://your_username@example.com': your_password</code></pre>
<p>입력한 인증정보가 <code>~/.git-credentials</code> 파일에 저장되어 동일한 서버를 사용하는 모든 프로젝트에서 자동으로 인증된다.</p>
<p><strong><code>Linux</code>의 <code>Git Credential Manager</code>설정 확인</strong></p>
<pre><code class="language-shell"># 깃 입력한 정보 설정 확인 명령어
cat ~/.gitconfig

# .gitconfig 파일
[user]
        email = your_username@example.com
        name = your_username
[credential &quot;https://gitlab.example.com&quot;]
        helper = store

# 깃 입력한 인증 정보
cat ~/.git-credentials

# .git-credentials 파일
https://your_username:****@gitlab.example.com</code></pre>
<hr />
<h2 id="ssh-방식">SSH 방식</h2>
<p><strong>SSH Key 생성</strong></p>
<p>암호화 알고리즘 <strong>ed25519 방식</strong></p>
<pre><code class="language-shell"># 우분투 터미널
ssh-keygen -t ed25519 -C &quot;**@example.com&quot;

# 이후 나오는 설정 그냥 Enter(비밀번호 없이 생성)
Generating public/private ed25519 key pair.
Enter file in which to save the key (/home/jaiden-linux/.ssh/id_ed25519):
Created directory '/home/jaiden-linux/.ssh'.
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /home/jaiden-linux/.ssh/id_ed25519
Your public key has been saved in /home/jaiden-linux/.ssh/id_ed25519.pub
The key fingerprint is:
SHA256:5if.......................................... **@example.com
The key's randomart image is:
+--[ED25519 256]--+
|           ==+   |
|      . . *....  |
|     . = . o.  . |
|      o =.  . . .|
|       oS=o..+ o |
|       o=.+++oo .|
|        ++++.+o..|
|        .=E.o +..|
|         ..+.+.. |
+----[SHA256]-----+</code></pre>
<hr />
<p>암호화 알고리즘 <strong>RSA 방식</strong></p>
<pre><code class="language-shell"># 우분투 터미널
ssh-keygen -t rsa -b 4096 -C &quot;**@example.com&quot;

# 이후 나오는 설정 그냥 Enter(비밀번호 없이 생성)
Generating public/private rsa key pair.
Enter file in which to save the key (/home/jaiden-linux/.ssh/id_rsa):
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /home/jaiden-linux/.ssh/id_rsa
Your public key has been saved in /home/jaiden-linux/.ssh/id_rsa.pub
The key fingerprint is:
SHA256:gKNY.......................................... **@example.com
The key's randomart image is:
+---[RSA 4096]----+
|. o   ....oo     |
|oo = +.oo..      |
|= + =.o.         |
|o+ . ...  o      |
|o .    .So .+ = o|
|      . o  o * *o|
|       +    = o E|
|      . = oo.. = |
|       + o.o  ..o|
+----[SHA256]-----+</code></pre>
<hr />
<p>이제 <code>~/.ssh/</code>폴더에 <code>id_&lt;암호화알고리즘&gt;</code>와 <code>id_&lt;암호화알고리즘&gt;.pub</code>파일이 생긴다.</p>
<ul>
<li><code>id_&lt;암호화알고리즘&gt;</code>: 개인키 (유출 금지)</li>
<li><code>id_&lt;암호화알고리즘&gt;.pub</code>: 깃랩/깃허브에 줄 공개키</li>
</ul>
<p><code>cat ~/.ssh/id_암호화알고리즘.pub</code> 또는 해당 디렉토리 기준이면 <code>cat id_ed25519.pub</code> or <code>cat id_rsa.pub</code></p>
<blockquote>
<p>ex) id_ed25519.pub</p>
</blockquote>
<pre><code class="language-shell">jaiden-linux@DESKTOP-TPMO2QL:~/.ssh$ cat id_ed25519.pub
ssh-ed25519 AAAA.../v+OX.....+iz... **@example.com</code></pre>
<p>해당 <code>ssh-ed25519</code> or <code>ssh-ras</code>로 시작하는 문자열 키 전체 복사</p>
<hr />
<h2 id="gitlab-기준-ssh-key-설정">GitLab 기준 SSH Key 설정</h2>
<blockquote>
<p>GitLab</p>
</blockquote>
<ul>
<li><p><strong>GitLab 접속</strong> -&gt; 우측 상단 프로필 클릭 -&gt; <strong>Edit Profile</strong> (또는 Preferences)</p>
</li>
<li><p>왼쪽 메뉴에서 <strong>[SSH Keys]</strong> 클릭</p>
</li>
<li><p><strong>[Add new key]</strong> 버튼 클릭</p>
</li>
<li><p><strong>Key</strong> 칸에 방금 복사한 내용을 붙여넣기</p>
</li>
<li><p><strong>Title</strong>은 <code>WSL-Ubuntu</code> 정도로 적고 <strong>[Add key]</strong> 클릭</p>
</li>
<li><p><strong>key</strong> : <code>id_ed25519.pub</code> 복사한 키 붙여넣기 </p>
</li>
<li><p><strong>Title</strong> :  타이틀 입력</p>
</li>
</ul>
<hr />
<blockquote>
<p>Git 주소를 SSH용으로 바꾸기</p>
</blockquote>
<p>기존에 <code>https://...</code>로 시작하는 주소는 SSH 열쇠를 쓰지 않고 주소를 SSH 형식으로 바꿔줘야 한다.</p>
<hr />
<p><strong>EX)</strong></p>
<ul>
<li><strong>기존 주소:</strong> <code>https://gitlab.example.com/그룹/프로젝트명.git</code></li>
<li><strong>SSH 주소:</strong> <code>git@gitlab.example.com:그룹/프로젝트명.git</code> (깃랩 프로젝트 페이지의 <strong>Clone</strong> 버튼을 누르면 SSH 주소를 복사할 수 있다.)</li>
</ul>
<hr />
<blockquote>
<p>우분투 터미널로 돌아와서</p>
</blockquote>
<pre><code class="language-shell"># 1. 프로젝트 폴더로 이동 
cd ~/projects/exam-front-app 

# 2. 주소를 SSH 형식으로 변경 
# 형식: git@도메인:그룹/프로젝트명.git git remote set-url origin &lt;SSH 주소&gt;.git 

# 3. 잘 바뀌었는지 확인 git remote -v
# 이후 clone width ssh 주소를 복사해서 사용 하면 됨</code></pre>
<hr />