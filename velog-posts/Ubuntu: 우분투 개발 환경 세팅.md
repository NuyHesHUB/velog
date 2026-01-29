<h2 id="wsl-기능-활성-여부-확인">WSL 기능 활성 여부 확인</h2>
<p><code>Win 키 + R → CMD</code> [터미널 실행]</p>
<p><code>wsl --version</code> [버전 확인] 커널 버전, WSLg 버전 표시</p>
<p><strong>설치가 되지 않은 경우</strong> : </p>
<pre><code>'wsl'은(는) 내부 또는 외부 명령, 실행할 수 있는 프로그램, 또는 배치 파일이 아닙니다.</code></pre><p><strong>설치가 된 경우</strong> : </p>
<pre><code>WSL 버전: 2.2.4.0
커널 버전: 5.15.153.1-2
WSLg 버전: 1.0.61
MSRDC 버전: 1.2.5326
Direct3D 버전: 1.611.1-81528511
DXCore 버전: 10.0.26091.1-240325-1447.ge-release
Windows 버전: 10.0.22631.4037</code></pre><p><strong>설치가 된 경우 리눅스 배포판 목록 보기</strong></p>
<p><code>wsl -l -v</code> 또는 <code>wsl --list --verbose</code> </p>
<ul>
<li><strong>wsl</strong>: Windows Subsystem for Linux</li>
<li><strong>-l</strong> or <strong>--list</strong>: 설치된 Linux 배포판 목록 보기</li>
<li><strong>-v</strong> or <strong>--verbose</strong>: 상세 정보 표시 (상태, 버전 포함)</li>
</ul>
<pre><code>출력 예시
  NAME                STATE   VERSION 
* Ubuntu-22.04        Running 2 
  docker-desktop      Running 2 
  docker-desktop-data Stopped 2</code></pre><ul>
<li><strong>NAME</strong>: 설치된 Linux 배포판 이름 (* 표시는 기본(default) 배포판)</li>
<li><strong>STATE</strong>: 현재 실행 상태 <code>Running(실행 중)</code>, <code>Stopped(정지됨)</code></li>
<li><strong>VERSION</strong>: <code>1 (WSL1 사용 중)</code>, <code>2 (WSL2 사용 중)</code></li>
</ul>
<hr />
<h2 id="windows-기능-켜기끄기-설정">Windows 기능 켜기/끄기 설정</h2>
<p><strong>Windows 기능 켜기/끄기 실행</strong></p>
<p><code>제어판 → 프로그램 및 기능 → [왼쪽 메뉴] Windows 기능 켜기/끄기</code></p>
<p>또는</p>
<p><code>Win키 → 검색 → Windows 기능 켜기/끄기</code></p>
<p><strong>목록 체크</strong></p>
<p>아래 3가지가 체크가 되어 있는지 확인</p>
<pre><code>[✓] Linux용 Windows 하위 시스템 (Windows Subsystem for Linux)
[✓] 가상 머신 플랫폼 (Virtual Machine Platform)
[✓] Windows 하이퍼바이저 플랫폼 (선택 사항이지만 체크 권장)</code></pre><hr />
<h2 id="하드웨어-가상화-활성화-여부-확인">하드웨어 가상화 활성화 여부 확인</h2>
<pre><code>1. Ctrl + Shift + Esc 를 눌러 작업 관리자 열기

2. [왼쪽 메뉴] 성능 탭 클릭

3. CPU 항목 선택

4. [오른쪽 아래] 가상화: '사용'으로 되어 있는지 확인</code></pre><blockquote>
<p>'사용 안 함' 으로 되어 있다면?</p>
</blockquote>
<p><strong>BIOS/UEFI 가상화 활성화</strong></p>
<p>PC 재부팅 후 BIOS/UEFI 진입 (보통 F2, F12, Del 키)</p>
<p>CPU 설정(Advanced, CPU Configuration 등)에서 다음 항목을 'Enabled'로 변경</p>
<p><strong>Intel:</strong> Intel Virtualization Technology, VT-x, VMX 등</p>
<hr />
<h2 id="wsl-설치-및-배포판-세팅">WSL 설치 및 배포판 세팅</h2>
<p><strong>🔗마이크로소프트 가이드</strong>  <a href="https://learn.microsoft.com/ko-kr/windows/wsl/install">WSL을 사용하여 Windows에 Linux를 설치하는 방법</a></p>
<p><strong>WSL 기본 설치</strong></p>
<p><code>wsl --install</code> 명령어 입력 (관리자 권한) → PC 재부팅</p>
<p><strong>WSL 기능은 켜져 있는데 배포판이 없다면</strong> (나의 케이스)</p>
<p>목록 확인</p>
<p><code>wsl --list --online</code> or <code>wsl -l -o</code></p>
<p>결과</p>
<pre><code class="language-powershell">다음은 설치할 수 있는 유효한 배포판 목록입니다.
'wsl.exe --install &lt;Distro&gt;'를 사용하여 설치합니다.

