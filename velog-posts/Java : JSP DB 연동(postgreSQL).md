<hr />
<h2 id="🕵️-jsp-dbpostgresql-연동">🕵️ JSP DB(PostgreSQL) 연동</h2>
<p>JSP 프로젝트를 하게 되어 학습을 하고있는 상황이다. 간단하게 해당 프로젝트에 DB연동을 위해 작성하게 되었다. 현재 환경은 <code>IntelliJ</code> + <code>Maven</code> + <code>JSP</code> + <code>PostgreSQL</code> 이다. </p>
<hr />
<h2 id="📌-1-maven-의존성-추가">📌 1. Maven 의존성 추가</h2>
<ol>
<li><code>pom.xml</code>에 PostgreSQL JDBC 드라이버를 넣는다.</li>
</ol>
<pre><code class="language-xml">&lt;dependencies&gt;  
    ...
    ...
    ...
    &lt;dependency&gt;  
        &lt;groupId&gt;org.postgresql&lt;/groupId&gt;  
        &lt;artifactId&gt;postgresql&lt;/artifactId&gt;  
        &lt;version&gt;42.7.3&lt;/version&gt;  
    &lt;/dependency&gt;  
&lt;/dependencies&gt;</code></pre>
<ol start="2">
<li><code>IntelliJ</code> → <code>View</code> → <code>Tool Windows</code> → <code>Maven</code> 클릭 후 상단 Sync 아이콘을 클릭하여 <code>Reload All Maven Projects</code>를 클릭한다.</li>
</ol>
<hr />
<h2 id="📌-2-jsp에서-jdbc를-이용한-db-연동">📌 2. JSP에서 JDBC를 이용한 DB 연동</h2>
<h3 id="1️⃣-url--sql-문자열">1️⃣ URL &amp; SQL 문자열</h3>
<ol>
<li>URL : DB URL 문자열을 만든다. </li>
</ol>
<pre><code class="language-jsp">&lt;%
    String url = &quot;jdbc:postgresql://localhost:5432/project&quot;;
    ...
    ...
%&gt;</code></pre>
<ul>
<li>형식 : <code>jdbc:postgresql://&lt;host&gt;:&lt;port&gt;/&lt;database&gt;?&lt;params&gt;</code></li>
<li>예 : <code>jdbc:postgresql://localhost:5432/project?currentSchema=public&amp;ApplicationName=myapp</code></li>
</ul>
<hr />
<h4 id="🕵️-자주-쓰는-postgres-파라미터">🕵️ 자주 쓰는 Postgres 파라미터</h4>
<ul>
<li><code>currentSchema=스키마명</code> : 기본 스키마 지정 (예 : app, public 다중도 가능)</li>
<li><code>sslmode=</code> : <code>disable</code>|<code>allow</code>|<code>prefer</code>|<code>require</code>|<code>verify-ca</code>|<code>verify-full</code></li>
<li><code>connectTimeout=10</code> : 접속 타임아웃(초)</li>
<li><code>socketTimeout=30</code> : 쿼리 실행 대기 타임아웃(초)</li>
<li><code>ApplicationName=myapp</code> : 접속 식별용 이름</li>
<li><code>reWriteBatchedInserts=true</code> : 배치 INSERT 최적화</li>
<li><code>stringtype=unspecified</code> : 문자열 파라미터 타입 유연화(특정 케이스에 유용)</li>
</ul>
<hr />
<ol start="2">
<li>SQL : 실행할 쿼리</li>
</ol>
<pre><code class="language-jsp">&lt;%
    String sql = &quot;SELECT * FROM NOTICE&quot;;
    ...
    ...
