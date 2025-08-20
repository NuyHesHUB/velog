<hr />
<h2 id="🕵️-jsp-와-컴파일-코드">🕵️ JSP 와 컴파일 코드</h2>
<p>📄example.jsp</p>
<pre><code class="language-jsp">// example.jsp
&lt;html lang=&quot;ko&quot;&gt;  
    &lt;head&gt;  
        &lt;meta charset=&quot;UTF-8&quot;&gt;  
        &lt;title&gt;JSP - Hello World&lt;/title&gt;  
    &lt;/head&gt;  
    &lt;body&gt;  
        &lt;h1&gt;Hello&lt;/h1&gt;  
    &lt;/body&gt;  
&lt;/html&gt;</code></pre>
<p>📄example.jsp 의 서블릿 컴파일 코드</p>
<pre><code class="language-java">public final class calculator_jsp extends org.apache.jasper.runtime.HttpJspBase
    implements org.apache.jasper.runtime.JspSourceDependent,
                 org.apache.jasper.runtime.JspSourceImports {

    // 멤버함수 , 멤버변수

    public void _jspService(final javax.servlet.http.HttpServletRequest request, final javax.servlet.http.HttpServletResponse response)
      throws java.io.IOException, javax.servlet.ServletException {

        // 지역변수 , 알고리즘

    }
}</code></pre>
<h3 id="_jspservice">_jspService()</h3>
<p>이 메서드가 <code>JSP</code>한 요청의 실제 처리를 한다.  원래 <code>service()</code>를 오버라이드하는 서블릿과 달리 <code>Jasper</code>가 <code>_jspService</code>로 생성하고 컨테이너가 호출한다.</p>
<hr />
<h3 id="예제">예제</h3>
<p>📄<code>example.jsp</code></p>
<pre><code class="language-jsp">// example.jsp

1️⃣ 환영합니다.

&lt;html lang=&quot;ko&quot;&gt;  
    &lt;head&gt;  
        &lt;meta charset=&quot;UTF-8&quot;&gt;  
        &lt;title&gt;JSP - Hello World&lt;/title&gt;  
    &lt;/head&gt;  
    &lt;body&gt;  
        &lt;h1&gt;Hello&lt;/h1&gt;  
    &lt;/body&gt;  
&lt;/html&gt;</code></pre>
<p>가령 상단에 1️⃣번 처럼 <code>환영합니다.</code>를 쓰게 된다면  서블릿 컴파일은 아래와 같이 출력을 하게된다.</p>
<pre><code class="language-java">public void _jspService(final javax.servlet.http.HttpServletRequest request, final javax.servlet.http.HttpServletResponse response)
      throws java.io.IOException, javax.servlet.ServletException {

        1️⃣out.write(&quot;환영합니다.&quot;);

    }</code></pre>
<hr />
<p>하지만 실행되어야할 코드를 넣을 땐 아래와 같이 코드 블록을 사용한다.</p>
<p>📄<code>example.jsp</code></p>
<pre><code class="language-jsp">// example.jsp
 &lt;%
    1️⃣ y = x + 3
   %&gt;
&lt;html lang=&quot;ko&quot;&gt;  
    &lt;head&gt;  
        &lt;meta charset=&quot;UTF-8&quot;&gt;  
        &lt;title&gt;JSP - Hello World&lt;/title&gt;  
    &lt;/head&gt;  
    &lt;body&gt;  
        &lt;h1&gt;Hello&lt;/h1&gt;  
    &lt;/body&gt;  
&lt;/html&gt;</code></pre>
<p>📄example.jsp 의 서블릿 컴파일 코드</p>
<pre><code class="language-java">public void _jspService(final javax.servlet.http.HttpServletRequest request, final javax.servlet.http.HttpServletResponse response)
      throws java.io.IOException, javax.servlet.ServletException {

        1️⃣ y = x + 3

    }</code></pre>
<p><code>&lt;% %&gt;</code> 를 사용하게 되면 <code>_jspService</code>메서드에 선언이 된다.</p>
<hr />
<h3 id="🕵️-함수를-선언하고-싶으면">🕵️ 함수를 선언하고 싶으면</h3>
<p>아래와 같이 <code>JSP</code>파일에서 함수를 선언하고 싶을 때는 이렇게 사용을 하면 에러가 발생한다.</p>
<pre><code class="language-jsp">❌
&lt;% 
    public int sum (int a, int b) {
        return a + b;
    }
%&gt;

👌
&lt;%!
    public int sum (int a, int b) {
        return a + b;
    }
