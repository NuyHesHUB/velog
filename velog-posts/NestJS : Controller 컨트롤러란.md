<hr />

<h3 id="controller-란">Controller 란?</h3>
<p>컨트롤러는 들어오는 요청을 처리하고 클라이언트에 응답을 반환합니다.</p>
<p>컨트롤러는 @Controller로 데코레이터로 클래스를 데코레이션하여 정의됩니다.</p>
<pre><code class="language-js">@Controller('/boards')
export class BoardsController {}</code></pre>
<p>데코레이터는 인자를 Controller에 의해서 처리되는 경로로 받습니다.</p>
<hr />

<h3 id="handler-란">Handler 란?</h3>
<p>핸들러는 @Get , @Post , @Delete 등과 같은 데코레이터로 장식 된 컨트롤러 클래스 내의 단순한 메서드입니다.</p>
<pre><code class="language-js">@Controller('/boards')
export class BoardsController {
    @Get()
    getBoards(): string {
        return 'This action returns all boards';
    }
}...</code></pre>
<hr />

<h3 id="controller-생성하기">Controller 생성하기</h3>
<h4 id="controllers-생성하기-명령어">Controllers 생성하기 명령어</h4>
<p><code>nest g controller '컨트롤러 이름' --no-spec</code></p>
<ul>
<li>--no-spec : 테스트를 위한 소스 코드생성을 하지 않는다는 의미입니다.</li>
</ul>
<p>board.module에 컨트롤러가 추가가 됩니다.</p>
<pre><code class="language-js">// board.module.ts

import { Module } from '@nestjs/common';
import { BoardController } from './board.controller';

@Module({
      controllers: [BoardController],  🔵 추가됨 🔵
})
export class BoardModule {}
</code></pre>
<pre><code class="language-js">// board.controller.ts

import { Controller } from '@nestjs/common';

@Controller('board')
export class BoardController {}
</code></pre>
<hr />

<p><strong>CLI로 명령어 입력시 Controller 만드는 순서</strong></p>
<ol>
<li>cli는 먼저 boards(만든 모듈, 컨트롤러) 폴더를 찾습니다.</li>
<li>boards 폴더 안에 controller 파일 생성</li>
<li>boards 폴더 안에 module 파일 찾기</li>
<li>module 파일 안에 controller 넣어주기</li>
</ol>
<hr />

<blockquote>
<p>출처: JhonAhn님의 유튜브 강의 NestJS를 참고하여 작성하였습니다.</p>
</blockquote>