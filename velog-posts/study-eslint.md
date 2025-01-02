<h1 id="study-eslint-설정">[study] eslint 설정</h1>
<hr />

<h3 id="env">env</h3>
<ul>
<li>node : Node.js 환경을 설정합니다. Node.js의 글로벌 변수를 사용할 수 있도록 합니다. 서버사이드 코드를 작성할 때 유용합니다.</li>
</ul>
<hr />

<h3 id="extends">extends</h3>
<p>ESLint 규칙을 상속받아 설정을 확장할 수 있습니다.</p>
<ul>
<li><p>"eslint:recommended" : ESLint가 권장하는 기본 규칙들을 사용합니다.</p>
</li>
<li><p>"plugin:@typescript-eslint/recommended" : TypeScript ESLint 플러그인에서 권장하는 규칙들을 사용합니다. TypeScript의 타입 체크와 연관된 규칙을 추가로 설정합니다.</p>
</li>
<li><p>"plugin:import/recommended" : import 플러그인의 권장 설정을 적용하여 모듈 간의 import/export 규칙을 정리합니다.</p>
</li>
<li><p>"plugin:import/typescript" : TypeScript 파일에서 import 관련 규칙을 설정합니다.</p>
</li>
<li><p>"plugin:vue/base", "plugin:vue/vue3-essential", "plugin:vue/vue3-recommended", "plugin:vue/vue3-strongly-recommended" : Vue 3와 관련된 플러그인입니다. Vue.js 프로젝트에서 사용하는 기본적인 규칙에서부터 좀 더 강력한 규칙까지 차례로 상속받습니다. vue3-essential은 필수적인 규칙을, vue3-recommended와 vue3-strongly-recommended는 추가로 권장되는 규칙을 포함합니다.</p>
</li>
</ul>
<hr />

<h3 id="globals">globals</h3>
<p>프로젝트에서 글로벌 변수로 사용할 키워드들을 설정합니다. 여기서 나열된 변수들은 readonly 속성으로 설정되어 있으며, 수정할 수 없습니다. 예: <code>Answer</code>, <code>Consumer</code>, <code>Pagination</code> 등.</p>
<hr />

<h3 id="ignorepatterns">ignorePatterns</h3>
<p>특정 파일과 폴더를 ESLint 검사에서 제외합니다. 예: .fleet/, .idea/, .vscode/, dist/, node_modules/ 등.</p>
<hr />

<h3 id="parser">parser</h3>
<p>vue-eslint-parser: Vue 파일을 분석하기 위해 사용되는 파서입니다. Vue 컴포넌트 파일의 <code>&lt;template&gt;</code> , <code>&lt;script&gt;</code> , <code>&lt;style&gt;</code> 섹션을 구분해 처리합니다.</p>
<hr />

<h3 id="parseroptions">parserOptions</h3>
<ul>
<li><p>parser: "@typescript-eslint/parser" : TypeScript 파일을 분석할 때 사용할 파서를 설정합니다.</p>
</li>
<li><p>sourceType: "module" : ECMAScript 모듈을 지원하는 소스 코드를 분석하도록 설정합니다.</p>
</li>
</ul>
<hr />

<h3 id="plugins">plugins</h3>
<ul>
<li><p>@typescript-eslint : TypeScript용 ESLint 플러그인입니다. TypeScript의 문법과 타입을 체크하는 추가적인 규칙을 제공합니다.</p>
</li>
<li><p>import : 모듈 import 관련 규칙을 제공하는 플러그인입니다.</p>
</li>
</ul>
<hr />

<h3 id="root">root</h3>
<p><strong>true</strong>로 설정하면 이 파일이 최상위 ESLint 설정 파일임을 명시합니다. 하위 폴더에 다른 .eslintrc 파일이 있더라도 무시됩니다.</p>
<hr />

