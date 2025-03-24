<blockquote>
<p>SpringBoot 프로젝트에서 DB를 연결하기 위해 글을 작성한다.</p>
</blockquote>
<h2 id="postgresql-설치-후-기본-셋팅">PostgreSQL 설치 후 기본 셋팅</h2>
<h3 id="1-psql-명령어가-안되는-경우">1. psql 명령어가 안되는 경우</h3>
<p>설치 후 PowerShell에서 psql -U postgres를 쳤을 때 다음과 같은 오류가 발생한다면</p>
<pre><code># PowerShell 

PS C:\WINDOWS\system32&gt; psql -U postgres

psql : The term 'psql' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
 spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:1
+ psql -U postgres
+ ~~~~
    + CategoryInfo          : ObjectNotFound: (psql:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException</code></pre><hr />
<p>** 윈도우의 환경변수에 추가를 한다.**</p>
<ol>
<li><p>윈도우 검색 - <code>시스템 환경 변수 편집</code> 클릭</p>
</li>
<li><p>환경 변수(N) 클릭 </p>
</li>
<li><p>시스템 변수(S)의 <code>Path</code> 편집 클릭</p>
</li>
<li><p>새로 만들기를 해서 PostgreSQL이 설치된 경로를 넣어준다.</p>
</li>
<li><p>보통 <code>C:\Program Files\PostgreSQL\버전\bin</code> 에 위치한다.</p>
</li>
</ol>
<hr />
<h3 id="2-powershell에서-postgresql-접속하기">2. PowerShell에서 PostgreSQL 접속하기</h3>
<h4 id="1-psql--u-postgres-로-접속">1. psql -U postgres 로 접속</h4>
<pre><code># powerShell 

psql -U postgres</code></pre><p>그래도 안될 경우에는</p>
<pre><code># powerShell

 &amp; "C:\Program Files\PostgreSQL\17\bin\psql.exe" -U postgres</code></pre><p>해당 설치된 bin 폴더 내부 psql.exe 경로까지 써주고 -U postgres를 입력한다.</p>
<h4 id="2-postgres-사용자의-암호">2. postgres 사용자의 암호:</h4>
<p>해당 사용자 암호를 요구한다. postgreSQL 설치할 때 설정한 암호 입력한다.</p>
<h4 id="3-db생성">3. DB생성</h4>
<p><code>CREATE DATABASE &lt;db명&gt;;</code> 입력 후 엔터</p>
<h4 id="4-해당-만든-db에-접속">4. 해당 만든 DB에 접속</h4>
<p><code>\c &lt;db명&gt;</code></p>
<h4 id="5-전체-db-목록-확인">5. 전체 DB 목록 확인</h4>
<p><code>\l</code></p>
<blockquote>
<p>해당 powerShell의 결과</p>
</blockquote>
<pre><code>postgres 사용자의 암호:

psql (17.4)
도움말을 보려면 "help"를 입력하십시오.

postgres=#
postgres=#
postgres=# CREATE DATABASE mydb;
CREATE DATABASE
postgres=# \c mydb
접속정보: 데이터베이스="mydb", 사용자="postgres".
mydb=# \l
                                             데이터베이스 목록
   이름    |  소유주  | 인코딩 | 로케일 제공자 | Collate | Ctype | 로케일 | ICU 룰 |      액세스 권한
-----------+----------+--------+---------------+---------+-------+--------+--------+-----------------------
 mydb      | postgres | UTF8   | libc          | ko-KR   | ko-KR |        |        |
 postgres  | postgres | UTF8   | libc          | ko-KR   | ko-KR |        |        |
 template0 | postgres | UTF8   | libc          | ko-KR   | ko-KR |        |        | =c/postgres          +
           |          |        |               |         |       |        |        | postgres=CTc/postgres
 template1 | postgres | UTF8   | libc          | ko-KR   | ko-KR |        |        | =c/postgres          +
           |          |        |               |         |       |        |        | postgres=CTc/postgres
(4개 행)</code></pre>