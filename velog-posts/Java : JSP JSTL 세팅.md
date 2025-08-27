<hr />
<h2 id="🕵️jstl이란">🕵️JSTL이란?</h2>
<p><strong>JSTL(JavaServer Pages Standard Tag Library)</strong>는 JSP에서 자주 쓰이는 기능을 표준 태그로 묶어둔 라이브러리이다.</p>
<p>원래 JSP는 <code>&lt;% ... %&gt;</code> 같은 스크립틀릿(Java 코드)을 직접 HTML에 넣어서 쓰곤 했는데 이 방식은 코드가 지저분하고 유지보수가 어려웠다</p>
<p>그래서 <strong>JSTL</strong>은 JSP화면에서 자바 코드를 직접 쓰지 않고 태그 문법(XML/HTML 비슷한 형태)으로 표현할 수 있게 해주는 표준 라이브러리이다.</p>
<hr />
<h2 id="📌-설치">📌 설치</h2>
<h3 id="1️⃣jar-다운로드-및-적용-순수-자바-프로젝트">1️⃣jar 다운로드 및 적용 (순수 자바 프로젝트)</h3>
<ol>
<li><a href="https://mvnrepository.com/artifact/javax.servlet/jstl/1.2">MVN 다운로드</a> 해당 링크에 들어가서 <code>jar</code>파일을 다운로드한다</li>
<li>프로젝트에 <code>jar</code>파일을 추가한다.<pre><code>프로젝트 루트
└─ src
└─ web
  └─ WEB-INF
      └─ lib
          └─ jstl-1.2.jar   ← 여기에 복사</code></pre></li>