%&gt;</code></pre>
<p><code>&lt;% %&gt;</code> 를 사용하게 되면 <code>_jspService</code>메서드에 선언이 되기 때문이다. 메서드 내부에 또다른 메서드가 정의가 되는 것이 되므로 컴파일 에러가 발생한다.  그래서 클래스 내부에 메서드가 정의되어야 함으로 <code>&lt;%! %&gt;</code> 를 사용한다.</p>
<hr />
<h2 id="🕵️-jsp-문법--스타일과-사용-예시">🕵️ JSP 문법 / 스타일과 사용 예시</h2>
<h3 id="📌-1-정적-템플릿--html">📌 1) 정적 템플릿 / HTML</h3>
<ul>
<li><p><strong>컴파일 시</strong> : <code>_jspService</code> 내부에 <code>out.write(&quot;...&quot;)</code></p>
</li>
<li><p><strong>런타임 시</strong> : <code>_jspService(...)</code> 안에서 그대로 출력됨</p>
</li>
</ul>
<blockquote>
<p>예시 </p>
</blockquote>
<p><strong>용도:</strong> 고정 레이아웃/마크업, 변하지 않는 안내문</p>
<pre><code class="language-jsp">&lt;!-- header.jsp --&gt;
&lt;header class=&quot;gnb&quot;&gt;
  &lt;a href=&quot;/&quot;&gt;Home&lt;/a&gt;
  &lt;nav&gt; ... &lt;/nav&gt;
&lt;/header&gt;</code></pre>
<p><strong>팁:</strong> 정적 레이아웃은 <strong>JSP 인클루드</strong>(정적/동적)로 재사용하면 유지보수 용이</p>
<hr />
<h3 id="📌-2-스크립틀릿---">📌 2) 스크립틀릿 <code>&lt;% ... %&gt;</code></h3>
<ul>
<li><p><strong>컴파일 시</strong> : <code>_jspService</code> 메서드 몸통에 그대로 삽입</p>
</li>
<li><p><strong>런타임 시</strong> : <code>_jspService(...)</code> 실행 시 자바 코드 수행</p>
</li>
<li><p>⚠️ 메서드/필드 선언 불가 → 선언부 <code>&lt;%! ... %&gt;</code> 사용해야 함</p>
</li>
</ul>
<blockquote>
<p>예시 </p>
</blockquote>
<p><strong>용도:</strong> 임시 디버깅/레거시 코드에서 빠른 분기</p>
<pre><code class="language-jsp">&lt;%-- 가급적 JSTL/EL로 대체 --%&gt;
&lt;%
  boolean isAdmin = &quot;admin&quot;.equals(session.getAttribute(&quot;role&quot;));
  if (!isAdmin) { response.sendRedirect(&quot;/403.jsp&quot;); return; }
