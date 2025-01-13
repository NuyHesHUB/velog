<hr />
<h3 id="🕵️-shallowref-란">🕵️ shallowRef 란?</h3>
<p>Vue 3 Compositon API에 있는 <code>ref()</code>의 얕은 버전이다. <a href="https://ko.vuejs.org/api/reactivity-advanced">Vue.js 문서</a></p>
<pre><code class="language-typescript">function shallowRef&lt;T&gt;(value: T): ShallowRef&lt;T&gt; 

interface ShallowRef&lt;T&gt; {
    value: T
}</code></pre>
<p><code>ref()</code>와 달리 <code>shallowRef()</code>의 내부 값은 있는 그대로 저장되고 노출되며 내부 깊숙이까지 반응형으로 동작하지는 않는다. <code>.value</code> 접근만 반응형이다.</p>
<p>객체 내부의 속성 변경을 추적하지 않고, Ref의 <code>value</code>가 변경될 때만 반응성을 트리거하는 특징이 있다.</p>
<hr />
<h2 id="1-얕은-반응성-vs-깊은-반응성">1. 얕은 반응성 vs 깊은 반응성</h2>
<blockquote>
<p>깊은 반응성 (ref)</p>
</blockquote>
<p>일반적인 <code>ref</code>는 객체 내부의 모든 속성을 반응적으로 감지한다. 내부 속성이 바뀌어도 반응성을 트리거한다.</p>
<pre><code class="language-js">import { ref } from 'vue'; 

const state = ref({ count: 1 }); 

state.value.count = 2; // 반응성을 트리거 

console.log(state.value.count); // 2</code></pre>
<blockquote>
<p>얕은 반응성 (shallowRef)</p>
</blockquote>
<p><code>shallowRef</code>는 객체 내부 속성 변경은 반응성을 트리거하지 않으며, value 자체가 변경될 때만 반응성을 트리거한다.</p>
<pre><code class="language-js">import { shallowRef } from 'vue'; 

const state = shallowRef({ count: 1 }); 

state.value.count = 2; // 반응성을 트리거하지 않음 
console.log(state.value.count); // 2 (값은 변경되지만 반응성 X) 

state.value = { count: 3 }; // 반응성을 트리거 console.log(state.value.count); // 3</code></pre>
<hr />
<h2 id="2-shallowref-사용-방법">2. shallowRef 사용 방법</h2>
<blockquote>
<p>기본 사용법</p>
</blockquote>
<pre><code class="language-js">import { shallowRef } from 'vue'; 

const user = shallowRef({ name: 'Alice', age: 25 }); 

// 내부 속성 변경 
user.value.name = 'Bob'; // 반응성을 트리거하지 않음 

// 전체 객체 교체 
user.value = { name: 'Charlie', age: 30 }; // 반응성을 트리거</code></pre>
<blockquote>
<p>배열의 경우</p>
</blockquote>
<p>배열에 <code>shallowRef</code>를 사용하면, 배열의 요소 변경은 반응성을 트리거하지 않는다.</p>
<pre><code class="language-js">const items = shallowRef([1, 2, 3]); 

items.value[0] = 99; // 반응성을 트리거하지 않음 
items.value = [4, 5, 6]; // 반응성을 트리거</code></pre>
<hr />
<h2 id="3-shallowref를-사용하는-이유">3. shallowRef를 사용하는 이유</h2>
<blockquote>
<p>성능 최적화</p>
</blockquote>
<ul>
<li>객체 내부의 세부 변경 사항을 감지할 필요가 없을 때, 불필요한 반응성 트리거를 방지하여 성능을 최적화할 수 있다.</li>
</ul>
<blockquote>
<p>외부 데이터 관리</p>
</blockquote>
<ul>
<li>외부 라이브러리나 API로부터 전달받은 데이터가 변경될 때만 반응성을 트리거하고, 내부 세부 사항은 Vue의 반응성 시스템에 포함하지 않을 때 유용하다.</li>
</ul>
<blockquote>
<p>반응성 수동 제어</p>
</blockquote>
<ul>
<li>세부 변경 사항은 무시하고, 객체 전체를 교체하거나 특정 이벤트에서만 반응성을 트리거하고 싶을 때 사용된다.</li>
</ul>
<hr />
<h2 id="4-shallowref-특징">4. shallowRef 특징</h2>
<table>
<thead>
<tr>
<th>특징</th>
<th>shallowRef</th>
<th>일반 ref</th>
</tr>
</thead>
<tbody><tr>
<td>반응성 추적 범위</td>
<td><code>value</code> 자체만</td>
<td>객체 내부의 속성까지 추적</td>
</tr>
<tr>
<td>객체 속성 변경 트리거 여부</td>
<td>트리거 X</td>
<td>트리거 O</td>
</tr>
<tr>
<td>주요 사용 목적</td>
<td>성능 최적화 및 외부 데이터 관리</td>
<td>모든 변경 사항을 추적해야 하는 경우</td>
</tr>
</tbody></table>
<hr />
<h2 id="5-shallowref를-사용하는-사례">5. shallowRef를 사용하는 사례</h2>
<pre><code class="language-js">import { shallowRef, onMounted } from 'vue'; 

const chart = shallowRef(null); 

onMounted(() =&gt; { 
    // 외부 라이브러리로 차트를 생성 
    chart.value = createChartLibraryInstance(); 
}); 

return { chart }</code></pre>
<p>외부 라이브러리 객체는 Vue의 반응성 시스템이 세부적으로 추적할 필요가 없으므로, <code>shallowRef</code>로 관리하면 불필요한 반응성을 줄일 수 있다.</p>
<hr />