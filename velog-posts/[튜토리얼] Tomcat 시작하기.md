<hr />
<h3 id="🕵️-톰캣이란">🕵️ 톰캣이란?</h3>
<p><code>Tomcat</code>은 자바 웹 애플리케이션 서버입니다.
즉 <code>JSP</code>나 <code>Servlet</code> 같은 웹 기반 <code>Java</code> 코드를 브라우저에서 실행할 수 있도록 해주는 소프트웨어입니다.</p>
<table>
<thead>
<tr>
<th>개념</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td>이름</td>
<td>Apache Tomcat</td>
</tr>
<tr>
<td>역할</td>
<td>JSP/Servlet코드를 실행시켜주는 서버</td>
</tr>
<tr>
<td>예시</td>
<td><code>http://localhost:8080/hello.jsp</code>처럼 JSP페이지를 띄우기 가능</td>
</tr>
<tr>
<td>특징</td>
<td>가볍고 빠르고 JAVA 웹 개발 기본 서버로 많이 사용됨</td>
</tr>
</tbody></table>
<p>동작 방식</p>
<ol>
<li>사용자가 브라우저에서 JSP 페이지를 요청함</li>
<li>Tomcat이 JSP를 서블릿으로 변환</li>
<li>변환된 서블릿을 실행하고 결과 HTML을 생성</li>
<li>HTML을 브라우저로 응답함</li>
</ol>
<hr />
<p><a href="https://tomcat.apache.org/">톰캣 아파치 다운로드 페이지</a></p>
<hr />
<h3 id="톰캣-설치-및-실행">톰캣 설치 및 실행</h3>
<p><img alt="" src="https://velog.velcdn.com/images/nuyhes/post/73cbe854-3811-4506-ac75-7f6d7a7034b6/image.png" /></p>
<ol>
<li>해당 페이지에서 왼쪽 <code>Download</code> 영역의 <code>Tomcat</code> 버전별로 다운을 할 수 있다.  해당 버전 클릭</li>
<li><code>Binary Distributions</code> 에서 <code>Core</code> 리스트 중 아래의 2개 중 하나를 다운로드한다.
 64-bit Windows zip (pgp, sha512) (학습, 개발용)
 32-bit/64-bit Windows Service Installer (pgp, sha512) (윈도우 서비스에 등록되는 프로그램)</li>
<li>압축을 풀고 <code>bin</code> 폴더의 <code>startup.bat</code>을 실행한다. </li>
</ol>
<hr />
<p>🕵️ <code>startup.bat</code>을 실행하자마자 닫히게 되면 톰캣이 실행되는 환경이 아니므로 설정이 필요하다. </p>
<ol>
<li>제어판 &gt; 시스템 &gt; 고급 시스템 설정 &gt; 환경 변수
 <code>시스템 변수(S)</code>에 <code>JAVA_HOME</code> (jdk) 가 없다면 <a href="https://www.oracle.com/java/technologies/downloads/">https://www.oracle.com/java/technologies/downloads/</a> 에서 다운로드를 한 후 <code>환경 변수</code>에서 새로 만들기를 한 후 변수 이름 : <code>JAVA_HOME</code> 변수 값 : <code>C:\Program Files\Java\jdk-17</code> 해당 디렉토리를 찾아서 등록을 한다.</li>
</ol>
<p><img alt="" src="https://velog.velcdn.com/images/nuyhes/post/d9ce4c48-59f5-43f6-8ac4-837588a2367c/image.png" /></p>
<ol start="2">
<li>다른 톰캣이 실행되어 포트가 사용 중 일 경우 확인</li>
</ol>
<hr />
<ol start="4">
<li><code>startup.bat</code>을 실행하고 <code>localhost:8080</code>을 접속하면 해당 Apache Tomcat 페이지가 나온다.</li>
</ol>
<p><img alt="" src="https://velog.velcdn.com/images/nuyhes/post/b2dc9586-fe44-438d-88f7-6132f7ef3453/image.png" /></p>
<hr />