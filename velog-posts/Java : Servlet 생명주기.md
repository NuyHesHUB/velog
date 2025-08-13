<hr />
<h3 id="🕵️-httpservlet-제대로-이해하기">🕵️ HttpServlet 제대로 이해하기</h3>
<p>📄HttpServlet.class</p>
<pre><code class="language-java">public abstract class HttpServlet extends GenericServlet {

    protected void doGet   ...

    protected void doPost  ...

    protected void service ...
}</code></pre>
<p>서블릿 컨테이너는 이름과 시그니처가 약속된 메서드만 호출한다. 그래서 <code>doGet</code> , <code>doPost</code> , <code>init</code> , <code>destroy</code> , <code>service</code> 같은 훅 메서드를 정확히 <code>override</code>해야 한다.</p>
<hr />
<h2 id="생명주기">생명주기</h2>
<table>
<thead>
<tr>
<th align="center">전체 생명 주기</th>
</tr>
</thead>
<tbody><tr>
<td align="center"><strong>배포/시작</strong></td>
</tr>
<tr>
<td align="center">웹앱이 배포되고 컨테이너(Tomcat 등)가 시작</td>
</tr>
<tr>
<td align="center">⬇️</td>
</tr>
<tr>
<td align="center"><strong>클래스 로딩 &amp; 인스턴스 생성</strong></td>
</tr>
<tr>
<td align="center">서블릿 클래스 로딩 👉 인스턴스 1개 생성(기본)</td>
</tr>
<tr>
<td align="center">⬇️</td>
</tr>
<tr>
<td align="center"><strong>초기화</strong></td>
</tr>
<tr>
<td align="center">init (ServletConfig) 👉 보통 <code>init()</code> ovverride로 리소스 준비</td>
</tr>
<tr>
<td align="center">⬇️</td>
</tr>
<tr>
<td align="center"><strong>요청 처리 루프 (요청마다 반복)</strong></td>
</tr>
<tr>
<td align="center">▫️ URL 매핑 결정 👉 필터 체인 전처리 👉 스레드에서 service(req, resp) 호출<br />▫️ HttpServlet (HttpServletRequest, HttpServletResponse)가<br />HTTP 메서드에 따라 <code>doGet/doPost/...</code>로 분기<br />▫️ 응답 커밋 👉 필터 체인 후처리 👉 커넥션 반환</td>
</tr>
<tr>
<td align="center">⬇️</td>
</tr>
<tr>
<td align="center"><strong>종료</strong></td>
</tr>
<tr>
<td align="center">앱/컨테이너가 내려갈 때 <code>destroy()</code> 호출 👉 리소스 정리, 스레드풀 종료</td>
</tr>
<tr>
<td align="center">⬇️</td>
</tr>
<tr>
<td align="center"><strong>재로딩/핫리로드</strong></td>
</tr>
<tr>
<td align="center">변경/재배포 시 기존 인스턴스 <code>destroy()</code> 후 새 인스턴스 <code>init()</code></td>
</tr>
</tbody></table>
<blockquote>
<p>🕵️ 인스턴스는 보통 하나이고 요청마다 다른 스레드가 <code>service()</code>를 호출한다. 따라서 인스턴스 필드에 요청상태를 저장하면 안됨</p>
</blockquote>
<hr />
<h2 id="메서드-요약">메서드 요약</h2>
<table>
<thead>
<tr>
<th align="center">메서드</th>
<th>누가 호출?</th>
<th>언제</th>
<th>기본 동작(override ❌)</th>
</tr>
</thead>
<tbody><tr>
<td align="center">init()</td>
<td>컨테이너</td>
<td>서블릿 초기화 1회</td>
<td>아무것도 안함 (리소스 준비는 개발자 구현)</td>
</tr>
<tr>
<td align="center">service(ServletRequest, ServletResponse)</td>
<td>컨테이너</td>
<td>모든 요청</td>
<td>HTTP가 아니면 예외<br />HTTP면 아래 service로 위임</td>
</tr>
<tr>
<td align="center">service(HttpServletRequest, HttpServletResponse)</td>
<td>HttpServlet</td>
<td>HTTP 요청</td>
<td>메서드별로 <strong>doXXX</strong> 디스패치, GET/HEAD의 캐싱 처리 포함</td>
</tr>
<tr>
<td align="center">doGet()</td>
<td>HttpServlet#service</td>
<td>GET</td>
<td>405/400 에러 (미구현시)</td>
</tr>
<tr>
<td align="center">doPost()</td>
<td>HttpServlet#service</td>
<td>POST</td>
<td>405/400 에러 (미구현시)</td>
</tr>
<tr>
<td align="center">doPut() / doDelete()</td>
<td>HttpServlet#service</td>
<td>PUT / DELETE</td>
<td>405/400 에러 (미구현시)</td>
</tr>
<tr>
<td align="center">doHead()</td>
<td>HttpServlet#service</td>
<td>HEAD</td>
<td>기본은 <strong>doGet</strong> 재사용 (바디 제거)</td>
</tr>
<tr>
<td align="center">doOptions()</td>
<td>HttpServlet#service</td>
<td>OPTIONS</td>
<td>서브클래스의 <strong>doXXX</strong> 존재 여부를 반영해 <strong>Allow</strong>헤더 자동 구성</td>
</tr>
<tr>
<td align="center">doTrace()</td>
<td>HttpServlet#service</td>
<td>TRACE</td>
<td>요청 라인 / 헤더 에코 (보안상 비활성 권장)</td>
</tr>
<tr>
<td align="center">destroy()</td>
<td>컨테이너</td>
<td>종료 1회</td>
<td>리로스 정리는 개발자 구현</td>
</tr>
</tbody></table>
<hr />
<h3 id="🕵️-servlet--genericservlet--httpservlet-구조">🕵️ Servlet / GenericServlet / HttpServlet 구조</h3>
<h4 id="📄servletclass">📄Servlet.class</h4>
<blockquote>
<p>인터페이스</p>
</blockquote>
<ol>
<li>정의 : 컨테이너 (톰캣 등)와 서블릿이 어떻게 상호작용하는지를 약속</li>
<li>핵심 메서드<ul>
<li><code>init(ServletConfig)</code> : 최초 1회 초기화</li>
<li><code>service(ServletRequest, ServletResponse)</code> : 요청마다 호출</li>
<li><code>destroy()</code> : 종료 시 1회 정리</li>
<li><code>getServletConfig()</code> , <code>getServletInfo()</code></li>
</ul>
</li>
</ol>
<blockquote>
<p>포인트 : 여기엔 로직이 없고 &quot;생명주기 훅이 이런 이름/시그니처로 제공된다&quot; 수준의 스펙만 있다.</p>
</blockquote>
<pre><code class="language-java">public interface Servlet {  
    void init(ServletConfig var1) throws ServletException;  

    ServletConfig getServletConfig();  

    void service(ServletRequest var1, ServletResponse var2) throws ServletException, IOException;  

    String getServletInfo();  

    void destroy();  
}</code></pre>
<h4 id="📄genericservletclass">📄GenericServlet.class</h4>
<blockquote>
<p>추상 클래스 - 프로토콜 무관 기본 구현</p>
</blockquote>
<ol>
<li>상속/구현 : implements <code>Servlet</code> , <code>ServletConfig</code><ul>
<li><code>Servlet</code>의 계약을 <strong>기본 구현</strong>으로 편하게 제공</li>
</ul>
</li>
<li>역할<ul>
<li><code>init(ServletConfig)</code> 안에서 <code>this.config</code> 보관 후 <strong>매개변수 없는</strong> <code>init()</code>을 호출</li>
<li><code>getServletConfig()</code> , <code>getServletContext()</code> , <code>getInitParameter()</code> 등 유틸 제공</li>
<li><code>log()</code> 같은 로깅 편의 메서드 제공</li>
<li><code>service(ServletRequest, ServletResponse)</code>는 <code>abstract</code> 실제 요청 처리는 하위 클래스가 구현하도록 남겨둔다.</li>
</ul>
</li>
</ol>
<pre><code class="language-java">public abstract class GenericServlet implements Servlet, ServletConfig, Serializable {  
    private static final String LSTRING_FILE = &quot;javax.servlet.LocalStrings&quot;;  
    private static ResourceBundle lStrings = ResourceBundle.getBundle(&quot;javax.servlet.LocalStrings&quot;);  
    private transient ServletConfig config;  

    public void destroy() {  
    }  

    public String getInitParameter(String name) {  
        ServletConfig sc = this.getServletConfig();  
        if (sc == null) {  
            throw new IllegalStateException(lStrings.getString(&quot;err.servlet_config_not_initialized&quot;));  
        } else {  
            return sc.getInitParameter(name);  
        }  
    }  

    public Enumeration&lt;String&gt; getInitParameterNames() {  
        ServletConfig sc = this.getServletConfig();  
        if (sc == null) {  
            throw new IllegalStateException(lStrings.getString(&quot;err.servlet_config_not_initialized&quot;));  
        } else {  
            return sc.getInitParameterNames();  
        }  
    }  

    public ServletConfig getServletConfig() {  
        return this.config;  
    }  

    public ServletContext getServletContext() {  
        ServletConfig sc = this.getServletConfig();  
        if (sc == null) {  
            throw new IllegalStateException(lStrings.getString(&quot;err.servlet_config_not_initialized&quot;));  
        } else {  
            return sc.getServletContext();  
        }  
    }  

    public String getServletInfo() {  
        return &quot;&quot;;  
    }  

    public void init(ServletConfig config) throws ServletException {  
        this.config = config;  
        this.init();  
    }  

    public void init() throws ServletException {  
    }  

    public void log(String msg) {  
        this.getServletContext().log(this.getServletName() + &quot;: &quot; + msg);  
    }  

    public void log(String message, Throwable t) {  
        this.getServletContext().log(this.getServletName() + &quot;: &quot; + message, t);  
    }  

    public abstract void service(ServletRequest var1, ServletResponse var2) throws ServletException, IOException;  

    public String getServletName() {  
        ServletConfig sc = this.getServletConfig();  
        if (sc == null) {  
            throw new IllegalStateException(lStrings.getString(&quot;err.servlet_config_not_initialized&quot;));  
        } else {  
            return sc.getServletName();  
        }  
    }  
}</code></pre>
<h4 id="📄httpservletclass">📄HttpServlet.class</h4>
<blockquote>
<p>추상 클래스 - HTTP 전용 구현 + 메서드 분기</p>
</blockquote>
<ol>
<li>상속 : extends <code>GenericServlet</code></li>
<li>핵심 아이디어 : HTTP 요청이라면 <code>GET/POST/PUT/DELETE/ . . .</code> 메서드 별로 자동 분기해주는 틀을 제공</li>
<li>메서드 구조<ul>
<li>오버로드된 <code>service</code> 2종<pre><code>  - `public void service(ServletRequest, ServletResponse)` HTTP 전용 객체로 캐스팅 후 아래 HTTP 전용 `service(HttpServletRequest, HttpServletResponse)` 호출
  - `protected void service(HttpServletRequest, HttpServletResponse)` `req.getMethod()`로 분기해서 `doGet/doPost/doPut/doDelete . . .` 호출</code></pre></li>