%&gt;</code></pre>
<p><strong>팁:</strong> 실무에선 <strong>JSTL/EL + 컨트롤러에서 데이터 준비</strong>로 대체하는 게 표준</p>
<hr />
<h3 id="📌-3-표현식---">📌 3) 표현식 <code>&lt;%= ... %&gt;</code></h3>
<ul>
<li><p><strong>컴파일 시</strong> : <code>_jspService</code> 안의<br />  <code>out.write(String.valueOf(...))</code></p>
</li>
<li><p><strong>런타임 시</strong> : 값이 계산된 뒤 즉시 출력</p>
</li>
<li><p>예제:</p>
<p>  <code>&lt;%= 1 + 2 %&gt;   &lt;!-- 출력: 3 --&gt;</code></p>
</li>
</ul>
<blockquote>
<p>예시 </p>
</blockquote>
<p><strong>용도:</strong> 간단 값 출력(로그인 사용자명 등)</p>
<pre><code class="language-jsp">&lt;p&gt;안녕하세요, &lt;strong&gt;&lt;%= request.getAttribute(&quot;userName&quot;) %&gt;&lt;/strong&gt; 님!&lt;/p&gt;</code></pre>
<p><strong>팁:</strong> 표현식도 지양하고 <strong><code>${userName}</code> EL</strong>을 쓰는 게 더 안전/일관</p>
<hr />
<h3 id="📌-4-el-expression-language---">📌 4) EL (Expression Language) <code>${ ... }</code></h3>
<ul>
<li><p><strong>컴파일 시</strong> :<br />  <code>PageContextImpl.proprietaryEvaluate(...)</code><br />  또는 <code>ExpressionFactory</code> 호출</p>
</li>
<li><p><strong>런타임 시</strong> : <code>_jspService(...)</code> 중 EL 평가 후 출력</p>
</li>
<li><p><strong>특징</strong> : <code>page/request/session/application</code> 스코프에서 속성 탐색</p>
</li>
</ul>
<blockquote>
<p>예시 </p>
</blockquote>
<p><strong>용도:</strong> 모델 데이터 출력/간단 계산/널 안전 접근</p>
<pre><code class="language-jsp">&lt;p&gt;안녕하세요, &lt;strong&gt;${user.name}&lt;/strong&gt; 님!&lt;/p&gt;
&lt;p&gt;장바구니: ${cart.totalCount}개 / 합계: ${cart.totalPrice}원&lt;/p&gt;
&lt;p&gt;기본값: ${empty user.nickname ? user.name : user.nickname}&lt;/p&gt;</code></pre>
<p><strong>팁:</strong> EL은 <strong>속성 스코프</strong>(page/request/session/application)에 있는 값만 본다.
컨트롤러/서블릿에서 <code>request.setAttribute(&quot;user&quot;, userDto)</code> 식으로 전달</p>
<hr />
<h3 id="📌-5-선언부----필드메서드-선언">📌 5) 선언부 <code>&lt;%! ... %&gt;</code> (필드/메서드 선언)</h3>
<ul>
<li><p><strong>컴파일 시</strong> : 클래스 레벨에 필드/메서드 정의<br />  <code>jspInit()</code> / <code>jspDestroy()</code> → 각각 <code>_jspInit()</code> / <code>_jspDestroy()</code></p>
</li>
<li><p><strong>런타임 시</strong> :</p>
<ul>
<li><p>로딩 시 1회 : <code>_jspInit()</code></p>
</li>
<li><p>언로드 시 1회 : <code>_jspDestroy()</code></p>
</li>
</ul>
</li>
</ul>
<blockquote>
<p>예시 </p>
</blockquote>
<p><strong>용도:</strong> (지양) 페이지 전역 유틸/상수/초기화 로직</p>
<pre><code class="language-jsp">&lt;%!
  private static final String VERSION = &quot;v1.2.3&quot;;
  public void jspInit() { getServletContext().log(&quot;calculator.jsp init&quot;); }
  public void jspDestroy() { getServletContext().log(&quot;calculator.jsp destroy&quot;); }
%&gt;
&lt;footer&gt;build: &lt;%= VERSION %&gt;&lt;/footer&gt;</code></pre>
<p><strong>팁:</strong> 전역/상태는 <strong>서블릿/필터/리스너/스프링 빈</strong>으로 옮기는 게 베스트</p>
<hr />
<h3 id="📌-6-page-디렉티브--page--">📌 6) page 디렉티브 <code>&lt;%@ page ... %&gt;</code></h3>
<ul>
<li><p><strong>컴파일 시</strong> : import, buffering, session, errorPage, contentType 등 메타 구성</p>
</li>
<li><p><strong>런타임 시</strong> : <code>_jspService</code> 시작부에서 <code>response.setContentType(...)</code> 등 설정 적용</p>
</li>
</ul>
<blockquote>
<p>예시 </p>
</blockquote>
<p><strong>용도:</strong> 인코딩/버퍼/임포트/에러 페이지 등 JSP 동작 설정</p>
<pre><code class="language-jsp">&lt;%@ page contentType=&quot;text/html; charset=UTF-8&quot; pageEncoding=&quot;UTF-8&quot;
         buffer=&quot;8kb&quot; autoFlush=&quot;true&quot; isELIgnored=&quot;false&quot; %&gt;
