<hr />
<p>🕵️ <code>Github Actions</code> 를 사용하여 코딩테스트 문제를 풀고 커밋 푸시를 하면 <code>README.md</code>에 나열된 테이블에 날짜, 난이도, 문제 타이틀, 바로가기 링크를 추가하고 싶었다. <code>yml</code> 파일과 <code>python</code> 코드를 작성하여 <code>ubuntu</code>에서 실행을 하게 되는데 디버깅을 일일히 커밋해서 확인했었다. 직접 로컬에서 실행하여 디버깅을 해보고 싶었고 아직 문제를 해결하지는 못했지만 쉽게 확인하여 문제를 해결할 수 있을거 같다. 요즘 의도치 않게 <code>python</code>으로 코드를 짜고 공부하고있다. <code>디버깅</code>하는 방법을 알아보자</p>
<hr />
<h2 id="python-설치-및-확인">Python 설치 및 확인</h2>
<ol>
<li>먼저 <a href="https://www.python.org/">파이썬 다운로드</a>를 한다. </li>
<li>설치 후 터미널에서 <code>python --version 또는 py --version</code>로 설치 확인 및 버전 확인을 한다.</li>
<li>해당 파이썬 코드의 경로로 이동한다. <code>ex) C:\Users\Desktop\py-test</code></li>
<li>해당 경로에서 (실행할 파일 명 예: test.py) <code>py test.py 또는 python test.py</code>를 실행한다.</li>
</ol>
<hr />
<h2 id="디버깅-및-모듈-설치">디버깅 및 모듈 설치</h2>
<blockquote>
<p>처음에 실행을 하니 이런 에러가 떴다. <code>우분투</code>에서는 <code>yml</code>로 모듈을 다 설치하고 실행하는데, 로컬에서는 설치를 하지 않아서다.</p>
</blockquote>
<pre><code>C:\Users\Desktop\coding-test\scripts&gt;py update_coding_test.py
Traceback (most recent call last):
  File &quot;C:\Users\Desktop\coding-test\scripts\update_coding_test.py&quot;, line 2, in &lt;module&gt;
    import git
ModuleNotFoundError: No module named 'git'</code></pre><hr />
<h3 id="gitpython-모듈-설치">GitPython 모듈 설치</h3>
<pre><code class="language-bash">pip install gitpython</code></pre>
<hr />
<blockquote>
<p>설치된 패키지 확인</p>
</blockquote>
<pre><code class="language-bash">pip show gitpython</code></pre>
<hr />
<blockquote>
<p>pip가 py와 연결된 Python 버전에서 동작하는지 확인</p>
</blockquote>
<p>만약 설치가 제대로 되지 않았다면, <code>py</code>와 연결된 Python 환경이 <code>pip</code>가 설치된 환경과 다를 수 있다. 
이를 확인하려면</p>
<pre><code class="language-bash">py -m pip install gitpython</code></pre>
<hr />
<h3 id="디버깅">디버깅</h3>
<pre><code>C:\Users\Desktop\coding-test\scripts&gt;py update_coding_test.py
Traceback (most recent call last):
  File &quot;C:\Users\Desktop\coding-test\scripts\update_coding_test.py&quot;, line 30, in &lt;module&gt;
    test_get_changed_files()
    ~~~~~~~~~~~~~~~~~~~~~~^^
  File &quot;C:\Users\Desktop\coding-test\scripts\update_coding_test.py&quot;, line 17, in test_get_changed_files
    result = get_changed_files_in_commit(test_repo_path, test_commit_hash)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^
NameError: name 'get_changed_files_in_commit' is not defined</code></pre><p>이렇게 에러가 아주 잘 뜬다 😊</p>
<pre><code>Latest pushed commit hash: da0e76f0ee3a746256aec53e2327f5baa4175d22
Checking commit: da0e76f0ee3a746256aec53e2327f5baa4175d22
get_changed_files_in_commit : Changed files: ['Programmers/Lv.1/20 test/20test.js']
get_changed_files_in_commit : Filtered files: ['Programmers/Lv.1/20 test/20test.js']
changed_files:['Programmers/Lv.1/20 test/20test.js']
file_paths: ['Programmers/Lv.1/20 test/20test.js']
parts: ['Programmers/Lv.1/20 test/20test.js']
Extracted information: []
main : not update readme</code></pre><p>이렇게 문제를 하나 풀면 해당 루트 경로의 폴더명을 담아서 <code>README.md</code>에 업데이트만 하면 되는데 생각보다 어렵다.</p>
<hr />