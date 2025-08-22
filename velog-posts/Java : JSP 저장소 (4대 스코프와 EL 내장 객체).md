<hr />
<h2 id="1-jspservlet의-저장-객체-4대-스코프">1. JSP/Servlet의 저장 객체 (4대 스코프)</h2>
<h3 id="📌-page-pagescope">📌 Page (PageScope)</h3>
<ul>
<li>실제 객체  : <code>PageContext</code></li>
<li>생존 범위/수명 : 현재 <code>JSP</code>한 페이지 처리 동안만</li>
<li>대표 용도 : 같은 <code>JSP</code> 안에서만 임시 공유</li>
</ul>
<h4 id="예시">예시</h4>
<ul>
<li>설정</li>
</ul>
<pre><code class="language-jsp"> // 📄JSP (해당 JSP 페이지에서만 사용 가능)
 &lt;%  
     pageContext.setAttribute(&quot;k&quot;, v);
   %&gt;</code></pre>
<ul>
<li>조회</li>
</ul>
<pre><code class="language-jsp">// 📄JSP
${ pageContext.k }</code></pre>
<hr />
<h3 id="📌-request">📌 Request</h3>
<ul>
<li>실제 객체 : <code>HttpServletRequest</code></li>
<li>생존 범위/수명 : 요청 한 번 (= forward/include 체인 전체)</li>
<li>대표 용도 : 컨트롤러 → 뷰 데이터 전달 (MVC 모델)</li>
</ul>
<h4 id="예시-1">예시</h4>
<ul>
<li>설정</li>
</ul>
<pre><code class="language-java">// 📄Servlet
req.setAttribute(&quot;k&quot;, v);</code></pre>
<ul>
<li>조회</li>
</ul>
<pre><code class="language-jsp">// 📄JSP
${ requestScope.k }</code></pre>
<hr />
<h3 id="📌-session">📌 Session</h3>
<ul>
<li>실제 객체 : <code>HttpSession</code></li>
<li>생존 범위/수명 : 사용자 세션 동안 (만료/로그아웃까지)</li>
<li>대표 용도 : 로그인/개인설정 등 사용자 상태</li>
</ul>
<h4 id="예시-2">예시</h4>
<ul>
<li>설정</li>
</ul>
<pre><code class="language-java">session.setAttribute(&quot;k&quot;, v);</code></pre>
<ul>
<li>조회</li>
</ul>
<pre><code class="language-jsp">// 📄JSP
${ sessionScope.k }</code></pre>
<hr />
<h3 id="📌-application">📌 Application</h3>
<ul>
<li>실제 객체 : <code>ServletContext</code></li>
<li>생존 범위/수명 : 웹앱 생존 기간 전체 (서버 구동-종료)</li>
<li>대표 용도 : 전역 캐시/설정값 (모든 사용자 공유)</li>
</ul>
<h4 id="예시-3">예시</h4>
<ul>
<li>설정</li>
</ul>
<pre><code class="language-java">getServletContext().setAttribute(&quot;k&quot;, v);</code></pre>
<ul>
<li>조회</li>
</ul>
<pre><code class="language-jsp">// 📄JSP
${ applicationScope.k }</code></pre>
<hr />
<h2 id="🕵️-jspel-탐색-우선순위-규칙">🕵️ JSP/EL 탐색 우선순위 규칙</h2>
<p>JSP/EL에서 <code>${ K }</code> 라고만 썼을 때 여러 스코프 (page, request, session, application)에 같은 이름의 속성이 있으면 우선순위 규칙으로 반환 된다.</p>
<h3 id="📌-el-변수-탐색-우선순위">📌 EL 변수 탐색 우선순위</h3>
<p>JSP EL은 내부적으로 4대 스코프를 순서대로 탐색한다.</p>
<pre><code>1️⃣pageScope

2️⃣requestScope

3️⃣sessionScope

4️⃣applicationScope</code></pre><p>즉, 동일한 key <code>&quot;k&quot;</code>가 여러 스코프에 존재하면 <strong>가장 가까운 (page → request → session → application)</strong>스코프의 값을 먼저 찾고 반환한다.</p>
<hr />
<h3 id="📌-예시">📌 예시</h3>
<ul>
<li>설정</li>
</ul>
<pre><code class="language-jsp">&lt;%
    pageContext.setAttribute(&quot;k&quot;, &quot;page-value&quot;);
    request.setAttribute(&quot;k&quot;, &quot;request-value&quot;);
    session.setAttribute(&quot;k&quot;, &quot;session-value&quot;);
    application.setAttribute(&quot;k&quot;, &quot;application-value&quot;);