&lt;%@ page import=&quot;java.time.LocalDateTime&quot; %&gt;</code></pre>
<p><strong>팁:</strong> 한글 깨짐 방지: <strong><code>contentType</code> + <code>pageEncoding</code> 둘 다 UTF-8</strong> 명시</p>
<hr />
<h3 id="📌-7-include-디렉티브--include-file--정적-include">📌 7) include 디렉티브 <code>&lt;%@ include file=&quot;...&quot; %&gt;</code> (정적 include)</h3>
<ul>
<li><p><strong>컴파일 시</strong> : 번역 시점에 파일 합쳐짐 → 하나의 서블릿으로 컴파일</p>
</li>
<li><p><strong>런타임 시</strong> : 별도 메서드 호출 없음 (정적 결합)</p>
</li>
</ul>
<blockquote>
<p>예시 </p>
</blockquote>
<p><strong>용도:</strong> <strong>빌드 타임 결합</strong>(공통 헤더/푸터/메뉴) – 한 서블릿으로 컴파일</p>
<pre><code class="language-jsp">&lt;%@ include file=&quot;/WEB-INF/views/common/header.jsp&quot; %&gt;
&lt;main&gt;...&lt;/main&gt;
&lt;%@ include file=&quot;/WEB-INF/views/common/footer.jsp&quot; %&gt;</code></pre>
<p><strong>팁:</strong> 정적 include는 <strong>변수 공유</strong>가 쉽고 성능도 좋음. 단 파일 간 의존 주의</p>
<hr />
<h3 id="📌-8-jsp-액션-jspinclude-page-동적-include">📌 8) JSP 액션: <code>&lt;jsp:include page=&quot;...&quot;&gt;</code> (동적 include)</h3>
<ul>
<li><p><strong>컴파일 시</strong> :<br />  <code>JspRuntimeLibrary.include(...)</code> 또는 <code>RequestDispatcher.include(...)</code> 호출 생성</p>
</li>
<li><p><strong>런타임 시</strong> : 실행 시 다른 리소스의 출력 포함</p>
</li>
</ul>
<blockquote>
<p>예시 </p>
</blockquote>
<p><strong>용도:</strong> <strong>런타임에 다른 리소스 출력 포함</strong>(동적 데이터 포함)</p>
<pre><code class="language-jsp">&lt;jsp:include page=&quot;/banner.jsp&quot;&gt;
  &lt;jsp:param name=&quot;slot&quot; value=&quot;HOME_TOP&quot;/&gt;
&lt;/jsp:include&gt;</code></pre>
<p><strong>팁:</strong> 동적 include는 <strong>각 JSP가 독립적으로 실행</strong>되어 유지보수에 유리</p>
<hr />
<h3 id="📌-9-jsp-액션-jspforward-page">📌 9) JSP 액션: <code>&lt;jsp:forward page=&quot;...&quot;&gt;</code></h3>
<ul>
<li><p><strong>컴파일 시</strong> :<br />  <code>JspRuntimeLibrary.forward(...)</code> 호출 후 <code>SkipPageException</code> 처리</p>
</li>
<li><p><strong>런타임 시</strong> : forward 호출 후 현재 JSP의 나머지 출력은 스킵</p>
</li>
</ul>
<blockquote>
<p>예시 </p>
</blockquote>
<p><strong>용도:</strong> 조건부로 다른 화면으로 넘기기(남은 출력 스킵)</p>
<pre><code class="language-jsp">&lt;c:if test=&quot;${empty sessionScope.user}&quot;&gt;
  &lt;jsp:forward page=&quot;/login.jsp&quot;/&gt;
&lt;/c:if&gt;</code></pre>
<p><strong>팁:</strong> 컨트롤러(서블릿/스프링)에서 <strong>forward/redirect</strong>를 결정하는 구조가 더 깔끔</p>
<hr />
<h3 id="📌-10-jsp-액션-usebean--setproperty--getproperty">📌 10) JSP 액션: useBean / setProperty / getProperty</h3>
<ul>
<li><p><strong>컴파일 시</strong> :<br />  <code>pageContext.findAttribute(...)</code> → 없으면 생성 → 세터 호출 코드 생성</p>
</li>
<li><p><strong>런타임 시</strong> : 빈 생성 및 속성 설정 코드 실행</p>
</li>
</ul>
<blockquote>
<p>예시 </p>
</blockquote>
<p><strong>용도:</strong> (레거시) JSP에서 자바빈을 생성/프로퍼티 채우기/출력</p>
<pre><code class="language-jsp">&lt;jsp:useBean id=&quot;form&quot; class=&quot;com.example.Form&quot; scope=&quot;request&quot;/&gt;
&lt;jsp:setProperty name=&quot;form&quot; property=&quot;*&quot; /&gt; &lt;%-- 파라미터 이름과 매핑 --%&gt;
이름: &lt;jsp:getProperty name=&quot;form&quot; property=&quot;name&quot;/&gt;</code></pre>
<p><strong>팁:</strong> 현대 실무는 컨트롤러가 DTO를 채워 <strong><code>request.setAttribute(&quot;form&quot;, dto)</code></strong> 로 전달</p>
<hr />
<h3 id="📌-11-커스텀-태그-jstl-c-fmt-등">📌 11) 커스텀 태그 (JSTL <code>&lt;c:...&gt;</code>, <code>&lt;fmt:...&gt;</code> 등)</h3>
<ul>
<li><p><strong>컴파일 시</strong> : 태그 핸들러 객체 생성 → <code>setPageContext</code> / 속성 setter → <code>doStartTag()</code> / <code>doEndTag()</code> 호출 코드 생성</p>
</li>
<li><p><strong>런타임 시</strong> : 태그 핸들러 메서드 실행으로 로직 수행</p>
</li>
</ul>
<blockquote>
<p>예시 </p>
</blockquote>
<p><strong>용도:</strong> 조건/반복/국제화/포맷팅/URL 빌드 등 뷰 로직</p>
<pre><code class="language-jsp">&lt;%@ taglib uri=&quot;http://java.sun.com/jsp/jstl/core&quot; prefix=&quot;c&quot; %&gt;
&lt;%@ taglib uri=&quot;http://java.sun.com/jsp/jstl/fmt&quot;  prefix=&quot;fmt&quot; %&gt;

