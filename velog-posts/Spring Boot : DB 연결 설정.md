<p>SprignBoot 백엔드 프로젝트에서 DB 연결 설정을 해보려고한다.</p>
<h2 id="1-buildgradle-의존성-확인">1. build.gradle (의존성 확인)</h2>
<p>현재 Gradle을 사용하고 있으므로 루트 디렉토리에 <code>build.gradle</code> 파일을 확인한다.</p>
<pre><code class="language-java">plugins {
    id 'java'
    id 'org.springframework.boot' version '3.4.3'
    id 'io.spring.dependency-management' version '1.1.7'
}

group = 'com.example'
version = '0.0.1-SNAPSHOT'

java {
    toolchain {
        languageVersion = JavaLanguageVersion.of(21)
    }
}

repositories {
    mavenCentral()
}

dependencies {
    implementation 'org.springframework.boot:spring-boot-starter'
    implementation 'org.springframework.boot:spring-boot-starter-web'
    testImplementation 'org.springframework.boot:spring-boot-starter-test'
    testRuntimeOnly 'org.junit.platform:junit-platform-launcher'
}

tasks.named('test') {
    useJUnitPlatform()
}
</code></pre>
<p><code>dependencies</code>에 의존성을 추가해준다.</p>
<pre><code class="language-java">// ✅ JPA 추가 (DB와 연결)
implementation 'org.springframework.boot:spring-boot-starter-data-jpa'

// ✅ PostgreSQL JDBC 드라이버 추가
runtimeOnly 'org.postgresql:postgresql'

// ✅ Lombok (선택) - 코드 간결하게 작성 가능
compileOnly 'org.projectlombok:lombok'
annotationProcessor 'org.projectlombok:lombok'

// ✅ 테스트 관련 (기존 유지)
testImplementation 'org.springframework.boot:spring-boot-starter-test'
testRuntimeOnly 'org.junit.platform:junit-platform-launcher'</code></pre>
<h2 id="2-yaml-또는-properties-파일-설정">2. yaml 또는 properties 파일 설정</h2>
<pre><code>src/
└── main/
    └── resources/
        ├── application.yml  ✅ (또는)
        └── application.properties ✅</code></pre><p>기존 <code>application.properties</code> 에서 </p>
<pre><code>spring.application.name=demo
server.port=9090</code></pre><p>로 설정해 놓은 게 있는데 <code>yml</code> 파일을 만들어서 해도 되고 기존의 properties파일에서 추가를 해도 된다.</p>
<p><strong>예시 1: application.yml로 설정 (YAML 형식)</strong></p>
<pre><code class="language-yml">spring:
  datasource:
    url: jdbc:postgresql://localhost:5432/mydb
    username: postgres
    password: 비밀번호
    driver-class-name: org.postgresql.Driver

  jpa:
    hibernate:
      ddl-auto: update
    show-sql: true</code></pre>
<p><strong>예시 2: application.properties로 설정 (Key-Value 형식)</strong></p>
<pre><code>spring.datasource.url=jdbc:postgresql://localhost:5432/mydb
spring.datasource.username=postgres
spring.datasource.password=비밀번호
spring.datasource.driver-class-name=org.postgresql.Driver

