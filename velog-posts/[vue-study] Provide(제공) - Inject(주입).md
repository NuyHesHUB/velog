<h1 id="vue-study-provide제공--inject주입">[vue-study] Provide(제공) / Inject(주입)</h1>
<p><a href="https://ko.vuejs.org/guide/components/provide-inject.html">vue 공식문서 (Provide-Inject 바로가기)</a></p>
<hr />

<p><strong>컴포넌트 예 )</strong> <code>&lt;Parent&gt;</code> -&gt; <code>&lt;Child&gt;</code> -&gt; <code>&lt;DeepChild&gt;</code></p>
<hr />

<h3 id="prop-드릴링">Prop 드릴링</h3>
<p>일반적으로 부모 컴포넌트에서 자식 컴포넌트로 데이터를 전달해야 할 때 props를 사용합니다. props만 사용하면 전체 부모 체인에 동일한 prop을 전달해야 합니다.</p>
<p><strong>Prop 드릴링</strong></p>
<p><code>&lt;Parent&gt;</code> -&gt; <code>&lt;Child :data="'message'"&gt;</code> -&gt; <code>&lt;DeepChild :data="'data'"&gt;</code></p>
<p><code>&lt;Child&gt;</code> 컴포넌트는 이 prop가 전혀 필요하지 않을 수 있지만, <code>&lt;DeepChild&gt;</code>가 접근할 수 있도록 여전히 선언하고 전달해야 합니다. 더 긴 상위 체인이 있으면 그 과정에서 더 많은 컴포넌트가 영향을 받습니다. 이것을 "prop 드릴링"이라고 합니다.</p>
<hr />

<h3 id="provide제공--inject주입">Provide(제공) / Inject(주입)</h3>
<p>우리는 provide와 inject로 props 드릴링을 해결할 수 있습니다. 부모 컴포넌트는 모든 자식 컴포넌트에 대한 의존성 제공자 역할을 할 수 있습니다. 하위 트리의 모든 컴포넌트는 깊이에 관계없이 상위 체인의 컴포넌트에서 제공(provide)하는 의존성을 주입(inject)할 수 있습니다.</p>
<p><code>&lt;Parent&gt;</code> -&gt; <code>&lt;DeepChild&gt;</code></p>
<hr />

<h4 id="provide제공">Provide(제공)</h4>
<p>부모 컴포넌트에서 하위 컴포넌트에 데이터를 제공하려면 <code>provide()</code> 함수를 사용합니다.</p>
<pre><code class="language-js">&lt;script setup&gt;
    import { provide } from 'vue'

    provide(/* 키 */ 'message', /* 값 */ '안녕!')
&lt;/script&gt;</code></pre>
<p><code>provide()</code> 함수는 두 개의 인자를 허용합니다. 첫 번째 인자는 주입 키라고 하며 문자열 또는 Symbol이 될 수 있습니다. 주입 키는 자식 컴포넌트에서 주입할 원하는 값을 조회하는 데 사용됩니다. 단일 컴포넌트는 다른 값을 제공하기 위해 다른 주입 키를 사용하여 <code>provide()</code>를 여러 번 호출할 수 있습니다.</p>
<p>두 번째 인자는 제공되는 값입니다. 값은 refs와 같은 반응 상태를 포함하여 모든 유형이 될 수 있습니다</p>
<pre><code class="language-js">import { ref, provide } from 'vue'

const count = ref(0)
provide('key', count)</code></pre>
<hr />

<h4 id="inject주입">Inject(주입)</h4>
<p>부모 컴포넌트에서 제공하는 데이터를 주입하려면 inject() 함수를 사용하세요</p>
<pre><code class="language-js">&lt;script setup&gt;
    import { inject } from 'vue'

    const message = inject('message')
&lt;/script&gt;</code></pre>
<blockquote>
<h4 id="📄parentvue">📄Parent.vue</h4>
</blockquote>
<pre><code class="language-js">// 📄Parent.vue

&lt;script setup&gt;
  import { ref, provide } from 'vue'
  import Child from './Child.vue'

  // ref를 제공함으로써 GrandChild는
  // 여기서 일어나는 변화에 반응할 수 있습니다.
  const message = ref('안녕')
  provide('message', message)
