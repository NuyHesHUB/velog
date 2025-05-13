<hr />
<h2 id="global-enum-열거-타입-사용">Global enum 열거 타입 사용</h2>
<p>기존 프로젝트의 전역으로 사용할 타입을 <code>global</code> 폴더 내부에 <code>declare global</code>로 지정하고 <code>.eslintrc</code> 에서 <code>import</code> 없이 전역으로 사용했다. </p>
<hr />
<p>📄global.d.ts</p>
<pre><code class="language-ts">declare global {
    ...
    enum UserRole {
        STD = 'S'
        TCH = 'T'
    }
    ...
}</code></pre>
<hr />
<p>📄.eslintrc</p>
<pre><code class="language-json">&quot;globals&quot;: {
        ...
        &quot;UserRole&quot;: &quot;readonly&quot;,
        &quot;Answer&quot;: &quot;readonly&quot;,
        ...
},</code></pre>
<hr />
<blockquote>
<p><strong>Error</strong></p>
</blockquote>
<p><code>🔴 Uncaught (in promise) ReferenceError: UserRole is not defined</code></p>
<hr />
<p>문제는 <code>enum</code> 열거 타입은 전역으로 사용이 되지 않았다. 위와 같이 에러가 뜬다.</p>
<p> <strong>TypeScript에서 <code>declare global</code>로만 enum을 정의했을 때</strong>, 그리고 <strong>런타임에서 그 enum을 객체처럼 접근하려고 할 때</strong> 발생한다고 한다.</p>
<p>이렇게 하면 TS 타입 시스템 상에서는 UserRole 존재하니까 자동완성도 되고, 오류도 안 난다.</p>
<p>하지만...  </p>
<hr />
<h3 id="실제-런타임에서는">실제 런타임에서는</h3>
<p>TypeScript는 declare된 enum은 JS 코드로 변환하지 않는다.</p>
<pre><code class="language-ts">console.log(UserRole.STD); // ReferenceError</code></pre>
<p>브라우저는 &quot;UserRole이라는 변수는 정의돼 있지 않다&quot; 고 말한다.</p>
<table>
<thead>
<tr>
<th>선언 방식</th>
<th>타입 인식</th>
<th>런타입 객체 존재</th>
<th>import 없이 사용</th>
<th>결과</th>
</tr>
</thead>
<tbody><tr>
<td>declare enum</td>
<td>✅</td>
<td>❌</td>
<td>✅</td>
<td>❌</td>
</tr>
<tr>
<td>const enum (.ts 파일)</td>
<td>✅</td>
<td>❌ (문자열로 인라인됨)</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td>export enum</td>
<td>✅</td>
<td>✅</td>
<td>❌ (import 필요)</td>
<td>✅</td>
</tr>
</tbody></table>
<p>내가 원하는건 enum 열거형 타입으로 매개변수로 하드코딩으로 'T' 나 'S' 를 사용하는 것이 아닌 enum으로 상수값을 싱글톤처럼 관리 하고싶었다.</p>
<hr />
<h2 id="import-없이-전역global에서-enum을-안전하게-쓰는-방법">import 없이 전역(Global)에서 enum을 안전하게 쓰는 방법</h2>
<ol>
<li>공통 폴더에 <code>user-role.enum.ts</code> 파일을 생성 후 열거형 타입을 만든다.</li>
</ol>
<p>📂 /src/type/common/user-role.enum.ts </p>
<pre><code class="language-ts">export enum UserRole {
    STD = 'S',
    TCH = 'T',
}</code></pre>
<ol start="2">
<li>글로벌 폴더에 <code>global-enums.ts</code> 파일을 생성 후 런타임 등록 스크립트를 작성한다.</li>
</ol>
<p>📂 /src/type/global/global-enums.ts </p>
<pre><code class="language-ts">import { UserRole } from '@/type/common/user-role.enum';

// 전역 객체에 붙여줌
(globalThis as any).UserRole = UserRole;</code></pre>
<ol start="3">
<li>해당 <code>global-enums.ts</code> 의 파일을 최상위 <code>main.ts</code> 또는 진입점 파일에서 <code>import</code>한다.</li>
</ol>
<p>📂 /src/main.ts </p>
<pre><code class="language-ts">import '@/type/global/global-enums';</code></pre>
<ol start="4">
<li>(선택적) 타입 보장을 위한 글로벌 선언도 추가한다.
📂 /src/type/global/global.d.ts</li>
</ol>
<pre><code class="language-ts">declare global {
    const UserRole: typeof import('@/type/common/user-role.enum').UserRole;

    ...
    ...
    ...
}

