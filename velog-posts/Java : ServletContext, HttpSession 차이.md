<hr />
<h3 id="🕵️-servletcontext-vs-httpsession-차이">🕵️ ServletContext vs HttpSession 차이</h3>
<ul>
<li><strong>ServletContext</strong> application 객체 : 애플리케이션 전역 공유 저장소</li>
<li><strong>HttpSession</strong> session 객체 : 사용자(브라우저)별 개별 저장소</li>
</ul>
<p>둘 다 메모리에 key-value 속성 저장이 가능하지만 <code>범위</code> , <code>수명</code> , <code>공유</code> 대상이 다르다.</p>
<hr />
<h2 id="👀한눈에-비교해보기">👀한눈에 비교해보기</h2>
<table>
<thead>
<tr>
<th align="center">구분</th>
<th align="center">application(ServletContext)</th>
<th align="center">session(HttpSession)</th>
</tr>
</thead>
<tbody><tr>
<td align="center">범위(Scope)</td>
<td align="center">웹앱 전체(전역)</td>
<td align="center">사용자 (브라우저) 1명</td>
</tr>
<tr>
<td align="center">생성</td>
<td align="center">앱 시작</td>
<td align="center">사용자 최초 접속</td>
</tr>
<tr>
<td align="center">수명</td>
<td align="center">앱 시작-종료 (재배포/재시작 시 초기화)</td>
<td align="center">세션 생성-만료 (기본 30분 유휴 시 만료)</td>
</tr>
<tr>
<td align="center">공유 대상</td>
<td align="center">모든 서블릿 / 필터 / JSP</td>
<td align="center">같은 사용자의 모든 요청/탭</td>
</tr>
<tr>
<td align="center">사용 예</td>
<td align="center">전역 설정값 , 공용 캐시 핸들 , 레지스트리</td>
<td align="center">로그인 정보 , 장바구니 , 개인 설정</td>
</tr>
<tr>
<td align="center">스레드</td>
<td align="center">다수 스레드 종시 접근 (전역) 👉 동시성 주의</td>
<td align="center">동일 사용자라도 탭/동시요청으로 경합 가능</td>
</tr>
<tr>
<td align="center">크기/부하</td>
<td align="center">전 사용자 공용이므로 과도하면 전반 영향</td>
<td align="center">사용자 수 * 세션 크기 👉 메모리/복제 비용 커짐</td>
</tr>
<tr>
<td align="center">클러스터</td>
<td align="center">노드 간 자동 공유 아님(보통)</td>
<td align="center">컨테이너 설정으로 세션 복제 가능</td>
</tr>
<tr>
<td align="center">저장 위치</td>
<td align="center">서버 메모리(전역) , 영속❌</td>
<td align="center">서버 메모리(사용자별) , 영속❌</td>
</tr>
<tr>
<td align="center">대표 API</td>
<td align="center"><code>getServletContext()</code> / <code>application.getAttribute()</code></td>
<td align="center"><code>request.getSession()</code> / <code>session.getAttribute()</code></td>
</tr>
</tbody></table>
<hr />
<h2 id="기본-예시">기본 예시</h2>
<h4 id="application-전역-값">application 전역 값</h4>
<pre><code class="language-java">// Servlet
@Override
public void init() {
  getServletContext().setAttribute(&quot;cdnBaseUrl&quot;, &quot;https://cdn.example.com&quot;);
}

// JSP
CDN: ${applicationScope.cdnBaseUrl}</code></pre>
<h4 id="session-사용자별-값">session 사용자별 값</h4>
<pre><code class="language-java">// Servlet (로그인 성공 시)
request.getSession().setAttribute(&quot;loginUser&quot;, userDto);</code></pre>
<pre><code class="language-jsp">&lt;!-- JSP --&gt;
&lt;c:if test=&quot;${not empty sessionScope.loginUser}&quot;&gt;
  안녕하세요, ${sessionScope.loginUser.name}님
&lt;/c:if&gt;</code></pre>
<hr />
<h3 id="🕵️-실무-가이드---언제-무엇을-쓰나">🕵️ 실무 가이드 - 언제 무엇을 쓰나</h3>
<ul>
<li>요청 1회 렌더용 데이터 : <code>request.setAttribute(...)</code> 👉 <code>forward</code> (페이지 바인딩용)</li>
<li>사용자별 상태(로그인 , 장바구니 , 일시 설정) : <code>session</code></li>
<li>앱 전역 설정/공용 리소스 핸들(예 : 캐시매니저 , 읽기 전용 설정 값)  : <code>application</code></li>
</ul>
<hr />
<h3 id="⚠️-주의할-점">⚠️ 주의할 점</h3>
<blockquote>
<p>동시성</p>
</blockquote>
<ul>
<li><code>application</code>에 넣는 가변 객체는 <code>ConcurrentHashMap</code> , <code>Atomic*</code> 등으로 스레드 안전하게</li>
<li><code>session</code>도 같은 사용자가 여러 탭에서 동시에 호출할 수 있어 경합 가능</li>
</ul>
<blockquote>
<p>용량 관리</p>
</blockquote>
<ul>
<li>세션에 큰 객체(대형 리스트 , 이미지 바이트 등) 넣지 말 것 (메모리 폭증 , 세션복제 비용🆙)</li>
<li>전역(application)에도 캐시 남발 금지 - 메모리/재배포 이슈</li>
</ul>
<blockquote>
<p>만료/타임아웃</p>
</blockquote>
<ul>
<li>세션 기본 타임아웃은 <code>web.xml</code> 또는 설정으로 조정 필요 시 <code>session.invalidate()</code>로 명시 종료</li>
</ul>
<blockquote>
<p>클러스터링</p>
</blockquote>
<ul>
<li>세션 복제 사용 시 세션 속성은 직렬화 가능해야 함</li>
<li><code>application</code> 전역 공유가 노드 간 자동 동기화 되는 건 아님 👉 외부 스토어(예 : Redis) 고려</li>
</ul>
<blockquote>
<p>보안</p>
</blockquote>
<ul>
<li>민감정보는 세션에도 최소한만 저장(토큰 , 식별자 등)</li>
<li><code>JSESSIONID</code>는 쿠키(또는 URL 재작성)로 식별됨 - HTTPS , HttpOnly 설정 확인</li>
</ul>
<hr />
<h2 id="메서드-요약">메서드 요약</h2>
<h3 id="servletcontext-application">ServletContext (application)</h3>
<table>
<thead>
<tr>
<th>메서드</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td><code>setAttribute(name, value)</code></td>
<td>앱 전역 키에 객체 저장(기존 값이면 교체)</td>
</tr>
<tr>
<td><code>getAttribute(name)</code></td>
<td>전역 키로 객체 조회</td>
</tr>
<tr>
<td><code>removeAttribute(name)</code></td>
<td>전역 키 제거</td>
</tr>
<tr>
<td><code>getAttributeNames()</code></td>
<td>전역 저장소의 키 나열</td>
</tr>
<tr>
<td><code>getInitParameter(name)</code></td>
<td><code>web.xml</code>의 <code>&lt;context-param&gt;</code> 값 읽기</td>
</tr>
<tr>
<td><code>getContextPath()</code></td>
<td>애플리케이션 컨텍스트 경로(<code>/myapp</code>)</td>
</tr>
<tr>
<td><code>getResourceAsStream(path)</code></td>
<td>리소스를 읽기용 <code>InputStream</code>으로 획득</td>
</tr>
<tr>
<td><code>getRequestDispatcher(path)</code></td>
<td>내부 <code>forward/include</code>용 디스패처 반환</td>
</tr>
<tr>
<td><code>getMimeType(file)</code></td>
<td>파일명으로 MIME 타입 추정</td>
</tr>
<tr>
<td><code>log(msg)</code></td>
<td>컨테이너 로그에 메시지 기록</td>
</tr>
<tr>
<td>전체 메서드 목록 공식 문서 참고: <strong>ServletContext Javadoc (Jakarta 6.0)</strong>. <a href="https://jakarta.ee/specifications/servlet/6.0/apidocs/jakarta.servlet/jakarta/servlet/servletcontext">jakarta.ee</a></td>
<td></td>
</tr>
<tr>
<td>(참고: <strong>javax Servlet 4.0 Javadoc</strong>도 필요 시 확인) <a href="https://www.javadoc.io/doc/javax.servlet/javax.servlet-api/latest/javax/servlet/ServletContext.html">Javadoc</a></td>
<td></td>
</tr>
</tbody></table>
<h3 id="httpsession-session">HttpSession (session)</h3>
<table>
<thead>
<tr>
<th>메서드</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td><code>setAttribute(name, value)</code></td>
<td>사용자 세션에 값 저장</td>
</tr>
<tr>
<td><code>getAttribute(name)</code></td>
<td>세션 값 조회</td>
</tr>
<tr>
<td><code>removeAttribute(name)</code></td>
<td>세션 값 제거</td>
</tr>
<tr>
<td><code>getAttributeNames()</code></td>
<td>세션 키 나열</td>
</tr>
<tr>
<td><code>getId()</code></td>
<td>현재 세션 ID 반환</td>
</tr>
<tr>
<td><code>isNew()</code></td>
<td>이번 요청에서 막 생성된 세션인지</td>
</tr>
<tr>
<td><code>getCreationTime()</code></td>
<td>세션 생성 시각(ms)</td>
</tr>
<tr>
<td><code>getLastAccessedTime()</code></td>
<td>마지막 접근 시각(ms)</td>
</tr>
<tr>
<td><code>setMaxInactiveInterval(seconds)</code></td>
<td>유휴 타임아웃(초) 설정</td>
</tr>
<tr>
<td><code>invalidate()</code></td>
<td>세션 무효화(로그아웃 등)</td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
</tbody></table>
<p>전체 메서드 목록 공식 문서: <strong>HttpSession Javadoc (Jakarta 6.0)</strong>. <a href="https://jakarta.ee/specifications/servlet/6.0/apidocs/jakarta.servlet/jakarta/servlet/http/httpsession">jakarta.ee</a><br />(참고: <strong>javax Servlet 4.0/EE7 Javadoc</strong>도 필요 시 확인) <a href="https://docs.oracle.com/javaee/7/api/javax/servlet/http/HttpSession.html?source=docs">Oracle Docs</a></p>
<hr />