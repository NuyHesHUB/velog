<p><img alt="" src="https://velog.velcdn.com/images/nuyhes/post/3c501302-3db1-4d26-b29d-165abefa64ec/image.png" /></p>
<hr />
<p>🕵️ 윈도우 단축키를 잘 사용하다가 잘못눌러져서 <code>Win</code> + <code>W</code> 키를 눌러 피드(위젯) 이 켜지는 게 너무 싫었다. 
개인적으론 내가 직접 찾아서 보는게 아닌 이상 위젯이나 이런게 뜨는게 불필요한 기능이다. 그래서 윈도우를 처음 깔면 지우거나 비활성화하는게 되게 많은데 위젯 단축키 비활성화 방법이다.</p>
<hr />
<h2 id="1-로컬-그룹-정책-편집기로-비활성화">1. 로컬 그룹 정책 편집기로 비활성화</h2>
<ol>
<li><code>Win</code> + <code>R</code> → <code>gpedit.msc</code> 입력 → Enter</li>
</ol>
<p><img alt="" src="https://velog.velcdn.com/images/nuyhes/post/093570d4-1c65-45e6-98be-0cab0fe39750/image.png" /></p>
<ol start="2">
<li>컴퓨터 구성 &gt; 관리 템플릿 &gt; Windows 구성 요소 &gt; 위젯
오른쪽에서 <strong>&quot;위젯 허용&quot;</strong>을 두 번 클릭</li>
</ol>
<p><img alt="" src="https://velog.velcdn.com/images/nuyhes/post/1775dfd2-9754-4f6b-88d0-b00aba960a5f/image.png" /></p>
<ol start="3">
<li><strong>&quot;사용 안 함&quot;</strong>으로 설정 → 적용</li>
</ol>
<p><img alt="" src="https://velog.velcdn.com/images/nuyhes/post/423dea6d-38cf-4ac8-aa40-5b060d5b7887/image.png" /></p>
<hr />
<h2 id="2-레지스트리-편집기로-비활성화">2. 레지스트리 편집기로 비활성화</h2>
<ol>
<li><code>Win</code> + <code>R</code> → <code>regedit</code> 입력 → Enter</li>
</ol>
<p><img alt="" src="https://velog.velcdn.com/images/nuyhes/post/a499a89b-d779-4cd0-b829-837fdc8da8ed/image.png" /></p>
<ol start="2">
<li><code>HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft
DWM</code> 또는 <code>Windows</code> 아래에 <code>Windows Widgets</code>라는 키가 없으면 새로 만듭니다.
오른쪽 클릭 → 새로 만들기 → 키 → Windows Widgets</li>
</ol>
<p><img alt="" src="https://velog.velcdn.com/images/nuyhes/post/41d23c9b-944b-4694-aa83-cd084cdbbd7c/image.png" /></p>
<ol start="3">
<li>해당 키 안에 새 <code>DWORD(32비트)</code> 값 생성
이름: AllowWidgets
값: 0</li>
</ol>
<p><img alt="" src="https://velog.velcdn.com/images/nuyhes/post/fa4a0a05-ca60-4745-9965-b2fd240b5b82/image.png" /></p>
<ol start="4">
<li>컴퓨터 재부팅</li>
</ol>
<hr />
<h2 id="3-powershell로-완전히-제거-위험성-있음">3. PowerShell로 완전히 제거 (위험성 있음)</h2>
<ol>
<li><code>PowerShell</code> 관리자로 실행</li>
</ol>
<p><img alt="업로드중.." src="blob:https://velog.io/56b7bafe-01e0-4761-90e3-e8201dbc1dcc" /></p>
<ol start="2">
<li><code>Get-AppxPackage *WebExperience* | Remove-AppxPackage</code> 명령어 입력</li>
</ol>
<ul>
<li><p>이 명령어는 Web Experience Pack을 제거해서 위젯 기능을 없애는 방법입니다.</p>
</li>
<li><p>Windows 업데이트 이후 다시 설치될 수 있고, 다른 시스템 요소에 영향 줄 수 있어 권장하지 않습니다.</p>
</li>
</ul>
<pre><code># 관리자: Windows PowerShell

Get-AppxPackage *WebExperience* | Remove-AppxPackage</code></pre><p><img alt="업로드중.." src="blob:https://velog.io/f2c02652-4a4c-4baf-99a4-28a946a22541" /></p>
<hr />