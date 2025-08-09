<hr />
<h3 id="🕵️-서블릿-필터filter란">🕵️ 서블릿 필터(Filter)란?</h3>
<p><strong>필터</strong>는 <code>Java</code> 웹 어플리케이션에서 <strong>클라이언트 요청(Request)</strong>과 서블릿/리소스 처리 그리고 <strong>응답(Response)</strong> 사이에 끼어들어 공통 작업을 처리할 수 있는 기능이다.</p>
<blockquote>
<p>필터가 할 수 있는 대표적인 일</p>
</blockquote>
<ul>
<li>요청/응답 인코딩 처리 (UTF-8)</li>
<li>인증/인가 처리</li>
<li>로깅/모니터링</li>
<li>압축, 이미지 변환 등 데이터 가공</li>
</ul>
<blockquote>
<p>구조</p>
</blockquote>
<p><code>[클라이언트] 👉 (Filter) 👉 [서블릿/JSP] 👉 (Filter) 👉 [클라이언트]</code></p>
<hr />
<h2 id="필터-생명주기--스레드-안전성">필터 생명주기 &amp; 스레드 안전성</h2>
<p>컨테이너 시작 시 <strong>한번 생성</strong> 👉 여러 요청을 <strong>다중 스레드</strong>로 처리</p>
<blockquote>
<p>생명 주기 메서드</p>
</blockquote>
<ul>
<li><code>init(FilterConfig config)</code> : 초기화 (초기 파라미터 읽기 등)</li>
<li><code>doFilter(ServletRequest, ServletResponse, FilterChain)</code> : 전/후처리</li>
<li><code>destory()</code> : 종료 정리</li>
</ul>
<hr />
<h2 id="패키지-생성">패키지 생성</h2>
<pre><code class="language-java">package com.example.test.filter;  

import javax.servlet.*;  
import java.io.IOException;  

