<hr />
<p>🕵️ 프로젝트를 진행하면서 바쁘게 기능 구현에만 집중하다 보니 정작 유지보수나 큰 수정이 필요할 때마다 코드가 발목을 잡는 경우가 많았다. 
물론 <code>SOLID</code> 원칙을 항상 100% 지킬 수는 없지만 일정 수준이라도 원칙을 의식하며 작성한 코드가 더 읽기 쉽고 유지보수도 훨씬 수월하다는 걸 몸소 느꼈다. 이번 글에서는 이러한 경험을 바탕으로 객체지향 설계의 핵심인 <code>SOLID</code> 원칙에 대해 정리해보려고 한다.</p>
<hr />
<p>🌐 <a href="https://ko.wikipedia.org/wiki/SOLID_(%EA%B0%9D%EC%B2%B4_%EC%A7%80%ED%96%A5_%EC%84%A4%EA%B3%84)">SOLID (객체 지향 설계) 위키피디아</a></p>
<h2 id="solid-란">SOLID 란?</h2>
<blockquote>
<p>SOLID 란?</p>
</blockquote>
<p>컴퓨터 프로그래밍에서 <code>SOLID</code>란 로버트 C. 마틴이 2000년대 초반에 명명한 객체 지향 프로그래밍 및 설계의 다섯 가지 기본 원칙을 마이클 페더스가 두문자어 기억술로 소개한 것이다. 프로그래머가 시간이 지나도 유지 보수와 확장이 쉬운 시스템을 만들고자 할 때 이 원칙들을 함께 적용할 수 있다. <code>SOLID</code> 원칙들은 소프트웨어 작업에서 프로그래머가 소스 코드가 읽기 쉽고 확장하기 쉽게 될 때까지 소프트웨어 소스 코드를 리팩터링하여 코드 냄새를 제거하기 위해 적용할 수 있는 지침이다. 이 원칙들은 애자일 소프트웨어 개발과 적응적 소프트웨어 개발의 전반적 전략의 일부다.</p>
<hr />
<table>
<thead>
<tr>
<th align="center">문자</th>
<th>약어</th>
<th>개념</th>
</tr>
</thead>
<tbody><tr>
<td align="center"><strong>S</strong></td>
<td>SRP</td>
<td>단일 책임 원칙 (Single responsibility principle)<br /> ➡ 한 <strong>클래스</strong>는 하나의 책임만 가져야 한다.</td>
</tr>
<tr>
<td align="center"><strong>O</strong></td>
<td>OCP</td>
<td>개방-폐쇄 원칙 (Open/closed principle)<br /> ➡ 소프트웨어 요소는 확장에는 열려 있으나 변경에는 닫혀 있어야 한다.</td>
</tr>
<tr>
<td align="center"><strong>L</strong></td>
<td>LSP</td>
<td>리스코프 치환 원칙 (Liskov substitution principle)<br /> ➡ 프로그램의 <strong>객체</strong>는 프로그램의 정확성을 깨뜨리지 않으면서 하위 타입의 인스턴스로 바꿀 수 있어야 한다.</td>
</tr>
<tr>
<td align="center"><strong>I</strong></td>
<td>ISP</td>
<td>인터페이스 분리 원칙 (Interface segregation principle)<br /> ➡ 특정 클라이언트를 위한 인터페이스 여러 개가 범용 인터페이스 하나보다 낫다.</td>
</tr>
<tr>
<td align="center"><strong>D</strong></td>
<td>DIP</td>
<td>의존관계 역전 원칙 (Dependency inversion principle)<br /> ➡ 프로그래머는 &quot;추상화에 의존해야지, 구체화에 의존하면 안된다.&quot; 의존성 주입은 이 원칙을 따르는 방법 중 하나다.</td>
</tr>
</tbody></table>
<hr />
<h2 id="간단한-예시와-설명">간단한 예시와 설명</h2>
<h3 id="🔵-s---srp-single-responsibility-principle">🔵 S - SRP (Single Responsibility Principle)</h3>
<blockquote>
<p><strong>단일 책임 원칙</strong> : 한 클래스(또는 모듈)는 하나의 책임만 가져야 한다.</p>
</blockquote>
<pre><code class="language-ts">❌ 위반된 예시 : 유저 데이터를 가져오고, UI를 업데이트

class UserManager {
    getUserData() // API 호출
    renderUserProfile() // DOM 조작
}

✅ 개선된 예시

class UserService {
    getUserData() // API 호출
}

class UserProfileUI {
    renderUserProfile() // DOM 조작
}
</code></pre>
<p>🕵️ <strong>UserService</strong>는 데이터만 처리하고 <strong>UserProfileUI</strong>는 UI만 담당한다. 하나의 책임만 맡는다.</p>
<hr />
<h3 id="🔵-o---ocp-openclosed-principle">🔵 O - OCP (Open/Closed Principle)</h3>
<blockquote>
<p><strong>개방-폐쇄 원칙</strong> : 확장에는 열려있고 변경에는 닫혀 있어야 한다.</p>
</blockquote>
<pre><code class="language-ts">❌ 나쁜 설계: 새 타입 추가할 때마다 조건문 수정 필요

