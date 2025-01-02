<h1 id="tsconfigjson--jsconfigjson">tsconfig.json / jsconfig.json</h1>
<blockquote>
<p>속성 설명</p>
</blockquote>
<p><code>tsconfig.json(jsconfig.json)</code> 파일은 TypeScript(JavaScript) 프로젝트의 설정을 정의하는 파일이다. 이 파일은 TypeScript(JavaScript) 컴파일러가 프로젝트를 어떻게 컴파일할지에 대한 다양한 옵션을 지정할 수 있다. </p>
<ul>
<li><p><code>compilerOptions</code>, : TypeScript(JavaScript) 컴파일러의 동작 방식을 설정한다. 예를 들어 target, module, sourceMap 등의 옵션을 지정할 수 있다.</p>
</li>
<li><p><code>include</code> , <code>exclude</code> : 컴파일에 포함할 파일과 제외할 파일을 지정할 수 있다. 예를 들어 특정 디렉토리나 파일 패턴을 포함하거나 제외할 수 있다.</p>
</li>
<li><p><code>typeRoots</code> , <code>types</code> : 프로젝트에서 사용할 타입 정의 파일의 위치를 지정할 수 있다. 이는 외부 라이브러리의 타입정의 파일을 포함하는 데 유용하다.</p>
</li>
<li><p><code>experimentalDecorators</code> , <code>skipLibCheck</code> , <code>forceConsistentCasingInFileNames</code> , <code>useDefineForClassFields</code> : 기타 속성들..</p>
</li>
</ul>
<hr />

<blockquote>
<p>EX ) tsconfig.json</p>
</blockquote>
<pre><code class="language-rust">{
  "compilerOptions": {
    "allowImportingTsExtensions": true,
    "allowJs": true,
    "alwaysStrict": true,
    "baseUrl": ".",
    "checkJs": true,
    "declaration": true,
    "emitDeclarationOnly": true,
    "esModuleInterop": true,
    "isolatedModules": true,
    "lib": [
      "dom",
      "dom.iterable",
      "esnext"
    ],
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "noFallthroughCasesInSwitch": true,
    "noImplicitAny": true,
    "noImplicitOverride": true,
    "noImplicitReturns": true,
    "noUnusedParameters": true,
    "outDir": "./dist",
    "paths": {
      "@api/*": [
        "src/api/*"
      ],
      "@app/App.vue": [
        "src/App.vue"
      ],
      "@config/*": [
        "src/config/*"
      ],
      "@components/*": [
        "src/components/*"
      ],
      "@composables/*": [
        "src/composables/*"
      ],
      "@composites/*": [
        "src/composites/*"
      ],
      "@declare/*": [
        "src/@declare/*"
      ],
      "@directives/*": [
        "src/directives/*"
      ],
      "@environment/*": [
        "src/environment/*"
      ],
      "@implement/*": [
        "src/@implement/*"
      ],
      "@store/*": [
        "src/store/*"
      ],
      "@router/*": [
        "src/router/*"
      ],
      "@utils/*": [
        "src/utils/*"
      ],
      "@views/*": [
        "src/views/*"
      ]
    },
    "removeComments": true,
    "rootDir": ".",
    "strict": true,
    "strictFunctionTypes": true,
    "strictPropertyInitialization": true,
    "target": "ESNext",
    "typeRoots": [
      "node_modules/@types",
      "src/@declare"
    ],
    "types": ["node"]
  },
  "exclude": [
    "dist",
    "node_modules"
  ],
  "include": [
    "src/**/*.ts",
    "src/**/*.vue",
    "vue.config.js"
  ]
}</code></pre>
<hr />

<h2 id="1-compileroptions">1. compilerOptions</h2>
<blockquote>
<p>1) allowSyntheticDefaultImports</p>
</blockquote>
<p>allowSyntheticDefaultImports 를 사용하지 않을 때는 import를 아래와 같이</p>
<pre><code class="language-js">import * as someModule from "some-module";
const someModule = require("some-module");</code></pre>
<p>이렇게 가져와야한다.</p>
<p>ES6 모듈 시스템을 따르지 않는 모듈에서 기본 가져오기를 허용하지 않는다.
<code>true</code>로 설정하면 <code>import defaultExport from "some-module";</code> ES6 스타일의 기본 가져오기를 사용할 수 있게 된다.</p>
<blockquote>
<p>2) allowImportingTsExtensions</p>
</blockquote>
<p>이 옵션이 없으면 TypeScript는 파일 확장자를 포함한 가져오기를 허용하지 않는다. </p>
<p>예를 들어 example.ts 파일이 있다고 가정해보자</p>
<pre><code class="language-ts">// example.ts
export const example = () =&gt; {
  console.log("Hello from example.ts");
};

// main.ts
import { example } from './example.ts';

example();</code></pre>
<p>다른 파일 main.ts 에서 example.ts를 가져올 때 파일 확장자를 포함하여 가져올 수 있다.</p>
<p>이렇게 하면 TypeScript 파일을 가져올 때 파일 확장자를 명시적으로 포함할 수 있어, JavaScript와의 호환성을 높이고 일부 번들러나 도구와의 통합을 용이하게 한다.</p>
<blockquote>
<p>3) allowJs</p>
</blockquote>
<p>JavaScript 파일을 TypeScript 프로젝트에 포함할 수 있도록 허용한다.</p>
<blockquote>
<p>4) alwaysStrict</p>
</blockquote>
<p>모든 소스 파일에 대해 엄격 모드를 활성화한다.</p>
<blockquote>
<p>5) baseUrl</p>
</blockquote>
<p>모듈 해석을 위한 기본 디렉토리를 설정한다.</p>
<p>예를 들어 이렇게 설정을 하고 프로젝트 구조가 아래와 같다면</p>
<pre><code class="language-js">{
  "compilerOptions": {
    "baseUrl": "."
  }
}

- project-root/
  - tsconfig.json
  - src/
    - index.ts
    - utils/
      - helper.ts
  - components/
    - button.ts
</code></pre>
<p>src/index.ts 파일에서 utils/helper.ts를 import할 때 원래는 상대 경로를 사용해야 한다.</p>
<p><code>import { someFunction } from './utils/helper';</code></p>
<p>하지만, "baseUrl"을 "."으로 설정하면 루트 디렉터리 기준으로 모듈을 참조할 수 있으므로, 다음과 같이 import 경로를 간단하게 작성할 수 있다.</p>
<p><code>import { someFunction } from 'src/utils/helper';</code></p>
<blockquote>
<p>6) checkJs</p>
</blockquote>
<p>TypeScript 컴파일러가 JavaScript 파일(.js)을 타입 체크할지 여부를 결정하는 옵션이다. 이 옵션을 활성화하면, JavaScript 파일도 TypeScript 파일처럼 타입 검사를 받게 된다. JavaScript 파일에서 JSDoc 주석을 사용하여 타입 정보를 제공할 수 있다. TypeScript는 이 정보를 기반으로 타입 검사를 수행한다.</p>
<pre><code class="language-js">/**
 * Adds two numbers together.
 * @param {number} a - The first number.
 * @param {number} b - The second number.
 * @returns {number} The sum of the two numbers.
 */
function add(a, b) {
  return a + b;
}

add(5, "10"); // 이 줄에서 타입 오류가 발생합니다.</code></pre>
<blockquote>
<p>7) declaration</p>
</blockquote>
<p>TypeScript 파일의 선언 파일(.d.ts)을 생성한다.</p>
<p>보통 "declaration" 옵션은 "outDir" 옵션과 함께 사용된다. "outDir"은 컴파일된 출력 파일들이 저장될 디렉터리를 지정하는 옵션이다. 이와 함께 .d.ts 파일도 이 디렉터리에 생성된다.</p>
<p>"declaration" 옵션은 "sourceMap" 옵션과 함께 사용될 수 있다. "sourceMap"은 컴파일된 JavaScript 파일에 대한 소스맵을 생성하여 디버깅을 도와준다.</p>
<p>폴더구조</p>
<ul>
<li>src/<ul>
<li>index.ts</li>
<li>utils.ts</li>
</ul>
</li>
<li>dist/
tsconfig.json 파일:</li>
</ul>
<pre><code class="language-js">{
  "compilerOptions": {
    "outDir": "./dist",
    "declaration": true
  }
}</code></pre>
<p>만약 src/index.ts와 src/utils.ts 파일이 다음과 같은 내용을 가지고 있다면</p>
<pre><code class="language-js">// src/index.ts
import { greet } from './utils';