spring.jpa.hibernate.ddl-auto=update
spring.jpa.show-sql=true</code></pre><table>
<thead>
<tr>
<th>상황</th>
<th>추천 방법</th>
</tr>
</thead>
<tbody><tr>
<td>기존에 <code>application.properties</code>만 있다</td>
<td>그 안에 설정 작성해도 OK</td>
</tr>
<tr>
<td>새로 application.yml 쓰고 싶다</td>
<td>.yml 파일 하나 만들어서 사용 OK (기존 properties 삭제 추천)</td>
</tr>
<tr>
<td>둘 다 있다</td>
<td>한 쪽만 유지하고 다른 쪽은 삭제하는 걸 권장</td>
</tr>
</tbody></table>
<hr />
<p>🕵️ application.yml 파일을 새로 만들어도, 별도로 "이 파일을 써라"라고 선언할 필요는 없다.
Spring Boot는 기본적으로 자동으로 읽어준다고 한다.</p>
<p><strong>왜 따로 선언 안 해도 되냐?</strong></p>
<ul>
<li><p>src/main/resources 경로에서</p>
</li>
<li><p>application.yml 또는 application.properties 중에서</p>
</li>
<li><p>자동으로 application.* 파일을 탐지해서 적용함</p>
</li>
</ul>
<p><strong>우선순위는 어떻게 되냐</strong></p>
<ul>
<li><p>Spring Boot는 .properties와 .yml 파일이 둘 다 있으면 .properties가 우선 적용될 수도 있다.</p>
</li>
<li><p>application.yml 하나만 쓰고 싶다면 → application.properties는 삭제하거나 비워두는 게 깔끔</p>
</li>
</ul>
<p>둘 다 쓰는 건 비추 (혼란의 지름길)</p>
<hr />
<h3 id="spring-boot의-설정-파일-동작-방식-기본-규칙">Spring Boot의 설정 파일 동작 방식 (기본 규칙)</h3>
<p>Spring Boot는 기본적으로 아래 파일들을 찾음:</p>
<ul>
<li><p>application.properties</p>
</li>
<li><p>application.yml</p>
</li>
</ul>
<p>위치는 항상 기본적으로: <code>src/main/resources/</code> 이름은 반드시 <code>application</code>이어야 자동 인식</p>
<p>예를 들어 my-config.yml 같은 걸 쓰고 싶다면 명시적으로 Spring Boot에 알려줘야 한다</p>
<p><code>application.yml 안에서 import</code></p>
<pre><code>spring:
  config:
    import: optional:classpath:my-config.yml</code></pre><h2 id="3-연결-확인">3. 연결 확인</h2>
<h3 id="1-서버-실행-후-콘솔-로그-확인">1. 서버 실행 후 콘솔 로그 확인</h3>
<p><code>./gradlew bootRun</code> 로 확인해본다.</p>
<pre><code>&gt; Task :bootRun

  .   ____          _            __ _ _
 /\\ / ___'_ __ _ _(_)_ __  __ _ \ \ \ \
( ( )\___ | '_ | '_| | '_ \/ _ | \ \ \ \
 \\/  ___)| |_)| | | | | || (_| |  ) ) ) )
  '  |____| .__|_| |_|_| |_\__, | / / / /
 =========|_|==============|___/=/_/_/_/

 :: Spring Boot ::                (v3.4.3)

