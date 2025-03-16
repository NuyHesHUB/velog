<hr />
<blockquote>
<p>👀 백엔드 공부를 병행하기 위해 어떤 언어로 해야할 지 고민이 많았다. 내가 프론트엔드로 시작을 해서 <code>Node.js</code>로 시작 하면 좋을 거 같아서 <code>Nest.js</code>를 생각하긴 했었는데, 주위에 도움을 받고 질문하기 좋은 건 <code>Java</code> <code>Spring Boot</code> 인 거 같아서 여기로 다시 도전을 해볼까 한다. </p>
</blockquote>
<hr />
<h2 id="1-spring-boot-프로젝트-시작하기-전-필수-설치-프로그램-목록">1. Spring Boot 프로젝트 시작하기 전 필수 설치 프로그램 목록</h2>
<table>
<thead>
<tr>
<th>프로그램</th>
<th>설명</th>
<th>다운로드 링크</th>
</tr>
</thead>
<tbody><tr>
<td>JDK (Java Development Kit)</td>
<td>Java 실행 환경 (Java 21 LTS 추천)</td>
<td>🔗<a href="https://adoptium.net/">JDK 21 다운로드</a></td>
</tr>
<tr>
<td>Maven 또는 Gradle</td>
<td>프로젝트 빌드 및 의존성 관리</td>
<td>JDK 설치 시 기본 포함</td>
</tr>
<tr>
<td>PostgreSQL</td>
<td>데이터 저장용 DBMS</td>
<td>🔗 <a href="https://www.postgresql.org/download/">PostgreSQL 다운로드</a></td>
</tr>
<tr>
<td>pgAdmin (PostgreSQL 관리 GUI 툴)</td>
<td>PostgreSQL 데이터 관리용 GUI</td>
<td>PostgreSQL 설치 시 포함</td>
</tr>
</tbody></table>
<hr />
<h2 id="windows-환경-설정">Windows 환경 설정</h2>
<p>cmd 터미널에서 <code>java -version</code> 을 치면 버전이 나오는데 없다고 나오면 윈도우 환경변수 설정을 한다.</p>
<blockquote>
<ol>
<li>고급 시스템 설정 (내 PC -&gt; 속성 -&gt; 고급 or win 검색창 고급 시스템 설정)</li>
</ol>
</blockquote>
<p><img alt="" src="https://velog.velcdn.com/images/nuyhes/post/8241a9f7-f966-401e-b020-fca9f3242ee0/image.png" /></p>
<blockquote>
<ol start="2">
<li>환경변수 클릭</li>
</ol>
</blockquote>
<p>위 아래 두개의 환경변수 목록이 나오는데 아래 시스템 변수에 JAVA_HOME이 없으면 새로 만들기</p>
<p><img alt="" src="https://velog.velcdn.com/images/nuyhes/post/45b6559e-8cc1-44d0-96a9-c715a53629f1/image.png" /></p>
<blockquote>
<ol start="3">
<li>새로 만들기 후 해당 JDK 설치된 경로 및 변수명 입력</li>
</ol>
</blockquote>
<p><img alt="" src="https://velog.velcdn.com/images/nuyhes/post/ce031f08-77ea-4ab3-80ee-6553f711f4ee/image.png" /></p>
<blockquote>
<ol start="4">
<li>시스템 변수에 path 영역을 찾아서 편집 클릭 금방 만든 변수에 bin 폴더 path 추가</li>
</ol>
</blockquote>
<p><img alt="" src="https://velog.velcdn.com/images/nuyhes/post/f698b467-6b87-4e5f-8956-743f77f49a5c/image.png" /></p>
<blockquote>
<ol start="5">
<li>터미널에서 <code>echo %JAVA_HOME%</code>을 치면 <code>C:\Program Files\Eclipse Adoptium\jdk-21.0.6.7-hotspot</code> 가 나오면 정상적으로 설정 됨</li>
</ol>
</blockquote>
<hr />
<h2 id="2-spring-boot-프로젝트-생성-방법">2. Spring Boot 프로젝트 생성 방법</h2>
<blockquote>
<ol>
<li>Spring Initializr 접속</li>
</ol>
</blockquote>
<p><a href="https://start.spring.io/">https://start.spring.io/</a> 로 접속한다. <img alt="" src="https://velog.velcdn.com/images/nuyhes/post/0e0572f7-4f37-4ef8-9d48-6f64c1ebe430/image.png" /></p>
<hr />
<blockquote>
<ol start="2">
<li>옵션 선택</li>
</ol>
</blockquote>
<ul>
<li><code>Project</code> : Maven or Gradle 선택</li>
<li><code>Language</code> : 언어 선택 </li>
<li><code>Spring Boot</code> : 버전 선택 (기본 선택이 3.4.3 으로 되어있는데 이게 안정적인 버전인거 같아서 그대로 선택)</li>
<li><code>Project Metadata</code> : <ol>
<li><code>Group</code> : 패키지 네임스페이스를 설정하는 부분 개인 프로젝트니까 그대로 사용</li>
<li><code>Artifact</code> : 프로젝트 기본 애플리케이션 이름 및 JAR 파일 이름. (예를 들어 my-spring-app을 입력하면 빌드 결과가 my-spring-app.jar가 됨)</li>
<li><code>Name</code> : 프로젝트 애플리케이션 이름 <code>Artifact</code>와 동일하게 설정되는 경우가 많음 <code>Artifact</code>와 동일하게 설정</li>
<li><code>Description</code> : 설명 프로젝트에 대한 간단한 설명을 입력하는 부분</li>
<li><code>Package Name</code> : 기본 패키지 경로 <code>Group</code> + <code>Artifact</code> 조합을 자동 생성됨 </li>
<li><code>Packaging</code> : JAR 또는 WAR 선택 </li>
<li><code>Java</code> : 사용할 Java 버전 Spring Boot 3.x 이상에서는 Java 17 이상 필수 LTS 버전 21 선택</li>
</ol>
</li>
</ul>
<hr />
<h3 id="🕵️-jar--war-란">🕵️ JAR , WAR 란?</h3>
<p>Spring Boot 프로젝트를 생성할 때 JAR과 WAR 중 선택해야 하는 이유는 배포 방식 때문입니다.
두 개의 차이점을 이해하면 프로젝트의 배포 방식에 따라 적절한 선택을 할 수 있습니다.</p>
<p>** JAR (Java ARchive) - 독립 실행형 **</p>
<table>
<thead>
<tr>
<th>항목</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td>파일 확장자</td>
<td>.jar</td>
</tr>
<tr>
<td>서버 포함 여부</td>
<td>✅ 내장 웹 서버 포함 (Tomcat, Jetty, Undertow 등)</td>
</tr>
<tr>
<td>실행 방식</td>
<td>java -jar mayapp.jar 로 실행 가능</td>
</tr>
<tr>
<td>배포 대상</td>
<td>독립적인 서버 환경 (AWS EC2, VPS, Docker 등)</td>
</tr>
<tr>
<td>Spring Boot 기본값</td>
<td>JAR (추천)</td>
</tr>
</tbody></table>
<p>** JAR의 특징 **</p>
<ul>
<li>내장 웹 서버 (Tomcat, Jettym Undertow)가 포함됨 (따로 설치할 필요 없음)</li>
<li>실행 파일만 있으면 어디서든 <code>java -jar myapp.jar</code>로 실행 가능</li>
<li>컨테이너(Docker 등)와 함께 사용하기 편리함</li>
<li>Spring Boot의 기본 실행 방식이므로 대부분 프로젝트에서 JAR를 선택함</li>
</ul>
<p>** WAR (Web Apllication Archive) - 외부 서버용 **</p>
<table>
<thead>
<tr>
<th>항목</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td>파일 확장자</td>
<td>.war</td>
</tr>
<tr>
<td>서버 포함 여부</td>
<td>내장 서버 없음 (Tomcat, JBoss 같은 외부 WAS 필요)</td>
</tr>
<tr>
<td>실행 방식</td>
<td>Tomcat, WildFly(JBoss), WebSphere 등에 배포</td>
</tr>
<tr>
<td>배포 대상</td>
<td>기존 웹 서버(WAS, Web Application Server) 환경</td>
</tr>
<tr>
<td>Spring Boot 기본값</td>
<td>기본적으로 WAR 아님 (설정 변경 필요)</td>
</tr>
</tbody></table>
<p>** WAR의 특징 **</p>
<ul>
<li>내장 서버가 없고, 외부 WAS(Web Application Server)에 배포해야 실행 가능</li>
<li>기존 Tomcat, WebSphere, JBoss 등 WAS환경에서 동작해야 할 때 사용</li>
<li>예전에는 대형 엔터프라이즈 기업에서 주로 사용했지만, 요즘은 JAR 방식이 대세 </li>
<li>Spring Boot 프로젝트를 WAR로 빌드하려면 설정 변경이 필요함</li>
</ul>
<hr />
<ul>
<li>옵션 선택을 하고 나서 GENERATE 를 클릭한다</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/nuyhes/post/c49ac073-e77b-4bda-84c2-a3c01bab9a92/image.png" /></p>
<ul>
<li><code>Zip</code> 파일이 다운로드 되고 압축을 풀고 IDE에서 오픈한다.</li>
</ul>
<hr />
<h2 id="3-spring-boot-프로젝트-실행-방법">3. Spring Boot 프로젝트 실행 방법</h2>
<h3 id="spring-boot-실행-maven">Spring Boot 실행 (Maven)</h3>
<p>터미널 또는 CMD에서 프로젝트 폴더로 이동한 후 실행한다.</p>
<p><strong>Maven을 사용하는 경우</strong>
<code>./mvnw spring-boot:run</code></p>
<p><strong>Windows에서</strong>
<code>mvnw.cmd spring-boot:run</code></p>
<hr />
<h3 id="spring-boot-실행-gradle">Spring Boot 실행 (Gradle)</h3>
<p><strong>MavGradleen을 사용하는 경우</strong>
<code>./gradlew bootRun</code></p>
<p><strong>Windows에서</strong>
<code>gradlew.bat bootRun</code></p>
<hr />
<h3 id="spring-boot-jar-파일로-실행-배포용">Spring Boot JAR 파일로 실행 (배포용)</h3>
<p>Maven 또는 Gradle로 JAR 파일을 빌드하여 실행할 수도 있다.</p>
<p><strong>JAR 파일 빌드 Maven 사용 시</strong></p>
<p><code>./mvnw clean package</code></p>
<p><strong>JAR 파일 빌드 Gradle 사용 시</strong></p>
<p><code>./gradlew clean build</code></p>
<p>빌드 후 target/ 또는 build/libs/ 폴더에 .jar 파일이 생성됨</p>
<hr />
<h2 id="4-실행-확인-방법">4. 실행 확인 방법</h2>
<ol>
<li><p>우선 <code>src/main/resources/application.properties</code>에 서버 포트가 설정 되어 있는지 확인한다. </p>
<pre><code class="language-bash">#application.properties

