<hr />
<h3 id="🕵️-인텔리제이로-jsp-생성-및-실행">🕵️ 인텔리제이로 JSP 생성 및 실행</h3>
<p>기존 이클립스로 JSP 프로젝트를 실행하였으나 인텔리제이를 사용하여 생성을 하는 방법을 알아보자</p>
<blockquote>
<p>필요한 프로그램</p>
</blockquote>
<ol>
<li>IntelliJ Ultimate version</li>
<li>Java EE</li>
<li>Tomcat 9.x</li>
</ol>
<blockquote>
<p>Step</p>
</blockquote>
<p><code>New Project</code>를 클릭 &gt; <code>Jakarta EE</code>선택 &gt; Version   : Java EE 8 선택 후 Create &gt; <code>Edit Configurations</code> 설정 &gt; Run</p>
<hr />
<h4 id="💡step">💡Step</h4>
<ol>
<li>인텔리제이를 실행 후 <code>New Project</code>를 클릭</li>
</ol>
<p><img alt="" src="https://velog.velcdn.com/images/nuyhes/post/afefcea6-5443-4051-8098-1ededeed85d3/image.png" /></p>
<hr />
<ol start="2">
<li><code>Jakarta EE</code>를 선택 프로젝트이름 , Template 설정 , Application server 설정 , JDK 버전 선택</li>
</ol>
<p><img alt="" src="https://velog.velcdn.com/images/nuyhes/post/969e55ca-eefd-43e5-87d4-3fc555f9dbd8/image.png" /></p>
<hr />
<ol start="3">
<li>Jakarta EE (구 Java EE) 버전 선택</li>
</ol>
<p><img alt="" src="https://velog.velcdn.com/images/nuyhes/post/1e539424-8fef-4096-b052-e14377abda7d/image.png" /></p>
<hr />
<h4 id="🕵️-jakarta-ee-구-java-ee-버전-특징">🕵️ Jakarta EE (구 Java EE) 버전 특징</h4>
<table>
<thead>
<tr>
<th>Jakarta EE 버전</th>
<th>Java 호환성</th>
<th>주요 특징</th>
<th>추천 상황</th>
</tr>
</thead>
<tbody><tr>
<td>Jakarta EE 8</td>
<td>Java 8~11</td>
<td>Java EE에서 Jakarta EE로 이름 변경된 첫 버전 (API는 Java EE 8과 동일)</td>
<td><strong>보수적이고 안정적인 개발 환경</strong>이 필요할 때</td>
</tr>
<tr>
<td>Jakarta EE 9</td>
<td>Java 11 이상</td>
<td><code>javax.*</code> → <code>jakarta.*</code> 네임스페이스 변경</td>
<td>새 프로젝트이며 최신 네임스페이스를 도입하고 싶을 때</td>
</tr>
<tr>
<td>Jakarta EE 10</td>
<td>Java 11 이상</td>
<td>네임스페이스 통일 + 새로운 기능 다수 추가</td>
<td><strong>최신 기능을 활용한 개발</strong>, <strong>Spring 없는 순수 Jakarta 프로젝트</strong></td>
</tr>
<tr>
<td>Jakarta EE 11</td>
<td>Java 21 이상</td>
<td>모듈화 개선, JSON 처리 등 강화</td>
<td><strong>Java 21 사용</strong>, 최신 스펙 적극 활용</td>
</tr>
</tbody></table>
<hr />
<h4 id="🔍-jakarta-ee-구-java-ee-버전-선택-가이드">🔍 Jakarta EE (구 Java EE) 버전 선택 가이드</h4>
<ol>
<li><p><strong>회사나 팀이 안정성을 중시</strong>하고 있다면<br /> → <strong>Jakarta EE 8</strong> (Java EE와 거의 동일, 이식성 좋음)</p>
</li>
<li><p><strong>최신 Jakarta API로 마이그레이션 고려 중</strong>이라면<br /> → <strong>Jakarta EE 9</strong> 이상</p>
</li>
<li><p><strong>Spring 없이 순수 Jakarta EE 구조로 현대적인 웹앱을 만든다</strong>면  
 → <strong>Jakarta EE 10 or 11</strong></p>
