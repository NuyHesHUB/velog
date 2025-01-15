<p>리액트 <code>18.3.1</code> 버전에서 <code>ESLint</code>에서 </p>
<blockquote>
<p>'React' must be in scope when using JS </p>
</blockquote>
<p>라는 린트 오류가 뜬다.</p>
<p><img alt="" src="https://velog.velcdn.com/images/nuyhes/post/bd5dd040-2a31-4b03-a9f5-c111dba9b1f2/image.png" /></p>
<p>찾아보니 React 17 버전 이후로는 JSX를 사용할 때 React를 import하지 않아도 된다고 한다. </p>
<hr />

<p>React 17 릴리즈 JSX Transform  [ <a href="https://legacy.reactjs.org/blog/2020/09/22/introducing-the-new-jsx-transform.html" rel="noopener noreferrer" target="_blank">JSX Transform 문서</a> ]</p>
<h3 id="🕵️-introducing-the-new-jsx-transform">🕵️ Introducing the New JSX Transform</h3>
<h4 id="jsx-변환은-무엇인가요">JSX 변환은 무엇인가요?</h4>
<p>브라우저는 JSX를 바로 이해하지 못하므로 대부분의 React 사용자는 Babel이나 TypeScript와 같은 컴파일러를 사용하여 JSX 코드를 일반 JavaScript로 변환합니다 . Create React App이나 Next.js와 같은 많은 사전 구성된 툴킷에도 JSX 변환이 후드 아래에 포함되어 있습니다.</p>
<p>React 17 릴리스와 함께 JSX 변환을 몇 가지 개선하고 싶었지만 기존 설정을 깨고 싶지 않았습니다. 이것이 업그레이드를 원하는 사람들을 위해 JSX 변환의 새롭고 재작성된 버전을 제공하기 위해 Babel과 협력한 이유입니다.</p>
<p>새로운 변형으로 업그레이드하는 것은 완전히 선택 사항이지만 몇 가지 이점이 있습니다.</p>
<p>새로운 변환을 사용하면 React를 가져오지 않고도 JSX를 사용할 수 있습니다 .
설정에 따라 컴파일된 출력으로 인해 번들 크기가 약간 개선 될 수 있습니다 .
이를 통해 향후 React를 배우는 데 필요한 개념의 수가 줄어들어 개선이 이루어질 수 있습니다 .
이 업그레이드는 JSX 구문을 변경하지 않으며 필요하지 않습니다. 이전 JSX 변환은 평소처럼 계속 작동하며, 이에 대한 지원을 제거할 계획은 없습니다.</p>
<p>React 17 RC에는 이미 새로운 변형에 대한 지원이 포함되어 있으므로, 시도해 보세요! 채택하기 쉽게 하기 위해 React 16.14.0, React 15.7.0, React 0.14.10에 대한 지원도 백포트했습니다 . 아래에서 다양한 도구에 대한 업그레이드 지침을 찾을 수 있습니다.</p>
<hr />

<h3 id="17버전-이전">17버전 이전</h3>
<p>React 17 이전에는 JSX를 사용할 때 React를 import해야 했습니다. 이는 Babel이 JSX를 React.createElement 호출로 변환할 때 React가 필요했기 때문입니다. </p>
<pre><code class="language-js">import React from 'react';

function App() {
  return &lt;h1&gt;Hello World&lt;/h1&gt;;
}

export default App;</code></pre>
<p>Babel이 이 코드를 다음과 같이 변환했습니다</p>
<pre><code class="language-js">import React from 'react';

function App() {
  return React.createElement('h1', null, 'Hello World');
}

export default App;</code></pre>
<hr />

<h3 id="17버전-이후">17버전 이후</h3>
<p>React 17 이후로는 새로운 JSX 변환이 도입되어, React를 import하지 않아도 JSX를 사용할 수 있게 되었습니다. Babel이 새로운 변환을 사용하여 JSX를 처리할 때, React를 import할 필요가 없습니다.</p>
<pre><code class="language-js">function App() {
  return &lt;h1&gt;Hello World&lt;/h1&gt;;
}

export default App;</code></pre>
<p>아래와 같이 React를 import 하지 않아도 babel이 변환해준다.</p>
<pre><code class="language-js">import { jsx as _jsx } from 'react/jsx-runtime';

function App() {
  return _jsx('h1', { children: 'Hello World' });
}

export default App;</code></pre>
<p>따라서 React17 버전인데 ESLint는 기본 설정으로 <code>react/react-in-jsx-scope</code>규칙을 적용하여 JSX를 사용할 때 React가 스코프에 있어야 한다고 경고한다. 이 문제를 해결하려면 ESLint 설정에서 이 규칙을 비활성화해야 한다.</p>
<hr />

<blockquote>
<p>eslint.config.js 파일</p>
</blockquote>
<pre><code class="language-js">export default [
    {
      ...
      rules: {
        ...
          "react/react-in-jsx-scope": "off",
        ...
      }
      ...
    }
]</code></pre>
<p><img alt="" src="https://velog.velcdn.com/images/nuyhes/post/7bd0181a-fbed-49f9-a684-9a6bf561b750/image.png" /></p>
<hr />