%&gt;</code></pre>
<ul>
<li>베스트 : <code>SELECT 컬럼명만</code> 지정 (와일드카드 * 지양) 스키마 명시 <code>ex) public.notice</code></li>
<li>동적 값이 섞이면 <code>PreparedStatement</code>로 파라미터 바인딩</li>
</ul>
<hr />
<h4 id="🕵️-preparedstatement란">🕵️ PreparedStatement란?</h4>
<p><code>SQL</code>문을 미리 준비하고 컴파일하여 캐시된 실행 계획을 반복적으로 재사용하는 데이터베이스 객체로, <code>SQL</code>쿼리 실행 속도를 향상시키고 <code>SQL Injection</code> 공격을 방지하는 보안 기능도 제공한다. <code>Statement</code>와 달리 물음표(?)와 같은 플레이스 홀더를 사용해 동적인 데이터 바인딩하는 방식으로 데이터 베이스에서 동일하거나 비슷한 <code>SQL</code>문을 효율적으로 실행할 때 사용된다.</p>
<p><strong>주요 특징 및 동작 방식</strong></p>
<ol>
<li>미리 컴파일 및 캐싱 : SQL문을 처음 실행할 때 구문 분석(parse) 및 컴파일 과정을 거쳐 실행 계획을 데이터베이스의 캐시에 저장</li>
<li>플레이스홀더 사용 : SQL문에 직접 데이터를 넣는 대신 플레이스홀더를 사용하여 변수 값을 전달할 위치를 지정</li>
<li>데이터 바인딩 : 이후 데이터가 필요할 때는 플레이스홀더에 해당 데이터를 바인딩하여 미리 컴파일된 실행 계획을 재사용</li>
<li>성능 향상 : 캐싱된 실행 계획 덕분에 동일한 SQL문을 여러번 실행할 때 구문 분석 및 컴파일 과정을 생략할 수 있어 실행 속도가 빨라진다.</li>
<li>SQL 삽입 방지 : 개발자가 SQL문과 데이터를 분리하여 처리하므로 악의적인 사용자가 SQL 코드를 삽입하여 데이터를 조작하는 SQL Injection 공격을 효과적으로 막을 수 있다.</li>
</ol>
<p><strong>Statement와 차이</strong></p>
<ol>
<li>성능 : PreparedStatement는 컴파일된 실행 계획을 캐시하여 재사용하므로 Statement보다 일반적으로 성능이 우수</li>
<li>사용 : PreparedStatement는 동일한 SQL 쿼리를 반복적으로 실행해야 할 때 유리하며 INSERT, UPDATE, DELETE 문에서 자주 사용된다. Statement는 고정된 SQL문을 실행하거나 SQL 구문 자체가 동적으로 변경될 때 적합하다.</li>
</ol>
<hr />
<h3 id="2️⃣-계정-정보">2️⃣ 계정 정보</h3>
<ol>
<li>단순 사용자/비밀번호 문자열을 적었다 실제 프로젝트에서는 다른 방식을 사용해야한다. (예 : 환경변수, properties, YAML 분리) 운영에서는 커넥션 풀(DataSource)로 관리</li>
</ol>
<pre><code class="language-jsp">&lt;%
    String user = &quot;postgres&quot;;
    String pass = &quot;비밀번호&quot;;
    ...
    ...
%&gt;</code></pre>
<blockquote>
<p>💡 하드코딩은 지양</p>
</blockquote>
<hr />
<h3 id="3️⃣-드라이버-로딩">3️⃣ 드라이버 로딩</h3>
<ol>
<li>드라이버 클래스 로딩 및 <code>DriverManager</code>등록</li>
</ol>
<pre><code class="language-jsp">&lt;%
    Class.forName(&quot;org.postgresql.Driver&quot;);
    ...
    ...
%&gt;</code></pre>
<ul>
<li><p>JDBC 4.0+ (PostgreSQL JDBC 8.x/42.x 계열)에서는 <strong>생략해도 자동 로딩</strong>되는 경우가 많음</p>
</li>
<li><p><code>ClassNotFoundException</code> 발생 시: Maven 의존성 확인</p>
</li>
</ul>
<hr />
<h3 id="4️⃣-연결-생성">4️⃣ 연결 생성</h3>
<ol>
<li><code>DriverManager.getConnection</code> 오버로드</li>
</ol>
<pre><code class="language-jsp">&lt;%
    Connection con = DriverManager.getConnection(url, user, pass);
    ...
    ...