greet('World');

// src/utils.ts
export function greet(name: string) {
  return `Hello, ${name}!`;
}</code></pre>
<p><code>tsc</code> 명령어 또는, <code>npx tsc</code> 명령어로 컴파일을 실행하면 dist 디렉터리에 다음과 같은 파일들이 생성된다.</p>
<ul>
<li>dist/<ul>
<li>index.js</li>
<li>index.d.ts</li>
<li>utils.js</li>
<li>utils.d.ts</li>
</ul>
</li>
</ul>
<p>여기서 .d.ts 파일들은 다음과 같은 내용을 포함하게 된다.</p>
<pre><code class="language-js">// dist/index.d.ts
export { greet } from "./utils";

// dist/utils.d.ts
export declare function greet(name: string): string;</code></pre>
<p><strong>"declaration" 옵션의 일반적인 사용 시나리오</strong></p>
<ul>
<li><p>라이브러리 개발: TypeScript로 라이브러리를 개발할 때, 라이브러리를 사용하는 다른 개발자들이 타입 정보를 사용할 수 있도록 .d.ts 파일을 함께 제공하는 것이 일반적이다.</p>
</li>
<li><p>프로젝트 구조화: 복잡한 프로젝트에서 컴파일된 코드와 함께 명확한 타입 정보를 제공하여, 코드의 유지보수성을 높일 수 있다.</p>
</li>
<li><p>서드파티 모듈: TypeScript로 작성된 서드파티 모듈을 배포할 때, .d.ts 파일을 포함시켜 모듈 사용자들이 정확한 타입 정보를 기반으로 개발할 수 있게 한다.</p>
</li>
</ul>
<blockquote>
<p>8) emitDeclarationOnly</p>
</blockquote>
<p>"emitDeclarationOnly" 옵션은 TypeScript 컴파일러가 타입 선언 파일(.d.ts)만 생성하고, JavaScript 파일(.js)을 생성하지 않도록 설정할 때 사용된다. 이 옵션은 주로 타입 정의만 필요한 경우에 유용하다.</p>
<p>"declaration" 옵션과 함께 사용: "emitDeclarationOnly" 옵션을 사용하려면 "declaration": true 옵션이 필요하다. 이 옵션이 없으면 .d.ts 파일이 생성되지 않는다.
JavaScript 파일 생성 불가: 이 옵션을 설정하면 JavaScript 파일이 생성되지 않으므로, 실제 실행 가능한 코드를 제공하지 않는다. 타입 정의만 제공할 때 유용하다.</p>
<p>"emitDeclarationOnly" 옵션의 주요 기능</p>
<ul>
<li><p>타입 선언 파일만 생성: "emitDeclarationOnly": true로 설정하면 TypeScript는 컴파일 과정에서 .d.ts 파일만 생성하고, 실제 JavaScript 파일은 생성하지 않는다. 즉, 컴파일된 JavaScript 파일이 필요 없고, 타입 정보만 제공하고 싶을 때 사용한다.</p>
</li>
<li><p>타입 정의 파일 배포: 주로 라이브러리 개발 시에 사용된다. 라이브러리의 타입 정의를 제공하면서, JavaScript 코드는 별도로 처리하거나 이미 제공된 경우에 유용하다.</p>
</li>
</ul>
<blockquote>
<p>9) esModuleInterop</p>
</blockquote>
<p>"esModuleInterop" 옵션은 TypeScript에서 CommonJS 모듈을 ES6 모듈처럼 가져오고 사용할 수 있도록 설정하는 옵션이다. 이 옵션을 활성화하면 TypeScript 컴파일러가 CommonJS 모듈과 ES6 모듈 간의 호환성을 개선해준다.</p>
<p>예시</p>
<pre><code class="language-js">// commonjs-module.js
module.exports = {
  greet: function(name) {
    return `Hello, ${name}!`;
  }
};</code></pre>
<p>esModuleInterop 옵션이 활성화되면, 위의 CommonJS 모듈을 ES6 스타일로 가져올 수 있다</p>
<pre><code class="language-js">// main.ts
import commonjsModule from './commonjs-module';

console.log(commonjsModule.greet('World'));</code></pre>
<p>여기서 commonjsModule은 CommonJS 모듈의 module.exports를 기본적으로 가져온 값이다. 만약 esModuleInterop이 false로 설정되어 있다면, import 구문 대신 require 구문을 사용해야 하며, 다음과 같이 작성해야 한다</p>
<pre><code class="language-js">// main.ts
const commonjsModule = require('./commonjs-module');

console.log(commonjsModule.greet('World'));</code></pre>
<blockquote>
<p>10) isolatedModules</p>
</blockquote>
<p>TypeScript 컴파일러가 파일을 개별적으로 처리하고 모듈화된 코드의 일부와 독립적으로 처리할 수 있도록 한다. 이 옵션은 주로 트랜스파일러와 함께 사용되는 경우에 유용하며, 특히 Babel과 함께 TypeScript를 사용할 때 중요한 역할을 한다.</p>
<p>"isolatedModules" 옵션의 주요 기능</p>
<ul>
<li><p>파일별 독립적 컴파일: "isolatedModules": true로 설정하면, TypeScript 컴파일러는 파일을 독립적으로 컴파일하며, 각 파일이 서로의 타입 정보를 필요로 하지 않도록 처리한다. 이는 파일 간의 의존성을 줄여준다.</p>
</li>
<li><p>타입 검사의 제한: 이 옵션이 활성화되면, TypeScript는 전체 프로젝트의 타입 검사 대신, 각 파일의 독립적인 검사만 수행한다. 따라서 파일 간의 종속성이나 모듈 시스템에 대한 검사에는 제한이 있다.</p>
</li>
<li><p>Babel과의 호환성: Babel과 함께 TypeScript를 사용할 때, Babel이 파일을 개별적으로 처리하는 경우, TypeScript의 "isolatedModules" 옵션을 사용하면 호환성을 유지할 수 있다.</p>
</li>
</ul>
<blockquote>
<p>11) lib</p>
</blockquote>
<p>TypeScript 컴파일러가 사용하는 라이브러리 파일의 목록을 지정한다. 이 옵션은 TypeScript가 타입 체크와 컴파일을 수행하는 데 필요한 타입 정의 파일을 명시적으로 설정하는 데 사용된다.</p>
<p>"lib" 옵션의 주요 기능</p>
<ul>
<li><p>타입 정의 포함: TypeScript는 내장 JavaScript 환경의 타입 정의를 포함하여 코드의 타입 검사를 수행한다. "lib" 옵션을 사용하여 이 내장 타입 정의 파일을 명시적으로 설정할 수 있다.</p>
</li>
<li><p>환경 설정: 다양한 JavaScript 환경 (예: 브라우저, Node.js 등)에 맞는 타입 정의를 설정할 수 있다. 이를 통해 특정 환경에서 사용하는 API에 대한 타입 정의를 제공받을 수 있다.</p>
</li>
<li><p>사용할 타입 정의 파일 제어: "lib" 옵션을 사용하여 어떤 타입 정의 파일이 포함될지 선택할 수 있으며, 이로 인해 불필요한 타입 정의를 제외하거나 특정 환경에 맞는 타입 정의만 포함할 수 있다.</p>
</li>
</ul>
<p>주요 라이브러리 옵션</p>
<ul>
<li>"ES5": ES5 표준의 타입 정의</li>
<li>"ES6": ES6 (ES2015) 표준의 타입 정의</li>
<li>"ES2016", "ES2017", ...: ES2016, ES2017 등 최신 ECMAScript 표준의 타입 정의</li>
<li>"DOM": 웹 브라우저 환경의 DOM API에 대한 타입 정의</li>
<li>"WebWorker": Web Worker API에 대한 타입 정의</li>
<li>"Node": Node.js 환경의 타입 정의</li>
</ul>
<p>tsconfig.json의 "lib" 옵션에 나열된 값들은 TypeScript가 타입 체크를 위해 사용하는 라이브러리 파일의 목록을 지정합니다. 각 값은 특정 JavaScript 환경 또는 ECMAScript 표준의 타입 정의를 포함하며, 이를 통해 TypeScript는 코드에서 사용하는 API와 기능의 타입을 알 수 있게 됩니다.</p>
<p><strong>기본적으로 설정되어있는 lib 옵션이다.</strong></p>
<pre><code class="language-js">"lib": [
      "esnext",
      "dom",
      "dom.iterable",
      "scripthost"
    ],</code></pre>
