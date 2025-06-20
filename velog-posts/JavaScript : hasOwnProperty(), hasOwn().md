<h2 id="🕵️-hasownproperty--hasown-란">🕵️ hasOwnProperty() , hasOwn() 란?</h2>
<p>JavaScript의 <code>Object</code> 클래스의 정적 메서드이다. 
정확하게는</p>
<ul>
<li><code>hasOwnProperty()</code> : <code>Object</code>의 프로토타입 메서드</li>
<li><code>hasOwn()</code> : <code>Object</code>의 정적 메서드</li>
</ul>
<hr />
<h2 id="1-hasownproperty">1. hasOwnProperty()</h2>
<p><code>hasOwnProperty()</code>는 <code>Object.prototype</code>에 정의된 <strong>인스턴스 메서드</strong>로 객체가 특정 <strong>속성을 자신의 속성으로 직접 가지고 있는지</strong>를 불리언 값을 반환한다.  </p>
<h3 id="📄-예시-코드">📄 예시 코드</h3>
<pre><code class="language-js">const object = {};
object.property1 = 42;

console.log(object.hasOwnProperty(&quot;property1&quot;));
// Expected output: true

console.log(object.hasOwnProperty(&quot;toString&quot;));
// Expected output: false

console.log(object.hasOwnProperty(&quot;hasOwnProperty&quot;));
// Expected output: false</code></pre>
<h3 id="🚫-주의점">🚫 주의점</h3>
<ul>
<li>객체가 <code>hasOwnProperty</code>라는 이름의 속성을 자체적으로 갖고 있다면 충돌 가능성 있음.</li>
<li><code>Object.create(null)</code>로 만든 객체는 <code>Object.prototype</code>을 상속받지 않으므로 <code>hasOwnProperty()</code> 없음.</li>
<li><code>Proxy</code> 객체에서는 예상치 못한 에러가 날 수 있음.</li>
</ul>
<hr />
<h2 id="2-objecthasown">2. Object.hasOwn()</h2>
<p><code>Object.hasOwn()</code>은 ES2022(ES13)에서 도입된 <strong>정적 메서드</strong>로 <code>hasOwnProperty()</code>와 같은 기능을 더 <strong>안전하고 간단하게</strong> 제공한다.</p>
<h3 id="📄-예시-코드-1">📄 예시 코드</h3>
<pre><code class="language-js">const object = {
  prop: &quot;exists&quot;,
};

console.log(Object.hasOwn(object, &quot;prop&quot;));
// Expected output: true

console.log(Object.hasOwn(object, &quot;toString&quot;));
// Expected output: false

