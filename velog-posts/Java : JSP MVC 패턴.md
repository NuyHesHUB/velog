<hr />
<h2 id="🕵️-mvc란">🕵️ MVC란</h2>
<p>초기 웹 개발은 <strong>템플릿</strong> 안에 서버 코드를 섞어 넣는 방식이 주류였다(ASP, PHP 그리고 JSP의 스크립틀릿) 배우기 쉽고 결과가 바로 보이는 장점이 있었지만 프로젝트 규모가 클 수록 스파게티 코드로 유지보수가 어려웠다.</p>
<p><strong>MVC(Model - View - Controller)</strong> : 화면, 데이터, 제어를 역할별로 분리해 개발 유지보수를 쉽게 만드는 아키텍쳐 패턴이다.</p>
<ul>
<li><code>Model</code> : 비즈니스 로직과 데이터(도메인, 서비스, DAO)</li>
<li><code>View</code> : 사용자에게 보여줄 화면(템플릿, JSP/Thymeleaf/HTML)</li>
<li><code>Controller</code> : 요청을 받아 검증/권한 확인 후 <code>Model</code>을 호출하고 결과를 <code>View</code>에 전달</li>
</ul>
<hr />
<h3 id="model-1-jsp가-controller--view">Model 1 (JSP가 Controller + View)</h3>
<blockquote>
<p>어떻게 생겼나?</p>
</blockquote>
<ul>
<li><code>JSP</code>가 요청을 직접 받고(request.getParameter), 비즈니스 호출(JavaBean/DAO) 화면 출력까지 한 페이지에서 해결한다.</li>
<li>필요하면 <code>RequestDispatcher.forward()</code>로 다른 <code>JSP</code>로 넘겨 출력만 분리하기도 했지만 컨트롤러 역할은 여전히 JSP가 맡았다.</li>
</ul>
<blockquote>
<p>등장 배경</p>
</blockquote>
<ul>
<li>당장 빠르게 화면을 만들 수 있음</li>
<li>도구/프레임워크가 성숙하지 않았고 팀도 소규모인 경우</li>
</ul>
<blockquote>
<p>드러난 문제</p>
</blockquote>
<ul>
<li>역할 혼재 : 파라미터 검증, 인증/권한, 로깅, 예외가 JSP마다 제각각</li>
<li>중복과 스파게티화 : 페이지가 늘수록 비슷한 로직의 복붙 지옥</li>
<li>테스트/보안/유지보수의 어려움 : 화면 바꾸다 로직이 깨지고 로직 바꾸다 화면이 깨짐</li>
</ul>
<p>이렇게 Model1은 빠르게 만들 수 있는 장점이 있지만 규모가 커질수록 관리가 어렵다는 한계를 드러냈다.</p>
<blockquote>
<p>개념</p>
</blockquote>
<ul>
<li>요청을 <code>JSP</code>가 직접 받음 👉 JSP 안에서 파라미터 처리/검증/비즈니스 호출 (보통 JavaBean/DAO) 👉 결과를 같은 <code>JSP</code>또는 다른 <code>JSP</code>로 출력</li>
<li>즉 <code>Controller</code>역할을 <code>JSP</code>가 겸함 <code>Model(JavaBean/DAO)</code>은 별도 클래스</li>
</ul>
<blockquote>
<p>요청 흐름</p>
</blockquote>
<pre><code class="language-markdown">Browser → list.jsp(컨트롤러 역할) → JavaBean/DAO → request.setAttribute(...)
       → (같은 JSP에서 렌더 or 다른 JSP로 forward)</code></pre>
<blockquote>
<p>짧은 예시</p>
</blockquote>
<pre><code class="language-jsp">&lt;%@ page import=&quot;com.example.MemberDao&quot; %&gt;
&lt;jsp:useBean id=&quot;memberDao&quot; class=&quot;com.example.MemberDao&quot; /&gt;
&lt;%
  var list = memberDao.findAll();          // 컨트롤러 역할
  request.setAttribute(&quot;members&quot;, list);   // 모델 전달
%&gt;
&lt;ul&gt;
  &lt;c:forEach var=&quot;m&quot; items=&quot;${members}&quot;&gt;
    &lt;li&gt;${m.name}&lt;/li&gt;
  &lt;/c:forEach&gt;