2025-03-24T01:12:46.066+09:00  INFO 2208 --- [demo] [           main] com.example.demo.DemoApplication         : Starting DemoApplication using Java 21.0.6 with PID 2208 (C:\Users\sehye\바탕 화면\code\study\First-Spring-Boot-Project\demo\demo\build\classes\java\main started by sehye in C:\Users\sehye\바탕 화면\code\study\First-Spring-Boot-Project\demo\demo)
2025-03-24T01:12:46.068+09:00  INFO 2208 --- [demo] [           main] com.example.demo.DemoApplication         : No active profile set, falling back to 1 default profile: "default"
2025-03-24T01:12:46.454+09:00  INFO 2208 --- [demo] [           main] .s.d.r.c.RepositoryConfigurationDelegate : Bootstrapping Spring Data JPA repositories in DEFAULT mode.
2025-03-24T01:12:46.473+09:00  INFO 2208 --- [demo] [           main] .s.d.r.c.RepositoryConfigurationDelegate : Finished Spring Data repository scanning in 8 ms. Found 0 JPA repository interfaces.
2025-03-24T01:12:46.817+09:00  INFO 2208 --- [demo] [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat initialized with port 9090 (http)
2025-03-24T01:12:46.827+09:00  INFO 2208 --- [demo] [           main] o.apache.catalina.core.StandardService   : Starting service [Tomcat]
2025-03-24T01:12:46.828+09:00  INFO 2208 --- [demo] [           main] o.apache.catalina.core.StandardEngine    : Starting Servlet engine: [Apache Tomcat/10.1.36]
2025-03-24T01:12:46.870+09:00  INFO 2208 --- [demo] [           main] o.a.c.c.C.[Tomcat].[localhost].[/]       : Initializing Spring embedded WebApplicationContext
2025-03-24T01:12:46.870+09:00  INFO 2208 --- [demo] [           main] w.s.c.ServletWebServerApplicationContext : Root WebApplicationContext: initialization completed in 776 ms
2025-03-24T01:12:46.981+09:00  INFO 2208 --- [demo] [           main] o.hibernate.jpa.internal.util.LogHelper  : HHH000204: Processing PersistenceUnitInfo [name: default]
2025-03-24T01:12:47.019+09:00  INFO 2208 --- [demo] [           main] org.hibernate.Version                    : HHH000412: Hibernate ORM core version 6.6.8.Final
2025-03-24T01:12:47.042+09:00  INFO 2208 --- [demo] [           main] o.h.c.internal.RegionFactoryInitiator    : HHH000026: Second-level cache disabled
2025-03-24T01:12:47.270+09:00  INFO 2208 --- [demo] [           main] o.s.o.j.p.SpringPersistenceUnitInfo      : No LoadTimeWeaver setup: ignoring JPA class transformer
2025-03-24T01:12:47.292+09:00  INFO 2208 --- [demo] [           main] com.zaxxer.hikari.HikariDataSource       : HikariPool-1 - Starting...
2025-03-24T01:12:47.428+09:00  INFO 2208 --- [demo] [           main] com.zaxxer.hikari.pool.HikariPool        : HikariPool-1 - Added connection org.postgresql.jdbc.PgConnection@48dff674
2025-03-24T01:12:47.429+09:00  INFO 2208 --- [demo] [           main] com.zaxxer.hikari.HikariDataSource       : HikariPool-1 - Start completed.
2025-03-24T01:12:47.480+09:00  INFO 2208 --- [demo] [           main] org.hibernate.orm.connections.pooling    : HHH10001005: Database info:
        Database JDBC URL [Connecting through datasource 'HikariDataSource (HikariPool-1)']
        Database driver: undefined/unknown
        Database version: 17.4
        Autocommit mode: undefined/unknown
        Isolation level: undefined/unknown
        Minimum pool size: undefined/unknown
        Maximum pool size: undefined/unknown
2025-03-24T01:12:47.714+09:00  INFO 2208 --- [demo] [           main] o.h.e.t.j.p.i.JtaPlatformInitiator       : HHH000489: No JTA platform available (set 'hibernate.transaction.jta.platform' to enable JTA platform integration)
2025-03-24T01:12:47.718+09:00  INFO 2208 --- [demo] [           main] j.LocalContainerEntityManagerFactoryBean : Initialized JPA EntityManagerFactory for persistence unit 'default'
2025-03-24T01:12:47.749+09:00  WARN 2208 --- [demo] [           main] JpaBaseConfiguration$JpaWebConfiguration : spring.jpa.open-in-view is enabled by default. Therefore, database queries may be performed during view rendering. Explicitly configure spring.jpa.open-in-view to disable this warning
2025-03-24T01:12:47.990+09:00  INFO 2208 --- [demo] [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat started on port 9090 (http) with context path '/'
2025-03-24T01:12:47.995+09:00  INFO 2208 --- [demo] [           main] com.example.demo.DemoApplication         : Started DemoApplication in 2.214 seconds (process running for 2.442)
</code></pre><pre><code>HikariPool-1 - Starting...
HikariPool-1 - Added connection org.postgresql.jdbc.PgConnection@48dff674
HikariPool-1 - Start completed.</code></pre><p>👉  <strong>HikariCP (DB 커넥션 풀)</strong>이 PostgreSQL에 연결을 시도했고,
👉 실제로 연결 성공해서 커넥션을 추가했다는 의미이다.</p>
<p><code>Initialized JPA EntityManagerFactory for persistence unit 'default'</code></p>
<p>👉 JPA 관련 설정도 잘 완료됐고 이제 Entity를 만들면 JPA가 자동으로 테이블을 만들어줄 준비가 되어 있다는 뜻이라고 한다.</p>
<p><code>Finished Spring Data repository scanning in 8 ms. Found 0 JPA repository interfaces.</code></p>
<p>이건 아직 @Repository 인터페이스를 만든 게 없다는 뜻이라고 한다 (다음 시간에).</p>
<hr />
<h3 id="2-db에-실제로-테이블이-생성되었는지-확인">2. DB에 실제로 테이블이 생성되었는지 확인</h3>