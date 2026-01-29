<h2 id="윈도우에서-wslconfig-설정-리소스-제한--네트워크-미러링-vpn-대비">윈도우에서 <code>.wslconfig</code> 설정 (리소스 제한 &amp; 네트워크 미러링 VPN 대비)</h2>
<p>윈도우에서 <code>Win + R</code>을 누르고 <code>%USERPROFILE%</code>을 입력 후 엔터</p>
<p>해당 폴더(<code>C:\Users\jaiden</code>)에서 새 텍스트 파일을 만들고 이름을 <strong><code>.wslconfig</code></strong>로 변경한다. (확장자 <code>.txt</code>가 없어야 함)</p>
<pre><code class="language-toml">[wsl2] 
# 메모리 절반 할당 (8GB) - 빌드 속도와 멀티태스킹 최적화 
memory=8GB 

# CPU 코어 할당 - i7-1165G7은 4코어 8스레드이므로 4개 할당이 적절 
processors=4 

# [중요] VPN 사용자를 위한 네트워크 미러링 모드 
networkingMode=mirrored 
dnsTunneling=true 
autoProxy=true 

# WSL 종료 시 메모리 반환 속도 향상 
autoMemoryReclaim=gradual</code></pre>
<ol>
<li>수정한 <code>.wslconfig</code>를 저장한다.</li>
<li><strong>CMD</strong>에서 다음 명령어 입력 <code>wsl --shutdown</code></li>
<li>다시 우분투 접속 <code>wsl</code> or <code>wsl -d Ubuntu-24.04 -u &lt;NAME&gt;</code></li>
</ol>
<hr />
<h2 id="wslconfig-설정-체크">.wslconfig 설정 체크</h2>
<p>*<em>할당 메모리 체크 *</em></p>
<p>메모리 확인 명령어 <code>free -h</code> </p>
<blockquote>
<p>Mem의 Total이 잘 적용되어 있다.</p>
</blockquote>
<pre><code class="language-bash">jaiden-linux@DESKTOP-TPMO2QL:~$ free -h
               total        used        free      shared  buff/cache   available
Mem:           7.8Gi       755Mi       7.0Gi       3.2Mi       274Mi       7.0Gi
Swap:          2.0Gi          0B       2.0Gi</code></pre>
<p><strong>미러링 모드 체크</strong></p>
<p>미러링 모드 확인 명령어 <code>ip addr</code></p>
<blockquote>
<p>기존 윈도우의 설정된 IP와 물리적주소 동일한지 확인</p>
</blockquote>
<pre><code class="language-bash">jaiden-linux@DESKTOP-XXXXXXX:~$ ip addr 

1: lo: &lt;LOOPBACK,UP,LOWER_UP&gt; mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000 link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00 inet 127.0.0.1/8 scope host lo 

2: eth0: &lt;BROADCAST,MULTICAST,UP,LOWER_UP&gt; mtu 1500 qdisc mq state UP group default qlen 1000 link/ether f8:e4:3b:xx:xx:xx brd ff:ff:ff:ff:ff:ff inet 192.168.0.xx/24 brd 192.168.0.255 scope global noprefixroute eth0 

3: eth1: &lt;BROADCAST,MULTICAST&gt; mtu 1500 qdisc mq state DOWN group default qlen 1000 link/ether ca:fe:83:xx:xx:xx brd ff:ff:ff:ff:ff:ff 

...

...

...</code></pre>
<p><strong>CPU 코어 할당 체크</strong></p>
<p>코어 수 확인 명령어 <code>nproc</code> (현재 OS가 사용할 수 있는 전체 코어(프로세서)의 숫자만 딱 보여준다.)</p>
<pre><code class="language-bash">jaiden-linux@DESKTOP-TPMO2QL:~$ nproc
4</code></pre>
<hr />