function paymentMethod(method: string) {
  if (method === 'card') {
    // 카드 결제 처리
  } else if (method === 'mobile') {
    // 모바일 결제 처리
  }
}

✅ 좋은 설계: 새로운 방식은 확장만 하면 됨

interface PaymentStrategy } {
    pay(amount: number): void;
}

class CardPayment implements PaymentStrategy {
    pay(ammount: number) {
        // 카드 결제 처리
    }
}

class MobilePayment implements PaymentStrategy {
    pay(amount: number) {
        // 모바일 결제 처리
    }
}

function processPayment(strategy: PaymentStrategy, ammount: number) {
    strategy.pay(amount);
}</code></pre>
<p>🕵️ 조건문을 늘리는 대신 <strong>새 클래스만 추가하면 되므로</strong> 기존 코드 수정 없이 확장 가능하다.</p>
<hr />
<h3 id="🔵-i---isp-interface-segregation-principle">🔵 I - ISP (Interface Segregation Principle)</h3>
<blockquote>
<p><strong>인터페이스 분리 원칙</strong> : 클라이언트는 자신이 사용하지 않는 메서드에 의존하지 않아야 한다</p>
</blockquote>
<pre><code class="language-ts">❌ 나쁜 설계: 하나의 인터페이스가 너무 많은 역할

interface Worker {
    work(): void;
      eat(): void;
}

class Robot implements Worker {
    work() { console.log('Robot 일함') }
      eat() { throw new Error('Robot은 안 먹음') } ❌
}

✅ 좋은 설계: 인터페이스를 역할별로 분리

interface Workable {
    work(): void;
}

interface Eatable {
    eat(): void;
}

class Human implements Workable, Eatable {
    work(): { console.log('Human 일함')}
    eat(): { console.log('Human 먹음')}
}

class Robot implements Workable {
    work(): { console.log('Robot 일함') }
}</code></pre>
<p>🕵️ 사용하는 기능만 의존하게 만들면 변경에 안전하고 코드도 유연해진다.</p>
<hr />
<h3 id="🔵-d---dip-dependency-inversion-principle">🔵 D - DIP (Dependency Inversion Principle)</h3>
<blockquote>
<p><strong>의존 역전 원칙</strong> : 고수준 모듈은 저수준 모듈에 의존하면 안 되고 추상화에 의존해야 한다.</p>
</blockquote>
<pre><code class="language-ts">❌ 나쁜 설계: 직접 클래스에 의존

class LightBulb {
    turnOn() { console.log('불 켜짐') }
}

class Switch {
    constructor (private bulb: LightBulb) {}

      operate() {
        this.bulb.turnOn(); ❌ 구체 클래스에 직접 의존
    }
}

✅ 좋은 설계: 인터페이스 도입으로 DIP 적용

interface Switchable {
    turnOn(): void;
}

class LightBulb implements Switchable {
    trurnOn() { console.log('전구 켜짐) }
}

class Fan implements Switchable {
    trurnOn() { console.log('선풍기 켜짐) }
}

class Switch {
    constructor (private device: Switchable) {}         
    operate() {
        this.device.turnOn(); ✅ 추상에 의존
    }
}
</code></pre>
<p>🕵️ 의존성 주입을 통해 다양한 장치를 연결할 수 있는 유연한 구조를 만듭니다.</p>
<hr />
<h2 id="정리">정리</h2>
<table>
<thead>
<tr>
<th>원칙</th>
<th>요약</th>
<th>TypeScript 설계 포인트</th>
</tr>
</thead>
<tbody><tr>
<td>SRO</td>
<td>하나의 책임만 가져라</td>
<td><strong>UI</strong>, <strong>비즈니스 로직</strong>, <strong>API</strong> 분리</td>
</tr>
<tr>
<td>OCP</td>
<td>확장에는 열려 있고 변경에는 닫혀라</td>
<td><strong>Strategy</strong>, <strong>Factory</strong> 패턴 사용</td>
</tr>
<tr>
<td>LCP</td>
<td>하위 타입은 상위 타입을 대체할 수 있어야 한다.</td>
<td>잘못된 상속 피하기</td>
</tr>
<tr>
<td>ISP</td>
<td>인터페이스는 작게 나눠라</td>
<td>역할 기반 인터페이스 분리</td>
</tr>
<tr>
<td>DIP</td>
<td>추상에 의존하고 구현에 의존하지 않는다</td>
<td>인터페이스 + 의존성 주입</td>
</tr>
</tbody></table>
<hr />