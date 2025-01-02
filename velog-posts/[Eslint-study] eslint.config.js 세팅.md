<h1 id="eslint-study-eslintconfigjs-세팅">[Eslint-study] eslint.config.js 세팅</h1>
<hr />

<p>기존에는 <code>eslintrc</code> 로 세팅을 하다가 <code>eslint.config.js</code> 로 세팅하는 방법을 알아보기 위해 작성하였다. </p>
<h3 id="strongeslintrcstrong-와-strongeslintconfigjsstrong-의-차이점"><strong>eslintrc</strong> 와 <strong>eslint.config.js</strong> 의 차이점</h3>
<table>
<thead>
<tr>
<th><strong>항목</strong></th>
<th><strong><code>.eslintrc</code></strong></th>
<th><strong><code>eslint.config.js</code></strong></th>
</tr>
</thead>
<tbody><tr>
<td><strong>도입 시기</strong></td>
<td>전통적인 방식</td>
<td>ESLint 8.0 이후 Flat Config에서 사용</td>
</tr>
<tr>
<td><strong>파일 포맷</strong></td>
<td>JSON, YAML, JS</td>
<td>JavaScript (JS)</td>
</tr>
<tr>
<td><strong>동적 설정 가능 여부</strong></td>
<td>제한적 (JS 사용 시 일부 가능)</td>
<td>완전한 JavaScript 지원</td>
</tr>
<tr>
<td><strong>사용성</strong></td>
<td>간단하고 직관적</td>
<td>더 복잡하지만 유연함</td>
</tr>
<tr>
<td><strong>성능</strong></td>
<td>기존 방식, 성능이 최적화되지 않음</td>
<td>더 나은 성능 제공</td>
</tr>
</tbody></table>
<h4 id="언제-무엇을-써야-할까">언제 무엇을 써야 할까?</h4>
<p><code>.eslintrc</code>: 기존 프로젝트에서 사용하는 경우 계속 사용할 수 있으며, 간단한 설정에는 충분합니다.</p>
<p><code>eslint.config.js</code>: 새로운 프로젝트에서 더 복잡하거나 동적인 설정이 필요할 경우 사용을 권장합니다. Flat Config를 통해 ESLint의 최신 기능을 활용할 수 있습니다.</p>
<hr />

<h3 id="eslintconfigjs-기본세팅">eslint.config.js 기본세팅</h3>
<pre><code class="language-js">import js from '@eslint/js'
import globals from 'globals'
import reactHooks from 'eslint-plugin-react-hooks'
import reactRefresh from 'eslint-plugin-react-refresh'
import tseslint from 'typescript-eslint'

export default tseslint.config(
  { ignores: ['dist'] },
  {
    extends: [js.configs.recommended, ...tseslint.configs.recommended],
    files: ['**/*.{ts,tsx}'],
    languageOptions: {
      ecmaVersion: 2020,
      globals: globals.browser,
    },
    plugins: {
      'react-hooks': reactHooks,
      'react-refresh': reactRefresh,
    },
    rules: {
      ...reactHooks.configs.recommended.rules,

      'react-refresh/only-export-components': [
        'warn',
        { allowConstantExport: true },
      ],
    },
  },
)</code></pre>
<hr />

<h3 id="import">import</h3>
<pre><code class="language-js">import js from '@eslint/js'
import globals from 'globals'
import reactHooks from 'eslint-plugin-react-hooks'
import reactRefresh from 'eslint-plugin-react-refresh'
import tseslint from 'typescript-eslint'</code></pre>
<ul>
<li><p><code>@eslint/js</code>: ESLint 기본 JavaScript 설정 패키지입니다. JavaScript 파일에 대한 추천 구성(js.configs.recommended)을 제공합니다.</p>
</li>
<li><p><code>globals</code>: 전역 변수 설정을 위한 패키지입니다. 예: 브라우저 환경(globals.browser)에 적합한 전역 변수 정의.</p>
</li>
<li><p><code>eslint-plugin-react-hooks</code>: React의 Hooks 규칙을 위한 ESLint 플러그인입니다. Hook의 올바른 사용을 보장합니다.</p>
</li>
<li><p><code>eslint-plugin-react-refresh</code>: React Fast Refresh와 관련된 규칙을 제공하는 ESLint 플러그인입니다. 개발 환경에서 핫 리로딩을 개선하는 데 사용됩니다.</p>
</li>
<li><p><code>typescript-eslint</code>: TypeScript 파일에 대한 ESLint 지원을 제공하는 패키지입니다.</p>
</li>
</ul>
<hr />