spring.application.name=demo
server.port=9090</code></pre>
</li>
<li><p><code>./gradlew bootRun</code> 을 사용하여 실행한다. </p>
<pre><code>PS C:\Users\sehye\바탕 화면\code\study\First-Spring-Boot-Project\demo\demo&gt; ./gradlew bootRun                                                                                                                                                                                                                                    
</code></pre></li>
</ol>
<blockquote>
<p>Task :bootRun</p>
</blockquote>
<p>  .   ____          _            __ _ _</p>
<p>  .   <strong>__          _            __ _ _
 /\ / _</strong>'_ <em>_ _ _(</em>)_ <em>_  __ _ \ \ \ <br />( ( )___ | '</em> | '<em>| | '</em> / <em>` | \ \ \ <br /> \/  ___)| |</em>)| | | | | || (<em>| |  ) ) ) )
  '  |<strong>__| .</strong>|</em>| |<em>|</em>| |<em>__, | / / / /
 =========|</em>|==============|<em>__/=/</em>/<em>/</em>/</p>
<p> :: Spring Boot ::                (v3.4.3)</p>
<p>2025-03-16T23:04:27.720+09:00  INFO 16508 --- [demo] [           main] com.example.demo.DemoApplication         : Starting DemoApplication using Java 21.0.6 with PID 16508 (C:\Users\sehye\바탕 화면\code\study\First-Spring-Boot-Project\demo\demo\build\classes\java\main started by sehye in C:\Users\sehye\바탕 화면\code\study\First-Spring-Boot-Project\demo\demo)
2025-03-16T23:04:27.722+09:00  INFO 16508 --- [demo] [           main] com.example.demo.DemoApplication         : No active profile set, falling back to 1 default profile: "default"
2025-03-16T23:04:28.022+09:00  INFO 16508 --- [demo] [           main] com.example.demo.DemoApplication         : Started DemoApplication in 0.552 seconds (process running for 0.74)</p>
<p>BUILD SUCCESSFUL in 2s</p>
<pre><code>
---

## 5. 현재 실행 중인 Java 프로세스 검색

`tasklist | findstr java`

```bash
#cmd 

C:\Users\sehye&gt;tasklist | findstr java
java.exe                      4512 Console                    1    241,192 K
java.exe                      8464 Console                    1    541,940 K
java.exe                      7736 Console                    1    594,836 K
java.exe                     18340 Console                    1    306,036 K
java.exe                     12468 Console                    1    769,248 K
java.exe                      6872 Console                    1    504,448 K
java.exe                     12680 Console                    1    113,488 K
java.exe                     18212 Console                    1    135,852 K
</code></pre><p>현재 18212 제외 다 종료를 하면된다.</p>
<hr />
<p><strong>모든 Java 프로세스 한꺼번에 종료</strong></p>
<p><code>taskkill /F /IM java.exe</code></p>
<hr />
<p><strong>특정 Java 프로세스 종료 (Windows)</strong></p>
<pre><code>taskkill /F /PID 4512
taskkill /F /PID 8464
taskkill /F /PID 7736
taskkill /F /PID 18340
taskkill /F /PID 12468
taskkill /F /PID 6872
taskkill /F /PID 12680</code></pre><hr />