<li><code>doGet/doPost/doPut/doDelete/ . . .</code><pre><code>  - 우리가 **주로 오버라이드하는 지점**
  - 오버라이드하지 않으면 보통 **405(Method Not Allowed**)가 응답된다.</code></pre></li>
<li><code>getLastModified(HttpServletRequest)</code><pre><code>  - `doGet`과 연계되는 **조건부 GET(if-Modified-Since) 지원 포인트** 타임스탬프를 반환하면 `Last-Modified` 헤더 처리와 304 응답 최적화가 가능 (미구현 시 -1)</code></pre></li>
</ul>
</li>
</ol>
<pre><code class="language-java">public abstract class HttpServlet extends GenericServlet {  
    private static final String METHOD_DELETE = &quot;DELETE&quot;;  
    private static final String METHOD_HEAD = &quot;HEAD&quot;;  
    private static final String METHOD_GET = &quot;GET&quot;;  
    private static final String METHOD_OPTIONS = &quot;OPTIONS&quot;;  
    private static final String METHOD_POST = &quot;POST&quot;;  
    private static final String METHOD_PUT = &quot;PUT&quot;;  
    private static final String METHOD_TRACE = &quot;TRACE&quot;;  
    private static final String HEADER_IFMODSINCE = &quot;If-Modified-Since&quot;;  
    private static final String HEADER_LASTMOD = &quot;Last-Modified&quot;;  
    private static final String LSTRING_FILE = &quot;javax.servlet.http.LocalStrings&quot;;  
    private static ResourceBundle lStrings = ResourceBundle.getBundle(&quot;javax.servlet.http.LocalStrings&quot;);  

    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {  
        String protocol = req.getProtocol();  
        String msg = lStrings.getString(&quot;http.method_get_not_supported&quot;);  
        if (protocol.endsWith(&quot;1.1&quot;)) {  
            resp.sendError(405, msg);  
        } else {  
            resp.sendError(400, msg);  
        }  

    }  

    protected long getLastModified(HttpServletRequest req) {  
        return -1L;  
    }  

    protected void doHead(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {  
        NoBodyResponse response = new NoBodyResponse(resp);  
        this.doGet(req, response);  
        response.setContentLength();  
    }  

    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {  
        String protocol = req.getProtocol();  
        String msg = lStrings.getString(&quot;http.method_post_not_supported&quot;);  
        if (protocol.endsWith(&quot;1.1&quot;)) {  
            resp.sendError(405, msg);  
        } else {  
            resp.sendError(400, msg);  
        }  

    }  

    protected void doPut(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {  
        String protocol = req.getProtocol();  
        String msg = lStrings.getString(&quot;http.method_put_not_supported&quot;);  
        if (protocol.endsWith(&quot;1.1&quot;)) {  
            resp.sendError(405, msg);  
        } else {  
            resp.sendError(400, msg);  
        }  

    }  

    protected void doDelete(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {  
        String protocol = req.getProtocol();  
        String msg = lStrings.getString(&quot;http.method_delete_not_supported&quot;);  
        if (protocol.endsWith(&quot;1.1&quot;)) {  
            resp.sendError(405, msg);  
        } else {  
            resp.sendError(400, msg);  
        }  

    }  

    private Method[] getAllDeclaredMethods(Class&lt;? extends HttpServlet&gt; c) {  
        Class&lt;?&gt; clazz = c;  

        Method[] allMethods;  
        for(allMethods = null; !clazz.equals(HttpServlet.class); clazz = clazz.getSuperclass()) {  
            Method[] thisMethods = clazz.getDeclaredMethods();  
            if (allMethods != null &amp;&amp; allMethods.length &gt; 0) {  
                Method[] subClassMethods = allMethods;  
                allMethods = new Method[thisMethods.length + allMethods.length];  
                System.arraycopy(thisMethods, 0, allMethods, 0, thisMethods.length);  
                System.arraycopy(subClassMethods, 0, allMethods, thisMethods.length, subClassMethods.length);  
            } else {  
                allMethods = thisMethods;  
            }  
        }  

        return allMethods != null ? allMethods : new Method[0];  
    }  

    protected void doOptions(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {  
        Method[] methods = this.getAllDeclaredMethods(this.getClass());  
        boolean ALLOW_GET = false;  
        boolean ALLOW_HEAD = false;  
        boolean ALLOW_POST = false;  
        boolean ALLOW_PUT = false;  
        boolean ALLOW_DELETE = false;  
        boolean ALLOW_TRACE = true;  
        boolean ALLOW_OPTIONS = true;  

        for(int i = 0; i &lt; methods.length; ++i) {  
            String methodName = methods[i].getName();  
            if (methodName.equals(&quot;doGet&quot;)) {  
                ALLOW_GET = true;  
                ALLOW_HEAD = true;  
            } else if (methodName.equals(&quot;doPost&quot;)) {  
                ALLOW_POST = true;  
            } else if (methodName.equals(&quot;doPut&quot;)) {  
                ALLOW_PUT = true;  
            } else if (methodName.equals(&quot;doDelete&quot;)) {  
                ALLOW_DELETE = true;  
            }  
        }  

        StringBuilder allow = new StringBuilder();  
        if (ALLOW_GET) {  
            allow.append(&quot;GET&quot;);  
        }  

        if (ALLOW_HEAD) {  
            if (allow.length() &gt; 0) {  
                allow.append(&quot;, &quot;);  
            }  

            allow.append(&quot;HEAD&quot;);  
        }  

        if (ALLOW_POST) {  
            if (allow.length() &gt; 0) {  
                allow.append(&quot;, &quot;);  
            }  

            allow.append(&quot;POST&quot;);  
        }  

        if (ALLOW_PUT) {  
            if (allow.length() &gt; 0) {  
                allow.append(&quot;, &quot;);  
            }  

            allow.append(&quot;PUT&quot;);  
        }  

        if (ALLOW_DELETE) {  
            if (allow.length() &gt; 0) {  
                allow.append(&quot;, &quot;);  
            }  

            allow.append(&quot;DELETE&quot;);  
        }  

        if (ALLOW_TRACE) {  
            if (allow.length() &gt; 0) {  
                allow.append(&quot;, &quot;);  
            }  

            allow.append(&quot;TRACE&quot;);  
        }  

        if (ALLOW_OPTIONS) {  
            if (allow.length() &gt; 0) {  
                allow.append(&quot;, &quot;);  
            }  

            allow.append(&quot;OPTIONS&quot;);  
        }  

        resp.setHeader(&quot;Allow&quot;, allow.toString());  
    }  

    protected void doTrace(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {  
        String CRLF = &quot;\r\n&quot;;  
        StringBuilder buffer = (new StringBuilder(&quot;TRACE &quot;)).append(req.getRequestURI()).append(&quot; &quot;).append(req.getProtocol());  
        Enumeration&lt;String&gt; reqHeaderEnum = req.getHeaderNames();  

        while(reqHeaderEnum.hasMoreElements()) {  
            String headerName = (String)reqHeaderEnum.nextElement();  
            buffer.append(CRLF).append(headerName).append(&quot;: &quot;).append(req.getHeader(headerName));  
        }  

        buffer.append(CRLF);  
        int responseLength = buffer.length();  
        resp.setContentType(&quot;message/http&quot;);  
        resp.setContentLength(responseLength);  
        ServletOutputStream out = resp.getOutputStream();  
        out.print(buffer.toString());  
    }  

    protected void service(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {  
        String method = req.getMethod();  
        if (method.equals(&quot;GET&quot;)) {  
            long lastModified = this.getLastModified(req);  
            if (lastModified == -1L) {  
                this.doGet(req, resp);  
            } else {  
                long ifModifiedSince = req.getDateHeader(&quot;If-Modified-Since&quot;);  
                if (ifModifiedSince &lt; lastModified) {  
                    this.maybeSetLastModified(resp, lastModified);  
                    this.doGet(req, resp);  
                } else {  
                    resp.setStatus(304);  
                }  
            }  
        } else if (method.equals(&quot;HEAD&quot;)) {  
            long lastModified = this.getLastModified(req);  
            this.maybeSetLastModified(resp, lastModified);  
            this.doHead(req, resp);  
        } else if (method.equals(&quot;POST&quot;)) {  
            this.doPost(req, resp);  
        } else if (method.equals(&quot;PUT&quot;)) {  
            this.doPut(req, resp);  
        } else if (method.equals(&quot;DELETE&quot;)) {  
            this.doDelete(req, resp);  
        } else if (method.equals(&quot;OPTIONS&quot;)) {  
            this.doOptions(req, resp);  
        } else if (method.equals(&quot;TRACE&quot;)) {  
            this.doTrace(req, resp);  
        } else {  
            String errMsg = lStrings.getString(&quot;http.method_not_implemented&quot;);  
            Object[] errArgs = new Object[1];  
            errArgs[0] = method;  
            errMsg = MessageFormat.format(errMsg, errArgs);  
            resp.sendError(501, errMsg);  
        }  

    }  

    private void maybeSetLastModified(HttpServletResponse resp, long lastModified) {  
        if (!resp.containsHeader(&quot;Last-Modified&quot;)) {  
            if (lastModified &gt;= 0L) {  
                resp.setDateHeader(&quot;Last-Modified&quot;, lastModified);  
            }  

        }  
    }  

    public void service(ServletRequest req, ServletResponse res) throws ServletException, IOException {  
        if (req instanceof HttpServletRequest &amp;&amp; res instanceof HttpServletResponse) {  
            HttpServletRequest request = (HttpServletRequest)req;  
            HttpServletResponse response = (HttpServletResponse)res;  
            this.service(request, response);  
        } else {  
            throw new ServletException(&quot;non-HTTP request or response&quot;);  
        }  
    }  
}</code></pre>
<h4 id="호출-흐름-요약">호출 흐름 요약</h4>
<table>
<thead>
<tr>
<th align="center">호출 흐름</th>
</tr>
</thead>
<tbody><tr>
<td align="center">컨테이너</td>
</tr>
<tr>
<td align="center">⬇️</td>
</tr>
<tr>
<td align="center">service(ServletRequest, ServletResponse)</td>
</tr>
<tr>
<td align="center">⬇️</td>
</tr>
<tr>
<td align="center">(HttpServletRequest/Response로 캐스팅)</td>
</tr>
<tr>
<td align="center">⬇️</td>
</tr>
<tr>
<td align="center">service(HttpServletRequest, HttpServletResponse)</td>
</tr>
<tr>
<td align="center">⬇️</td>
</tr>
<tr>
<td align="center">HTTP 메서드별 doXXX ... 로 분기</td>
</tr>
</tbody></table>
<hr />
<h3 id="🕵️-언제-무엇을-오버라이드할까">🕵️ 언제 무엇을 오버라이드할까</h3>
<ul>
<li>대부분의 경우 : <code>doGet()</code> , <code>doPost()</code>만 구현하면 충분</li>
<li>공통 전/후처리 (로깅, 트랜잭션 등) : <code>service(HttpServletRequest, HttpServletResponse)</code>를 오버라이드하고 반드시 <code>super.service(req, resp)</code>호출해서 기본 분기 유지<pre><code class="language-java">@Override
protected void service(HttpServletRequest req, HttpServletResponse resp)
  throws ServletException, IOException {
long t0 = System.nanoTime();
try {
  super.service(req, resp); // doGet/doPost 분기 유지!
} finally {
  log(req.getMethod() + &quot; &quot; + req.getRequestURI() + &quot; took &quot; + (System.nanoTime()-t0));
}
}</code></pre>
</li>
</ul>
<blockquote>
<p>💡정말 필요할 때만 : <code>service(ServletRequest, ServletResponse)</code>를 건드리자 (비-HTTP 요청 차단 등 특수 케이스)</p>
</blockquote>
<hr />
<h2 id="최소-예시">최소 예시</h2>
<pre><code class="language-java">@WebServlet(&quot;/hello&quot;)
public class HelloServlet extends HttpServlet {

  @Override
  protected void doGet(HttpServletRequest req, HttpServletResponse resp)
      throws IOException {
    resp.setCharacterEncoding(&quot;UTF-8&quot;);
    resp.setContentType(&quot;text/plain;charset=UTF-8&quot;);
    resp.getWriter().println(&quot;Hello, GET!&quot;);
  }

  @Override
  protected void doPost(HttpServletRequest req, HttpServletResponse resp)
      throws IOException {
    // 폼 처리 등
    resp.getWriter().println(&quot;Hello, POST!&quot;);
  }
}</code></pre>
<hr />