<p>다음은 "lib" 옵션에 지정된 값들에 대한 설명이다.</p>
<p><code>"esnext"</code></p>
<ul>
<li><p>설명: 최신 ECMAScript 표준의 타입 정의를 포함한다. "esnext"는 현재 표준이 아닌 최신 제안된 ECMAScript 기능들을 포함할 수 있다.</p>
</li>
<li><p>용도: 최신 ECMAScript 기능을 사용하고자 할 때 유용하다. 예를 들어, 최신 자바스크립트 기능(예: 옵셔널 체이닝, null 병합 연산자 등)을 타입 검사를 수행하면서 사용할 수 있다.</p>
</li>
</ul>
<p>예시</p>
<pre><code class="language-js">const dynamicImport = import('./module');</code></pre>
<p>import()는 ESNext 기능으로, 모듈을 동적으로 가져오는 구문이다. dynamicImport 변수가 동적 import를 처리하기 위해 사용된다.</p>
<p>"esnext" 라이브러리가 설정되어 있지 않으면 TypeScript는 이 기능을 인식하지 못하고, 다음과 같은 오류가 발생할 수 있다</p>
<pre><code class="language-js">1. Error: Cannot find name 'import'.

2. Error: 'import' statements are not allowed in this context.</code></pre>
<p><code>"dom"</code></p>
<ul>
<li><p>설명: 웹 브라우저 환경에서 DOM (Document Object Model) API의 타입 정의를 포함한다. 이 타입 정의는 웹 브라우저의 기본적인 DOM 관련 API를 제공한다.</p>
</li>
<li><p>용도: 웹 애플리케이션을 개발할 때, 브라우저에서 사용하는 DOM API (예: document, window, Element 등)를 타입 체크하고 사용할 수 있도록 한다.</p>
</li>
</ul>
<p>예시</p>
<pre><code class="language-js">const element = document.getElementById('myElement');
if (element) {
  element.textContent = 'Hello, world!';
}</code></pre>
<p>document.getElementById와 textContent는 웹 브라우저의 DOM API를 사용한 코드이다.</p>
<p>"dom" 라이브러리가 설정되어 있지 않으면 TypeScript는 document와 관련된 API를 인식하지 못하고, 다음과 같은 오류가 발생할 수 있다</p>
<pre><code class="language-js">1. Error: Cannot find name 'document'.

2. Error: Property 'textContent' does not exist on type 'HTMLElement'.</code></pre>
<p><code>"dom.iterable"</code></p>
<ul>
<li><p>설명: DOM 컬렉션과 같은 반복 가능한 객체의 타입 정의를 포함한다. 이 옵션은 DOM 컬렉션(예: NodeList, HTMLCollection)을 이터러블로 처리할 수 있도록 타입을 정의한다.</p>
</li>
<li><p>용도: DOM 컬렉션에 대한 이터레이션을 지원한다. 예를 들어, for...of 루프를 사용하여 NodeList를 순회할 때 필요하다.</p>
</li>
</ul>
<p>예시</p>
<pre><code class="language-js">const list = document.querySelectorAll('div');
for (const item of list) {
  console.log(item);
}</code></pre>
<p>document.querySelectorAll은 NodeList를 반환하며, for...of 루프를 사용하여 이터레이션할 수 있다.</p>
<p>"dom.iterable" 라이브러리가 설정되어 있지 않으면 NodeList가 이터러블로 인식되지 않아 다음과 같은 오류가 발생할 수 있다.</p>
<pre><code class="language-js">1. Error: Type 'NodeListOf&lt;Element&gt;' is not iterable.

2. Error: Property 'Symbol.iterator' is missing in type 'NodeListOf&lt;Element&gt;'.</code></pre>
<p><code>"scripthost"</code></p>
<ul>
<li><p>설명: Microsoft의 스크립트 호스트 환경 (예: Windows Script Host)의 타입 정의를 포함한다. 이는 WScript 객체와 같은 스크립트 호스트 API를 제공한다.</p>
</li>
<li><p>용도: 스크립트 호스트 환경 (주로 Node.js가 아닌 Windows Script Host에서 실행되는 스크립트)에 대한 타입 정의를 사용할 수 있다.</p>
</li>
</ul>
<p>예시</p>
<pre><code class="language-js">declare var WScript: any;
WScript.Echo('Hello, ScriptHost!');</code></pre>
<p>WScript는 Windows Script Host 환경에서 사용하는 객체다.</p>
<p>"scripthost" 라이브러리가 설정되어 있지 않으면 WScript와 관련된 타입 정의를 찾을 수 없으므로 다음과 같은 오류가 발생할 수 있다.</p>
<pre><code class="language-js">1. Error: Cannot find name 'WScript'.