<li>IntelliJ에서 라이브러리 등록
```</li>
</ol>
<ul>
<li><p>File → Project Structure (Ctrl+Alt+Shift+S</p>
</li>
<li><p>Modules → Dependencies 탭 이동</p>
</li>
<li><ul>
<li>클릭 → JARs or directories... 선택</li>
</ul>
</li>
<li><p>WEB-INF/lib/jstl-1.2.jar 선택 → 추가</p>
<pre><code></code></pre></li>
</ul>
<hr />
<p>💡 - 원래 Maven 프로젝트에서는 <strong>pom.xml에 dependency 등록</strong>하는 게 표준이다.</p>
<ul>
<li><p>직접 jar를 <code>WEB-INF/lib</code>에 넣으면 Maven이 관리하지 않아서</p>
<ul>
<li><strong>빌드할 때 누락될 수 있고</strong></li>
<li><strong>의존성 충돌 관리가 어렵다.</strong></li>
</ul>
</li>
<li><p>하지만 <strong>수동 테스트용 / 네트워크가 안될 때 / 버전 문제 해결</strong> 목적으로 jar를 직접 넣는 경우가 있다.</p>
</li>
</ul>
<hr />
<h3 id="2️⃣maven-의존성-추가">2️⃣Maven 의존성 추가</h3>
<ol>
<li><p>📄<code>pom.xml</code>에 JSTL의 의존성을 추가한다</p>
<pre><code class="language-xml">...
...
&lt;dependency&gt;
 &lt;groupId&gt;javax.servlet&lt;/groupId&gt;
 &lt;artifactId&gt;jstl&lt;/artifactId&gt;
 &lt;version&gt;1.2&lt;/version&gt;
&lt;/dependency&gt;</code></pre>
</li>
<li><p><code>IntelliJ</code>에서 <code>pom.xml</code>을 저장하고 <code>Maven</code>탭 → <code>Reload All Maven Projects</code> 버튼을 클릭 (이 과정을 통해 <code>jstl-1.2.jar</code>가 자동으로 받아지고 <code>External Libraries</code>에 추가된다)</p>
</li>
</ol>
<hr />
<h2 id="📌적용">📌적용</h2>
<p>아래와 같이 <code>JSP</code> 파일 최상단에 <strong>한 번 선언</strong>하면 해당 JSP 안에서 JSTL 태그를 사용할 수 있다.</p>
<pre><code class="language-jsp">&lt;%@ taglib prefix=&quot;c&quot; uri=&quot;http://java.sun.com/jsp/jstl/core&quot; %&gt;
&lt;%@ taglib prefix=&quot;fmt&quot; uri=&quot;http://java.sun.com/jsp/jstl/fmt&quot; %&gt;
&lt;%@ taglib prefix=&quot;fn&quot; uri=&quot;http://java.sun.com/jsp/jstl/functions&quot; %&gt;</code></pre>
<h3 id="예시">예시</h3>
<p><strong>스크립틀릿으로 표현한 반복문 템플릿</strong></p>
<pre><code class="language-jsp">&lt;%  
    List&lt;Notice&gt; list = (List&lt;Notice&gt;)request.getAttribute(&quot;list&quot;);  
    for (Notice n : list) {  
        pageContext.setAttribute(&quot;n&quot;, n);  
%&gt;  
    &lt;tr&gt;  
        &lt;td&gt;${n.id}&lt;/td&gt;  
        &lt;td class=&quot;title indent text-align-left&quot;&gt;&lt;a href=&quot;detail?id=${n.id}&quot;&gt;${n.title}&lt;/a&gt;&lt;/td&gt;  
        &lt;td&gt;${n.writerId}&lt;/td&gt;  
        &lt;td&gt;${n.regDate}&lt;/td&gt;  
        &lt;td&gt;${n.hit}&lt;/td&gt;  
    &lt;/tr&gt;  
&lt;% } %&gt;</code></pre>
<p><strong>JSTL 반복문 템플릿</strong></p>
<pre><code class="language-jsp">&lt;c:forEach var=&quot;n&quot; items=&quot;${list}&quot;&gt;  
    &lt;tr&gt;  
        &lt;td&gt;${n.id}&lt;/td&gt;  
        &lt;td class=&quot;title indent text-align-left&quot;&gt;&lt;a href=&quot;detail?id=${n.id}&quot;&gt;${n.title}&lt;/a&gt;&lt;/td&gt;  
        &lt;td&gt;${n.writerId}&lt;/td&gt;  
        &lt;td&gt;${n.regDate}&lt;/td&gt;  
        &lt;td&gt;${n.hit}&lt;/td&gt;  
    &lt;/tr&gt;  
&lt;/c:forEach&gt;</code></pre>
<p>Java코드 없이 가독성 좋은 형태로 변환되었다.</p>
<hr />
<h2 id="📌jstl의-주요기능">📌JSTL의 주요기능</h2>
<p>JSTL은 크게 다섯 가지 기능 그룹으로 나뉜다.</p>
<h3 id="1️⃣core-c-태그">1️⃣Core (c 태그)</h3>
<blockquote>
<p>변수 선언/출력, 조건문/반복문</p>
</blockquote>
<table>
<thead>
<tr>
<th>태그</th>
<th>기능</th>
<th>보강 설명 / 예시</th>
</tr>
</thead>
<tbody><tr>
<td><code>&lt;c:out&gt;</code></td>
<td>출력</td>
<td><code>${변수}</code>를 출력할 때 사용. HTML 이스케이프 처리 가능 (<code>escapeXml=&quot;true&quot;</code> 기본값).👉 <code>&lt;c:out value=&quot;${msg}&quot; default=&quot;값 없음&quot; /&gt;</code></td>
</tr>
<tr>
<td><code>&lt;c:set&gt;</code></td>
<td>사용할 변수를 설정</td>
<td>JSP 스코프(page, request, session, application)에 값 저장 가능.👉 <code>&lt;c:set var=&quot;name&quot; value=&quot;홍길동&quot; scope=&quot;session&quot;/&gt;</code></td>
</tr>
<tr>
<td><code>&lt;c:remove&gt;</code></td>
<td>설정한 변수 제거</td>
<td>지정한 스코프에서 변수를 삭제.👉 <code>&lt;c:remove var=&quot;name&quot; scope=&quot;session&quot;/&gt;</code></td>
</tr>
<tr>
<td><code>&lt;c:catch&gt;</code></td>
<td>예외 처리</td>
<td>JSP 태그 실행 중 발생하는 예외를 잡아 변수에 저장.👉 <code>&lt;c:catch var=&quot;error&quot;&gt;&lt;% int a = 10/0; %&gt;&lt;/c:catch&gt;에러: ${error}</code></td>
</tr>
<tr>
<td><code>&lt;c:if&gt;</code></td>
<td>조건문 처리</td>
<td>단일 조건만 평가. <code>test</code> 속성은 반드시 Boolean 값이어야 함.👉 <code>&lt;c:if test=&quot;${age &gt;= 20}&quot;&gt;성인입니다&lt;/c:if&gt;</code></td>
</tr>
<tr>
<td><code>&lt;c:choose&gt;</code></td>
<td>다중 조건문 처리</td>
<td><code>switch-case</code>와 유사. <code>&lt;c:when&gt;</code>과 <code>&lt;c:otherwise&gt;</code>와 함께 사용.</td>
</tr>
<tr>
<td><code>&lt;c:when&gt;</code></td>
<td><code>&lt;c:choose&gt;</code>의 서브태그</td>
<td>조건이 <code>true</code>이면 실행. 여러 개 가능. 위에서부터 순차적으로 평가됨.</td>
</tr>
<tr>
<td><code>&lt;c:otherwise&gt;</code></td>
<td><code>&lt;c:choose&gt;</code>의 서브태그</td>
<td>모든 <code>&lt;c:when&gt;</code>이 거짓일 때 실행되는 블록.</td>
</tr>
<tr>
<td><code>&lt;c:import&gt;</code></td>
<td>다른 리소스의 결과 삽입</td>
<td>JSP/Servlet/외부 URL의 결과를 현재 JSP에 포함.👉 <code>&lt;c:import url=&quot;/header.jsp&quot; /&gt;</code> 또는 <code>&lt;c:import url=&quot;http://example.com&quot; /&gt;</code></td>
</tr>
<tr>
<td><code>&lt;c:forEach&gt;</code></td>
<td>반복문 처리</td>
<td>배열, List, Map 등 컬렉션을 순회. 인덱스(<code>varStatus</code>) 제공.👉 <code>&lt;c:forEach var=&quot;item&quot; items=&quot;${list}&quot; varStatus=&quot;s&quot;&gt;${s.index}: ${item}&lt;br/&gt;&lt;/c:forEach&gt;</code></td>
</tr>
<tr>
<td><code>&lt;c:forTokens&gt;</code></td>
<td>문자열 토큰화 반복</td>
<td><code>items</code> 문자열을 <code>delims</code> 구분자로 나눠서 반복.👉 <code>&lt;c:forTokens items=&quot;A,B,C&quot; delims=&quot;,&quot; var=&quot;x&quot;&gt;${x}&lt;/c:forTokens&gt;</code></td>
</tr>
<tr>
<td><code>&lt;c:param&gt;</code></td>
<td>URL 파라미터 설정</td>
<td><code>&lt;c:import&gt;</code> 또는 <code>&lt;c:url&gt;</code> 내부에서 사용하여 query string 추가.👉 <code>&lt;c:url var=&quot;go&quot; value=&quot;search.jsp&quot;&gt;&lt;c:param name=&quot;q&quot; value=&quot;JSTL&quot;/&gt;&lt;/c:url&gt;</code></td>
</tr>
<tr>
<td><code>&lt;c:redirect&gt;</code></td>
<td>페이지 리다이렉트</td>
<td>클라이언트를 지정한 URL로 이동시킴. 주로 로그인 후 페이지 이동 등에서 활용.👉 <code>&lt;c:redirect url=&quot;/login.jsp&quot; /&gt;</code></td>
</tr>
<tr>
<td><code>&lt;c:url&gt;</code></td>
<td>URL 재작성</td>
<td>세션 트래킹을 위해 JSESSIONID를 자동으로 추가해주기도 함. 보통 링크 생성에 사용.👉 <code>&lt;a href=&quot;&lt;c:url value='/mypage'/&gt;&quot;&gt;마이페이지&lt;/a&gt;</code></td>
</tr>
</tbody></table>
<hr />
<h3 id="2️⃣formatting-fmt-태그">2️⃣Formatting (fmt 태그)</h3>
<blockquote>
<p>숫자, 날짜, 통화 포맷</p>
</blockquote>
<table>
<thead>
<tr>
<th>태그</th>
<th>기능</th>
<th>예시</th>
</tr>
</thead>
<tbody><tr>
<td><code>&lt;fmt:formatNumber&gt;</code></td>
<td>숫자/통화/퍼센트 형식 변환</td>
<td><code>type=&quot;number&quot;</code>, <code>currency</code>, <code>percent</code> 옵션 가능. 소수점 자리수도 지정 가능.  <br />👉 <code>&lt;fmt:formatNumber value=&quot;12345.678&quot; type=&quot;number&quot; maxFractionDigits=&quot;2&quot;/&gt;</code> → <code>12,345.68</code></td>
</tr>
<tr>
<td><code>&lt;fmt:parseNumber&gt;</code></td>
<td>문자열 → 숫자 변환</td>
<td>문자열을 Number 객체(Integer/Double 등)로 변환.  <br />👉 <code>&lt;fmt:parseNumber var=&quot;num&quot; type=&quot;number&quot; value=&quot;1234.56&quot;/&gt;</code> (<code>${num}</code> → 1234.56)</td>
</tr>
<tr>
<td><code>&lt;fmt:formatDate&gt;</code></td>
<td>날짜/시간 포맷팅</td>
<td><code>type=&quot;date&quot;</code>, <code>time</code>, <code>both</code> 옵션 가능. <code>pattern</code>으로 커스텀 포맷도 가능.  <br />👉 <code>&lt;fmt:formatDate value=&quot;${now}&quot; pattern=&quot;yyyy-MM-dd HH:mm&quot;/&gt;</code></td>
</tr>
<tr>
<td><code>&lt;fmt:parseDate&gt;</code></td>
<td>문자열 → 날짜 변환</td>
<td>문자열을 <code>java.util.Date</code> 객체로 변환.  <br />👉 <code>&lt;fmt:parseDate value=&quot;2025-08-26&quot; pattern=&quot;yyyy-MM-dd&quot; var=&quot;d&quot;/&gt;</code></td>
</tr>
<tr>
<td><code>&lt;fmt:setLocale&gt;</code></td>
<td>로케일(locale) 설정</td>
<td>날짜, 숫자 포맷에 적용할 지역/언어 지정.  <br />👉 <code>&lt;fmt:setLocale value=&quot;en_US&quot;/&gt;</code></td>
</tr>
<tr>
<td><code>&lt;fmt:setTimeZone&gt;</code></td>
<td>타임존 설정</td>
<td>날짜/시간 태그(<code>formatDate</code>) 등에 적용할 타임존 지정.  <br />👉 <code>&lt;fmt:setTimeZone value=&quot;GMT+9&quot;/&gt;</code></td>
</tr>
<tr>
<td><code>&lt;fmt:timeZone&gt;</code></td>
<td>특정 블록에 타임존 적용</td>
<td>블록 안에서만 지정한 타임존을 적용.  <br />👉 <code>&lt;fmt:timeZone value=&quot;GMT&quot;&gt;&lt;fmt:formatDate value=&quot;${now}&quot; type=&quot;both&quot;/&gt;&lt;/fmt:timeZone&gt;</code></td>
</tr>
<tr>
<td><code>&lt;fmt:bundle&gt;</code></td>
<td>리소스 번들 지정</td>
<td>다국어 리소스(properties 파일) 사용 시 묶음 지정.  <br />👉 <code>&lt;fmt:bundle basename=&quot;messages&quot;&gt; ... &lt;/fmt:bundle&gt;</code></td>
</tr>
<tr>
<td><code>&lt;fmt:message&gt;</code></td>
<td>리소스 번들 메시지 출력</td>
<td><code>key</code>에 해당하는 다국어 문자열 출력. <code>&lt;fmt:param&gt;</code>과 함께 사용 가능.  <br />👉 <code>&lt;fmt:message key=&quot;welcome&quot;&gt;&lt;fmt:param value=&quot;홍길동&quot;/&gt;&lt;/fmt:message&gt;</code></td>
</tr>
<tr>
<td><code>&lt;fmt:param&gt;</code></td>
<td>메시지 치환 파라미터</td>
<td><code>&lt;fmt:message&gt;</code> 안에서 동적 값 삽입.  <br />👉 <code>messages.properties</code> → <code>welcome=안녕하세요 {0}님</code>  <br />JSP → <code>&lt;fmt:message key=&quot;welcome&quot;&gt;&lt;fmt:param value=&quot;홍길동&quot;/&gt;&lt;/fmt:message&gt;</code></td>
</tr>
</tbody></table>
<hr />
<h3 id="3️⃣sql-sql-태그">3️⃣SQL (sql 태그)</h3>
<blockquote>
<p>DB 쿼리 실행 (실무에서는 보안 문제 때문에 거의 안 씀) PreparedStatement 미지원 → SQL Injection 위험</p>
</blockquote>
<table>
<thead>
<tr>
<th>태그</th>
<th>기능</th>
<th>예시</th>
</tr>
</thead>
<tbody><tr>
<td><code>&lt;sql:setDataSource&gt;</code></td>
<td>DB 연결 설정</td>
<td>DB 드라이버, URL, 사용자, 비밀번호를 지정. 이후 SQL 태그들이 이 DataSource를 사용.👉 <code>&lt;sql:setDataSource var=&quot;db&quot; driver=&quot;org.postgresql.Driver&quot; url=&quot;jdbc:postgresql://localhost:5432/test&quot; user=&quot;postgres&quot; password=&quot;1234&quot;/&gt;</code></td>
</tr>
<tr>
<td><code>&lt;sql:query&gt;</code></td>
<td>SELECT 실행</td>
<td>DB 조회. 결과는 <code>Result</code> 객체로 저장됨.👉 <code>&lt;sql:query var=&quot;rs&quot; dataSource=&quot;${db}&quot;&gt;SELECT * FROM notice&lt;/sql:query&gt;</code></td>
</tr>
<tr>
<td><code>&lt;sql:update&gt;</code></td>
<td>INSERT / UPDATE / DELETE 실행</td>
<td>변경 쿼리 실행. 반영된 row 수 반환.👉 <code>&lt;sql:update dataSource=&quot;${db}&quot;&gt;INSERT INTO notice(title) VALUES('테스트')&lt;/sql:update&gt;</code></td>
</tr>
<tr>
<td><code>&lt;sql:param&gt;</code></td>
<td>SQL 파라미터 바인딩</td>
<td><code>&lt;sql:query&gt;</code> 또는 <code>&lt;sql:update&gt;</code> 내부에서 <code>?</code> 자리에 값 바인딩.👉 <code>&lt;sql:query var=&quot;rs&quot; dataSource=&quot;${db}&quot;&gt;SELECT * FROM notice WHERE id=?&lt;sql:param value=&quot;1&quot;/&gt;&lt;/sql:query&gt;</code></td>
</tr>
<tr>
<td><code>&lt;sql:dateParam&gt;</code></td>
<td>SQL 파라미터 중 날짜 타입 지정</td>
<td>DB에 날짜 값 바인딩할 때 사용.</td>
</tr>
</tbody></table>
<hr />
<h3 id="4️⃣xml-x-태그">4️⃣XML (x 태그)</h3>
<blockquote>
<p>XML 데이터를 다루기 위한 태그 DOM/SAX 파싱 없이 JSP에서 XML 처리 가능</p>
</blockquote>
<table>
<thead>
<tr>
<th>태그</th>
<th>기능</th>
<th>보강 설명 / 예시</th>
</tr>
</thead>
<tbody><tr>
<td><code>&lt;x:parse&gt;</code></td>
<td>XML 문서 파싱</td>
<td>XML 문자열이나 외부 파일을 XML DOM 객체로 변환.👉 <code>&lt;x:parse var=&quot;doc&quot; xml=&quot;${xmlString}&quot;/&gt;</code></td>
</tr>
<tr>
<td><code>&lt;x:out&gt;</code></td>
<td>XPath 결과 출력</td>
<td>XPath로 찾은 노드/값 출력.👉 <code>&lt;x:out select=&quot;$doc/root/name&quot;/&gt;</code></td>
</tr>
<tr>
<td><code>&lt;x:set&gt;</code></td>
<td>XPath 결과 변수에 저장</td>
<td>XML 노드/값을 변수로 설정.👉 <code>&lt;x:set var=&quot;username&quot; select=&quot;$doc/root/user/name&quot;/&gt;</code></td>
</tr>
<tr>
<td><code>&lt;x:if&gt;</code></td>
<td>XPath 조건 검사</td>
<td>XPath 조건이 true일 때 실행.👉 <code>&lt;x:if select=&quot;$doc/root/user[@role='admin']&quot;&gt;관리자&lt;/x:if&gt;</code></td>
</tr>
<tr>
<td><code>&lt;x:forEach&gt;</code></td>
<td>XPath 결과 반복</td>
<td>XPath로 찾은 여러 노드를 순회.👉 <code>&lt;x:forEach select=&quot;$doc/root/item&quot; var=&quot;i&quot;&gt;&lt;x:out select=&quot;$i/name&quot;/&gt;&lt;/x:forEach&gt;</code></td>
</tr>
</tbody></table>
<hr />
<h3 id="5️⃣functions-fn-함수">5️⃣Functions (fn 함수)</h3>
<blockquote>
<p>JSTL 함수 라이브러리. 주로 <strong>문자열 처리</strong>와 <strong>컬렉션 처리</strong>에 사용.<br />반드시 선언 필요</p>
</blockquote>
<pre><code class="language-jsp">&lt;%@ taglib prefix=&quot;fn&quot; uri=&quot;http://java.sun.com/jsp/jstl/functions&quot; %&gt;</code></pre>
<table>
<thead>
<tr>
<th>함수</th>
<th>기능</th>
<th>예시</th>
</tr>
</thead>
<tbody><tr>
<td><code>fn:length(obj)</code></td>
<td>길이 반환</td>
<td>문자열/컬렉션/배열의 길이. 👉 <code>${fn:length(&quot;Hello&quot;)}</code> → <code>5</code></td>
</tr>
<tr>
<td><code>fn:contains(str, substr)</code></td>
<td>부분 문자열 포함 여부</td>
<td>👉 <code>${fn:contains(&quot;abcdef&quot;,&quot;cd&quot;)}</code> → <code>true</code></td>
</tr>
<tr>
<td><code>fn:containsIgnoreCase(str, substr)</code></td>
<td>대소문자 무시 포함 여부</td>
<td>👉 <code>${fn:containsIgnoreCase(&quot;Hello&quot;,&quot;HEL&quot;)}</code> → <code>true</code></td>
</tr>
<tr>
<td><code>fn:startsWith(str, prefix)</code></td>
<td>접두사 검사</td>
<td>👉 <code>${fn:startsWith(&quot;Hello&quot;,&quot;He&quot;)}</code> → <code>true</code></td>
</tr>
<tr>
<td><code>fn:endsWith(str, suffix)</code></td>
<td>접미사 검사</td>
<td>👉 <code>${fn:endsWith(&quot;Hello&quot;,&quot;lo&quot;)}</code> → <code>true</code></td>
</tr>
<tr>
<td><code>fn:indexOf(str, substr)</code></td>
<td>부분 문자열 위치</td>
<td>👉 <code>${fn:indexOf(&quot;Hello&quot;,&quot;l&quot;)}</code> → <code>2</code></td>
</tr>
<tr>
<td><code>fn:substring(str, begin, end)</code></td>
<td>부분 문자열 추출</td>
<td>👉 <code>${fn:substring(&quot;Hello&quot;,1,3)}</code> → <code>el</code></td>
</tr>
<tr>
<td><code>fn:substringAfter(str, substr)</code></td>
<td>지정 문자열 이후 반환</td>
<td>👉 <code>${fn:substringAfter(&quot;abc-def&quot;,&quot;-&quot;)}</code> → <code>def</code></td>
</tr>
<tr>
<td><code>fn:substringBefore(str, substr)</code></td>
<td>지정 문자열 이전 반환</td>
<td>👉 <code>${fn:substringBefore(&quot;abc-def&quot;,&quot;-&quot;)}</code> → <code>abc</code></td>
</tr>
<tr>
<td><code>fn:replace(str, before, after)</code></td>
<td>문자열 치환</td>
<td>👉 <code>${fn:replace(&quot;a-b-c&quot;,&quot;-&quot;,&quot;/&quot;)}</code> → <code>a/b/c</code></td>
</tr>
<tr>
<td><code>fn:trim(str)</code></td>
<td>앞뒤 공백 제거</td>
<td>👉 <code>${fn:trim(&quot; Hello &quot;)}</code> → <code>Hello</code></td>
</tr>
<tr>
<td><code>fn:toLowerCase(str)</code></td>
<td>소문자로 변환</td>
<td>👉 <code>${fn:toLowerCase(&quot;HELLO&quot;)}</code> → <code>hello</code></td>
</tr>
<tr>
<td><code>fn:toUpperCase(str)</code></td>
<td>대문자로 변환</td>
<td>👉 <code>${fn:toUpperCase(&quot;hello&quot;)}</code> → <code>HELLO</code></td>
</tr>
<tr>
<td><code>fn:split(str, delimiter)</code></td>
<td>문자열 분할 (배열 반환)</td>
<td>👉 <code>${fn:split(&quot;a,b,c&quot;,&quot;,&quot;)[1]}</code> → <code>b</code></td>
</tr>
<tr>
<td><code>fn:join(array, delimiter)</code></td>
<td>배열을 문자열로 합치기</td>
<td>👉 <code>${fn:join(fn:split(&quot;a,b,c&quot;,&quot;,&quot;), &quot;-&quot;)}</code> → <code>a-b-c</code></td>
</tr>
<tr>
<td><code>fn:escapeXml(str)</code></td>
<td>XML/HTML 이스케이프</td>
<td>👉 <code>${fn:escapeXml(&quot;&lt;h1&gt;Hi&lt;/h1&gt;&quot;)}</code> → <code>&amp;lt;h1&amp;gt;Hi&amp;lt;/h1&amp;gt;</code></td>
</tr>
</tbody></table>
<hr />