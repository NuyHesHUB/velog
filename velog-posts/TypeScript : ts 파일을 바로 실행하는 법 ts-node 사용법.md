<hr />
<p>🕵️ 프로젝트에서 <code>index.ts</code>을 만들고 터미널에서 테스트를 해보고싶은데 js파일로 컴파일하고 나서 node로 다시 실행하는게 번거로워 한방에 실행시키는 방법을 알게되어 쓰게 되었다.</p>
<p><strong>현재</strong></p>
<p>1️⃣<code>npx tsc</code><br />2️⃣<code>node index.js</code>  </p>
<hr />
<h2 id="현재-폴더-구조">현재 폴더 구조</h2>
<pre><code>📂folder
├── index.ts
├── package.json
├── package-lock.json
└── node_modules</code></pre><hr />
<h3 id="먼저-tsconfig-파일-생성">먼저 tsconfig 파일 생성</h3>
<p><strong>명령어</strong></p>
<p><code>npx tsc --init</code></p>
<p><strong>🗂️ tsconfig.ts</strong></p>
<pre><code class="language-ts">{
  "compilerOptions": {
    "target": "ES2015",              
    "module": "commonjs",            
    "lib": ["ES2015", "DOM"],        
    "strict": true,
    "esModuleInterop": true,
    "moduleResolution": "node",
    "outDir": "./dist",
    "rootDir": "./",
    "skipLibCheck": true      
  },
  "include": ["**/*.ts"]
}</code></pre>
<p>여기서 <code>outDir</code>에서 <code>js컴파일</code> 파일이 생성된다.</p>
<pre><code class="language-ts">"outDir": "./dist",
"rootDir": "./",</code></pre>
<p>여기서 매번 <code>index.ts</code>에서 코드를 추가하고 node로 실행하려면 매번 컴파일을 하고 실행을 해야한다.</p>
<h2 id="ts-node-모듈">ts-node 모듈</h2>
<p><a href="https://www.npmjs.com/package/ts-node">[NPM] ts-node 링크</a></p>
<hr />
<h4 id="🕵️-ts-node란">🕵️ ts-node란?</h4>
<p>ts-node는 TypeScript 파일(.ts)을 컴파일 없이 바로 실행할 수 있게 해주는 Node.js 실행기입니다.</p>
<table>
<thead>
<tr>
<th>기능</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td>즉시 실행</td>
<td>.ts 파일을 따로 tsc로 컴파일하지 않고 바로 실행</td>
</tr>
<tr>
<td>빠른 개발</td>
<td>테스트할 때 빠르고 간편함 (console.log() 확인 등)</td>
</tr>
<tr>
<td>설정 연동</td>
<td>tsconfig.json 설정도 적용됨</td>
</tr>
</tbody></table>
<p><strong>설치 명령어</strong>
<code>npm i -g ts-node</code></p>
<p><strong>실행 방법</strong>
<code>ts-node index.ts</code></p>
<hr />