2. Error: Property 'Echo' does not exist on type 'any'.</code></pre>
<blockquote>
<p>12) module</p>
</blockquote>
<p>TypeScript 컴파일러가 JavaScript 모듈 시스템을 어떻게 변환할지를 지정한다. 이 옵션은 TypeScript 코드를 JavaScript로 트랜스파일할 때 사용하는 모듈 시스템을 결정한다.</p>
<p>"module" 옵션의 주요 기능</p>
<ul>
<li><p>모듈 시스템 선택: JavaScript의 다양한 모듈 시스템 (CommonJS, ES6 Modules, AMD 등) 중에서 어떤 것을 사용할지를 선택한다.</p>
</li>
<li><p>호환성 설정: 프로젝트가 사용하는 모듈 시스템에 따라 코드의 호환성을 맞추어, 다양한 실행 환경 (브라우저, Node.js 등)에서 올바르게 동작하도록 한다.</p>
</li>
<li><p>출력 코드 형식: TypeScript가 생성하는 JavaScript 코드의 모듈 시스템을 결정합니다.</p>
</li>
</ul>
<p><code>"commonjs"</code> : Node.js 환경에서 사용, require와 module.exports를 사용한다.</p>
<p><code>"es6" / "es2015"</code>: ES6 모듈 시스템, import와 export를 사용한다.</p>
<p><code>"amd"</code>: 브라우저 환경에서 비동기적으로 모듈을 로드한다.</p>
<p><code>"system"</code>: SystemJS 모듈 시스템을 사용한다.</p>
<p><code>"umd"</code>: 다양한 환경에서 호환되는 모듈 시스템을 제공한다.</p>
<p><code>"esnext"</code>: 최신 ECMAScript 모듈 시스템을 사용하며, 최신 브라우저 및 Node.js 환경에 적합하다.</p>
<p><code>"NodeNext"</code>: Node.js의 ESM 모듈 시스템을 지원하며, .mjs 파일 확장자와 함께 Node.js의 모듈 해석 방식에 맞춘다.</p>
<blockquote>
<p>13) moduleResolution</p>
</blockquote>
<p>"moduleResolution" 옵션은 모듈을 해석하는 방법을 설정한다. 이 옵션은 TypeScript 컴파일러가 모듈을 어떻게 찾고 가져올지를 결정하며, 특히 모듈의 경로를 어떻게 해석할지 정의한다.</p>
<p><code>"classic"</code>: TypeScript의 오래된 모듈 해석 방식. node_modules를 탐색하지 않으며, 상대 및 절대 경로를 사용한다.</p>
<p><code>"node"</code>: Node.js의 모듈 해석 방식. node_modules 폴더를 포함하여 모듈을 탐색하며, Node.js의 규칙을 따른다.</p>
<p><code>"NodeNext"</code>: Node.js의 ES 모듈 시스템과 호환되도록 모듈을 해석하는 방법을 지정한다. 최신 Node.js 환경에서 ES 모듈을 사용할 때 유용하다.</p>
<blockquote>
<p>14) noFallthroughCasesInSwitch</p>
</blockquote>
<p>"noFallthroughCasesInSwitch" 옵션은 switch 문에서 case가 break 없이 계속 진행(fall-through)되는 것을 방지하도록 설정하는 옵션이다. 이 옵션을 활성화하면 switch 문 내의 각 case 블록이 명시적으로 종료되지 않으면 컴파일 오류가 발생한다.</p>
<p>이 옵션을 true로 설정하면, switch 문 내의 각 case 블록이 break, return, throw 등으로 종료되지 않는 경우 컴파일 타임에 오류를 발생시킨다.</p>
<ul>
<li><p>버그 방지: switch 문에서 의도치 않게 case 블록이 계속 진행되거나 fall-through 되는 것을 방지한다. 이를 통해 코드의 안정성을 높이고, 예상치 못한 동작을 방지할 수 있다.</p>
</li>
<li><p>명시적인 종료: 각 case 블록이 명시적으로 종료되도록 강제하여, 코드의 의도를 명확히 할 수 있다.</p>
</li>
</ul>
<p>기본값은 false다. 즉, fall-through가 허용되며, 이를 방지하려면 이 옵션을 명시적으로 설정해야 한다.</p>
<blockquote>
<p>15) noImplicitAny</p>
</blockquote>
<p>TypeScript 컴파일러가 암시적으로 any 타입을 사용하는 것을 방지하는 옵션이다. 이 옵션을 true로 설정하면 TypeScript는 타입을 명시적으로 정의하지 않거나 추론할 수 없는 경우에 컴파일 오류를 발생시킨다.</p>
<p>true로 설정하면, TypeScript는 변수, 함수 매개변수, 반환 값 등에서 타입이 명확하지 않거나 추론할 수 없는 경우 any 타입을 사용하지 않도록 강제한다. 이를 통해 타입의 명확성을 보장할 수 있다.</p>
<p>기본값은 false다. 기본값에서는 타입이 명시적으로 정의되지 않은 경우에도 컴파일 오류가 발생하지 않는다.</p>
<ul>
<li><p>타입 안전성: any 타입은 TypeScript의 타입 시스템의 이점을 무시하게 만들 수 있다. noImplicitAny를 활성화하면 개발자는 명시적으로 타입을 정의해야 하므로 코드의 타입 안전성을 높일 수 있다.</p>
</li>
<li><p>버그 방지: 암시적인 any 타입 사용을 방지하여, 런타임에서 발생할 수 있는 타입 관련 오류를 사전에 방지한다.</p>
</li>
<li><p>코드 가독성: 코드의 타입을 명확히 하여 다른 개발자들이 코드의 의도를 이해하기 쉽게 한다.</p>
</li>
</ul>
<p>TypeScript는 가능한 경우 타입을 자동으로 추론할 수 있지만, noImplicitAny 옵션이 활성화되면 타입을 명시적으로 정의해야 한다.</p>
<blockquote>
<p>16) noImplicitOverride</p>
</blockquote>
<p>"noImplicitOverride" 옵션은 클래스를 상속할 때 메서드나 속성을 오버라이드(재정의)할 때 명시적으로 override 키워드를 사용하는 것을 강제한다. 이 옵션은 TypeScript 4.3 버전에서 도입되었다.</p>
<p>이 옵션을 true로 설정하면, 자식 클래스에서 부모 클래스의 메서드나 속성을 오버라이드할 때 override 키워드를 명시적으로 사용해야 한다.</p>
<p>기본값은 false다. 기본값에서는 override 키워드를 사용하지 않아도 컴파일 오류가 발생하지 않는다.</p>
<ul>
<li><p>명시적인 오버라이드: override 키워드를 사용함으로써, 개발자는 해당 메서드나 속성이 부모 클래스에서 정의된 것을 오버라이드하고 있음을 명확히 할 수 있다.</p>
</li>
<li><p>버그 방지: 오타나 잘못된 메서드 시그니처로 인한 버그를 방지할 수 있습니다. 예를 들어, 부모 클래스에서 정의된 메서드와 자식 클래스에서 정의된 메서드의 시그니처가 일치하지 않을 경우, override 키워드를 사용하면 컴파일러가 오류를 발생시킨다.</p>
</li>
<li><p>코드 가독성: 코드의 가독성을 높이고, 코드 리뷰 시 오버라이드 여부를 명확히 할 수 있다.</p>
</li>
</ul>
<p>예시</p>
<pre><code class="language-js">class Parent {
  greet() {
    console.log('Hello from Parent');
  }
}

class Child extends Parent {
  override greet() { // Correct: This method overrides a method in the parent class
    console.log('Hello from Child');
  }
}</code></pre>
<blockquote>
<p>17) noImplicitReturns</p>
</blockquote>
<p>"noImplicitReturns" 옵션은 함수에서 모든 코드 경로가 값을 반환하도록 강제하는 옵션이다. 이 옵션을 true로 설정하면, 함수가 모든 분기에서 값을 반환하지 않으면 컴파일 오류가 발생한다. 이는 코드의 완전성을 보장하고, 함수가 모든 코드 경로에서 값을 반환하도록 강제한다.</p>
<p>이 옵션을 true로 설정하면, 함수에서 모든 가능한 코드 경로가 값을 반환해야 함을 강제한다. 만약 함수가 특정 코드 경로에서 값을 반환하지 않으면 컴파일 오류가 발생한다.</p>
<p>기본값은 false다. 기본값에서는 함수의 모든 코드 경로가 값을 반환하지 않아도 오류가 발생하지 않는다.</p>
<ul>
<li><p>코드 안정성: 함수가 모든 코드 경로에서 값을 반환하도록 보장함으로써, 런타임에서 예상치 못한 동작이나 버그를 예방할 수 있다.</p>
</li>
<li><p>명시적인 반환: 함수의 반환 값이 명확하게 정의되어 있어, 함수 호출 시 예측 가능한 결과를 얻을 수 있다.</p>
</li>
<li><p>문서화: 함수의 반환 값을 명확히 문서화하여, 코드의 가독성과 유지보수성을 높일 수 있다.</p>
</li>
</ul>
<p>예시</p>
<pre><code class="language-js">function processValue(value: number): number {
  if (value &gt; 0) {
    return value;
  }
  // Missing return statement in this branch
}</code></pre>
<p>processValue 함수는 value가 0보다 클 때 값을 반환하지만, value가 0 이하일 때는 값을 반환하지 않는다. "noImplicitReturns"가 true로 설정된 경우, 이 코드에서는 컴파일 오류가 발생한다.</p>
<pre><code class="language-js">function processValue(value: number): number {
  if (value &gt; 0) {
    return value;
  } else {
    return -value;
  }
}</code></pre>
<p>위 코드에서는 value가 0보다 클 때와 그렇지 않을 때 모두 값을 반환한다. "noImplicitReturns"가 true로 설정된 경우에도 오류가 발생하지 않는다.</p>
<blockquote>
<p>18) noUnusedParameters</p>
</blockquote>
<p>"noUnusedParameters" 옵션은 선언된 함수의 매개변수 중 사용되지 않는 것에 대해 경고하거나 오류를 발생시키는 옵션이다. 이 옵션을 true로 설정하면, 코드 내에서 선언된 함수의 매개변수가 사용되지 않을 경우 컴파일 오류가 발생한다. 이는 코드의 청결성과 유지보수성을 높이는 데 도움이 된다.</p>
<p>이 옵션을 true로 설정하면, 함수의 매개변수가 선언되었으나 사용되지 않는 경우 컴파일 오류가 발생한다.</p>
<p>기본값은 false입니다. 기본값에서는 사용되지 않는 매개변수에 대해 경고나 오류가 발생하지 않는다.</p>
<ul>
<li><p>코드 청결성: 사용되지 않는 매개변수를 식별하고 제거하여 코드를 더 깔끔하고 이해하기 쉽게 만들 수 있다.</p>
</li>
<li><p>유지보수성: 코드에서 불필요한 부분을 제거하여 유지보수를 더 쉽게 할 수 있다. 특히, 코드가 복잡해질 때 불필요한 매개변수를 제거하는 것이 중요하다.</p>
</li>
<li><p>버그 예방: 불필요한 매개변수를 제거함으로써, 향후 코드 변경 시 의도치 않은 버그를 예방할 수 있다.</p>
</li>
</ul>
<p>예시</p>
<pre><code class="language-js">function greet(name: string, age: number) {
  console.log(`Hello, ${name}`);
  // 매개변수 'age'는 사용되지 않음
}</code></pre>
<blockquote>
<p>19) paths</p>
</blockquote>
<p>paths 옵션은 모듈 경로를 매핑하여 모듈을 가져오는 경로를 커스터마이즈할 수 있게 해주는 기능이다. 이 옵션을 사용하면 상대 경로의 복잡성을 줄이고, 모듈을 더 간결하고 읽기 쉽게 가져올 수 있다.</p>
<p>paths는 특정 모듈 경로를 별칭(alias)으로 매핑할 수 있게 해준다. 이를 통해 모듈을 import할 때 상대 경로 대신 별칭을 사용할 수 있다.</p>
<p>paths 옵션은 baseUrl 옵션과 함께 사용된다. baseUrl은 모듈 해석의 기준이 되는 루트 디렉토리를 정의하고, paths는 이 기준을 기반으로 별칭을 정의한다.</p>
<p>paths 옵션의 값은 객체 형태로, 각 키는 별칭이며, 값은 별칭이 매핑되는 실제 경로 배열이다.</p>
<ul>
<li><p>경로 간소화: 긴 상대 경로를 줄이고, 모듈을 더 간단하게 import할 수 있다.</p>
</li>
<li><p>코드 가독성: 코드에서 import 경로가 더 읽기 쉽고 명확해진다.</p>
</li>
<li><p>리팩토링 용이: 프로젝트 구조를 변경하거나 디렉토리 이름을 변경할 때 import 경로를 쉽게 업데이트할 수 있다.</p>
</li>
</ul>
<p>예시</p>
<pre><code class="language-js">{
  "compilerOptions": {
    "baseUrl": "./src",
    "paths": {
      "@components/*": ["components/*"],
      "@utils/*": ["utils/*"],
      "@models/*": ["models/*"]
    }
  }
}</code></pre>
<p>이 설정은 baseUrl을 ./src로 설정한 상태에서, 다음과 같은 별칭을 정의한다</p>
<p>@components/<em>는 ./src/components/</em>로 매핑된다.
@utils/<em>는 ./src/utils/</em>로 매핑된다.
@models/<em>는 ./src/models/</em>로 매핑된다.</p>
<pre><code class="language-js">// tsconfig.json 설정에 따른 import 경로
import { Button } from '@components/Button';
import { calculate } from '@utils/helpers';
import { User } from '@models/User';</code></pre>
<blockquote>
<p>20) removeComments</p>
</blockquote>
<p>"removeComments" 옵션은 컴파일된 JavaScript 파일에서 주석을 제거할지 여부를 지정하는 옵션이다. 이 옵션을 사용하면, TypeScript 컴파일러가 TypeScript 소스 코드에서 작성된 주석을 JavaScript로 컴파일된 결과에서 제거할 수 있다.</p>
<p>이 옵션을 true로 설정하면 컴파일 과정에서 주석이 제거된다.</p>
<p>기본값은 false다. 기본값으로 설정되어 있으면, 컴파일된 JavaScript 파일에 주석이 포함된다.</p>
<ul>
<li><p>코드 축소: 배포된 코드에서 주석을 제거하여 파일 크기를 줄이고, 최종 코드의 용량을 줄일 수 있다.</p>
</li>
<li><p>보안: 소스 코드에 작성된 주석이 공개되는 것을 방지할 수 있다. 특히, 민감한 정보나 개발 중의 메모가 포함된 주석을 제거할 때 유용하다.</p>
</li>
<li><p>청결한 배포 코드: 배포용 코드를 보다 깔끔하게 유지할 수 있다. 주석이 포함되지 않아 코드의 가독성이 높아질 수 있다.</p>
</li>
</ul>
<p>예시</p>
<pre><code class="language-js">// This is a single-line comment
/**
 * This is a multi-line comment
 */