NAME                            FRIENDLY NAME
Ubuntu                          Ubuntu
Debian                          Debian GNU/Linux
kali-linux                      Kali Linux Rolling
Ubuntu-20.04                    Ubuntu 20.04 LTS
Ubuntu-22.04                    Ubuntu 22.04 LTS
Ubuntu-24.04                    Ubuntu 24.04 LTS
OracleLinux_7_9                 Oracle Linux 7.9
OracleLinux_8_10                Oracle Linux 8.10
OracleLinux_9_5                 Oracle Linux 9.5
openSUSE-Leap-15.6              openSUSE Leap 15.6
SUSE-Linux-Enterprise-15-SP6    SUSE Linux Enterprise 15 SP6
openSUSE-Tumbleweed             openSUSE Tumbleweed</code></pre>
<p>특정 버전(Ubuntu 24.04) 설치 </p>
<p><code>wsl --install -d Ubuntu-24.04</code></p>
<p>설치 및 유저네임 패스워드 설정</p>
<pre><code class="language-powershell">C:\Users\jaiden&gt;wsl -i -d Ubuntu-24.04
잘못된 명령줄 인수: -i
지원되는 인수 목록을 가져오려면 'wsl.exe --help'를 사용하세요.

C:\Users\jaiden&gt;wsl --install -d Ubuntu-24.04
설치 중: Ubuntu 24.04 LTS
Ubuntu 24.04 LTS이(가) 설치되었습니다.
Ubuntu 24.04 LTS을(를) 시작하는 중...
Installing, this may take a few minutes...
Please create a default UNIX user account. The username does not need to match your Windows username.
For more information visit: https://aka.ms/wslusers
Enter new UNIX username: jaiden-linux
New password: ✅패스워드
Retype new password: ✅패스워드 재입력
passwd: password updated successfully
Installation successful!
To run a command as administrator (user &quot;root&quot;), use &quot;sudo &lt;command&gt;&quot;.
See &quot;man sudo_root&quot; for details.