%&gt;</code></pre>
<ul>
<li><p><code>(url, user, pass)</code> — 지금 방식</p>
</li>
<li><p><code>(url)</code> — URL에 user/password 파라미터 포함 시</p>
</li>
<li><p><code>(url, Properties props)</code> — 세부 옵션을 <code>Properties</code>로 전달</p>
</li>
</ul>
<ol start="2">
<li><p>유용한 Connection 설정</p>
<ul>
<li><code>con.setAutoCommit(false);</code> 트랜잭션 수동제어 (INSERT/UPDATE/DELETE 후 commit/rollback)</li>
<li><code>con.setTransactionIsolation(Connection.TRANSACTION_REPEATABLE_READ);</code> 등 격리수준 설정</li>
</ul>
</li>
<li><p>더 좋은 실무 방식</p>
<ul>
<li>커넥션 풀(DataSource) 사용 (예 : HikariCP) → 성능/안정성 ↑</li>
<li>서블릿 컨테이너(Tomcat)라면 JNDI로 DataSource 바인딩해서 꺼내 쓰기</li>
</ul>
</li>
</ol>
<hr />
<h3 id="5️⃣statement-생성">5️⃣Statement 생성</h3>
<pre><code class="language-jsp">&lt;%
    Statement st = con.createStatement();
    ...
    ...
%&gt;</code></pre>
<ul>
<li>기본(전방만, 읽기 전용) ResultSet을 생성하는 Statement</li>
<li>오버로드(스크롤/동시성/홀더빌리티 지정)<pre><code class="language-java">Statement st = con.createStatement(
  ResultSet.TYPE_SCROLL_INSENSITIVE,   // 스크롤 가능(원본 변경 반영 X)
  ResultSet.CONCUR_READ_ONLY,          // 읽기 전용
  ResultSet.HOLD_CURSORS_OVER_COMMIT   // COMMIT 후에도 커서 유지(드물게 사용)
);</code></pre>
</li>
<li>권장 : Statement 대신 PreparedStatement(파라미터 바인딩 + SQL 인젝션 방지 + 캐시)</li>
</ul>
<hr />
<h3 id="6️⃣sql-실행">6️⃣SQL 실행</h3>
<pre><code class="language-jsp">&lt;%
    ResultSet rs = st.executeQuery(sql);
    ...
    ...
%&gt;</code></pre>
<ul>
<li><code>executeQuery(sql)</code> : SELECT 전용, 결과는 <code>ResultSet</code></li>
<li>다른 실행 메서드<ul>
<li><code>executeUpdate(sql)</code> : INSERT/UPDATE/DELETE 반환값은 영향 받은 행 수 <code>int</code></li>
<li><code>execute(sql)</code> : 결과가 <code>ResultSet</code>인지 업데이트 카운트인지 모를 때</li>
<li>배치 : <code>addBatch()/executeBatch()</code> - 대량 <code>INSERT/UPDATE</code>최적화</li>
</ul>
</li>
</ul>
<hr />
<p>9️⃣🔟</p>
<h3 id="7️⃣resultset-사용-요령핵심">7️⃣ResultSet 사용 요령(핵심)</h3>
<p><strong>읽기 패턴</strong></p>
<pre><code class="language-java">while (rs.next()) {               // 다음 행으로 이동, 없으면 false
    int id = rs.getInt(&quot;id&quot;);     // 컬럼명 또는 1부터 시작하는 인덱스
    String title = rs.getString(&quot;title&quot;);
}</code></pre>
<ul>
<li>컬럼명/라벨<ul>
<li><code>SELECT id AS notice_id</code> 라벨 지정 시 <code>rs.getInt(&quot;notice_id&quot;)</code></li>
<li>Postgres는 따옴표 없이 만든 컬럼은 소문자 라벨로 취급(대소문자 헷갈리면 컬럼 라벨 확인)</li>
</ul>
</li>
<li>NULL 처리<ul>
<li><code>rs.getInt(...)</code>뒤에 <code>rs.wasNull()</code>로 방금 읽은 값이 NULL인지 확인 가능</li>
<li>객체형(<code>getObject</code>, <code>getString</code>, <code>getTimestamp</code>)은 그대로 null 반환</li>
</ul>
</li>
<li>스크롤 가능 ResultSet(필요 시)</li>
</ul>
<hr />
<h4 id="🕵️-resultset에서-스크롤이란">🕵️ ResultSet에서 스크롤이란?</h4>
<p>JDBC에서 <strong>ResultSet을 스크롤 가능하게 만들 수 있는 옵션</strong>은 <code>ResultSet</code>이 기본적으로 <strong>순방향(Forward-only)</strong> 으로만 레코드를 읽을 수 있기 때문이다.</p>
<p>즉, 기본 <code>ResultSet</code>은</p>
<ul>
<li><p><code>.next()</code> 메서드로 <strong>앞으로 한 칸씩</strong>만 이동 가능</p>
</li>
<li><p>이미 지난 행으로 <strong>뒤로 돌아갈 수 없음</strong></p>
</li>
<li><p>특정 행 번호로 바로 이동도 불가능</p>
</li>
</ul>
<p>이를 해결하기 위해 <strong>스크롤 가능한 ResultSet</strong> 옵션을 사용하면,<br /><code>next()</code> 뿐만 아니라 <code>previous()</code>, <code>absolute(n)</code>, <code>relative(n)</code> 같은 메서드로 <strong>앞뒤 이동</strong>과 <strong>임의 위치 이동</strong>이 가능해진다.</p>
<hr />
<h3 id="8️⃣예외자원-정리매우-중요">8️⃣예외/자원 정리(매우 중요)</h3>
<ul>
<li>예외<ul>
<li><code>ClassNotFoundException</code> : 드라이버 없음 → 의존성 점검</li>
<li><code>SQLException</code> : 인증 실패, URL 오타, 권한, 타임아웃 등</li>
</ul>
</li>
<li>자원 닫기 순서 : <code>ResultSet</code> → <code>Statement</code> → <code>Connection</code></li>
<li>try-with-resources 권장<pre><code class="language-java">String sql = &quot;SELECT id, title FROM notice&quot;;
try (Connection con = DriverManager.getConnection(url, user, pass);
   PreparedStatement ps = con.prepareStatement(sql);
   ResultSet rs = ps.executeQuery()) {
  while (rs.next()) {
      ...
  }
} catch (SQLException e) {
  // 로깅/처리
}</code></pre>
</li>
</ul>
<hr />
<h4 id="🕵️-jsp에-jdbc를-직접-넣는-것에-대해">🕵️ JSP에 JDBC를 직접 넣는 것에 대해</h4>
<ul>
<li>학습 수준에선 괜찮으나 실무에선 MVC 분리 권장<ul>
<li><strong>DAO/Service(자바 클래스)</strong>에 DB코드 → 서블릿/컨트롤러에서 호출 → JSP는 출력만(JSTL/EL)</li>
</ul>
</li>
</ul>
<blockquote>
<p>실전형 리팩터링 예시</p>
</blockquote>
<p><strong>자바(서블릿/DAO) - 데이터 읽기</strong></p>
<pre><code class="language-java">// NoticeDao.java
public class NoticeDao {
    private final DataSource ds; // HikariCP or JNDI로 주입