console.log(Object.hasOwn(object, &quot;undeclaredPropertyValue&quot;));
// Expected output: false
</code></pre>
<h3 id="💡장점">💡장점</h3>
<ul>
<li>충돌 위험 없음</li>
<li>프로토타입이 없는 객체도 안전하게 사용 가능</li>
<li>Proxy 객체에도 잘 작동</li>
<li>MDN 및 TC39에서 공식적으로 권장</li>
</ul>
<h3 id="🚫-주의점-1">🚫 주의점</h3>
<ul>
<li>구버전 환경에서는 미지원 ES2022 이상</li>
<li>첫 인자가 <code>null</code>, <code>undefined</code>면 타입 에러</li>
<li>TypeScript 4.9 버전 미만에서는 타입 정의가 없음</li>
</ul>
<hr />
<h2 id="3-in-연산자-key-in-obj">3. in 연산자 ('key' in obj)</h2>
<p><code>in</code> 연산자는 객체에 <strong>해당 키가 존재하는지만</strong> 확인한다.  <strong>자기 속성이든 상속 속성이든 모두 포함</strong>한다.</p>
<ul>
<li>단순히 속성이 있는지 여부만 빠르게 체크할 때 사용</li>
<li>상속된 프로퍼티도 포함되므로 정확한 소유 여부 확인엔 부적합<h3 id="📄-예시-코드-2">📄 예시 코드</h3>
</li>
</ul>
<pre><code class="language-js">'key' in obj</code></pre>
<hr />
<h2 id="🆚-비교표">🆚 비교표</h2>
<table>
<thead>
<tr>
<th align="center">구분</th>
<th align="center">hasOwnProperty()</th>
<th align="center">Object.hasOwn()</th>
<th align="center">'key' in obj</th>
</tr>
</thead>
<tbody><tr>
<td align="center">정의 위치</td>
<td align="center"><code>Object.prototype</code></td>
<td align="center"><code>Object</code> 정적 메서드</td>
<td align="center">연산자</td>
</tr>
<tr>
<td align="center">상속된 속성 포함 여부</td>
<td align="center">❌</td>
<td align="center">❌</td>
<td align="center">✅</td>
</tr>
<tr>
<td align="center">안전성</td>
<td align="center">제한적</td>
<td align="center">매우 안전</td>
<td align="center">-</td>
</tr>
<tr>
<td align="center">권장 여부</td>
<td align="center">MDN기준 비권장</td>
<td align="center">권장</td>
<td align="center">조건부</td>
</tr>
</tbody></table>
<hr />
<h2 id="📄-실제-예제">📄 실제 예제</h2>
<pre><code class="language-js">// vue3
const apiParams = reactive({
    selectDate: null,
    selectId  : null,
});</code></pre>
<p>위 <code>apiParams</code>에 있는 값을 <code>update</code>하는 함수를 만들어야 한다. 매개 변수로 들어오는 값이 <code>apiParams</code>에 있는 속성인지 먼저 체크를 한 후 실행하는 함수인데 조건문을 만든다.</p>
<pre><code class="language-js">function updateApiParam (paramKey: string) {
    if (apiParams.hasOwnProperty(paramKey)) {
        ...
        ...
        ...
    }
}</code></pre>
<p>저렇게 사용하면 별 문제 없어보였는데 아래와 같은 <code>ESlint</code> 에러가 뜬다.</p>
<pre><code class="language-ts">Do not access Object.prototype method 'hasOwnProperty' from target object.eslint[no-prototype-builtins](https://eslint.org/docs/latest/rules/no-prototype-builtins)

(method) Object.hasOwnProperty(v: PropertyKey): boolean

Determines whether an object has a property with the specified name.

_@param_ `v` — A property name.</code></pre>
<p>에러 메시지는 ESLint의 <a href="https://eslint.org/docs/latest/rules/no-prototype-builtins">no-prototype-builtins</a> 규칙에 의해 발생한 것이다. </p>
<hr />
<h3 id="no-prototype-builtins"><code>no-prototype-builtins</code></h3>
<ul>
<li>이 규칙은 <code>obj.hasOwnProperty()</code> 같은 <strong>Prototype 메서드 직접 호출</strong>을 막습니다.</li>
<li><code>hasOwnProperty</code>, <code>isPrototypeOf</code>, <code>propertyIsEnumerable</code> 등에 적용됩니다.</li>
</ul>
<hr />
<ol>
<li>어떤 객체는 <code>hasOwnProperty</code>라는 속성을 <strong>덮어쓸(overwrite)</strong> 수도 있다.</li>
</ol>
<pre><code class="language-js">const obj = { hasOwnProperty: () =&gt; false };
obj.hasOwnProperty('key'); // ❌ 예상과 다르게 동작</code></pre>
<ol start="2">
<li><code>Object.create(null)</code>로 생성된 객체는 <code>Object.prototype</code>을 <strong>상속받지 않기 때문에</strong>, <code>hasOwnProperty()</code> 메서드 자체가 없다.</li>
</ol>
<pre><code class="language-js">const obj = Object.create(null);
obj.hasOwnProperty('key'); // ❌ TypeError</code></pre>
<h3 id="해결-방법">해결 방법</h3>
<blockquote>
<ol>
<li>안전한 방식 사용 <code>Object.prototype.hasOwnProperty.call(...)</code></li>
</ol>
</blockquote>
<pre><code class="language-js">if (Object.prototype.hasOwnProperty.call(obj, 'key')) {
  // 안전하게 확인 가능
}</code></pre>
<ul>
<li><code>call</code>을 사용해 <code>hasOwnProperty</code>를 명확히 <code>Object.prototype</code>에서 호출한다.</li>
<li><code>ESLint</code> 경고가 발생하지 않는다.</li>
<li>모든 객체에 대해 안전하게 동작한다 (Proxy 포함).</li>
</ul>
<blockquote>
<ol start="2">
<li>최신 권장 방식 <code>Object.hasOwn(...)</code> (ES2022 이상)</li>
</ol>
</blockquote>
<pre><code class="language-js">if (Object.hasOwn(obj, 'key')) {
  // 가장 깔끔하고 안전한 방법
}</code></pre>
<ul>
<li>최신 JS 환경에서 기본적으로 지원</li>
<li>MDN과 ESLint에서도 권장</li>
<li>단, <strong>구형 브라우저나 Node.js v16 미만에서는 지원되지 않을 수 있음</strong></li>
</ul>
<hr />
<p>그래서 아래 3가지로 사용할 수 있다. 나는 내부 속성값만 찾으면 돼서 1번 조건문을 사용하거나 3번 조건문을 사용하려고 한다.</p>
<pre><code class="language-js">function updateApiParam (paramKey: string) {
    // 1️⃣ in 연산자 사용
    if ( paramKey in apiParams) {
        ...
        ...
        ...
    }
    // 2️⃣ hasOwnProperty를 에러 없이 call을 사용해 안전하게 사용
    if (Object.prototype.hasOwnProperty.call(apiParams, paramKey)) {
        ...
        ...
        ...
    }
    // 3️⃣ 최신 문법 안전하게 사용
    if (Object.hasOwn(apiParams, paramKey)) {
        ...
        ...
        ...
    }
}</code></pre>
<hr />