</li>
</ol>
<hr />
<ol start="4">
<li>프로젝트가 생성되면 상단 <code>Run</code> 버튼 쪽엣 <code>Edit Configurations</code>를 선택</li>
</ol>
<p><img alt="" src="https://velog.velcdn.com/images/nuyhes/post/2177754c-8646-4e3c-8ec6-1de54ea193ff/image.png" /></p>
<hr />
<ol start="5">
<li>Server 탭에서 톰캣을 설정 , <code>Configure</code>에서 톰캣이 설치된 경로 선택 , 오픈 브라우저 선택 , HTTP 포트 설정</li>
</ol>
<p><img alt="" src="https://velog.velcdn.com/images/nuyhes/post/1fb2ddd5-6e2f-4f58-8c43-fe493286cd3a/image.png" /></p>
<hr />
<ol start="6">
<li>Deployment 탭에서 <code>war exploded</code> 확인</li>
</ol>
<p><img alt="" src="https://velog.velcdn.com/images/nuyhes/post/b16718d9-99dd-45c2-b7ec-e0d5eccf8969/image.png" /></p>
<hr />
<ol start="7">
<li>프로젝트 생성 후 해당 프로젝트 폴더에 <code>F4</code> 및 우 클릭 <code>Open Module Setting</code> 클릭</li>
</ol>
<p><img alt="" src="https://velog.velcdn.com/images/nuyhes/post/6bb48fd1-e441-4c00-890a-3e3e7930ab03/image.png" /></p>
<hr />
<ol start="8">
<li>Project Setting &gt; Project 에서 <code>Language level</code> 선택 및 체크</li>
</ol>
<p><img alt="" src="https://velog.velcdn.com/images/nuyhes/post/3d2a8d7c-f68b-4b42-8606-54b9b9b82d75/image.png" /></p>
<hr />
<h4 id="🕵️-language-level-옵션-특징">🕵️ Language Level 옵션 특징</h4>
<table>
<thead>
<tr>
<th>Language Level</th>
<th>주요 특징</th>
<th>사용 가능 문법 예시</th>
</tr>
</thead>
<tbody><tr>
<td>8</td>
<td>람다, 스트림 도입</td>
<td><code>()-&gt;{}</code></td>
</tr>
<tr>
<td>9</td>
<td>모듈 시스템 도입</td>
<td><code>module-info.java</code></td>
</tr>
<tr>
<td>10</td>
<td><code>var</code> 지역변수 사용</td>
<td><code>var name = &quot;abc&quot;;</code></td>
</tr>
<tr>
<td>11</td>
<td><code>var</code> in lambda 파라미터</td>
<td><code>(var x) -&gt; x * 2</code></td>
</tr>
<tr>
<td>14</td>
<td>switch expression</td>
<td><code>switch (x) { case 1 -&gt; &quot;A&quot;; }</code></td>
</tr>
<tr>
<td>17</td>
<td>sealed classed 등</td>
<td><code>sealed class A permits B {}</code></td>
</tr>
</tbody></table>
<p>💡 <strong>SDK default</strong></p>
<ul>
<li><p>&quot;SDK default&quot;는 <strong>현재 설정된 Project SDK의 버전에 맞춰 자동으로 Language Level을 설정</strong>한다는 뜻이다.</p>
</li>
<li><p>예를 들어 <code>Project SDK</code>가 Java 11이라면 → Language Level도 자동으로 Java 11로 맞춰진다.</p>
</li>
<li><p><code>Project SDK</code>가 Java 17이면 → Language Level도 Java 17로 설정된다.</p>
</li>
</ul>
<hr />
<ol start="9">
<li><code>HelloServlet.java</code> , <code>index.jsp</code> , <code>web.xml</code> 파일 확인 후 실행</li>
</ol>
<p><img alt="" src="https://velog.velcdn.com/images/nuyhes/post/4e53fceb-f0a8-4b7f-a643-e3a097bb98f5/image.png" /></p>
<hr />