    public NoticeDao(DataSource ds) { this.ds = ds; }

    public List&lt;Notice&gt; findAll() throws SQLException {
        String sql = &quot;SELECT id, title FROM public.notice ORDER BY id ASC&quot;;
        List&lt;Notice&gt; list = new ArrayList&lt;&gt;();
        try (Connection con = ds.getConnection();
             PreparedStatement ps = con.prepareStatement(sql);
             ResultSet rs = ps.executeQuery()) {
            while (rs.next()) {
                Notice n = new Notice();
                n.setId(rs.getInt(&quot;id&quot;));
                n.setTitle(rs.getString(&quot;title&quot;));
                list.add(n);
            }
        }
        return list;
    }
}</code></pre>
<blockquote>
<p>💡 컨트롤러(서블릿)에서 <code>request.setAttribute(&quot;noticeList&quot;, dao.findAll());</code> 후 JSP로 <code>forward</code>.</p>
</blockquote>
<p><strong>JSP - 출력만(JSTL)</strong></p>
<pre><code class="language-jsp">&lt;%@ taglib prefix=&quot;c&quot; uri=&quot;http://java.sun.com/jsp/jstl/core&quot; %&gt;
&lt;table&gt;
  &lt;thead&gt;&lt;tr&gt;&lt;th&gt;ID&lt;/th&gt;&lt;th&gt;Title&lt;/th&gt;&lt;/tr&gt;&lt;/thead&gt;
  &lt;tbody&gt;
    &lt;c:forEach var=&quot;n&quot; items=&quot;${noticeList}&quot;&gt;
      &lt;tr&gt;
        &lt;td&gt;${n.id}&lt;/td&gt;
        &lt;td&gt;${n.title}&lt;/td&gt;
      &lt;/tr&gt;
    &lt;/c:forEach&gt;
  &lt;/tbody&gt;
&lt;/table&gt;</code></pre>
<hr />