export {};</code></pre>
<p><strong>결과</strong></p>
<p>import 안 해도, 타입 추론 잘 됨</p>
<pre><code class="language-ts">console.log(UserRole.TCH); // &quot;T&quot;</code></pre>
<hr />
<h3 id="번외">번외</h3>
<p>가끔 UserRole 과 해당 유저 타입에 따른 쿠키 값 <code>ex :  T or S</code> 이 있는데 조건문을 만들면 너무 길어지기도 하고 가독성이 떨어져 바로 boolean 값으로 나오게 하는 방법을 모색했는데, 이런 방법이 있어 작성해보게 되었다.</p>
<pre><code class="language-ts">// account.util.ts
const userType: UserType = toCookie('userType') as UserType;

const _getUserType = (): UserType =&gt; {
    if (matchesProfile('LOCAL')) {
        return LOCAL_USER_TYPE;
    }
    return userType;

};

// App.vue
const userType = getUserType();

userType === UserRole.TCH;</code></pre>
<h4 id="🕵️-proxy-기반-enum-객체-만들기">🕵️ proxy 기반 enum 객체 만들기</h4>
<pre><code class="language-ts">// user-type-proxy.ts
const userTypeValue = {
    Teacher: 'T',
    Student: 'S',
};

export const UserType = new Proxy(userTypeValue, {
    get(target, prop: keyof typeof userTypeValue) {
        return cookie.get('userType') === target[prop];
    },
});</code></pre>
<p>쿠키 안의 값과 비교해서 <code>true/false</code> 반환하게 만들어서 </p>
<pre><code class="language-ts">if (UserType.Teacher) {
    // 자동으로 쿠키에서 'T' 비교해줌
}</code></pre>
<p>위와 같이 사용할 수도 있다.</p>
<p><strong>🌟 장점</strong></p>
<table>
<thead>
<tr>
<th>장점</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td>🟢코드 가독성</td>
<td>if (UserRole.TCH) 직관적, 간결</td>
</tr>
<tr>
<td>🟢쿠키 값 비교를 추상화</td>
<td>로직 중복 제거, 어디서든 일관됨</td>
</tr>
<tr>
<td>🟢의미적 표현력</td>
<td>로직이 의미 단위로 구성됨</td>
</tr>
<tr>
<td>🟢enum-like 사용</td>
<td>UserRole.TCH , UserRole.SDT 가능</td>
</tr>
<tr>
<td><strong>🚫단점</strong></td>
<td></td>
</tr>
</tbody></table>
<table>
<thead>
<tr>
<th>단점</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td>🔴자동완성, 타입추론 약함</td>
<td>TS에서는 UserRole.TCH 가 boolean으로 추론되지 않음</td>
</tr>
<tr>
<td>🔴예상치 못한 사이드 이펙트</td>
<td>단순 접근인데 내부에서 cookie.get()이 실행됨, 순수하지 않은 접근자</td>
</tr>
<tr>
<td>🔴테스트 어려움</td>
<td>테스트 시 쿠키 상태 mocking 필요</td>
</tr>
<tr>
<td>🔴추론 어려움</td>
<td>협업 시 프록시 동작을 모르면 이해 안 되는 코드</td>
</tr>
</tbody></table>
<hr />
<h4 id="개선-가능-포인트-예제">개선 가능 포인트 예제</h4>
<p><strong>1. <code>enum</code> 값은 따로 유지</strong></p>
<pre><code class="language-ts">// user-type.enum.ts
export const UserTypeValue = {
    Teacher: 'T',
    Student: 'S',
} as const;

export type UserType = typeof UserTypeValue[keyof typeof UserTypeValue];</code></pre>
<p><strong>2. 프록시 유틸은 따로 구성</strong></p>
<pre><code class="language-ts">// user-type-proxy.ts
import { UserTypeValue } from './user-type.enum';
import { cookie } from '@/utils/cookie.util'; // 예시

export const isUserType = new Proxy(UserTypeValue, {
    get(target, prop: keyof typeof UserTypeValue) {
        return cookie.get('userType') === target[prop];
    },
});</code></pre>
<p><strong>3.사용</strong></p>
<pre><code class="language-ts">if (isUserType.Teacher) {
    // 간결함 + 의미적 명확성 유지
}</code></pre>
<hr />