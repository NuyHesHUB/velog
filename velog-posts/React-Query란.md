<hr />
<h2 id="react-query--tanstack-query">React-Query / TanStack Query</h2>
<p><a href="https://tanstack.com/">TanStack Query 문서</a></p>
<p><code>TanStack Query</code>는 서버 상태를 관리하고 비동기 데이터 페칭을 간편하게 할 수 있도록 도와주는 라이브러리다. <code>React Query</code>로 시작했지만, 이제는 <code>React</code>뿐만 아니라 다른 프레임워크에서도 사용할 수 있도록 확장되었다.</p>
<hr />
<h3 id="설치">설치</h3>
<blockquote>
<p><code>npm install @tanstack/react-query</code></p>
</blockquote>
<hr />
<h3 id="기능-특징">기능 특징</h3>
<ol>
<li><p><code>자동 캐싱 및 동기화</code> : 데이터를 자동으로 캐싱하고, 필요할 때 자동으로 동기화한다.</p>
</li>
<li><p><code>백그라운드 데이터 업데이트</code>: 백그라운드에서 데이터를 자동으로 업데이트하여 최신 상태를 유지한다.</p>
</li>
<li><p><code>쿼리 무효화 및 재페칭</code>: 특정 조건이 충족되면 쿼리를 무효화하고 재페칭할 수 있다.</p>
</li>
<li><p><code>폴링 및 실시간 데이터</code>: 주기적으로 데이터를 페칭하거나 실시간 데이터를 처리할 수 있다.</p>
</li>
<li><p><code>오프라인 지원</code>: 오프라인 상태에서도 데이터를 관리할 수 있다.</p>
</li>
<li><p><code>개별 쿼리 관리</code>: 각 쿼리를 독립적으로 관리할 수 있다.</p>
</li>
</ol>
<hr />
<h3 id="기본-사용법">기본 사용법</h3>
<pre><code class="language-js">import { QueryClient, QueryClientProvider, useQuery } from '@tanstack/react-query';

const queryClient = new QueryClient();

// App.jsx 또는 main.jsx
function App() {
  return (
    &lt;QueryClientProvider client={queryClient}&gt;
      &lt;MyComponent /&gt;
    &lt;/QueryClientProvider&gt;
  );
}</code></pre>
<p><code>App.jsx</code> 또는 <code>main.jsx</code> 최상위 컴포넌트에 QueryClientProvide 로 감싼다.</p>
<hr />
<pre><code class="language-js">// MyComponent
function MyComponent() {
  const { isLoading, error, data } = useQuery(['todos'], fetchTodos);

  if (isLoading) return 'Loading...';
  if (error) return 'An error has occurred: ' + error.message;

  return (
    &lt;div&gt;
      {data.map(todo =&gt; (
        &lt;p key={todo.id}&gt;{todo.title}&lt;/p&gt;
      ))}
    &lt;/div&gt;
  );
}

//fetchTodos
async function fetchTodos() {
  const response = await fetch('/api/todos');
  return response.json();
}</code></pre>
<p><code>fetchTodos</code> 라는 서버에서 데이터를 가져오는 함수를 만들고 사용하는 컴포넌트에서 <code>const { isLoading, error, data } = useQuery(['todos'], fetchTodos);</code> 를 사용한다.</p>
<hr />
<h3 id="usequery-훅">useQuery 훅</h3>
<pre><code class="language-js">const { data, isLoading, error } = useQuery(
    ['posts', userId],
    () =&gt; fetchPosts(userId), 
    { enabled: !!userId } 
  );</code></pre>
<p><code>React Query</code>의 <code>useQuery</code> 훅은 쿼리의 상태를 관리하는 여러 유용한 값들을 반환한다. 각 값은 현재 쿼리의 상태를 나타내거나 조작하는 데 사용된다.</p>
<hr />
<h4 id="기본-반환값과-설명">기본 반환값과 설명</h4>
<blockquote>
<ol>
<li><code>data</code></li>
</ol>
</blockquote>
<ul>
<li>역할 : 쿼리가 성공적으로 데이터를 가져왔을 때 반환되는 값이다.</li>
<li>값의 종류 :<ol>
<li>쿼리함수(<code>queryFn</code>)가 반환한 데이터</li>
<li>초기 데이터(<code>initialData</code> 옵션)를 제공한 경우 초기값으로 설정</li>
</ol>
</li>
<li>초기 상태 : <code>undefined</code></li>
<li>사용 예시 :<pre><code class="language-js">  const { data } = useQuery('posts', fetchPosts);
  console.log(data); // 서버에서 가져온 데이터</code></pre>
