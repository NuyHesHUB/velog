<hr />
<h3 id="🕵️-typescript-클래스에서-생성자-한-줄로-멤버-변수-선언하기-parameter-properties">🕵️ TypeScript 클래스에서 생성자 한 줄로 멤버 변수 선언하기 (Parameter Properties)</h3>
<pre><code class="language-ts">abstract class AC {
  name: string;

  constructor(name: string) {
    this.name = name;
  }
}</code></pre>
<p>이런 방식은 명확하지만 변수 선언과 할당이 중복되는 느낌이 있다.</p>
<hr />
<h3 id="typescript에서는-이걸-한-줄로-줄일-수-있다">TypeScript에서는 이걸 한 줄로 줄일 수 있다.</h3>
<pre><code class="language-ts">abstract class AC {
  constructor(public name: string) {}
}</code></pre>
<blockquote>
<p>이게 가능한 이유는?</p>
</blockquote>
<p>이건 <code>파라미터 프로퍼티(Parameter Properties)</code> 라는 TypeScript의 기능 덕분이다.</p>
<p>public, private, readonly, protected 등의 접근 제어자를 생성자 매개변수 앞에 붙이면</p>
<p>TypeScript는 해당 매개변수를 자동으로 클래스의 멤버 변수로 선언하고 초기화한다.</p>
<blockquote>
<p>위 코드는 다음 두 단계를 자동으로 수행하는 것과 같다:</p>
</blockquote>
<ol>
<li><p>name: string 멤버 변수 선언</p>
</li>
<li><p>this.name = name 초기화</p>
</li>
</ol>
<hr />
<h3 id="접근-제어자에-따라-이렇게도-가능">접근 제어자에 따라 이렇게도 가능</h3>
<pre><code class="language-ts">class User {
  constructor(
    private id: number,
    public name: string,
    readonly role: string
  ) {}

  getId() {
    return this.id;
  }
}</code></pre>
<ul>
<li><p>id: 외부에서 접근 불가 (private)</p>
</li>
<li><p>name: 외부에서 자유롭게 접근 가능 (public)</p>
</li>
<li><p>role: 외부에서 읽기만 가능 (readonly)</p>
</li>
</ul>
<blockquote>
<p>언제 쓰면 좋을까?</p>
</blockquote>
<ol>
<li>생성자에서 멤버 변수를 단순히 초기화만 하는 경우</li>
<li>코드 라인을 줄이고, 가독성을 높이고 싶을 때</li>
<li>멤버 변수 선언이 중복될 때</li>
</ol>