&lt;/ul&gt;</code></pre>
<hr />
<h3 id="model-2-mvc--servlet-controller--jsp-view">Model 2 (MVC : Servlet Controller + JSP View)</h3>
<blockquote>
<p>어떻게 생겼나?</p>
</blockquote>
<ul>
<li><code>Servlet</code>이 <code>Front Controller</code>가 되어 라우팅, 검증, 권한, 예외, 로깅 등 흐름 제어를 한곳에서 처리</li>
<li><code>Service/DAO</code>로 비즈니스 데이터 계층을 분리</li>
<li><code>JSP</code>는 <code>View</code>전용(JSTL/EL)으로 표현만 담당</li>
<li>필요한 데이터는 <code>request.setAttribute()</code>로 모델을 담아 <code>forward</code>로 <code>JSP</code>에 전달</li>
</ul>
<blockquote>
<p>왜 이렇게 바뀌었나?</p>
</blockquote>
<ul>
<li>관심사 분리를 강제해 테스트/리팩토링/협업을 가능하게 하려면 컨트롤러를 코드(서블릿)로 통일해야 했다.</li>
<li>공통 로직(인증/로깅/인코딩)을 Filter/Interceptor에서 중앙집중으로 처리하고 싶었음</li>
<li>Post, Redirect, Get 국제화, 예외 처리 표준화 같은 베스트 프랙티스를 일관되게 적용하려면 중앙 진입점이 필요</li>
</ul>
<blockquote>
<p>개념</p>
</blockquote>
<ul>
<li><code>Servlet</code>이 Controller, <code>JSP</code>는 View전용(JSTL/EL로만 표현)</li>
<li><code>Front Controller(하나의 서블릿)</code>로 URL 매핑/검증/권한/예외/로그를 중앙집중</li>
<li>오늘날 <strong>Spring MVC</strong>가 이 철학을 프레임워크로 표준화한 형태</li>
</ul>
<p>💡 <code>Model2</code>는 규모와 팀을 견딜 수 있는 구조를 제공했고 오늘날 Spring MVC/Boot로 사실상 표준이 되었다.</p>
<blockquote>
<p>요청 흐름</p>
</blockquote>
<pre><code class="language-markdown">Browser → Servlet(Controller) → Service → DAO
       → request.setAttribute(... 모델 ...)
       → forward(&quot;/WEB-INF/views/xxx.jsp&quot;) → JSP(View)</code></pre>
<blockquote>
<p>짧은 예시</p>
</blockquote>
<pre><code class="language-java">// controller
@WebServlet(&quot;/members/detail&quot;)
public class MemberController extends HttpServlet {
  private final MemberService svc = new MemberService();
  @Override protected void doGet(HttpServletRequest req, HttpServletResponse resp)
      throws IOException, ServletException {
    String id = req.getParameter(&quot;id&quot;);
    if (id == null || id.isBlank()) { resp.sendError(400); return; }
    var member = svc.findById(id);
    if (member == null) { resp.sendError(404); return; }
    req.setAttribute(&quot;member&quot;, member);
    req.getRequestDispatcher(&quot;/WEB-INF/views/member/detail.jsp&quot;).forward(req, resp);
  }
}</code></pre>
<pre><code class="language-jsp">// view
&lt;!-- /WEB-INF/views/member/detail.jsp --&gt;
&lt;h1&gt;회원 상세&lt;/h1&gt;
&lt;p&gt;이름: ${member.name}&lt;/p&gt;</code></pre>
<hr />
<h2 id="비-mvc--model-1--model-2-요약">비 MVC / Model 1 / Model 2 요약</h2>
<h3 id="📌-비-mvc-페이지-스크립틀릿-중심">📌 비-MVC (페이지 스크립틀릿 중심)</h3>
<ul>
<li>핵심 아이디어 : JSP 한 장이 입력 처리 + 비즈니스 + 출력까지</li>
<li>요청 흐름 : Browser → JSP(모두 처리) → HTML</li>
<li>주 사용 기술 : JSP 스크립틀릿 <code>&lt;% ... %&gt;</code>, JDBC 직결</li>
<li>장점 : 시작이 빠름, 파일 수 적음</li>
<li>단점 : 뷰 로직 혼재, 테스트/확장/보안 취약, 유지보수 어려움</li>
</ul>
<hr />
<h3 id="📌-model-1">📌 Model 1</h3>
<ul>
<li>핵심 아이디어 : JSP가 <strong>Controller+View</strong>, Model은 JavaBean</li>
<li>요청 흐름 : Browser → <strong>JSP(컨트롤러 역할)</strong> → JavaBean/DAO → <strong>JSP(View)</strong></li>
<li>주 사용 기술 : JSP + JSTL + JavaBean</li>
<li>장점 : Model 분리 일부 가능, 곡선 완만</li>
<li>단점 : 여전히 컨트롤러가 JSP, URL/보안/검증의 중복</li>
</ul>
<hr />
<h3 id="📌-model-2">📌 Model 2</h3>
<ul>
<li>핵심 아이디어 : <strong>Servlet Controller</strong> + <strong>JSP View</strong> (정통 MVC)</li>
<li>요청 흐름 : Browser → <strong>Servlet(Controller)</strong> → Service/DAO → <strong>JSP(View)</strong></li>
<li>주 사용 기술 : Servlet, JSP/JSTL, Filter(Front Controller)</li>
<li>장점 : 책임분리, 테스트/확장/보안 용이</li>
<li>단점 : 초기 구조화 필요</li>
</ul>
<hr />