%&gt;</code></pre>
<hr />
<ul>
<li>조회</li>
</ul>
<pre><code class="language-jsp">${k}                  &lt;!-- EL 기본 탐색 (page → request → session → application 순서) --&gt;
${pageScope.k}        &lt;!-- 특정 스코프 강제 --&gt;
${requestScope.k}
${sessionScope.k}
${applicationScope.k}</code></pre>
<hr />
<ul>
<li>출력 결과</li>
</ul>
<pre><code>page-value
page-value
request-value
session-value
application-value</code></pre><p>💡결론</p>
<ul>
<li><code>${ k }</code>만 쓰면 EL은 가장 가까운 스코프부터 순서대로 탐색</li>
<li>page → request → session → application</li>
<li>동일 key가 여러 스코프에 있으면 <strong>우선순위가 높은 쪽이 출력된다</strong></li>
<li>특정 스코프를 강제하고 싶으면 <code>${ pageScope.k }</code> ... 처럼 명시해야 한다.</li>
</ul>
<hr />
<h2 id="2-el-기본-내장-객체-읽기-전용">2. EL 기본 내장 객체 (읽기 전용)</h2>
<p>개발자가 직접 <code>setAttribute()</code>로 저장하는게 아니라 JSP 컨테이너 EL에서 바로 조회할 수 있도록 제공하는 객체이다.</p>
<h3 id="📌-param">📌 param</h3>
<ul>
<li>설명 : 단일 요청 파라미터(String)</li>
<li>읽기 예시 : <code>${ param.id }</code> → &quot;hong&quot;</li>
</ul>
<hr />
<h3 id="📌-paramvalues">📌 paramValues</h3>
<ul>
<li>설명 : 요청 파라미터 배열(String[])</li>
<li>읽기 예시 : <code>${ paramValues.hobby[0] }</code></li>
</ul>
<hr />
<h3 id="📌-header">📌 header</h3>
<ul>
<li>설명 : HTTP 요청 헤더 (첫 값만)</li>
<li>읽기 예시 : <code>${ header[&quot;User-Agent&quot;] }</code></li>
</ul>
<hr />
<h3 id="📌-headervalues">📌 headerValues</h3>
<ul>
<li>설명 : 요청 헤더 전체 배열</li>
<li>읽기 예시 : <code>${ headerValues[&quot;Accept&quot;][0] }</code></li>
</ul>
<hr />
<h3 id="📌-cookie">📌 cookie</h3>
<ul>
<li>설명 : 요청 쿠키(Map&lt;쿠키명, Cookie객체&gt;)</li>
<li>읽기 예시 : <code>${ cookie.userId.value }</code></li>
</ul>
<hr />
<h3 id="📌-initparam">📌 initParam</h3>
<ul>
<li>설명 : <code>web.xml</code>의 <code>&lt;context-param&gt;</code> 초기화 파라미터 (ServletContext init-param)</li>
<li>읽기 예시 : <code>${ initParam[&quot;cdn.url&quot;] }</code></li>
</ul>
<hr />
<h2 id="3-pagecontext">3. PageContext</h2>
<p>JSP의 최상위 내장 객체 중 하나</p>
<blockquote>
<p>💡 EL에서는 잘 쓰지 않지만 스크립틀릿이나 커스텀 태그에서 활용됨</p>
</blockquote>
<h3 id="🕵️-다양한-내장-객체-접근-가능">🕵️ 다양한 내장 객체 접근 가능</h3>
<pre><code class="language-jsp">&lt;%= pageContext.getRequest() %&gt;       // HttpServletRequest
&lt;%= pageContext.getSession() %&gt;       // HttpSession
&lt;%= pageContext.getServletContext() %&gt; // Application</code></pre>
<ul>
<li>특징 : pageContext.findAttribute(&quot;name&quot;) 호출 시 <strong>page → request → session → application</strong> 순서로 검색</li>
</ul>
<p>💡 EL로 사용할 때는 템플릿 언어처럼 깔끔하게 데이터 표현만 하도록 전용 문법으로 작성한다.</p>
<ul>
<li>예시 :</li>
</ul>
<pre><code class="language-jsp">// 📄JSP (스크립틀릿 표현식)
&lt;%= pageContext.getRequest().getMethod() %&gt;

// 📄JSP (EL)
${pageContext.request.method}</code></pre>
<hr />