function greet(name: string): void {
  console.log(`Hello, ${name}`);
}</code></pre>
<p>true로 설정</p>
<pre><code class="language-js">function greet(name) {
  console.log("Hello, " + name);
}</code></pre>
<blockquote>
<p>21) rootDir</p>
</blockquote>
<p>"rootDir" 옵션은 TypeScript 컴파일러에게 소스 파일의 루트 디렉토리를 지정하는 역할을 한다. 이 옵션은 프로젝트 내에서 TypeScript 소스 파일의 구조를 설정하고, 컴파일된 JavaScript 파일이 배치될 디렉토리를 결정하는 데 중요한 역할을 한다.</p>
<p>"rootDir"은 TypeScript 소스 파일의 루트 디렉토리를 정의한다. 이 옵션을 설정하면, TypeScript 컴파일러는 이 디렉토리 내의 파일들을 소스 파일로 간주하고, 이 디렉토리 구조를 기준으로 컴파일을 수행한다.</p>
<ul>
<li><p>디렉토리 구조 관리: rootDir을 설정하면, 소스 파일이 위치한 루트 디렉토리를 명확히 하여 프로젝트의 디렉토리 구조를 관리할 수 있다.</p>
</li>
<li><p>출력 디렉토리 구조 유지: rootDir을 설정하면, 컴파일된 JavaScript 파일이 출력 디렉토리에서 원본 소스 파일의 디렉토리 구조를 유지하게 된다. 이는 소스와 출력 디렉토리 간의 구조적 일관성을 제공한다.</p>
</li>
</ul>
<blockquote>
<p>22) strict</p>
</blockquote>
<p>"strict" 옵션은 여러 가지 엄격한 타입 검사 옵션을 활성화하여 코드의 정확성과 안정성을 높이는 설정이다. 이 옵션을 true로 설정하면, TypeScript의 모든 엄격한 타입 검사 옵션이 활성화된다. 이로 인해, 코드에서 잠재적인 오류를 사전에 발견하고, 더 견고하고 안정적인 코드를 작성할 수 있다.</p>
<p>"strict" 옵션을 true로 설정하면, TypeScript의 여러 엄격한 타입 검사 옵션이 모두 활성화된다. 이 옵션은 타입 안전성을 높이기 위한 여러 설정을 한 번에 적용할 수 있게 해준다.</p>
<p>기본값은 false다. 기본적으로 엄격한 검사 옵션이 비활성화되어 있다.</p>
<p>true로 설정하면 다음과 같은 타입 검사 옵션이 자동으로 활성화된다</p>
<ul>
<li><p><code>noImplicitAny</code>: 암시적 any 타입 사용에 대해 오류를 발생시킨다.</p>
</li>
<li><p><code>noImplicitThis</code>: 암시적인 this에 대해 오류를 발생시킨다.</p>
</li>
<li><p><code>alwaysStrict</code>: 모든 JavaScript 파일을 엄격 모드로 처리한다.</p>
</li>
<li><p><code>strictNullChecks</code>: null과 undefined에 대한 타입 검사를 엄격히 수행한다.</p>
</li>
<li><p><code>strictFunctionTypes</code>: 함수 타입의 인수와 반환 값에 대한 엄격한 검사를 수행한다.</p>
</li>
<li><p><code>strictPropertyInitialization</code>: 클래스의 속성이 초기화되지 않은 상태로 사용되는 경우 오류를 발생시킨다.</p>
</li>
<li><p><code>noImplicitReturns</code>: 함수에서 모든 경로에서 값을 반환하지 않으면 오류를 발생시킨다.</p>
</li>
<li><p><code>noFallthroughCasesInSwitch</code>: switch 문에서 case 문이 누락된 경우 오류를 발생시킨다.</p>
</li>
</ul>
<blockquote>
<p>23) strictFunctionTypes</p>
</blockquote>
<p>"strictFunctionTypes" 옵션은 함수 타입의 호환성 검사를 더 엄격하게 만들어 함수 매개변수의 타입에 대한 검사를 강화하는 기능이다. 이 옵션은 함수 타입의 인수에 대해 더 강력한 타입 검사를 수행하며, 특히 함수 타입 간의 호환성을 엄격히 검사한다.</p>
<p>strictFunctionTypes 옵션을 활성화하면, TypeScript는 함수 타입의 매개변수와 관련된 타입 호환성을 더 엄격하게 검사한다. 이 옵션이 활성화되면, 함수의 매개변수 타입이 더 강력하게 일치해야 한다.</p>
<p>기본적으로 strictFunctionTypes는 true로 설정되어 있다. 이는 TypeScript의 strict 모드가 활성화될 때 자동으로 적용된다.</p>
<ul>
<li><p>타입 안전성 향상: 함수 타입의 인수에 대해 더욱 엄격한 검사를 수행하여, 타입 불일치로 인한 잠재적인 버그를 사전에 방지할 수 있다.</p>
</li>
<li><p>타입 호환성 강화: 함수 타입을 사용할 때, 인수의 타입이 정확하게 맞아야만 호환되도록 하여, 더 안정적인 코드를 작성할 수 있다.</p>
</li>
</ul>
<blockquote>
<p>24) strictPropertyInitialization</p>
</blockquote>
<p>"strictPropertyInitialization" 옵션은 클래스의 속성이 초기화되지 않았을 때 오류를 발생시키는 옵션이다. 이 옵션을 활성화하면, 클래스의 속성이 생성자에서 초기화되지 않거나 클래스 외부에서 초기화되지 않은 경우, TypeScript가 오류를 발생시킨다. 이로써, 클래스의 모든 속성이 초기화되어야 한다는 것을 보장할 수 있다.</p>
<p>strictPropertyInitialization은 클래스의 속성 초기화를 강제하는 옵션이다. 이 옵션이 활성화되면, 클래스의 모든 속성이 생성자에서 초기화되거나, 명시적으로 초기값을 제공해야 한다.
기본값은 true다. 이는 strict 모드가 활성화될 때 자동으로 적용된다.</p>
<ul>
<li><p>안정성 향상: 클래스 속성이 항상 초기화되도록 보장하여, 런타임에서 발생할 수 있는 오류를 방지한다.</p>
</li>
<li><p>코드 품질: 클래스 속성 초기화가 누락된 경우를 사전에 잡아내어 코드의 품질을 향상시킨다.</p>
</li>
</ul>
<blockquote>
<p>25) target</p>
</blockquote>
<p>"target" 옵션은 TypeScript 코드를 컴파일할 때 생성되는 JavaScript 코드의 버전을 결정하는 옵션이다. 이 옵션을 통해 TypeScript 코드를 어떤 JavaScript 버전으로 변환할지 설정할 수 있다.</p>
<p>"target" 옵션은 TypeScript 파일을 컴파일할 때 출력될 JavaScript 코드의 ECMAScript(ES) 버전을 지정한다. 이 설정에 따라 생성되는 JavaScript 코드의 문법과 기능이 결정된다.</p>
<p>TypeScript 코드에서 최신 ECMAScript 기능을 사용할 수 있지만, 컴파일된 JavaScript 코드가 특정 JavaScript 엔진과 호환되도록 하기 위해 target 옵션을 사용한다.</p>
<p><strong>지원하는 값</strong></p>
<p>target 옵션은 다양한 ECMAScript 버전을 지원한다. 일반적으로 사용되는 값은 다음과 같다</p>
<ul>
<li><p><code>"ES3"</code>: 매우 오래된 ECMAScript 3 버전이다. (구형 브라우저 지원)</p>
</li>
<li><p><code>"ES5"</code>: 거의 모든 브라우저와 호환되는 ECMAScript 5 버전이다.</p>
</li>
<li><p><code>"ES6"</code> / <code>"ES2015"</code>: ES6(또는 ECMAScript 2015) 버전이다.</p>
</li>
<li><p><code>"ES2016"</code>, <code>"ES2017"</code>, <code>"ES2018"</code>, <code>"ES2019"</code>, <code>"ES2020"</code>, <code>"ES2021"</code>, <code>"ES2022"</code>: 각 연도에 해당하는 ECMAScript 버전이다.</p>
</li>
<li><p><code>"ESNext"</code>: 최신 ECMAScript 기능을 사용한다. (항상 최신 버전으로 컴파일)</p>
</li>
</ul>
<p><strong>컴파일러 동작</strong></p>
<p>예를 들어, target을 "ES5"로 설정하면 최신 TypeScript 코드에서 사용하는 let, const, 화살표 함수 등은 ECMAScript 5에 맞게 변환된다.
반대로 target을 "ESNext"로 설정하면 최신 ECMAScript 기능이 그대로 사용된다.</p>
<pre><code class="language-js">// target: ES5
let x: string = "Hello";
const add = (a: number, b: number) =&gt; a + b;

