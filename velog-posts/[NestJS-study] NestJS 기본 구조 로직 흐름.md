<h1 id="nestjs-study-nestjs-기본-구조-로직-흐름">[NestJS-study] NestJS 기본 구조 로직 흐름</h1>
<hr />

<blockquote>
<p>설치를 하고 <code>npm run start:dev</code> 로 하고 <code>await app.listen(3000);</code> 로 설정된 <code>http://localhost:3000/</code>  으로 들어가면 'Hello World!' 가 나온다. 해당 파일을 보고 어떻게 실행이 되는지 알아보자.</p>
</blockquote>
<hr />

<h2 id="src-폴더-구조">src 폴더 구조</h2>
<pre style="font-size: 25px;">
<b style="font-size: 30px;">src/</b>
|
├── <b>app.controller.spec.ts</b>
|
├── <b>app.controller.ts</b>
|
├── <b>app.module.ts</b>
|
├── <b>app.service.ts</b>
|
└── <b>main.ts</b>
</pre>

<hr />

<h2 id="maints">main.ts</h2>
<pre><code class="language-js">import { NestFactory } from '@nestjs/core'; 🔵 NestJS의 핵심 모듈인 NestFactory를 가져옵니다.
import { AppModule } from './app.module'; 🔵 애플리케이션의 루트 모듈인 AppModule을 가져옵니다.

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  await app.listen(3000); 🔵 애플리케이션이 3000번 포트에서 수신 대기하도록 설정합니다. 
}
bootstrap();</code></pre>
<h2 id="appmodulets">app.module.ts</h2>
<pre><code class="language-js">import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';

@Module({
  imports: [],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}</code></pre>
<h2 id="appcontrollerts">app.controller.ts</h2>
<pre><code class="language-js">import { Controller, Get } from '@nestjs/common';
import { AppService } from './app.service';

@Controller()
export class AppController {
  constructor(private readonly appService: AppService) {}

  @Get() 🔵 '/' 엔드포인트 
  getHello(): string {
    return this.appService.getHello(); 
  }
}</code></pre>
<h2 id="appservicets">app.service.ts</h2>
<pre><code class="language-js">import { Injectable } from '@nestjs/common';

@Injectable()
export class AppService {
  🔵 리턴 헬로 월드!
  getHello(): string {
    return 'Hello World!';
  }
}
</code></pre>
<hr />

<h2 id="expressjs-와-nestjs-비교">express.js 와 Nest.js 비교</h2>
<blockquote>
<p>express.js</p>
</blockquote>
<h3 id="serverjs-진입점">server.js 진입점</h3>
<pre><code class="language-js">app.use('/api/user', require('./routes/user')); 🔵 ex) 유저에 관한 =&gt; ./routes/user
app.use('/api/board', require('./routes/board')); 
app.use('/api/auth', require('./routes/auth'));</code></pre>
<h3 id="routesuserroutejs">routes/user.route.js</h3>
<pre><code class="language-js">router.get("/", userController.getUsers); 🔵 ex) 유저 ./routes/user =&gt; 모든유저를..
router.get("/:bandId", userController.getUser); 🔵 ex) 유저 ./routes/user =&gt; 특정유저를..
router.put("/", userController.updateUser);
router.delete("/", userController.deleteUser);</code></pre>
<h3 id="controllersusersjs">controllers/users.js</h3>
<pre><code class="language-js">🔵 ex) 모든유저를 가져오는 함수
export const getUsers = async(req, res) {
    let users = db.getUsers();
    return users
}</code></pre>
<blockquote>
<p>Nest.js</p>
</blockquote>
<h3 id="appmodulets-진입점">app.module.ts 진입점</h3>
<pre><code class="language-js">@Module({
    imports: [
        TypeOrmModule.forRoot(typeORMConfig),
          BoardsModule, 🔵 ex) 게시물에 관한 =&gt; board.controller.ts
          AuthModule,
          UserModule
    ],
})
export class AppModule {}</code></pre>
<h3 id="boardcontrollerts">board.controller.ts</h3>
<pre><code class="language-js">@Get() 🔵 엔드포인트 =&gt; board.service.ts
getAllBoards(
    @GetUser() user: User,
) : Promise&lt;Board[]&gt; {
  this.logger.verbose('User "${user.username} trying ... all boards`);
  return this.boardsService.getAllBoards(user);
}

@Get('/:id') 🔵 엔드포인트
getBoardById(
    @Param('id', ParseIntPipe) id: number,
      @GetUser() user: User,
) : Promise&lt;Board&gt; {
    return this.boardsService.getBoardById(id, user);
} </code></pre>
<h3 id="boardservicets">board.service.ts</h3>
<pre><code class="language-js">🔵 DB작업 , 연산 =&gt; return 

async getAllBoards(
    user: User,
) : Promise&lt;Board[]&gt; {
    const query = this.boardRepository.createQueryBuilder('board');

    query.where('board.userId = :userId', { userId: user.id})

    const boards = await query.getMany();
    return boards;
}</code></pre>
<hr />

<blockquote>
<p>출처: JhonAhn님의 유튜브 강의 NestJS를 참고하여 작성하였습니다.</p>
</blockquote>