<h3 id="주요구성">주요구성</h3>
<h4 id="ignores">ignores</h4>
<pre><code class="language-js">{ ignores: ['dist'] },</code></pre>
<p>디렉토리의 파일을 ESLint 검사에서 제외합니다. 주로 빌드 출력 파일을 대상으로 합니다.</p>
<hr />

<h4 id="extends">extends</h4>
<pre><code class="language-js"> extends: [js.configs.recommended, ...tseslint.configs.recommended],</code></pre>
<p>ESLint의 기본 추천 규칙과 TypeScript ESLint의 추천 규칙을 확장합니다.</p>
<ul>
<li><p><code>js.configs.recommended</code>: ESLint 기본 JavaScript 규칙 집합.</p>
</li>
<li><p><code>tseslint.configs.recommended</code>: TypeScript 코드에 적합한 추천 규칙 집합.</p>
</li>
</ul>
<h4 id="files">files</h4>
<pre><code class="language-js">files: ['**/*.{ts,tsx}']</code></pre>
<p>ESLint가 검사할 파일 패턴을 정의합니다.</p>
<p><em>*/</em>.{ts,tsx}: 모든 디렉토리 내의 .ts 및 .tsx 파일을 대상으로 합니다.</p>
<hr />

<h4 id="languageoptions">languageOptions</h4>
<pre><code class="language-js">languageOptions: {
  ecmaVersion: 2020,
  globals: globals.browser,
}</code></pre>
<ul>
<li><p><code>ecmaVersion</code>: 2020: ECMAScript 2020을 지원합니다.</p>
</li>
<li><p><code>globals</code>: globals.browser: 브라우저 환경에서 사용되는 전역 변수(window, document 등)를 허용합니다.</p>
</li>
</ul>
<hr />

<h4 id="plugins">plugins</h4>
<pre><code class="language-js">plugins: {
  'react-hooks': reactHooks,
  'react-refresh': reactRefresh,
}</code></pre>
<ul>
<li><code>react-hooks</code>: React Hooks의 규칙을 검사합니다.</li>
<li><code>react-refresh</code>: React Fast Refresh 관련 규칙을 검사합니다.</li>
</ul>
<hr />

<h4 id="rules">rules</h4>
<pre><code class="language-js">rules: {
  ...reactHooks.configs.recommended.rules,

  'react-refresh/only-export-components': [
    'warn',
    { allowConstantExport: true },
  ],
}</code></pre>
<ul>
<li><code>...reactHooks.configs.recommended.rules</code>: React Hooks의 추천 규칙을 적용합니다.</li>
</ul>
<p>예: </p>
<p>react-hooks/rules-of-hooks(Hook의 규칙 준수) 및 react-hooks/exhaustive-deps(의존성 배열 검사) 규칙.
react-refresh/only-export-components: React Refresh와 관련된 규칙입니다.</p>
<p>설정:</p>
<p>warn: 이 규칙이 위반되면 경고를 표시합니다.
allowConstantExport: true: 상수를 기본 내보내기로 설정하는 것을 허용합니다.
예: export default MyComponent는 규칙 위반이 아니게 설정됩니다.</p>
<hr />