public class CharacterEncodingFilter implements Filter {  
        @Override  
        public void doFilter(ServletRequest req, ServletResponse resp, FilterChain chain)  
        throws IOException, SecurityException, ServletException {  
            req.setCharacterEncoding(&quot;UTF-8&quot;);  
            chain.doFilter(req, resp);  
        }  
}</code></pre>
<p>해당 패키지에 filter를 추가한 패키지를 만들고 클래스를 생성한다.</p>
<hr />
<h2 id="실행-순서">실행 순서</h2>
<ul>
<li><code>web.xml</code>에서 선언한 <code>&lt;filter-mapping&gt;</code> 순서대로 실행<pre><code class="language-xml">&lt;filter-mapping&gt;  
  &lt;filter-name&gt;Filter&lt;/filter-name&gt;  
  &lt;url-pattern&gt;/*&lt;/url-pattern&gt;  
&lt;/filter-mapping&gt;
  ...
&lt;filter-mapping&gt;  
  ...
&lt;/filter-mapping&gt;
  ...
  ...</code></pre>
</li>
<li><strong>어노테이션(@WebFilter)</strong>만 쓰면 순서는 컨테이너 구현에 의존할 수 있음 -&gt; 순서가 중요하면 web.xml에 명시</li>
</ul>
<hr />
<h2 id="매핑-방법">매핑 방법</h2>
<ul>
<li>URL 패턴 : <code>/*</code> , <code>/api/*</code> , <code>*.jsp</code> 등</li>
<li>디스패처 타입 (기본 : REQUEST) : <code>REQUEST</code> , <code>FORWARD</code> , <code>INCLUDE</code> , <code>ERROR</code> , <code>ASYNC</code> ( 예 : 에러 페이지에도 적용하려면 <code>ERROR</code> 추가)</li>
</ul>
<hr />
<h2 id="많이-쓰이는-패턴-예제">많이 쓰이는 패턴 예제</h2>
<blockquote>
<p>1) 인코딩 필터 (전처리만)</p>
</blockquote>
<pre><code class="language-java">public class CharacterEncodingFilter implements Filter {
  @Override
  public void doFilter(ServletRequest req, ServletResponse resp, FilterChain chain)
      throws IOException, ServletException {
    req.setCharacterEncoding(&quot;UTF-8&quot;);   // getParameter 호출보다 먼저!
    chain.doFilter(req, resp);
  }
}</code></pre>
<hr />
<blockquote>
<p>2) 로깅/타이밍 필터 (전 후처리)</p>
</blockquote>
<pre><code class="language-java">public class LoggingFilter implements Filter {
  @Override
  public void doFilter(ServletRequest req, ServletResponse resp, FilterChain chain)
      throws IOException, ServletException {
    long start = System.currentTimeMillis();
    try {
      chain.doFilter(req, resp); // 다음 단계로
    } finally {
      long took = System.currentTimeMillis() - start;
      System.out.println(&quot;Request took &quot; + took + &quot;ms&quot;);
    }
  }
}</code></pre>
<p><code>try/finally</code>로 <strong>후처리 보장</strong></p>
<hr />
<blockquote>
<p>3) 인증 필터 (짧게 차단하기)</p>
</blockquote>
<pre><code class="language-java">public class AuthFilter implements Filter {
  @Override
  public void doFilter(ServletRequest req, ServletResponse resp, FilterChain chain)
      throws IOException, ServletException {
    var httpReq = (javax.servlet.http.HttpServletRequest) req;
    var httpResp = (javax.servlet.http.HttpServletResponse) resp;

    boolean ok = httpReq.getSession(false) != null;
    if (!ok) {
      httpResp.sendError(401); // 또는 redirect
      return;                  // 체인 중단
    }
    chain.doFilter(req, resp);
  }
}</code></pre>
<hr />
<h2 id="설정-방법">설정 방법</h2>
<h3 id="webxml-방법-명시적-순서-제어-용이">web.xml 방법 (명시적, 순서 제어 용이)</h3>
<pre><code class="language-xml">&lt;filter&gt;
  &lt;filter-name&gt;CharacterEncodingFilter&lt;/filter-name&gt;
  &lt;filter-class&gt;com.example.test.filter.CharacterEncodingFilter&lt;/filter-class&gt;
&lt;/filter&gt;

&lt;filter-mapping&gt;
  &lt;filter-name&gt;CharacterEncodingFilter&lt;/filter-name&gt;
  &lt;url-pattern&gt;/*&lt;/url-pattern&gt;
  &lt;dispatcher&gt;REQUEST&lt;/dispatcher&gt;
&lt;/filter-mapping&gt;</code></pre>
<ul>
<li>여러 필터가 있으면 <code>&lt;filter-mapping&gt;</code> 순서가 실행 순서</li>
<li>환경별 설정 분리, 팀 협업, 세밀한 순서 제어에 유리</li>
</ul>
<hr />
<h3 id="어노테이션-webfilter-방법">어노테이션 (@WebFilter 방법)</h3>
<pre><code class="language-java">import javax.servlet.*;
import javax.servlet.annotation.WebFilter;
import java.io.IOException;

@WebFilter(
  urlPatterns = &quot;/*&quot;,
  dispatcherTypes = { DispatcherType.REQUEST, DispatcherType.ERROR }  // 필요 시
  // asyncSupported = true
)
public class CharacterEncodingFilter implements Filter {
  @Override
  public void doFilter(ServletRequest req, ServletResponse resp, FilterChain chain)
      throws IOException, ServletException {
    req.setCharacterEncoding(&quot;UTF-8&quot;);
    chain.doFilter(req, resp);
  }
}</code></pre>
<ul>
<li>장점 : <code>XML</code>없이 한 파일에 정의 (빠르고 직관적)</li>
<li>주의 : 필터 순서 보장 어려움 (정밀한 순서 제어 필요하면 web.xml 추천) </li>
</ul>
<hr />