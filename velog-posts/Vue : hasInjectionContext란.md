<hr />
<h3 id="🕵️-hasinjectioncontext-란">🕵️ hasInjectionContext 란?</h3>
<p>Vue 3 Compositon API의 헬퍼 함수로, 현재 코드가 종속성 주입(Context Injection)을 사용할 수 있는 환경(컨텍스트) 안에 있는지를 확인하는 데 사용된다. 
현재 컴포넌트가 Vue의 종속성 주입 시스템에 접근할 수 있는지를 알려준다.  <a href="https://vuejs.org/api/composition-api-dependency-injection.html">Vue.js 문서</a></p>
<pre><code class="language-typescript">function hasInjectionContext(): boolean</code></pre>
<hr />
<h2 id="1-사용-목적">1. 사용 목적</h2>
<p>Vue 컴포넌트는 부모에서 제공된 종속성을 <code>provide</code>와 <code>inject</code>를 통해 사용할 수 있다. 하지만 종속성 주입은 Vue의 컴포넌트 컨텍스트 안에서만 동작하기 때문에 컴포넌트 외부(ex: 독립적으로 실행되는 함수)에서는 접근할 수 없다.</p>
<p><code>hasInjectionContext</code>를 사용하면, 코드가 컴포넌트 컨텍스트 안에 있는지 동적으로 확인하고 안전하게 <code>inject</code>를 호출할 수 있도록 한다.</p>
<p>📣쉽게 vue의 컴포넌트 컨텍스트 안에서만 작동하니 종속성 주입이 되는지 여부를 확인하고 나서, 안전하게 <code>inject</code>를 호출할 수 있게 하기위해 사용한다.</p>
<hr />
<h2 id="2-hasinjectioncontext의-사용법">2. hasInjectionContext의 사용법</h2>
<pre><code class="language-js">import { inject, hasInjectionContext } from 'vue'; 

export function useMyInjectedValue() { 
    if (hasInjectionContext()) { 
        const injectedValue = inject('myKey', 'defaultValue'); 

        return injectedValue; 
    } else { 
        console.warn('No injection context available!'); 

        return 'defaultValue'; // 기본값 반환 
    }</code></pre>
<p><code>hasInjectionContext()</code>: 현재 코드가 컴포넌트 컨텍스트 내에 있는지 반환한다.</p>
<ul>
<li><strong><code>true</code></strong>: 종속성 주입 가능.</li>
<li><strong><code>false</code></strong>: 종속성 주입 불가능.</li>
</ul>
<hr />
<h2 id="3-주요-특징">3. 주요 특징</h2>
<ul>
<li>동작 방식 : 현재 코드가 Vue의 컴포넌트 컨텍스트 안에 있는지 반환 <code>true</code> | <code>false</code></li>
<li>사용 이유 : 독립적인 유틸리티 함수 또는 라이브러리에서 <code>inject</code> 호출이 안전한지 확인</li>
<li>주 사용 사례 : 독립 유틸리티 함수, 컴포넌트 내부와 외부에서 모두 호출 가능한 코드</li>
</ul>
<hr />
<h2 id="4-주의점">4. 주의점</h2>
<blockquote>
<p>컴포넌트 내부에서는 항상 <code>true</code> 반환</p>
</blockquote>
<p>컴포넌트 내부에서 <code>hasInjectionContext()</code>는 항상 <code>true</code>를 반환하므로, 내부에서는 직접 <code>inject</code>를 호출하는 것이 더 간단할 수 있다.</p>
<blockquote>
<p>컴포넌트 외부에서는 <code>inject</code> 불가</p>
</blockquote>
<p><code>inject</code>는 컨텍스트가 없는 곳에서 호출하면 런타임 에러가 발생하므로, 외부 함수에서는 반드시 <code>hasInjectionContext()</code>로 확인 후 호출해야 한다.</p>
<hr />
<p>즉, <strong>종속성 주입 시스템이 없는 경우를 안전하게 처리</strong>하는 방법이라고 이해하면 될 거 같다.</p>