// 컴파일된 JavaScript 코드 (타겟 ES5)
var x = "Hello";
var add = function (a, b) { return a + b; };</code></pre>
<p>let과 const가 각각 var로 변환되고, 화살표 함수가 일반 함수로 변환된다.</p>
<pre><code class="language-js">// target: ES6
let x: string = "Hello";
const add = (a: number, b: number) =&gt; a + b;

// 컴파일된 JavaScript 코드 (타겟 ES6)
let x = "Hello";
const add = (a, b) =&gt; a + b;</code></pre>
<p>let, const, 화살표 함수 등 ES6 문법이 그대로 유지된다.</p>
<blockquote>
<p>26) typeRoots</p>
</blockquote>
<p>"typeRoots" 옵션은 컴파일러가 타입 정의 파일(.d.ts 파일)을 찾을 디렉토리 경로를 지정하는 데 사용된다. 이 옵션을 사용하면 TypeScript가 특정 디렉토리에서 타입 정의 파일을 탐색하도록 설정할 수 있다.</p>
<p>"typeRoots" 옵션은 TypeScript 컴파일러가 타입 정의 파일을 검색할 디렉토리 목록을 지정하는 옵션이다. 이 옵션에 설정된 경로들은 TypeScript가 자동으로 참조하는 타입 정의 파일들을 포함하는 디렉토리들이다.</p>
<p>"typeRoots"를 설정하면, TypeScript는 해당 디렉토리들에서 타입 정의 파일을 검색한다. 이를 통해 특정 라이브러리나 프로젝트의 커스텀 타입 정의 파일을 명시적으로 지정할 수 있다.</p>
<p><strong>기본값</strong></p>
<p>typeRoots 옵션을 설정하지 않으면, TypeScript는 기본적으로 node_modules/@types 디렉토리에서 타입 정의 파일을 찾는다. 이 디렉토리는 npm을 통해 설치된 타입 패키지들이 위치하는 곳이다.</p>
<pre><code class="language-js">"typeRoots": [
      "node_modules/@types",
      "src/@declare"
    ],</code></pre>
