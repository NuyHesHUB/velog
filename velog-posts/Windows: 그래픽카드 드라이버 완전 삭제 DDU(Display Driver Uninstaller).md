<hr />
<p>🕵️ <code>Windows</code>에서 <code>그래픽카드 드라이버</code>를 삭제하고 다시 설치하는 방법 중 완전히 삭제하는 툴을 사용하여 재설치하는 방법을 알게되어 글을 쓰게 되었다. </p>
<p>기본적으로 삭제하는 방식과 DDU : Display Driver Uninstaller 를 사용하여 재설치하는 방법을 알아보자.</p>
<hr />
<h2 id="1-그래픽-드라이버-제거-windows-기본-방식">1. 그래픽 드라이버 제거 (Windows 기본 방식)</h2>
<ol>
<li><strong>장치 관리자 열기</strong></li>
</ol>
<ul>
<li><code>Win + X</code> → <strong>장치 관리자</strong> 선택<br />  또는 시작 메뉴에 <code>장치 관리자</code> 검색</li>
</ul>
<ol start="2">
<li><strong>디스플레이 어댑터 항목 찾기</strong></li>
</ol>
<ul>
<li><p>보통 <code>Intel UHD Graphics</code>, <code>Intel Iris Xe</code>, 또는 <code>NVIDIA MX450</code> 같은 이름이 있다.</p>
<p>  <img alt="" src="https://velog.velcdn.com/images/nuyhes/post/5914aded-9aea-41fd-a82b-02c75b9d0eb0/image.png" /></p>
</li>
</ul>
<ol start="3">
<li>** 디바이스 제거**</li>
</ol>
<ul>
<li><p>해당 항목을 <strong>우클릭</strong> → <code>디바이스 제거</code></p>
</li>
<li><p>→ <strong>제거</strong></p>
<p>  <img alt="" src="https://velog.velcdn.com/images/nuyhes/post/f5059f0b-3fec-49a7-892c-5408f545e3d8/image.png" /></p>
</li>
</ul>
<ol start="4">
<li><strong>재부팅</strong></li>
</ol>
<ul>
<li>제거 후 <strong>재부팅</strong>하면 Windows가 기본 드라이버로 자동 부팅됨 </li>
</ul>
<hr />
<h2 id="2-드라이버-재설치">2. 드라이버 재설치</h2>
<h3 id="방법-1-제조사-공식-드라이버-사용">방법 1: 제조사 공식 드라이버 사용</h3>
<hr />
<p>🕵️나는 현재 사용하는 업무용 노트북은 MSI 제조사이다.</p>
<ul>
<li><p>MSI 공식 홈페이지: MSI Summit B14 Support</p>
</li>
<li><p>모델명에 따라 아래 항목 선택 → <strong>VGA Driver</strong> 다운로드<br />  (Intel/NVIDIA 둘 다 있다면 둘 다 설치)</p>
</li>
</ul>
<hr />
<h3 id="방법-2-intelnvidia-공식-최신-드라이버">방법 2: Intel/NVIDIA 공식 최신 드라이버</h3>
<ul>
<li><p><strong>Intel 그래픽 드라이버</strong> (Iris Xe 등):<br />  👉 <a href="https://www.intel.com/content/www/us/en/download/19344/intel-graphics-windows-dch-drivers.html">https://www.intel.com/content/www/us/en/download/19344/intel-graphics-windows-dch-drivers.html</a></p>
</li>
<li><p><strong>NVIDIA 드라이버 (MX 시리즈 등)</strong>:  
  👉 <a href="https://www.nvidia.com/Download/index.aspx">https://www.nvidia.com/Download/index.aspx</a></p>
</li>
</ul>
<blockquote>
<p>설치 후 재부팅하면 정상 적용된다.</p>
</blockquote>
<hr />
<h2 id="💡3-ddu-display-driver-uninstaller를-사용한-깔끔한-제거-선택사항">💡3. DDU (Display Driver Uninstaller)를 사용한 깔끔한 제거 (선택사항)</h2>
<ul>
<li><p>완전히 제거하고 싶다면 무료 툴인 <strong>DDU</strong> 사용 가능</p>
</li>
<li><p>👉 <a href="https://www.wagnardsoft.com/">https://www.wagnardsoft.com/</a></p>
</li>
<li><p>안전모드에서 실행 → 기존 드라이버 흔적 없이 제거해줌</p>
</li>
</ul>
<hr />
<h3 id="🕵️-안전모드-실행-방법">🕵️ 안전모드 실행 방법</h3>
<ol>
<li><p><code>win</code> + <code>i</code>로 설정을 연다</p>
</li>
<li><p>왼쪽 메뉴에서 [시스템] → [복구] 선택</p>
</li>
</ol>
<p><img alt="" src="https://velog.velcdn.com/images/nuyhes/post/adb01156-baa5-486a-9180-0f2b989269ec/image.png" /></p>
<ol start="3">
<li>오른쪽에서 [고급 시작 옵션] → [지금 다시 시작] 클릭</li>
</ol>
<p><img alt="" src="https://velog.velcdn.com/images/nuyhes/post/285aa857-65c3-400c-bdb3-07466a12766e/image.png" /></p>
<p>다시 시작되면 옵션 선택 화면이 나온다:</p>
<p>[문제 해결] → [고급 옵션] → [시작 설정] → [다시 시작] 클릭</p>
<blockquote>
<p>재부팅 후 숫자 키를 눌러 선택:</p>
</blockquote>
<p>4: 안전모드</p>
<p>5: 네트워크 포함 안전모드</p>
<p>6: 명령 프롬프트 포함 안전모드</p>
<hr />
<h3 id="안전모드에서-ddu-실행">안전모드에서 DDU 실행</h3>
<ol>
<li>---장치 유형 선택--- / ---장치 선택--- 을 셀렉트한다.</li>
</ol>
<p><img alt="" src="https://velog.velcdn.com/images/nuyhes/post/ac58922b-fc2a-4f13-b799-e2018606d7e4/image.png" /></p>
<hr />
<ol start="2">
<li>셀렉트를 하고 나서 <code>지우고. 다시 시작(적극 권장)</code></li>
</ol>
<p><img alt="" src="https://velog.velcdn.com/images/nuyhes/post/bf0da00d-773f-403b-8f33-a51f7ca3c0cf/image.png" /></p>
<ol start="3">
<li>그리고 나서 해당 그래픽 카드 드라이버를 재설치한다. </li>
</ol>
<hr />