</li>
</ul>
<hr />
<blockquote>
<ol start="2">
<li><code>isLoading</code></li>
</ol>
</blockquote>
<ul>
<li>역할 : 쿼리가 처음 실행될 때 로딩 상태를 나타낸다.</li>
<li>값의 종류 : <ol>
<li><code>true</code> : 쿼리가 데이터를 가져오는 중.</li>
<li><code>false</code> : 데이터 가져오기가 완료되었거나 실패한 경우</li>
</ol>
</li>
<li>초기 상태 : <code>true</code></li>
<li>사용 예시 :<pre><code class="language-js">  const { isLoading } = useQuery('posts', fetchPosts);
  if (isLoading) return &lt;div&gt;Loading...&lt;/div&gt;;</code></pre>
</li>
</ul>
<hr />
<blockquote>
<ol start="3">
<li><code>error</code></li>
</ol>
</blockquote>
<ul>
<li>역할 : 쿼리 함수가 실패했을 때 반환되는 에러 객체</li>
<li>값의 종류 :<ol>
<li><code>null</code> : 에러가 발생하지 않은 경우</li>
<li>Error 객체 : 쿼리가 실패한 경우 발생한 에러</li>
</ol>
</li>
<li>초기 상태 : <code>null</code></li>
<li>사용 예시 :<pre><code class="language-js">  const { error } = useQuery('posts', fetchPosts);
  if (error) return &lt;div&gt;Error: {error.message}&lt;/div&gt;;</code></pre>
</li>
</ul>
<hr />
<blockquote>
<ol start="4">
<li><code>isError</code></li>
</ol>
</blockquote>
<ul>
<li>역할 : 쿼리의 상태가 에러인지 여부를 나타낸다.</li>
<li>값의 종류 :<ol>
<li><code>true</code> : 쿼리가 실패했음</li>
<li><code>false</code> : 에러가 발생하지 않음</li>
</ol>
</li>
<li>초기 상태 : <code>false</code></li>
<li>사용 예시 :<pre><code class="language-js">  const { isError } = useQuery('posts', fetchPosts);
  if (isError) return &lt;div&gt;Something went wrong!&lt;/div&gt;;</code></pre>
</li>
</ul>
<hr />
<blockquote>
<ol start="5">
<li><code>isFetching</code></li>
</ol>
</blockquote>
<ul>
<li>역할 : 쿼리가 현재 데이터를 가져오는 중인지 여부를 나타낸다.</li>
<li>값의 종류 : <ol>
<li><code>true</code> : 데이터를 가져오는 중</li>
<li><code>false</code> : 데이터를 가져오기가 완료되었거나 대기 상태</li>
</ol>
</li>
<li>차이점 : <code>isLoading</code>과 달리 쿼리가 초기 로딩 상태가 아닌 경우에도 데이터를 리패칭할 때 <code>true</code>가 된다.</li>
<li>사용 예시 :<pre><code class="language-js">  const { isFetching } = useQuery('posts', fetchPosts);
  if (isFetching) return &lt;div&gt;Fetching latest data...&lt;/div&gt;;</code></pre>
</li>
</ul>
<hr />
<blockquote>
<ol start="6">
<li><code>status</code></li>
</ol>
</blockquote>
<ul>
<li>역할 : 쿼리의 상태를 나타내는 문자열</li>
<li>값의 종류 :<ol>
<li><code>&quot;idel&quot;</code> : 쿼리가 아직 실행되지 않음</li>
<li><code>&quot;loading</code> : 데이터를 가져오는 중</li>
<li><code>&quot;success&quot;</code> : 데이터 가져오기 성공</li>
<li><code>&quot;error&quot;</code> : 데이터 가져오기 실패</li>
</ol>
</li>
<li>사용 예시 :<pre><code class="language-js">  const { status } = useQuery('posts', fetchPosts);
  if (status === 'loading') return &lt;div&gt;Loading...&lt;/div&gt;;
  if (status === 'error') return &lt;div&gt;Error occurred!&lt;/div&gt;;</code></pre>
</li>
</ul>
<hr />
<blockquote>
<ol start="7">
<li><code>refetch</code></li>
</ol>
</blockquote>
<ul>
<li><p>역할 : 데이터를 다시 가져오는 함수</p>
</li>
<li><p>사용 예시 :</p>
<pre><code class="language-js">  const { refetch } = useQuery('posts', fetchPosts);

  const handleRefresh = () =&gt; {
    refetch();
  };

  return &lt;button onClick={handleRefresh}&gt;Refresh Data&lt;/button&gt;;</code></pre>
