<hr />

<h3 id="nestjs를-사용해서-만드는-앱구조">NestJS를 사용해서 만드는 앱구조</h3>
<p>App Module안에 BoardModule과 AuthModule이 있으면 각 모듈안에 Controller Entity Service등이 있습니다. 그래서 우선 모듈이 무엇인지 알아보겠습니다.</p>
<blockquote>
<p><strong>앱 구조</strong></p>
</blockquote>
<pre><code>AppModule (root)
├── BoardModule
│   ├── BoardController
│   ├── BoardEntity
│   ├── BoardService
│   ├── BoardRepository
│   └── ValidationPipe
└── AuthModule
    ├── AuthController
    ├── UserEntity
    ├── AuthService
    ├── UserRepository
    └── JWT, Passport</code></pre><h3 id="nestjs-모듈이란">NestJS 모듈이란?</h3>
<p>모듈은 @Module() 데코레이터로 주석이 달린 클래스입니다. @Module () 데코레이터는 Nest가 애플리케이션 구조를 구성하는 데 사용하는 메타 데이터를 제공합니다. 각 응용 프로그램에는 하나 이상의 모듈이 있습니다. 루트 모듈은 Nest가 사용하는 시작점입니다.</p>
<p>모듈은 밀접하게 관련된 기능 집합으로 구성 요소를 구성하는 효과적인 방법입니다. 기능 별로 만들어서 구성합니다. ex) 유저 모듈, 주문 모듈...</p>
<p>같은 기능에 해당하는 것들은 하나의 모듈 폴더안에 넣어서 사용합니다. ex) UserController , UserService, UserEntity 다 같은 기능이므로 UserModule안에 넣습니다.</p>
<p>모듈은 기본적으로 싱글 톤이므로 여러 모듈간에 쉽게 공급자의 동일한 인스턴스를 공유할 수 있습니다.</p>
<h3 id="board-module-생성하기">Board Module 생성하기</h3>
<p><strong>초기 폴더구조</strong></p>
<pre><code>NEST-APP
├── dist
├── node_modules
├── src
│   ├── 🔵 app.controller.spec.ts
│   ├── 🔵 app.controller.ts
│   ├── 🔵 app.module.ts
│   ├── app.service.ts
│   └── main.ts
├── 🔵 test
├── .eslintrc.js
├── .gitignore
├── .prettierrc
├── nest-cli.json
├── package-lock.json
├── package.json
├── README.md
├── tsconfig.build.json
└── tsconfig.json</code></pre><p>새로운 모듈을 만들기 위해 초기 생성된 파일을 삭제한다.</p>
<ul>
<li>app.controller.spec.ts </li>
<li>app.controller.ts</li>
<li>app.service.ts</li>
<li>test 폴더</li>
</ul>
<h4 id="모듈-생성-명령어">모듈 생성 명령어</h4>
<p><code>nest g module '모듈이름'</code></p>
<p>명령어를 입력하면 해당 모듈 폴더가 생기고 모듈 파일이 생성된다.</p>
<pre><code class="language-js">import { Module } from '@nestjs/common';

@Module({})
export class BoardModule {}</code></pre>
<p>그리고 </p>
<p>app.module.ts 파일에 자동으로 추가가 된다.</p>
<pre><code class="language-js">import { Module } from '@nestjs/common';
import { BoardModule } from './board/board.module';

@Module({
  imports: [BoardModule],
})
export class AppModule {}
</code></pre>
<blockquote>
<p>출처: JhonAhn님의 유튜브 강의 NestJS를 참고하여 작성하였습니다.</p>
</blockquote>