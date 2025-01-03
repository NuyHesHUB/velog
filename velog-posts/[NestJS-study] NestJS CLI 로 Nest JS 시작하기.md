<h1 id="nestjs-study-nestjs-cli-로-nest-js-시작하기">[NestJS-study] NestJS CLI 로 Nest JS 시작하기</h1>
<hr />

<h2 id="nest-js-cli-설치하기">Nest JS CLI 설치하기</h2>
<blockquote>
<p>NestJS를 이용해서 프로젝트를 시작할 때 Nest CLI를 이용하면 간단히 프로젝트를 시작할 수 있습니다. 
Nest CLI를 이용해서 아래의 명령어를 작성하면 새 프로젝트 디렉토리가 생성되고 초기 핵심 Nest 파일 및 지원 모듈로 디렉토리가 채워져 프로젝트의 기존 기본 구조가 생성됩니다.</p>
</blockquote>
<p><code>$ npm i -g @nestjs/cli</code>
<code>$ nest new [project-name]</code></p>
<p>이렇게 한 후 NestJS가 잘 설치되어있는지 보려면 "nest --version" 명령어를 이용해서 확인하면 된다.</p>
<p><img alt="" src="https://velog.velcdn.com/images/nuyhes/post/85d2fc4c-9a9d-46b6-8102-52acf479db52/image.png" /></p>
<blockquote>
<p>설치 완료</p>
</blockquote>
<p><img alt="" src="https://velog.velcdn.com/images/nuyhes/post/d98a875f-2330-4c8a-be7c-7e006b4cb8b6/image.png" /></p>
<hr />

<h2 id="프로젝트-생성">프로젝트 생성</h2>
<p>IDE 터미널에서 아래의 명령어로 프로젝트를 생성한다.</p>
<p><code>$ nest new [project-name]</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/nuyhes/post/a3358c13-7126-466c-b99f-c38c079d0d17/image.png" />
<img alt="" src="https://velog.velcdn.com/images/nuyhes/post/0b58b66a-e3af-48c5-aec6-08648be81011/image.png" /></p>
<blockquote>
<p>폴더 구조</p>
</blockquote>
<p><img alt="" src="https://velog.velcdn.com/images/nuyhes/post/9ab2ae1a-12e4-47f7-a64c-d61e47730a2a/image.png" /></p>
<hr />

<pre style="font-size: 25px;">
<b style="font-size: 30px;">NestJS Project/</b>
|
├── <b>eslint.js</b> - ESLint 설정 파일
|
├── <b>prettierrc</b> - Prettier 설정 파일 : 코드 포맷터 역할
|
├── <b>nest-cli.json</b> - Nest CLI 설정 파일
|
├── <b>tsconfig.json</b> - TypeScript 컴파일러 설정 파일
|
├── <b>tsconfig.build.json</b> - 빌드를 위한 TypeScript 설정 파일
|
├── <b>package.json</b> - 프로젝트의 의존성 및 스크립트를 정의하는 파일
|
└── <b>src</b>
   |
   ├── <b>main.ts</b> - 애플리케이션의 진입점
   |
   └── <b>app.module.ts</b> - 루트 모듈 파일
</pre>

<hr />

<blockquote>
<p>출처: JhonAhn님의 유튜브 강의 NestJS를 참고하여 작성하였습니다.</p>
</blockquote>