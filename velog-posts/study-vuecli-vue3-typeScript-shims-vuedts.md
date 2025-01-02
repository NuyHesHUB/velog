<h1 id="study-vuecli-vue3--typescript-초기-세팅--shims-vuedts">[study] vue/cli vue3 + typeScript 초기 세팅 / shims-vue.d.ts</h1>
<hr />

<p>🕵️shims-vue.d.ts 이란?</p>
<p>shims-vue.d.ts 파일은 TypeScript 프로젝트에서 Vue 파일(*.vue)을 사용할 수 있도록 도와주는 선언 파일입니다. TypeScript는 기본적으로 .vue 파일을 인식하지 못하기 때문에, 이 파일을 통해 TypeScript에게 .vue 파일의 모듈을 어떻게 처리해야 하는지 알려줍니다.</p>
<hr />

<h3 id="기본-값">기본 값</h3>
<pre><code class="language-ts">/* eslint-disable */
declare module '*.vue' {
  import type { DefineComponent } from 'vue'
  const component: DefineComponent&lt;{}, {}, any&gt;
  export default component
}</code></pre>
<p>vue/cli 로 vue3 + typeScript 프로젝트를 생성하면 루트디렉토리에</p>
<p><code>shims-vue.d.ts</code> 파일이 생성</p>
<pre><code class="language-ts">1️⃣  declare module '*.vue' {
2️⃣    import type { DefineComponent } from 'vue'
3️⃣    const component: DefineComponent&lt;{}, {}, any&gt;
4️⃣    export default component
      }</code></pre>
<hr />

<blockquote>
<ol>
<li>declare module '*.vue' { ... }:</li>
</ol>
</blockquote>
<p>이 구문은 모든 .vue 파일을 모듈로 선언합니다. TypeScript는 기본적으로 .vue 파일을 인식하지 못하기 때문에, 이 선언을 통해 .vue 파일을 모듈로 취급하도록 합니다.</p>
<hr />

<blockquote>
<ol start="2">
<li>import type { DefineComponent } from 'vue':</li>
</ol>
</blockquote>
<p>Vue 3에서 제공하는 DefineComponent 타입을 가져옵니다. DefineComponent는 Vue 컴포넌트를 정의하는 타입입니다.
import type 구문은 타입만 가져오겠다는 의미로, 런타임에 영향을 미치지 않습니다.</p>
<hr />

<blockquote>
<ol start="3">
<li>const component: DefineComponent&lt;{}, {}, any&gt;:</li>
</ol>
</blockquote>
<p>모든 .vue 파일이 DefineComponent 타입의 컴포넌트임을 명시합니다.
DefineComponent&lt;{}, {}, any&gt;는 제네릭 타입으로, 첫 번째와 두 번째 인자는 컴포넌트의 props와 상태를 나타내며, 여기서는 빈 객체로 설정되어 있습니다. 세 번째 인자는 컴포넌트의 메서드 타입을 나타내며, any로 설정되어 있습니다.</p>
<p>각 제네릭 인자는 컴포넌트의 <code>props</code> , <code>emits</code> , <code>slots</code> 등을 정의합니다.</p>
<hr />

<p>🕵️더 엄격한 타입 검사를 하려면?</p>
<pre><code class="language-ts">const component: DefineComponent&lt;NonNullable&lt;unknown&gt;, NonNullable&lt;unknown&gt;, any&gt;;</code></pre>
<ol>
<li><p>첫 번째 인자: <code>NonNullable&lt;unknown&gt;</code>
<code>NonNullable&lt;unknown&gt;</code>는 <code>unknown</code> 타입에서 <code>null</code>과 <code>undefined</code>를 제외한 타입을 의미합니다. 즉, 이 컴포넌트의 props는 <code>null</code>이나 <code>undefined</code>가 될 수 없습니다.</p>
</li>
<li><p>두 번째 인자: <code>NonNullable&lt;unknown&gt;</code>
마찬가지로, <code>setup</code> 함수의 반환값도 <code>null</code>이나 <code>undefined</code>가 될 수 없습니다.</p>
</li>
<li><p>세 번째 인자: <code>any</code>
컴포넌트의 데이터, 메서드, 컴퓨티드 속성 등을 포함하는 타입을 정의하며, 여기서는 <code>any</code>로 설정되어 있어 어떤 타입이든 될 수 있습니다.</p>
</li>
</ol>
<hr />

<blockquote>
<ol start="4">
<li>export default component:</li>
</ol>
</blockquote>
<p>이 컴포넌트를 기본 내보내기로 설정합니다. 이렇게 하면 .vue 파일을 import할 때 기본적으로 이 컴포넌트를 가져오게 됩니다.</p>
<hr />