Welcome to Ubuntu 24.04.1 LTS (GNU/Linux 5.15.153.1-microsoft-standard-WSL2 x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

 System information as of Wed Jan 28 12:07:45 KST 2026

  System load:  0.25                Processes:             45
  Usage of /:   0.1% of 1006.85GB   Users logged in:       0
  Memory usage: 6%                  IPv4 address for eth0: 172.17.60.74
  Swap usage:   0%


This message is shown once a day. To disable it please create the
/home/jaiden-linux/.hushlogin file.
jaiden-linux@DESKTOP-TPMO2QL:~$</code></pre>
<p><strong>리눅스 배포판 설치 후 업데이트</strong></p>
<p>터미널을 열고 다음 명령어로 패키지 목록을 업데이트하고 필수 패키지를 설치한다.</p>
<pre><code class="language-bash">sudo apt update &amp;&amp; sudo apt upgrade

또는

sudo apt update &amp;&amp; sudo apt upgrade -y

# 중간에 &quot;Do you want to continue? [Y/n] Y&quot;라고 물어볼 때 자동으로 Yes라고 대답해주는 옵션</code></pre>
<hr />
<h2 id="리눅스-명령어">리눅스 명령어</h2>
<p><strong>시스템 관리 필수 명령어</strong></p>
<ul>
<li><strong><code>sudo apt update</code></strong>: 설치 가능한 패키지 리스트를 최신화</li>
<li><strong><code>sudo apt upgrade -y</code></strong>: 실제로 설치된 프로그램들을 최신 버전으로 업그레이드</li>
<li><strong><code>clear</code></strong>: 지저분해진 터미널 화면을 깨끗하게 비움 (<code>Ctrl + L</code> 단축키로도 가능)</li>
</ul>
<p><strong>파일 및 디렉토리 탐색</strong></p>
<p><strong><code>ls -al</code></strong>: 현재 폴더의 모든 파일 목록을 보기 (숨겨진 파일까지 상세히)
<strong><code>pwd</code></strong>: 현재 작업 중인 경로를 보여준다.
<strong><code>cd ~</code></strong>: 어디에 있든 내 홈 디렉토리(<code>/home/jaiden-linux</code>)로 즉시 돌아간다.
<strong><code>mkdir 폴더명</code></strong>: 새로운 폴더를 만든다.</p>
<blockquote>
<p><strong>🕵️ 윈도우와 WSL 사이의 (윈도우 도구 호출)</strong></p>
</blockquote>
<ul>
<li><strong><code>explorer.exe .</code></strong>: (점 포함) 현재 리눅스 경로를 <strong>윈도우 파일 탐색기</strong>로 연다. 리눅스 파일을 윈도우로 옮길 때 좋다.</li>
<li><strong><code>code .</code></strong>: 현재 폴더를 <strong>VS Code</strong>로 오픈. </li>
</ul>
<p><strong>시스템 상태 확인 (내 PC 자원 감시)</strong></p>
<ul>
<li><p><strong><code>htop</code></strong>: 윈도우의 '작업 관리자' 같은 기능 CPU, RAM 사용량을 실시간 그래픽으로 보여준다. (없다면 <code>sudo apt install htop</code>으로 설치)</p>
</li>
<li><p><strong><code>df -h</code></strong>: 현재 리눅스 하드 디스크 용량이 얼마나 남았는지 확인</p>
</li>
</ul>
<hr />
<h2 id="explorerexe--에러">explorer.exe . 에러</h2>
<pre><code class="language-bash">jaiden-linux@DESKTOP-TPMO2QL:~$ explorer.exe .
-bash: /mnt/c/Windows/explorer.exe: cannot execute binary file: Exec format error</code></pre>
<blockquote>
<p>cannot execute binary file: Exec format error</p>
</blockquote>
<p>&quot;cannot execute binary file: Exec format error&quot;는 ==실행하려는 프로그램이 현재 시스템의 CPU 아키텍처(예: 64-bit, ARM)나 운영체제(OS) 버전과 맞지 않을 때 발생하는 오류==로, <strong>다른 아키텍처용으로 컴파일된 파일을 실행하려 하거나</strong>, <strong>32-bit 파일을 64-bit 시스템에서 실행하려 할 때</strong>, 또는 <strong>Windows용 파일을 리눅스에서 실행</strong>하려 할 때 주로 발생합니다. 해결 방법은 <strong>해당 시스템에 맞는 아키텍처/OS용 파일로 교체</strong>하거나, <strong>가상 환경(WSL, VM)을 사용</strong>하여 맞는 환경에서 실행하는 것입니다.</p>
<p>주요 원인</p>
<ol>
<li><strong>아키텍처 불일치</strong>: 가장 흔한 원인으로, 예를 들어 ARM(M1/M2 맥, 라즈베리 파이 등)용으로 만들어진 프로그램을 x86_64(일반 PC)에서 실행하거나 그 반대로 실행하는 경우.</li>
<li><strong>32-bit / 64-bit 불일치</strong>: 32-bit용으로 컴파일된 프로그램을 64-bit 시스템의 32-bit 호환성 라이브러리(multiarch-support 등) 없이 실행하려 할 때 발생.</li>
<li><strong>운영체제(OS) 불일치</strong>: Windows용 실행 파일(.exe)을 Linux/macOS 터미널에서 직접 실행하려 할 때.</li>
<li><strong>파일 손상 또는 잘못된 파일</strong>: 다운로드 중 파일이 손상되었거나, 실행 파일이 아닌 다른 형식의 파일을 실행하려 할 때 (예: 셸 스크립트를 바이너리로 인식)</li>
</ol>
<p>🕵️ Windows용 실행 파일을 직접 실행해서 생긴 에러 같다.</p>
<p><strong>상호운용성(Interop) 설정 강제 활성화</strong></p>
<p>우분투 터미널에서 </p>
<pre><code class="language-bash">sudo nano /etc/wsl.conf</code></pre>
<p>입력 후 아래의 화면이 나온다.</p>
<pre><code class="language-bash">  GNU nano 7.2                   /etc/wsl.conf
[boot]
systemd=true

#아래 내용 추가
[interop]
enabled=true
appendWindowsPath=true



                                 [ Read 6 lines ]
^G Help  ^O Write Out  ^W Where Is  ^K Cut    ^T Execute  ^C Location    M-U Undo
^X Exit  ^R Read File  ^\ Replace   ^U Paste  ^J Justify  ^/ Go To Line  M-E Redo</code></pre>
<pre><code class="language-bash">[interop]
enabled=true
appendWindowsPath=true</code></pre>
<p><strong>저장 후 나가기:</strong> <code>Ctrl + O</code> 누르고 <code>Enter</code> (저장), 이어서 <code>Ctrl + X</code> (나가기).</p>
<p><strong>WSL 완전히 재시작:</strong> * <strong>중요:</strong> 우분투 터미널을 끄고, <strong>Windows PowerShell</strong>을 열어서 아래 명령어를 입력</p>
<pre><code class="language-powershell">wsl --shutdown</code></pre>
<p><strong>다시 리눅스 우분투 터미널로 이동</strong></p>
<pre><code>wsl -d Ubuntu-24.04 -u jaiden-linux</code></pre><p>만약</p>
<p><code>jaiden-linux@DESKTOP-TPMO2QL:/mnt/c/Users/...$</code></p>
<p>경로가 윈도우 C드라이브 경로로 되어 있다면 <code>cd ~</code> 우분투 홈으로 이동</p>
<p>다시 <code>explorer.exe .</code>로 하니 우분투 경로로 탐색기가 잘 열린다.</p>
<hr />