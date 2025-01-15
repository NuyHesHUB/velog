<hr />
<h2 id="🕵️-디자인-패턴이란">🕵️ 디자인 패턴이란?</h2>
<p>디자인 패턴(Design Pattern)은 소프트웨어 설계에서 자주 발생하는 문제를 해결하기 위해 검증된 일반적인 해결책을 제공하는 템플릿이다. 이는 코드를 재사용 가능하고 유지보수가 쉬우며 확장 가능하게 설계하기 위해 사용된다. 디자인 패턴은 특정 언어나 프로젝트에 종속되지 않으며, 다양한 상황에 맞게 응용할 수 있다.</p>
<hr />
<h3 id="왜-디자인-패턴이-중요할까">왜 디자인 패턴이 중요할까?</h3>
<ol>
<li><strong>시간 절약</strong>:  문제를 처음부터 다시 고민할 필요가 없다.</li>
<li><strong>읽기 좋은 코드</strong>: 다른 개발자도 쉽게 이해할 수 있는 코드가 된다.</li>
<li><strong>변경에 강한 코드</strong>: 나중에 기능을 추가하거나 고칠 때도 쉽게 대응할 수 있다.</li>
</ol>
<hr />
<h3 id="1-컨테이너-프레젠테이션-패턴-container-presentation-pattern">1. 컨테이너-프레젠테이션 패턴 (Container-Presentation Pattern)</h3>
<ul>
<li>컨테이너 컴포넌트는 상태 관리와 비즈니스 로직을 담당한다.</li>
<li>프레젠테이션 컴포넌트는 UI 렌더링을 담당한다.</li>
</ul>
<p>🕵️ 프레젠테이션-컨테이너 패턴에서는 <strong>UI와 비즈니스 로직을 명확히 분리</strong>하여 관리한다. UI는 프레젠테이션 컴포넌트로, 비즈니스 로직과 상태 관리는 컨테이너 컴포넌트로 분리된다.</p>
<hr />
<h3 id="📂-폴더-구조">📂 폴더 구조</h3>
<pre><code>src/ 
├── components/               # UI 컴포넌트 (프레젠테이션 컴포넌트) 
│   └── UserList.jsx          # 사용자 목록을 보여주는 UI 컴포넌트 
├── containers/               # 비즈니스 로직을 담당하는 컴포넌트 (컨테이너 컴포넌트) 
│   └── UserListContainer.jsx # 사용자 데이터를 처리하고 프레젠테이션 컴포넌트를 호출
└── App.jsx                   # 앱의 메인 컴포넌트</code></pre><hr />
<h3 id="📄-예시-코드">📄 예시 코드</h3>
<p><code>containers/UserListContainer.jsx</code></p>
<pre><code class="language-js">import { useState, useEffect } from "react"; 
import UserList from "../components/UserList"; 

const UserListContainer = () =&gt; { 
    const [users, setUsers] = useState([]); 
    const [loading, setLoading] = useState(true); 

    useEffect(() =&gt; { 
        fetch("/api/users") 
            .then((res) =&gt; res.json()) 
            .then((data) =&gt; { 
                setUsers(data); 
                setLoading(false); 
            }); 
    }, []); 

    return &lt;UserList users={users} loading={loading} /&gt;; 
}; 

export default UserListContainer;</code></pre>
<hr />
<p><code>components/UserList.jsx</code></p>
<pre><code class="language-js">const UserList = ({ users, loading }) =&gt; { 
    if (loading) return &lt;p&gt;Loading...&lt;/p&gt;; 

    return ( 
        &lt;ul&gt; 
            {users.map((user) =&gt; ( 
                &lt;li key={user.id}&gt;{user.name}&lt;/li&gt; 
            ))} 
        &lt;/ul&gt; 
    ); 
}; 

export default UserList;</code></pre>
<hr />
<h3 id="2-커스텀-훅-패턴-custom-hook-pattern">2 .커스텀 훅 패턴 (Custom Hook Pattern)</h3>
<ul>
<li>데이터 페칭 로직을 커스텀 훅으로 분리하여 재사용성을 높인다.</li>
</ul>
<p>🕵️ 커스텀 훅 패턴에서는 <strong>비즈니스 로직을 훅으로 분리</strong>하고 UI는 그 훅을 활용하는 컴포넌트에서 처리한다. 따라서 폴더 구조는 훅을 중심으로 구성이 된다.</p>
<hr />
<h3 id="📂-폴더-구조-1">📂 폴더 구조</h3>
<pre><code>src/ 
├── components/        # UI 컴포넌트 
│   └── UserList.jsx   # 사용자 목록을 보여주는 UI 컴포넌트 
├── hooks/             # 커스텀 훅 
│   └── useUserData.js # 사용자 데이터를 처리하는 커스텀 훅 
└── App.jsx            # 앱의 메인 컴포넌트</code></pre><ul>
<li><code>components/</code> 폴더는 UI 컴포넌트들을 보관한다. UI 컴포넌트는 로직을 알 필요 없이 커스텀 훅에서 제공하는 데이터를 <code>props</code>로 받아 사용한다.</li>
<li><code>hooks/</code> 폴더는 커스텀 훅을 모아두는 폴더이다. 각 훅은 비즈니스 로직을 담당하며 재사용 가능하도록 만들어진다.</li>
</ul>
<hr />
<h3 id="📄-예시-코드-1">📄 예시 코드</h3>
<p><code>hooks/useUserData.js</code></p>
<pre><code class="language-js">import { useState, useEffect } from "react"; 

const useUserData = () =&gt; { 
    const [users, setUsers] = useState([]); 
    const [loading, setLoading] = useState(true); 

    useEffect(() =&gt; { 
        fetch("/api/users") 
            .then((res) =&gt; res.json()) 
            .then((data) =&gt; { 
                setUsers(data); 
                setLoading(false); 
            }); 
    }, []); 

    return { users, loading }; }; export default useUserData;</code></pre>
<hr />
<p><code>components/UserList.jsx</code></p>
<pre><code class="language-js">import useUserData from "../hooks/useUserData"; 

const UserList = () =&gt; { 
    const { users, loading } = useUserData(); 

    if (loading) return &lt;p&gt;Loading...&lt;/p&gt;; 

    return ( 
        &lt;ul&gt; 
            {users.map((user) =&gt; ( 
                &lt;li key={user.id}&gt;{user.name}&lt;/li&gt; 
            ))} 
        &lt;/ul&gt; ); 
}; 

export default UserList;</code></pre>
<hr />
<p>프로젝트를 하면서 돌아보니 어느정도 획일화 된 패턴보다는 어느정도 장점을 모아서 구현해놓은거 같다.</p>