</li>
</ul>
<hr />
<h4 id="요약">요약</h4>
<table>
<thead>
<tr>
<th>반환값</th>
<th>설명</th>
<th>초기 상태</th>
</tr>
</thead>
<tbody><tr>
<td><code>data</code></td>
<td>쿼리 함수가 반환한 데이터</td>
<td><code>undefined</code></td>
</tr>
<tr>
<td><code>isLoading</code></td>
<td>데이터 가져오는 중인지 여부</td>
<td><code>true</code></td>
</tr>
<tr>
<td><code>error</code></td>
<td>실패 시 발생한 에러 객체</td>
<td><code>null</code></td>
</tr>
<tr>
<td><code>isError</code></td>
<td>에러 발생 여부</td>
<td><code>false</code></td>
</tr>
<tr>
<td><code>isFetching</code></td>
<td>데이터 가져오는 중인지 여부</td>
<td><code>false</code></td>
</tr>
<tr>
<td><code>status</code></td>
<td>쿼리의 상태 (<code>idle</code>, <code>loading</code>, 등)</td>
<td><code>&quot;idle&quot;</code></td>
</tr>
<tr>
<td><code>refetch</code></td>
<td>데이터를 다시 가져오는 함수</td>
<td><code>-</code></td>
</tr>
</tbody></table>
<hr />
<h3 id="usequery-매개변수">useQuery 매개변수</h3>
<blockquote>
<ol>
<li>첫 번째 인자 : <code>queryKey</code> (유니크한 키)</li>
</ol>
</blockquote>
<pre><code>- 데이터 쿼리를 식별하기 위한 고유한 키이다.
- 타입 : string | unknown[]
- 역할 :
    - React Query는 이 키를 기반으로 데이터를 캐싱하고 중복 요청을 방지한다.
    - 배열 형태로 구체화된 키를 사용할 수 있으며, 배열의 요소는 동적으로 변경 가능하다.
- 예시 : </code></pre><pre><code class="language-js">    const { data } = useQuery(['posts', userId], fetchPosts);
    // 'posts'는 데이터의 이름이고, userId는 특정 데이터를 식별하는 동적 요소입니다.</code></pre>
<hr />
<blockquote>
<ol start="2">
<li>두 번째 인자 : <code>queryFn</code> (데이터를 가져오는 함수)</li>
</ol>
</blockquote>
<pre><code>- 서버에서 데이터를 가져오는 함수이다.
- 타입 : (context: QueryFunctionContext) =&gt; Promise&lt;TData&gt;
- 역할 :
    - 데이터를 비동기로 가져오며, React Query가 이 함수의 반환값을 캐싱한다.
    - 함수 내부에서 queryKey를 사용할 수 있다.
- 예시 :</code></pre><pre><code class="language-js">    const fetchPosts = async (context) =&gt; {
          const [_, userId] = context.queryKey; // queryKey로부터 userId 추출
          const response = await fetch(`https://api.example.com/posts/${userId}`);
          if (!response.ok) throw new Error('Failed to fetch posts');
          return response.json();
    };

    const { data } = useQuery(['posts', userId], fetchPosts);</code></pre>
<hr />
<ol start="3">
<li><p>세 번째 인자 : <code>options</code> (선택 사항)</p>
<ul>
<li>쿼리의 동작을 제어하는 옵션 객체이다.</li>
<li>타입 : <code>UseQueryOptions&lt;TData, TError, TQueryFnData&gt;</code></li>
<li>주요 옵션 :<ul>
<li><code>enabled</code> :<ul>
<li><code>boolean</code> 값으로 쿼리 실행 여부를 제어한다.</li>
<li>기본값은 <code>true</code>이며, <code>false</code>로 설정하면 쿼리가 자동으로 실행되지 않는다.</li>
<li>동적 매개변수(<code>userId</code>)가 유효할 때만 실행하도록 설정할 때 유용하다.</li>
</ul>
</li>
</ul>
</li>
<li>예시 : <pre><code class="language-js">const { data } = useQuery(
    ['posts', userId],
    () =&gt; fetchPosts(userId),
    { enabled: !!userId } // userId가 유효할 때만 쿼리를 실행
);</code></pre>
</li>
</ul>
<hr />
</li>
</ol>