&lt;/script&gt;

&lt;template&gt;
  &lt;input v-model="message"&gt;
  &lt;Child /&gt;
&lt;/template&gt;</code></pre>
<hr />

<blockquote>
<h4 id="📄childvue">📄Child.vue</h4>
</blockquote>
<pre><code>// 📄Child.vue

&lt;script setup&gt;
    import DeepChild from './DeepChild.vue'
&lt;/script&gt;

&lt;template&gt;
  &lt;DeepChild /&gt;
&lt;/template&gt;</code></pre><hr />

<blockquote>
<h4 id="📄deepchildvue">📄DeepChild.vue</h4>
</blockquote>
<pre><code class="language-js">// 📄DeepChild.vue
&lt;script setup&gt;
import { inject } from 'vue'

const message = inject('message')
&lt;/script&gt;

&lt;template&gt;
  &lt;p&gt;
    손자에게 전하는 메시지: {{ message }}
  &lt;/p&gt;
&lt;/template&gt;</code></pre>
<hr />

<h3 id="반응형으로-만들기">반응형으로 만들기</h3>
<p>반응형 제공/주입 값을 사용할 때, 가능하면 제공자 내부에서 모든 변경사항을 반응성 상태로 유지하는 것이 좋습니다. 이렇게 하면 제공된 상태와 가능한 변화가 동일한 컴포넌트에 함께 배치되어 향후 유지 관리가 더 쉬워집니다.</p>
<p>주입 대상 컴포넌트에서 데이터를 업데이트해야 하는 경우가 있습니다. 이러한 경우 상태 변경을 담당하는 함수를 제공하는 것이 좋습니다.</p>
<pre><code class="language-js">&lt;!-- 제공자 컴포넌트 내부 --&gt;
&lt;script setup&gt;
import { provide, ref } from 'vue'

const location = ref('북극')

function updateLocation() {
  location.value = '남극'
}

provide('location', {
  location,
  updateLocation
})
&lt;/script&gt;</code></pre>
<pre><code class="language-js">&lt;!-- 주입되는 컴포는트 내부 --&gt;
&lt;script setup&gt;
import { inject } from 'vue'

const { location, updateLocation } = inject('location')
&lt;/script&gt;

&lt;template&gt;
  &lt;button @click="updateLocation"&gt;{{ location }}&lt;/button&gt;
&lt;/template&gt;</code></pre>
<p>마지막으로, provide를 통해 전달된 데이터가 주입된 컴포넌트에 의해 변경될 수 없도록 하려면, 제공된 값을 readonly()로 래핑할 수 있습니다.</p>
<pre><code class="language-js">&lt;script setup&gt;
import { ref, provide, readonly } from 'vue'

const count = ref(0)
provide('read-only-count', readonly(count))
&lt;/script&gt;</code></pre>
<hr />

<h3 id="🐵-심볼-키-사용하기">🐵 심볼 키 사용하기</h3>
<p>위 예제에서 문자열 삽입 키를 사용했습니다. 많은 의존성 제공자가 있는 대규모 앱에서 작업하거나, 다른 개발자가 사용할 컴포넌트를 작성하는 경우, <strong>잠재적 충돌</strong>을 피하기 위해 제공 키로 <strong>Symbol(심볼)</strong>을 사용하는 것이 가장 좋습니다.</p>
<p>심볼을 전용 파일로 내보내는 것이 좋습니다.</p>
<pre><code class="language-js">// keys.js
export const myInjectionKey = Symbol()</code></pre>
<pre><code class="language-js">// 제공하는 곳의 컴포넌트에서
import { provide } from 'vue'
import { myInjectionKey } from './keys.js'

provide(myInjectionKey, {
  /* 제공할 데이터 */
})</code></pre>
<pre><code class="language-js">// 주입되는 곳의 컴포넌트에서
import { inject } from 'vue'
import { myInjectionKey } from './keys.js'

const injected = inject(myInjectionKey)</code></pre>
<hr />

<p>👍해당 글은 <a href="https://ko.vuejs.org/">vue 공식문서</a> 기반으로 작성되었습니다.</p>