<h3 id="rules">rules</h3>
<p>ESLint 규칙을 직접 정의하여 케이스별로 설정을 조정할 수 있습니다.</p>
<ul>
<li><p>@typescript-eslint/ban-ts-comment: <code>"off"</code> : TypeScript의 @ts-주석을 사용하는 것을 허용합니다.</p>
</li>
<li><p>@typescript-eslint/no-explicit-any: <code>"off"</code> : any 타입을 사용하는 것을 허용합니다.</p>
</li>
<li><p>@typescript-eslint/no-var-requires: <code>0</code> : require() 사용을 허용합니다. TypeScript에서는 일반적으로 import를 권장하지만, 이 규칙을 끕니다.</p>
</li>
<li><p>import/order: import 문을 정렬하는 규칙입니다. 알파벳 순으로 정렬하며, 그룹 간에 줄바꿈을 적용하여 가독성을 높입니다.</p>
</li>
<li><p>quotes: <code>["error", "single"]</code>: 문자열은 반드시 작은 따옴표(')를 사용해야 합니다.</p>
</li>
<li><p>vue/component-definition-name-casing: <code>"off"</code>: Vue 컴포넌트 이름 정의의 케이스를 강제하지 않습니다.</p>
</li>
<li><p>vue/html-indent: <code>["error", "tab"]</code>: HTML 코드에서 들여쓰기는 탭(tab)을 사용하도록 강제합니다.</p>
</li>
<li><p>vue/script-indent: <code>["error", "tab", { "baseIndent": 1 }]</code>: Vue의 <code>&lt;script&gt;</code>에서 탭을 이용한 들여쓰기를 사용합니다. 기본 들여쓰기 레벨은 1로 설정합니다.</p>
</li>
<li><p>vue/html-self-closing: <code>"off"</code>: HTML 태그의 자동 닫기를 강제하지 않습니다.</p>
</li>
<li><p>vue/max-attributes-per-line: <code>"off"</code>: 한 줄에 몇 개의 속성을 넣을지 제한하지 않습니다.</p>
</li>
<li><p>vue/multi-word-component-names: <code>"off"</code>: 다중 단어로 구성된 Vue 컴포넌트 이름을 강제하지 않습니다.</p>
</li>
</ul>
<hr />

<h3 id="settings">settings</h3>
<ul>
<li><p>import/parsers: 특정 파일 형식에 대해 어떤 파서를 사용할지 정의합니다. TypeScript 파일에서는 @typescript-eslint/parser를 사용합니다.</p>
</li>
<li><p>import/resolver: 모듈을 어떻게 해석할지 설정합니다. node와 typescript 모듈 해석기를 사용하여 TypeScript에서 import 구문을 제대로 인식할 수 있도록 합니다.</p>
</li>
</ul>
<hr />

<blockquote>
<p>📌 대중적으로 많이 사용되는 ESLint 설정</p>
</blockquote>
<ul>
<li><p>airbnb 스타일 가이드: 엄격하고 일관된 코드 스타일을 제공하며, 많은 프로젝트에서 채택하고 있습니다. eslint-config-airbnb 패키지를 통해 쉽게 설정할 수 있습니다.</p>
</li>
<li><p>prettier와 ESLint 통합: 코드 포매팅 도구인 prettier와 ESLint를 함께 사용하는 것이 일반적입니다. eslint-config-prettier를 사용하여 충돌하는 규칙을 해제할 수 있습니다.</p>
</li>
<li><p>no-console: 콘솔 로그 사용을 금지하거나 경고를 출력하는 규칙입니다. 운영 환경에서 console.log를 사용하지 않도록 강제하는 데 유용합니다.</p>
</li>
<li><p>no-debugger: 디버거 사용을 금지하여 배포 시 실수로 디버거가 포함되지 않도록 방지합니다.</p>
</li>
<li><p>max-len: 코드의 가독성을 위해 한 줄의 최대 길이를 제한하는 규칙입니다. 예를 들어 80자나 100자로 설정할 수 있습니다.</p>
</li>
</ul>
<hr />