<p>이 경로들에서 발견되는 모든 .d.ts 파일들이 자동으로 포함된다.</p>
<p><strong>동작 방식</strong></p>
<p>typeRoots에 설정된 디렉토리는 각각 타입 정의 파일을 포함하는 폴더로 취급되며, TypeScript는 이 경로들에서 타입 정의 파일을 자동으로 인식하고 사용한다.</p>
<p>typeRoots를 설정하면, 기본적으로 node_modules/@types 디렉토리는 포함되지 않는다. 따라서 모든 타입 정의 경로를 명시적으로 지정해야 한다.</p>
<p>기본 <code>"node_modules/@types"</code>을 포함한 필요시 커스텀, 추가할 타입은 <code>src/@declare</code> 경로도 추가로 지정한다.</p>
<blockquote>
<p>27) types</p>
</blockquote>
<p>"types" 옵션은 컴파일러가 어떤 타입 정의 파일(.d.ts 파일)을 포함할지 명시적으로 지정하는 옵션이다. 이 옵션을 사용하면 특정 타입 패키지를 포함하거나 제외할 수 있으며, 프로젝트에서 필요한 타입만을 명시적으로 로드할 수 있다.</p>
<p>"types" 옵션은 <strong style="color: red;">TypeScript가 타입 정의 파일을 찾는 위치를 지정하는 것이 아니라, 포함할 특정 타입 정의 패키지의 이름을 지정하는 옵션이다.</strong>
이 옵션에 명시된 패키지들만 TypeScript 컴파일러에 의해 포함된다.</p>
<p>"types" 옵션을 설정하면, 프로젝트에서 명시된 타입 정의 패키지들만 로드되며, 그 외의 타입 정의 파일들은 무시된다. 이를 통해 불필요한 타입 정의를 제외하고, 필요한 타입 정의만을 사용하도록 강제할 수 있다.</p>
<p><strong>기본값</strong></p>
<p>"types" 옵션을 설정하지 않으면, TypeScript는 기본적으로 node_modules/@types에 있는 모든 타입 정의 패키지를 포함합니다. 이는 프로젝트에 설치된 모든 타입 패키지들이 자동으로 포함된다는 의미다.</p>
<p><strong>예시</strong></p>
<pre><code class="language-js">{
  "compilerOptions": {
    "types": ["node", "jest"]
  }
}</code></pre>
<p>이 설정을 사용하면 TypeScript는 @types/node와 @types/jest 패키지들만 포함한다. 즉, node_modules/@types에 다른 타입 정의 패키지가 존재하더라도, 컴파일러는 이 두 패키지에 대해서만 타입 정보를 로드한다.</p>
<p>"types" 옵션에 나열된 타입 정의 패키지는 반드시 node_modules/@types 폴더에 있어야 한다.
이 옵션을 사용하면, 프로젝트에서 불필요한 타입 패키지를 제외하고, 필요한 타입 패키지들만을 포함할 수 있다.</p>
<pre><code class="language-js">{
  "compilerOptions": {
    "types": []
  }
}</code></pre>
<p>이 설정은 node_modules/@types 폴더에 있는 모든 타입 정의 패키지를 무시한다. 즉, 어떤 타입 정의 패키지도 포함되지 않는다. 이 경우, 프로젝트에서 직접 참조하는 .d.ts 파일이나 import 문으로 명시적으로 포함한 타입 정의만 사용된다.</p>
<blockquote>
<p>28) jsx</p>
</blockquote>
<p>"jsx" 옵션은 TypeScript 파일에서 JSX 구문을 사용할 때, 이를 어떻게 처리할지를 지정하는 옵션이다. JSX는 React에서 주로 사용되는 구문으로, HTML과 유사한 문법을 JavaScript 코드 내에서 사용할 수 있게 해준다.</p>
<p>이 옵션은 TypeScript가 JSX 구문을 포함한 코드를 어떻게 변환할지를 지정한다.</p>
<p>주로 React와 같은 프레임워크에서 사용되는 JSX 코드를 JavaScript로 변환하는 방식을 결정한다.</p>
<p><strong>jsx 옵션의 값</strong></p>
<ul>
<li><p><code>react</code>: JSX 구문을 React.createElement 함수 호출로 변환한다. (기본값)</p>
</li>
<li><p><code>react-jsx</code>: TypeScript 4.1부터 도입된 새로운 변환 방식으로, React 17 이상을 사용할 때 JSX 변환 시 React.createElement 대신 자동으로 JSX 런타임을 사용한다.</p>
</li>
<li><p><code>react-jsxdev</code>: react-jsx와 유사하지만, 개발 모드에서 추가적인 디버깅 정보를 제공한다.</p>
</li>
<li><p><code>preserve</code>: JSX 구문을 변환하지 않고 그대로 유지한다. 이 경우 .jsx 확장자로 파일이 저장되며, 후속 단계에서 Babel이나 다른 도구로 처리된다.</p>
</li>
<li><p><code>react-native</code>: JSX 구문을 React Native 환경에 맞게 변환한다. React Native 프로젝트에서 사용된다.</p>
</li>
</ul>
<p><strong>예시</strong></p>
<pre><code class="language-js">// tsconfig.json
{
  "compilerOptions": {
    "jsx": "react"
  }
}

// tsx
const element = &lt;div&gt;Hello, world!&lt;/div&gt;;

// 변환
const element = React.createElement('div', null, 'Hello, world!');</code></pre>
<blockquote>
<p>29) experimentalDecorators</p>
</blockquote>
<p>"experimentalDecorators" 옵션은 TypeScript에서 데코레이터 기능을 사용하기 위해 활성화하는 옵션이다. 데코레이터는 클래스 및 클래스 멤버(예: 메서드, 속성)에 주석처럼 붙여서, 특정 기능을 추가하거나 수정할 수 있게 해주는 메타프로그래밍 도구이다.</p>
<p><strong>데코레이터의 배경</strong></p>
<p>데코레이터는 JavaScript에 제안된 기능으로, ECMAScript(ES) 표준에는 아직 정식으로 포함되지 않았다. 하지만 TypeScript에서는 이 기능을 실험적으로 도입하여 사용할 수 있도록 하고 있다.
이 기능은 TypeScript의 데코레이터와 관련된 문법을 사용할 때, 컴파일러에서 이를 인식하고 올바르게 처리할 수 있게 해준다.</p>
<p><strong>experimentalDecorators 옵션의 특징</strong></p>
<p>데코레이터 문법을 사용하려면 experimentalDecorators 옵션을 true로 설정해야 한다.</p>
<p>이 옵션을 활성화하면 클래스, 메서드, 접근자(getter/setter), 속성, 파라미터 등에 데코레이터를 사용할 수 있다.</p>
<p><strong>예시</strong></p>
<p>데코레이터의 기본 구조</p>
<pre><code class="language-js">function MyDecorator(target: any, propertyKey: string, descriptor: PropertyDescriptor) {
  // 데코레이터의 동작을 정의합니다.
}</code></pre>
<ol>
<li>기본 로그 데코레이터</li>
</ol>
<p>아래는 로그를 출력하는 기본적인 데코레이터의 예</p>
<pre><code class="language-js">// 로그를 출력하는 데코레이터
function Log(target: any, propertyKey: string, descriptor: PropertyDescriptor) {
  const originalMethod = descriptor.value;  // 원래의 메서드를 저장합니다.

  descriptor.value = function (...args: any[]) {
    console.log(`Calling ${propertyKey} with arguments: ${args}`);  // 로그 출력
    return originalMethod.apply(this, args);  // 원래 메서드를 호출합니다.
  };
}

// 클래스와 메서드에 데코레이터를 적용
class MyClass {
  @Log  // 이 메서드 호출 시 자동으로 로그가 출력됩니다.
  sayHello(name: string) {
    return `Hello, ${name}!`;
  }
}

const instance = new MyClass();
console.log(instance.sayHello('World'));  // 콘솔에 "Calling sayHello with arguments: World"가 출력됨</code></pre>
<p>데코레이터는 코드에 기능을 추가하는 주석처럼 생각할 수 있다.</p>
<ul>
<li>재사용성: 한번 정의한 데코레이터는 여러 메서드나 클래스에서 재사용할 수 있다.</li>
<li>예시: @Log 데코레이터는 메서드 호출 시 자동으로 콘솔 로그를 출력하게 해준다.</li>
</ul>
<hr />

<ol start="2">
<li>입력 유효성 검사 데코레이터</li>
</ol>
<p>다음은 메서드의 입력값이 숫자인지 검사하는 데코레이터다.</p>
<pre><code class="language-js">// 데코레이터 정의
function Validate(target: any, propertyKey: string, descriptor: PropertyDescriptor) {
  const originalMethod = descriptor.value;

  descriptor.value = function (...args: any[]) {
    for (const arg of args) {
      if (typeof arg !== 'number') {
        throw new Error('Invalid argument');
      }
    }
    return originalMethod.apply(this, args);
  };
}

// 데코레이터 사용
class Calculator {
  @Validate
  add(a: number, b: number): number {
    return a + b;
  }
}

