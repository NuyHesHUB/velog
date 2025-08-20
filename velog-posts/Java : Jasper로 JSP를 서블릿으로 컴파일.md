<hr />
<h2 id="jasper의-역할">Jasper의 역할</h2>
<h4 id="1-jsp를-서블릿으로-변환">1) JSP를 서블릿으로 변환</h4>
<p><code>Jasper</code>는 JSP 파일 내의 코드를 Java 서블릿 코드로 변환한다.
이 과정에서 <code>HTML</code> , <code>CSS</code> , <code>JavaScript</code>와 같은 정적 요소는 그대로 유지되고 JSP 코드 부분은 서블릿의 <code>_jspService()</code>메서드 내로 삽입된다.</p>
<h4 id="2-변환-및-컴파일">2) 변환 및 컴파일</h4>
<p>변환된 서블릿 코드는 <code>Java</code>컴파일러에 의해 컴파일 되어 실행 가능한 클래스 파일 <code>.class</code>로 만들어진다.</p>
<h4 id="3-서블릿-실행">3) 서블릿 실행</h4>
<p>컴파일된 서블릿은 웹 서버(Tomcat 등)에 의해 실행되어 동적인 웹 페이지를 생성한다. 생성된 결과는 <code>HTML</code> 형태로 웹 브라우저에 반환된다.</p>
<hr />
<h2 id="🕵️-jasper-서블릿-출력">🕵️ Jasper 서블릿 출력</h2>
<p>기존의 방식은 해당 클래스에서 <code>service</code>메서드에서 <code>write</code>메서드를 사용하여 한줄씩 출력을 했는데 <code>Jasper</code>로 서블릿 코드로 컴파일되는 과정을 알아보자.</p>
<blockquote>
<p>기존 직접 write 메서드 출력</p>
</blockquote>
<pre><code class="language-java">@Override
protected void service(HttpServletRequest req, HttpServletResponse resp) throws IOException {
    PrintWriter out = resp.getWriter();
    out.write(&quot;&lt;!DOCTYPE html&gt;&quot;);  
    out.write(&quot;&lt;html lang=\&quot;ko\&quot;&gt;&quot;);
    out.write(&quot;&lt;h1&gt;Hello&lt;/h1&gt;&quot;);
    ...
    ...
    ...
}</code></pre>
<h3 id="intellij에서-컴파일-소스-및-경로-확인하는-방법">IntelliJ에서 컴파일 소스 및 경로 확인하는 방법</h3>
<ol>
<li>프로젝트 <code>Run</code> 👉 <code>Tomcat</code> 실행</li>
<li><code>JSP</code> 페이지를 한 번 요청 (하지 않으면 컴파일 안됨)</li>
<li>Run 로그를 보면 아래와 같은 해당 프로젝트 컴파일 폴더 확인</li>
</ol>
<pre><code>NOTE: Picked up JDK_JAVA_OPTIONS:  --add-opens=java.base/java.lang=ALL-UNNAMED --

...

...

org.apache.catalina.startup.VersionLoggerListener.log 서버 버전 이름:    Apache Tomcat/9.0.107

...

...

org.apache.catalina.startup.VersionLoggerListener.log 🟢CATALINA_BASE:     C:\Users\AppData\Local\JetBrains\IntelliJIdea2025.2\tomcat\2596f31e-f49b-4c02-8e15-adf6744b5601🟢

...

...
</code></pre><blockquote>
<p>해당 프로젝트의 톰캣 컴파일 경로</p>
</blockquote>
<pre><code class="language-powershell">&quot;C:\Users\AppData\Local\JetBrains\IntelliJIdea2025.2\tomcat\2596f31e-f49b-4c02-8e15-adf6744b5601\work\Catalina\localhost\ROOT\org\apache\jsp\프로젝트명_jsp.java&quot;</code></pre>
<p>📄 프로젝트명_jsp.java <code>_jsp.java</code> 파일로 컴파일이 된다.</p>
<h3 id="컴파일-코드">컴파일 코드</h3>
<pre><code class="language-java">public final class 프로젝트명_jsp extends HttpJspBase {

  // JSP 실행에 필요한 팩토리 (PageContext 생성용)
  private static final JspFactory _jspxFactory = JspFactory.getDefaultFactory();

  public void _jspInit() {
    // 필요 시 초기화 로직 (JSP 선언부 &lt;%! %&gt;에서 넘어옴)
  }

  public void _jspDestroy() {
    // 종료 시 정리 로직
  }

  public void _jspService(HttpServletRequest request, HttpServletResponse response)
      throws IOException, ServletException {

    // 1) 허용 메서드 간단 체크 (실제 Jasper는 OPTIONS/HEAD 등도 처리)
    String m = request.getMethod();
    if (!&quot;GET&quot;.equals(m) &amp;&amp; !&quot;POST&quot;.equals(m)) {
      response.setHeader(&quot;Allow&quot;, &quot;GET, POST&quot;);
      response.sendError(HttpServletResponse.SC_METHOD_NOT_ALLOWED,
          &quot;JSP는 GET/POST만 허용(요약본)&quot;);
      return;
    }

    // 2) PageContext/암묵객체 준비
    PageContext pageContext = null;
    JspWriter out = null;
    try {
      // 문자셋 명시 (원본 코드에서 한글 깨짐 방지 포인트)
      response.setContentType(&quot;text/html; charset=UTF-8&quot;);

      pageContext = _jspxFactory.getPageContext(
          this, request, response,
          null,      // errorPage URL
          true,      // needsSession
          8192,      // buffer size
          true       // autoflush
      );

      HttpSession session = pageContext.getSession();
      ServletContext application = pageContext.getServletContext();
      ServletConfig config = pageContext.getServletConfig();
      out = pageContext.getOut();

      // 3) 정적 HTML은 out.write(...)
      out.write(&quot;&lt;!DOCTYPE html&gt;\n&quot;);
      out.write(&quot;&lt;html lang=\&quot;ko\&quot;&gt;\n&lt;head&gt;\n&lt;meta charset=\&quot;UTF-8\&quot;/&gt;\n&quot;);
      out.write(&quot;&lt;title&gt;JSP - Hello World&lt;/title&gt;\n&quot;);
      ...
      ...
      ...



    } catch (Throwable t) {
      // 4) 예외 처리 (버퍼/에러 페이지 처리 요약)
      if (out != null) {
        try {
          if (response.isCommitted()) out.flush();
          else out.clearBuffer();
        } catch (IOException ignore) {}
      }
      if (pageContext != null) pageContext.handlePageException(t);
      else throw new ServletException(t);
    } finally {
      // 5) PageContext 반환(리소스 정리)
      _jspxFactory.releasePageContext(pageContext);
    }
  }
}
</code></pre>
<ul>
<li><code>_jspService</code> 안에서 모든 출력과 로직이 실행된다.</li>
<li>정적 HTML 👉 <code>out.write</code>, El 👉 전용 평가 호출, 스크립틀릿 👉 자바 코드로 들어간다.</li>
<li>EL이 보려면 <code>attribute</code> 스코프에 넣어야한다.</li>
<li>문자셋은 <code>contentType</code>에 <code>charset</code>지정이 핵심</li>
<li>에러 처리 / 버퍼 / 리소스 반납의 기본적인 뼈대</li>
</ul>
<hr />