<h3 id="🕵️-터미널에서-npx-eslint-로-하면-정상적으로-에러를-찾아서-검사를-하는데-에디터에서-에러-표시가-나지-않았다">🕵️ 터미널에서 <code>npx eslint .</code>로 하면 정상적으로 에러를 찾아서 검사를 하는데 에디터에서 에러 표시가 나지 않았다.</h3>
<p>1️⃣ <code>Ctrl</code> + <code>Shift</code> + <code>P</code>  </p>
<p>2️⃣ <code>&gt;Preferences: Open User Settings (JSON)</code></p>
<p>3️⃣ 현재 내 설정..</p>
<pre><code class="language-scss">{
  "editor.stickyScroll.enabled": false,
  "git.autofetch": true,
  "diffEditor.ignoreTrimWhitespace": false,
  "github.copilot.editor.enableAutoCompletions": true,
  "[vue]": {
    "editor.defaultFormatter": "Vue.volar"
  },
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "github.copilot.advanced": {},
  "sonarlint.rules": {
    "Web:AvoidCommentedOutCodeCheck": {
      "level": "off"
    },
    "Web:S6850": {
      "level": "off"
    }
  },
  "git.openRepositoryInParentFolders": "never",
  "eslint.execArgv": null,
  "editor.codeActionsOnSave": {
    "source.fixAll.eslint": "explicit"
  }
}
</code></pre>
<p>4️⃣ "source.fixAll.eslint": "explicit" 는 true 로 바꾸고</p>
<pre><code class="language-scss">"editor.codeActionsOnSave": {
    "source.fixAll.eslint": true
  },</code></pre>
<p>이 부분을 넣어준다.</p>
<pre><code class="language-scss">"eslint.experimental.useFlatConfig": true,
  "eslint.validate": [
    "javascript",
    "javascriptreact",
    "typescript",
    "typescriptreact",
    "vue"
  ],
  "[typescriptreact]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "editor.formatOnSave": true</code></pre>
<ul>
<li><p><code>eslint.experimental.useFlatConfig</code>: Flat Config를 사용하는 경우 필요하다. 설정이 없으면 VS Code가 eslint.config.js를 인식하지 못할 수 있다.</p>
</li>
<li><p><code>eslint.validate</code>: ESLint가 .tsx 파일을 검사할 수 있도록 "typescriptreact"를 명시적으로 포함한다.</p>
</li>
<li><p><code>[typescriptreact]의 기본 포맷터</code>: TypeScript React 파일(.tsx)의 기본 포맷터를 Prettier로 설정한다. 하지만 ESLint의 규칙을 우선 적용하도록 source.fixAll.eslint를 활성화한다.</p>
</li>
<li><p><code>editor.formatOnSave</code>: 저장 시 자동 포맷팅을 활성화합니다.</p>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/nuyhes/post/8a7399c5-8e7e-4bdb-b2f2-1487df93f3c9/image.png" /></p>
<hr />

<h4 id="현재-적용된-eslintconfigjs">현재 적용된 eslint.config.js</h4>
<pre><code class="language-js">import js from '@eslint/js'
import globals from 'globals'
import react from 'eslint-plugin-react'
import reactHooks from 'eslint-plugin-react-hooks'
import reactRefresh from 'eslint-plugin-react-refresh'
import jsxA11y from 'eslint-plugin-jsx-a11y'
import importPlugin from 'eslint-plugin-import'
import eslintPlugin from '@typescript-eslint/eslint-plugin'
import parser from '@typescript-eslint/parser'

export default [
  {
    ignores: [
      'dist',
      'node_modules',
      'lib',
      'idea',
    ],
  },
  {
    files: ['**/*.{ts,tsx}'],
    languageOptions: {
      ecmaVersion: 2020,
      globals: globals.browser,
      parser: parser
    },
    plugins: {
      '@typescript-eslint': eslintPlugin,
      'react': react,
      'react-hooks': reactHooks,
      'react-refresh': reactRefresh,
      'jsx-a11y': jsxA11y,
      'import': importPlugin,
    },
    settings: {
      react: {
        version: 'detect',
      },
    },
    rules: {
      ...js.configs.recommended.rules,
      ...eslintPlugin.configs.recommended.rules,
      ...react.configs.recommended.rules,
      ...reactHooks.configs.recommended.rules,
      ...jsxA11y.configs.recommended.rules,
      'quotes': ['error', 'single'],
      "no-unused-vars": "off",

      'react/react-in-jsx-scope': 'off', 
      'react-refresh/only-export-components': [
        'warn',
        { allowConstantExport: true },
      ],
      'indent': ['error', 'tab', {
        'SwitchCase': 1,
        'ignoredNodes': ['TemplateLiteral'],
      }],
      'react/jsx-indent': ['error', 'tab'], 
      'react/jsx-indent-props': ['error', 'tab'],
    },
  },
]</code></pre>
<hr />