const calculator = new Calculator();
console.log(calculator.add(10, 5));  // 정상 동작
console.log(calculator.add(10, '5'));  // 오류 발생: Invalid argument</code></pre>
<blockquote>
<p>30) skipLibCheck</p>
</blockquote>
<p>"skipLibCheck" 옵션은 TypeScript의 컴파일러 옵션 중 하나로, 라이브러리 파일의 타입 검사를 건너뛰도록 설정한다.</p>
<p>TypeScript는 프로젝트의 타입 검사뿐만 아니라, node_modules에 있는 외부 라이브러리의 타입 정의 파일 (.d.ts)도 검사한다. skipLibCheck 옵션을 true로 설정하면, 이러한 외부 라이브러리의 타입 검사를 건너뛰게 된다.</p>
<p>주로 사용하는 이유</p>
<ul>
<li><p>컴파일 속도 개선: 외부 라이브러리의 타입 검사 때문에 컴파일 속도가 느려질 수 있다. 이 옵션을 사용하면 이러한 검사 과정을 건너뛰어 컴파일 속도를 개선할 수 있다.</p>
</li>
<li><p>타입 정의의 오류 방지: 외부 라이브러리의 타입 정의가 잘못되었거나, 프로젝트와 호환되지 않을 경우, 이를 무시하고 컴파일을 계속할 수 있다.</p>
</li>
<li><p>타입 정의 문제 해결: 외부 라이브러리의 타입 정의에 문제가 있을 때, skipLibCheck를 사용하여 해당 문제로 인해 프로젝트의 컴파일이 실패하지 않도록 할 수 있다.</p>
</li>
</ul>
<blockquote>
<p>31) forceConsistentCasingInFileNames</p>
</blockquote>
<p>"forceConsistentCasingInFileNames" 옵션은 TypeScript 컴파일러의 설정 중 하나로, 파일 이름의 대소문자 일관성을 강제하는 기능을 제공한다.</p>
<p>이 옵션을 활성화하면, TypeScript 컴파일러는 프로젝트 내에서 파일의 대소문자가 일관되도록 강제한다. 즉, 파일 이름의 대소문자가 프로젝트의 다른 부분에서 참조되는 방식과 일치해야 한다.</p>
<p>기본적으로 false로 설정되어 있다. 즉, 대소문자 일관성을 강제하지 않는다.</p>
<p>주로 사용하는 이유</p>
<ul>
<li><p>호환성: 파일 시스템에 따라 대소문자 구분 여부가 다를 수 있다. 예를 들어, Windows는 기본적으로 대소문자를 구분하지 않지만, Linux와 macOS는 대소문자를 구분한다. 이 옵션을 활성화하면, 이러한 차이로 인한 문제를 방지할 수 있다.</p>
</li>
<li><p>일관성 유지: 프로젝트 내에서 파일 이름의 대소문자가 일관되게 유지되도록 강제할 수 있다. 이는 코드의 일관성과 가독성을 높이는 데 도움이 된다.</p>
</li>
<li><p>빌드 오류 방지: 파일 이름의 대소문자 문제로 인해 빌드 오류가 발생할 수 있다. 이 옵션을 활성화하면 이러한 문제를 사전에 방지할 수 있다.</p>
</li>
</ul>
<p><strong>예시</strong></p>
<p>옵션이 false인 경우</p>
<pre><code class="language-js">import { MyComponent } from './MyComponent'; // 실제 파일명이 'mycomponent.ts'인 경우</code></pre>
<p>forceConsistentCasingInFileNames가 <strong>false</strong>로 설정되어 있으면, TypeScript는 파일 이름의 대소문자를 검사하지 않으므로, 실제 파일 이름이 mycomponent.ts여도 오류가 발생하지 않는다. 즉, MyComponent와 mycomponent의 대소문자가 일치하지 않더라도 문제없이 컴파일된다.</p>
<p>옵션이 true인 경우</p>
<pre><code class="language-js">import { MyComponent } from './MyComponent'; // 실제 파일명이 'mycomponent.ts'인 경우</code></pre>
<p>forceConsistentCasingInFileNames가 <strong>true</strong>로 설정되어 있으면, TypeScript는 파일 이름의 대소문자가 정확히 일치해야 한다고 요구한다. 따라서 실제 파일명이 mycomponent.ts일 때, MyComponent를 import하려고 하면 오류가 발생한다. 이 경우, 대소문자가 맞지 않기 때문에 컴파일 오류가 발생하게 된다.</p>
<blockquote>
<p>32) useDefineForClassFields</p>
</blockquote>
<p>"useDefineForClassFields" 옵션은 TypeScript 컴파일러의 설정 중 하나로, 클래스 필드의 정의 방식을 결정한다. 이 옵션은 TypeScript에서 클래스 필드의 값을 정의할 때 사용하는 방법을 제어한다.</p>
<p>"useDefineForClassFields" 옵션은 true일 때, 클래스 필드의 값을 정의할 때 ECMAScript의 define 방식을 사용한다. 이 방식은 클래스 필드를 클래스 정의의 최상위에서 정의하는 방식이다.</p>
<p>기본적으로 false로 설정되어 있으며, 이 경우 TypeScript는 기존의 방식으로 클래스 필드를 정의한다. 이 방식은 TypeScript가 클래스를 정의할 때, 필드의 초기화가 클래스 생성자에 의해 수행되도록 한다.</p>
<p><strong>옵션의 효과</strong></p>
<ul>
<li><p>ECMAScript 호환성: useDefineForClassFields를 <strong>true</strong>로 설정하면, TypeScript의 클래스 필드 정의가 ECMAScript의 define 방식을 따른다. 이는 ECMAScript의 표준에 더 가깝다.</p>
</li>
<li><p>필드 정의 방식: true 클래스 필드가 정의될 때 Object.defineProperty를 사용하여 프로퍼티를 정의한다. 이 방식은 ECMAScript의 클래스 필드 정의와 동일하다.
false: 기존 TypeScript 방식으로, 필드가 생성자 함수에서 초기화된다.</p>
</li>
</ul>
<blockquote>
<p>33) sourceMap</p>
</blockquote>
<p>"sourceMap" 옵션은 TypeScript 컴파일러의 설정 중 하나로, 소스 맵을 생성할지 여부를 제어한다. 소스 맵은 디버깅을 돕기 위해 원본 소스 코드와 변환된 자바스크립트 코드 사이의 매핑 정보를 제공하는 파일이다.</p>
<p><strong>설명</strong></p>
<p>소스 맵(Source Map): 소스 맵 파일(.map 확장자)은 컴파일된 자바스크립트 코드가 원본 TypeScript 또는 다른 소스 코드와 어떻게 매핑되는지를 나타낸다. 이를 통해 브라우저 개발자 도구에서 디버깅할 때, 변환된 자바스크립트 코드가 아니라 원본 코드에서 직접 디버깅할 수 있게 된다.</p>
<p>기본적으로 <strong>false</strong>로 설정되어 있다. 즉, 소스 맵 파일이 생성되지 않는다.</p>
<p>주요 사용 이유</p>
<ul>
<li><p>디버깅: 소스 맵을 사용하면 브라우저의 개발자 도구에서 TypeScript 원본 코드에 직접 접근하고 디버깅할 수 있다. 이는 자바스크립트로 변환된 코드가 아닌, 원본 TypeScript 코드에서 디버깅할 수 있게 해준다.</p>
</li>
<li><p>문제 해결: 애플리케이션의 문제를 해결할 때, 소스 맵을 통해 변환된 코드가 아닌 원본 코드의 행과 열을 기준으로 문제를 찾을 수 있다.</p>
</li>
<li><p>가독성 향상: 소스 맵을 사용하면 변환된 자바스크립트 코드와 원본 소스 코드 간의 관계를 명확하게 파악할 수 있어, 코드의 가독성과 유지보수성이 향상된다.</p>
</li>
</ul>
<p><strong>예시</strong></p>
<pre><code class="language-js">// index.ts
const greet = (name: string) =&gt; `Hello, ${name}`;
console.log(greet('World'));

// index.js (컴파일된 자바스크립트)
const greet = (name) =&gt; `Hello, ${name}`;
console.log(greet('World'));

// index.js.map (소스 맵)
{
  "version": 3,
  "file": "index.js",
  "sources": ["index.ts"],
  "names": ["greet", "name", "console", "log"],
  "mappings": "AAAA,MAAM,GAAG,CAAC,GAAR,CAAY,GAAG,CAAC,CAAC;AAC1B,OAAO,CAAC,GAAR,CAAY,CAAC,CAAC"
}
</code></pre>
<hr />

<h2 id="2-include">2. include</h2>
<blockquote>
<p>include 속성</p>
</blockquote>
<p>include 속성은 컴파일러가 포함할 파일 또는 폴더를 지정한다. 이 속성에 나열된 경로의 파일과 폴더는 TypeScript 컴파일러의 컴파일 대상이 된다.</p>
<p>형식은 배열로 지정하며, 파일 경로나 패턴을 나열한다.</p>
<p><strong>예시</strong></p>
<pre><code class="language-js">{
  "include": [
    "src/**/*"
  ]
}</code></pre>
<p>위 예시는 src 폴더와 그 하위 폴더에 있는 모든 파일을 포함하도록 지정한다. <code>**/*</code>는 모든 하위 폴더와 파일을 의미한다.</p>
<hr />

<h2 id="3-exclude">3. exclude</h2>
<blockquote>
<p>exclude 속성</p>
</blockquote>
<p>exclude 속성은 컴파일러가 제외할 파일 또는 폴더를 지정한다. 이 속성에 나열된 경로의 파일과 폴더는 컴파일러가 무시한다.</p>
<p>형식은 배열로 지정하며, 파일 경로나 패턴을 나열한다.</p>
<p><strong>예시</strong></p>
<pre><code class="language-js">{
  "exclude": [
    "node_modules",
    "**/*.spec.ts"
  ]
}</code></pre>
<p>위 예시는 node_modules 폴더와 모든 .spec.ts 확장자를 가진 파일을 제외하도록 지정한다.</p>
<hr />