&lt;c:if test=&quot;${not empty products}&quot;&gt;
  &lt;ul&gt;
    &lt;c:forEach var=&quot;p&quot; items=&quot;${products}&quot;&gt;
      &lt;li&gt;${p.name} - &lt;fmt:formatNumber value=&quot;${p.price}&quot; type=&quot;currency&quot;/&gt;&lt;/li&gt;
    &lt;/c:forEach&gt;
  &lt;/ul&gt;
&lt;/c:if&gt;</code></pre>
<p><strong>팁:</strong> 조건/반복은 <strong>JSTL</strong>로, 단순 출력/연산은 <strong>EL</strong>로. 스크립틀릿은 지양</p>
<hr />
<h3 id="📌-12-jsp-주석-------">📌 12) JSP 주석 <code>&lt;%-- ... --%&gt;</code></h3>
<ul>
<li><p><strong>번역 시</strong> : 아예 제거됨</p>
</li>
<li><p><strong>런타임 시</strong> : 실행/출력 없음 (클라이언트에 노출되지 않음)</p>
</li>
</ul>
<blockquote>
<p>예시 </p>
</blockquote>
<p><strong>용도:</strong> 운영에 노출되면 안 되는 내부 메모/비밀 값</p>
<pre><code class="language-jsp">&lt;%-- TODO: 결제 수수료 정책 변경(9/1) --%&gt;</code></pre>
<p><strong>팁:</strong> <strong>클라이언트에 절대 노출 안 됨</strong>. 반면 HTML 주석은 노출됨!</p>
<hr />
<h3 id="📌-13-html-주석-------">📌 13) HTML 주석 <code>&lt;!-- ... --&gt;</code></h3>
<ul>
<li><p><strong>컴파일 시</strong> : <code>out.write(&quot;&lt;!-- ... --&gt;&quot;)</code></p>
</li>
<li><p><strong>런타임 시</strong> : 그대로 클라이언트에 출력됨 (소스 보기에서 보임)</p>
</li>
</ul>
<blockquote>
<p>예시 </p>
</blockquote>
<p><strong>용도:</strong> 프론트 협업용 가이드 주석(노출 허용 가능 내용만)</p>
<pre><code class="language-jsp">&lt;!-- 여기는 런딩 상단 배너 영역 --&gt;</code></pre>
<p><strong>팁:</strong> <strong>브라우저 “보기-소스”에 그대로 보임</strong> 민감한 내용 금지</p>
<hr />
<h3 id="⚙️-실행-흐름-요약">⚙️ 실행 흐름 요약</h3>
<ol>
<li><p><strong>서블릿 로딩 시 (1회)</strong></p>
<ul>
<li>선언부의 <code>jspInit()</code> → <code>_jspInit()</code> 실행</li>
</ul>
</li>
<li><p><strong>매 요청마다</strong></p>
<ul>
<li><p><code>_jspService(request, response)</code> 실행</p>
</li>
<li><p>암묵 객체 준비 (<code>request</code>, <code>response</code>, <code>session</code>, <code>application</code>, <code>out</code> 등)</p>
</li>
<li><p>page 디렉티브 설정 적용</p>
</li>
<li><p>스크립틀릿 / 표현식 / EL / 액션 / 태그 순서대로 실행</p>
</li>
</ul>
</li>
<li><p><strong>서블릿 언로드 시 (1회)</strong></p>
<ul>
<li>선언부의 <code>jspDestroy()</code> → <code>_jspDestroy()</code></li>
</ul>
</li>
</ol>
<hr />