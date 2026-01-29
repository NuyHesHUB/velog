<h2 id="wsl2-ubuntu-개발-환경-세팅nvm-nodejs-npm">WSL2 Ubuntu 개발 환경 세팅(NVM, Node.js, NPM)</h2>
<h3 id="nvm-설치">NVM 설치</h3>
<p><strong>우분투 터미널 설치 명령어</strong></p>
<pre><code class="language-bash">curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash</code></pre>
<p><strong>결과</strong></p>
<pre><code class="language-bash">jaiden-linux@DESKTOP-TPMO2QL:~$ curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 16555  100 16555    0     0   326k      0 --:--:-- --:--:-- --:--:--  329k
=&gt; Downloading nvm from git to '/home/jaiden-linux/.nvm'
=&gt; Cloning into '/home/jaiden-linux/.nvm'...
remote: Enumerating objects: 399, done.
remote: Counting objects: 100% (399/399), done.
remote: Compressing objects: 100% (328/328), done.
remote: Total 399 (delta 57), reused 261 (delta 43), pack-reused 0 (from 0)
Receiving objects: 100% (399/399), 400.18 KiB | 15.39 MiB/s, done.
Resolving deltas: 100% (57/57), done.
* (HEAD detached at FETCH_HEAD)
  master
=&gt; Compressing and cleaning up git repository

=&gt; Appending nvm source string to /home/jaiden-linux/.bashrc
=&gt; Appending bash_completion source string to /home/jaiden-linux/.bashrc
=&gt; You currently have modules installed globally with `npm`. These will no
=&gt; longer be linked to the active version of Node when you install a new node
=&gt; with `nvm`; and they may (depending on how you construct your `$PATH`)
=&gt; override the binaries of modules installed with `nvm`:

C:\Users\jaiden\AppData\Roaming\npm
+-- @nestjs/cli@11.0.16
+-- @vue/cli@5.0.8
`-- create-vite@5.5.2
=&gt; If you wish to uninstall them at a later point (or re-install them under your
=&gt; `nvm` Nodes), you can remove them from the system Node as follows:

     $ nvm use system
     $ npm uninstall -g a_module

=&gt; Close and reopen your terminal to start using nvm or run the following to use it now:

export NVM_DIR=&quot;$HOME/.nvm&quot;
[ -s &quot;$NVM_DIR/nvm.sh&quot; ] &amp;&amp; \. &quot;$NVM_DIR/nvm.sh&quot;  # This loads nvm
[ -s &quot;$NVM_DIR/bash_completion&quot; ] &amp;&amp; \. &quot;$NVM_DIR/bash_completion&quot;  # This loads nvm bash_completion</code></pre>
<p>🕵️ 중간에 <code>C:\Users\jaiden\AppData\Roaming\npm</code> 경로와 함께 기존 윈도우에 설치된 목록들이 나와서 의아했는데</p>
<p><strong>&quot;너 윈도우 쪽에 전역(Global)으로 깔아둔 npm 패키지들이 있네? 리눅스 nvm으로 노드를 새로 깔면 얘네랑은 별개로 관리될 거야&quot;</strong>라고 안내해 주는 것이다.</p>
<p><strong>NVM 명령어 활성화</strong></p>
<p>설정적용 명령어</p>
<p><code>source ~/.bashrc</code></p>
<p>Node.js LTS 버전 설치</p>
<p><code>nvm install --lts</code></p>
<pre><code class="language-bash">jaiden-linux@DESKTOP-TPMO2QL:~$ nvm install --lts
Installing latest LTS version.
Downloading and installing node v24.13.0...
Downloading https://nodejs.org/dist/v24.13.0/node-v24.13.0-linux-x64.tar.xz...
######################################################################################################################## 100.0%
Computing checksum with sha256sum
Checksums matched!
Now using node v24.13.0 (npm v11.6.2)
Creating default alias: default -&gt; lts/* (-&gt; v24.13.0)</code></pre>
<p><strong>버전 확인</strong></p>
<pre><code class="language-bash">jaiden-linux@DESKTOP-TPMO2QL:~$ node -v
v24.13.0
jaiden-linux@DESKTOP-TPMO2QL:~$ npm -v
11.6.2
jaiden-linux@DESKTOP-TPMO2QL:~$ nvm -v
0.39.7</code></pre>
<hr />
<h3 id="vs-code-연동하기">VS Code 연동하기</h3>
<p><strong>우분투 디렉토리 생성</strong></p>
<p><strong>우분투 홈 디렉토리</strong>에 프로젝트 폴더를 하나 만든다</p>
<blockquote>
<p>윈도우 경로인 <code>/mnt/c/...</code>가 아닌 리눅스 홈 디렉토리 만든다</p>
</blockquote>
<pre><code class="language-bash">mkdir -p ~/projects/test-node 

cd ~/projects/test-node</code></pre>
<p><strong>VS Code 실행 (WSL 연결)</strong></p>
<p>해당 <code>test-node</code>에서 <code>code .</code> 명령어 입력</p>
<p><strong>결과</strong></p>
<pre><code class="language-bash">jaiden-linux@DESKTOP-TPMO2QL:~/projects/test-node$ code .
Installing VS Code Server for Linux x64 (c9d77990917f3102ada88be140d28b038d1dd7c7)
Downloading: 100%
Unpacking: 100%
Unpacked 2202 files and folders to /home/jaiden-linux/.vscode-server/bin/c9d77990917f3102ada88be140d28b038d1dd7c7.
Looking for compatibility check script at /home/jaiden-linux/.vscode-server/bin/c9d77990917f3102ada88be140d28b038d1dd7c7/bin/helpers/check-requirements.sh
Running compatibility check script
Compatibility check successful (0)</code></pre>
<p>위와 같이 성공 후 <code>VS Code</code>프로그램이 실행되는데 왼쪽 하단 구석에 <code>&gt;&lt;</code> 파란색바에 <strong>해당 리눅스 배포판</strong>이 뜨면 성공 나는 Ubuntu-24.04 배포판을 사용하여 하단에 </p>
<blockquote>
<p>WSL: Ubuntu-24.04 버전이 뜬다.</p>
</blockquote>
<p>해당 VS Code에서 샘플용 새 <code>.js</code>파일을 만든다. </p>
<p>ex) <code>app.js</code> 생성</p>
<pre><code class="language-js">const os = require('os');

console.log(&quot;-----------------------------------------&quot;);
console.log(&quot;🚀 Hello WSL! Node.js is running here.&quot;);
console.log(`💻 OS Platform: ${os.platform()}`);
console.log(`🧠 Allocated Memory: ${(os.totalmem() / 1024 / 1024 / 1024).toFixed(2)} GB`);
console.log(`🔥 Node.js Version: ${process.version}`);
console.log(&quot;-----------------------------------------&quot;);</code></pre>
<p>해당 터미널에서 <code>app.js</code> 콘솔 찍어보기 WSL <code>.wslconfig</code>설정과 OS 체크를 확인해본다.</p>
<p><code>node app.js</code></p>
<pre><code class="language-bash">jaiden-linux@DESKTOP-TPMO2QL:~/projects/test-node$ node app.js
-----------------------------------------
🚀 Hello WSL! Node.js is running here.
💻 OS Platform: linux
🧠 Allocated Memory: 7.76 GB
🔥 Node.js Version: v24.13.0
-----------------------------------------</code></pre>
<hr />