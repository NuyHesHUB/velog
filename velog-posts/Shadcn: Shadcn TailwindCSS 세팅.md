<h2 id="shadcn이란">Shadcn이란?</h2>
<p><a href="https://ui.shadcn.com/">🌐shadcn/ui</a></p>
<p>기본적인 UI 라이브러리와 <code>Shadcn</code>의 큰 차이는 코드가 어디에 저장되는가? 이다.</p>
<h3 id="차이점">차이점</h3>
<p><strong>일반 라이브러리(MUI, AntDesign 등)</strong></p>
<ul>
<li><code>node_modules</code> 안에 들어있음</li>
<li>사용자는 그저 <code>import { Button } from 'mui'</code>로 불러 쓸 뿐 버튼 내부의 로직이나 스타일을 직접 수정하려면 복잡한 방법을 거쳐야한다.</li>
</ul>
<p><strong>Shadcn</strong></p>
<ul>
<li><code>npx shadcn add button</code>을 입력하면 버튼 전체 소스 코드가 내 프로젝트의 예) <code>src/components/ui/button.tsx</code>에 파일로 복사가 되어 들어온다.</li>
<li>이렇게 복사가 된 파일은 해당 프로젝트의 소유권이 된다. 직접 커스텀 및 조작이 용이하다.</li>
</ul>
<hr />
<h3 id="기능과-디자인의-분리">기능과 디자인의 분리</h3>
<p>&quot;그럼 코드를 일일이 다 짜주는 건가?&quot; 싶겠지만 shadcn은 바닥부터 만드는 건 아니다. <strong>Radix UI</strong>라는 '뼈대(Headless UI)' 위에 <strong>Tailwind CSS</strong>라는 '스타일'을 붙여놓은 상태이다.</p>
<ul>
<li><strong>Radix UI (뼈대):</strong> 접근성(Accessibility), 키보드 조작, 팝업 열고 닫기 같은 <strong>복잡한 기능</strong> 담당 (눈에 안 보임).</li>
<li><strong>Tailwind CSS (살):</strong> 디자인과 스타일링 담당.</li>
<li><strong>shadcn (조합기):</strong> 이 둘을 조합해서 <strong>&quot;바로 쓸 수 있는 코드 파일&quot;</strong> 형태로 우리에게 전달해주는 역할을 한다.</li>
</ul>
<hr />
<h2 id="프로젝트-생성-및-tailwind-css-설치">프로젝트 생성 및 Tailwind CSS 설치</h2>
<p><strong>설치</strong></p>
<pre><code># Tailwind CSS 및 관련 라이브러리 설치
npm install -D tailwindcss postcss autoperfixer</code></pre><p><strong>tailwind.config.js 생성</strong></p>
<pre><code class="language-shell"># tailwind.config.js 생성
npx tailwindcss init -p 

또는 

npx tailwindcss init</code></pre>
<hr />
<blockquote>
<p>🕵️ 명령어 <strong><code>-p</code></strong>라는 옵션은?</p>
</blockquote>
<ul>
<li><p><code>npx tailwindcss init</code>: <code>tailwind.config.js</code>만 생성</p>
</li>
<li><p><strong><code>npx tailwindcss init -p</code></strong>: <code>tailwind.config.js</code>와 함께 <strong><code>postcss.config.js</code>를 세트로 생성</strong></p>
</li>
</ul>
<p><strong>Q: PostCSS랑 Autoprefixer는 꼭 설치해야 되나?</strong> 
<strong>A:</strong> <code>Tailwind</code>가 작성한 클래스명을 실제 CSS로 변환하고 모든 브라우저에서 디자인이 유지되도록 접두사를 붙여주는 핵심 일꾼들이다. <code>init -p</code> 명령어로 한 번에 생성하는 걸 권장</p>
<hr />
<blockquote>
<p>🕵️ TailwindCSS PostCSS Autoprefixer 란?</p>
</blockquote>
<p><strong>Tailwind CSS</strong></p>
<ul>
<li>유틸리티 퍼스트(utility-first) CSS 프레임워크</li>
</ul>
<pre><code class="language-html"># 무슨기능?
# 미리 만들어진 작은 CSS 클래스들을 조합해서 UI를 만든다
# 직접 CSS 길게 작성하지 않고 클래스만으로 스타일을 구성

&lt;div class=&quot;bg-blue-500 text-white p-4 rounded-lg&quot;&gt;
  버튼
&lt;/div&gt;

- `bg-blue-500` → 배경 파랑
- `text-white` → 글자 흰색
- `p-4` → 패딩
- `rounded-lg` → 둥근 모서리</code></pre>
<p><strong>PostCSS</strong></p>
<ul>
<li>CSS를 변환해주는 <strong>도구(플랫폼)</strong></li>
</ul>
<pre><code class="language-html"># 무슨기능?
# CSS에 여러 플러그인을 적용해 기능을 확장
# 자체적으로 스타일을 제공하는 게 아니라 플러그인을 통해 CSS를 가공하는 역할

- 최신 CSS 문법을 구형 브라우저용으로 변환
- 자동으로 prefix 추가
- CSS 압축
- Tailwind 처리</code></pre>
<p><strong>Autoprefixer</strong></p>
<ul>
<li>PostCSS 플러그인 중 하나 브라우저 호환성을 위해 CSS에 자동으로 vendor prefix를 붙여준다.</li>
</ul>
<pre><code class="language-css"># 작성 코드
display: flex;

# Autoprefixer 적용 후
display: -webkit-box;
display: -ms-flexbox;
display: flex;</code></pre>
<p>Tailwind CSS  →  PostCSS 위에서 동작
Autoprefixer  →  PostCSS 플러그인
PostCSS       →  CSS 가공 엔진</p>
<hr />
<h3 id="필수-환경-설정">필수 환경 설정</h3>
<p><code>shadcn</code>은 내 프로젝트의 파일을 직접 수정하기 때문에, 경로 별칭(Alias) 설정을 반드시 해줘야 한다.</p>
<blockquote>
<p>절대 경로 설정</p>
</blockquote>
<h5 id="1-tsconfigjson-수정">1. tsconfig.json 수정</h5>
<p>경로를 <code>@/</code>로 시작할 수 있도록 <code>compilerOptions</code> 안에 추가한다.</p>
<pre><code class="language-json">{
  &quot;compilerOptions&quot;: {
    &quot;baseUrl&quot;: &quot;.&quot;,
    &quot;paths&quot;: {
      &quot;@/*&quot;: [&quot;./src/*&quot;]
    }
  }
}</code></pre>
<h5 id="2-viteconfigts-수정">2. vite.config.ts 수정</h5>
<p>Vite가 <code>@</code> 기호를 실제 <code>./src</code> 폴더로 인식하게 설정 (에러 방지를 위해 <code>@types/node</code>를 먼저 설치: <code>npm i -D @types/node</code>)</p>
<pre><code class="language-json">export default defineConfig({
    plugins: [react()], 
    resolve: { 
        alias: { 
            &quot;@&quot;: path.resolve(__dirname, &quot;./src&quot;), 
        }, 
    }, 
})</code></pre>
<h5 id="3-tailwindconfigjs-수정">3. tailwind.config.js 수정</h5>
<p>어떤 파일에서 Tailwind 클래스를 사용할지 명시</p>
<pre><code class="language-json">/** @type {import('tailwindcss').Config} */ 
export default { 
    content: [&quot;./index.html&quot;, &quot;./src/**/*.{ts,tsx,js,jsx}&quot;], 
    theme: { extend: {} }, 
    plugins: [],</code></pre>
<h5 id="4-postcssconfigjs">4. postcss.config.js</h5>
<p><code>Tailwind</code>가 작성한 클래스명을 실제 CSS로 변환하고 모든 브라우저에서 디자인이 유지되도록 하는 설정 부분 체크만 !</p>
<pre><code class="language-json">export default {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}</code></pre>
<h5 id="5-tailwind-css의-엔진-켜기">5. Tailwind CSS의 엔진 켜기</h5>
<p>프로젝트의 <strong>가장 최상위 엔트리 CSS(또는 SCSS) 파일</strong>에 넣어야 한다.</p>
<ul>
<li><strong>Vite 프로젝트 기준:</strong> 보통 <code>src/index.css</code> 또는 <code>src/main.scss</code> 파일</li>
</ul>
<blockquote>
<p>🕵️ <strong>중요한 기준:</strong> <code>main.tsx</code> 또는 <code>App.tsx</code>에서 <strong><code>import &quot;./index.css&quot;</code></strong>와 같이 직접적으로 불러오고 있는 파일에 적용</p>
</blockquote>
<pre><code class="language-css">@tailwind base;
@tailwind components;
@tailwind utilities;</code></pre>
<ul>
<li><strong>base:</strong> 브라우저마다 제각각인 기본 여백 등을 초기화 이게 제일 밑바닥에 깔려야 함</li>
<li><strong>components:</strong> 버튼이나 카드 같은 덩어리 스타일이 들어감</li>
<li><strong>utilities:</strong> <code>mt-4</code>, <code>text-red-500</code> 처럼 아주 구체적인 속성들이다. 가장 마지막에 와야 내가 클래스로 준 속성이 다른 스타일을 <strong>덮어쓰기(Override)</strong> 할 수 있다.</li>
</ul>
<h5 id="6-shadcnui-초기화-init">6. shadcn/ui 초기화 (Init)</h5>
<p>아래 명령어를 입력하면 <code>shadcn</code>이 필요한 유틸리티 파일들을 생성</p>
<p><code>npx shadcn@latest init</code></p>
<p><code>Base color: Which color would you like to use as the base color?</code> 를 결정한다.</p>
<ul>
<li><p><strong>선택지:</strong> <code>Slate</code>, <code>Gray</code>, <code>Zinc</code>, <code>Neutral</code>, <code>Stone</code></p>
</li>
<li><p><strong>설명:</strong> 프로젝트의 기본 무채색 톤을 결정</p>
</li>
<li><p><strong>추천:</strong> <strong><code>Slate</code></strong> 또는 <strong><code>Zinc</code></strong>.</p>
</li>
</ul>
<pre><code class="language-shell">✔ Writing components.json.
✔ Checking registry.
✔ Updating tailwind.config.ts
✔ Updating CSS variables in src/shared/styles/index.scss
✔ Installing dependencies.
✔ Created 1 file:
  - src/lib/utils.ts

Success! Project initialization completed.
You may now add components.</code></pre>
<p><code>src/lib/utils.ts</code> 경로에 <strong>중복 Tailwind 클래스는 정리</strong>해주는 헬퍼 유틸 함수가 생성되는데 그대로 두거나 해당 프로젝트의 폴더구조에 옮기고 <code>components.json</code>에서 경로 수정을 한다.</p>
<p><code>index.scss</code>에 자동으로 CSS 변수가 생성되는데 나는 따로 관리를 하기 위해 <code>index.scss</code>가 아닌 따로 <code>tailwind.css</code>로 옮겼다.</p>
<p>그리고 이때 <code>lucide-react</code>(아이콘), <code>tailwind-merge</code>, <code>clsx</code>(클래스 합성 유틸) 같은 <strong>기본 의존성</strong>들이 한꺼번에 설치된다.</p>
<hr />
<h3 id="componentsjson-상세-속성">components.json 상세 속성</h3>
<pre><code class="language-json"># components.json
{
  &quot;$schema&quot;: &quot;https://ui.shadcn.com/schema.json&quot;,
  &quot;style&quot;: &quot;new-york&quot;,
  &quot;rsc&quot;: false,
  &quot;tsx&quot;: true,
  &quot;tailwind&quot;: {
    &quot;config&quot;: &quot;tailwind.config.ts&quot;,
    &quot;css&quot;: &quot;src/shared/styles/tailwind.css&quot;,
    &quot;baseColor&quot;: &quot;neutral&quot;,
    &quot;cssVariables&quot;: true,
    &quot;prefix&quot;: &quot;&quot;
  },
  &quot;iconLibrary&quot;: &quot;lucide&quot;,
  &quot;rtl&quot;: false,
  &quot;aliases&quot;: {
    &quot;components&quot;: &quot;@/components&quot;,
    &quot;utils&quot;: &quot;@/lib/utils&quot;,
    &quot;ui&quot;: &quot;@/components/ui&quot;,
    &quot;lib&quot;: &quot;@/lib&quot;,
    &quot;hooks&quot;: &quot;@/hooks&quot;
  },
  &quot;registries&quot;: {}
}</code></pre>
<h5 id="1-기본-설정-core">1. 기본 설정 (Core)</h5>
<ul>
<li><strong><code>$schema</code></strong>: 이 파일이 지켜야 할 규격을 정의, VS Code 같은 에디터에서 자동 완성이나 오타 검사를 도와준다.</li>
<li><strong><code>style</code></strong>: 컴포넌트의 디자인 스타일 (<code>new-york</code> 또는 <code>default</code>)<ul>
<li><code>new-york</code>: 더 작은 폰트와 세밀한 패딩을 가진 현대적인 스타일</li>
</ul>
</li>
<li><strong><code>rsc</code> (React Server Components)</strong>: Next.js의 서버 컴포넌트를 사용할지 여부</li>
<li><strong><code>tsx</code></strong>: 생성되는 컴포넌트 파일의 확장자를 <code>.tsx</code>로 할지 결정 TypeScript 사용자라면 당연히 <code>true</code></li>
</ul>
<h5 id="2-테일윈드-설정-tailwind">2. 테일윈드 설정 (<code>tailwind</code>)</h5>
<ul>
<li><strong><code>config</code></strong>: <code>tailwind.config.ts</code> 파일의 위치 CLI가 테마를 업데이트할 때 이 파일을 참조</li>
<li><strong><code>css</code></strong>: <strong>가장 중요한 부분</strong> 프로젝트의 메인 CSS/SCSS 파일 경로</li>
<li><strong><code>baseColor</code></strong>: <code>shadcn</code>이 생성하는 기본 색상 팔레트 (<code>neutral</code>, <code>slate</code> 등)</li>
<li><strong><code>cssVariables</code></strong>: 색상을 HSL 값으로 직접 박을지, CSS 변수(<code>--primary</code> 등)로 관리할지 결정</li>
<li><strong><code>prefix</code></strong>: Tailwind 클래스 앞에 붙일 접두사 (예: <code>tw-</code>) 보통은 비워둠</li>
</ul>
<h5 id="3-라이브러리-및-기타">3. 라이브러리 및 기타</h5>
<ul>
<li><strong><code>iconLibrary</code></strong>: 사용할 아이콘 라이브러리 기본값은 <code>lucide</code></li>
<li><strong><code>rtl</code> (Right-to-Left)</strong>: 아랍어처럼 오른쪽에서 왼쪽으로 읽는 언어를 지원할지 여부</li>
</ul>
<h5 id="4-경로-별칭-aliases">4. 경로 별칭 (<code>aliases</code>)</h5>
<p>컴포넌트가 설치될 <strong>'주소'</strong>를 정의 <code>tsconfig</code>의 <code>paths</code> 설정과 일치해야 한다.</p>
<ul>
<li><strong><code>components</code></strong>: 직접 만든 컴포넌트가 들어갈 루트 경로입니다 (<code>@/components</code>)</li>
<li><strong><code>ui</code></strong>: <strong>핵심</strong> <code>shadcn</code>에서 내려받는 순수 UI 컴포넌트(Button, Input 등)가 저장되는 곳(<code>@/components/ui</code>)</li>
<li><strong><code>utils</code></strong>: <code>cn</code> 함수 같은 유틸리티 파일의 위치</li>
<li><strong><code>lib</code>, <code>hooks</code></strong>: 각각 공통 라이브러리와 커스텀 훅이 저장될 위치</li>
</ul>
<hr />
<h3 id="컴포넌트-추가-및-사용">컴포넌트 추가 및 사용</h3>
<h5 id="1-컴포넌트-설치-명령">1. 컴포넌트 설치 명령</h5>
<p><a href="https://ui.shadcn.com/docs/components">🌐Components - shadcn/ui</a></p>
<p>Shadcn의 공식 사이트 - 컴포넌트 검색을 통해 컴포넌트 추가 명령어를 확인하고 추가 명령어를 입력한다.</p>
<p><strong>버튼 컴포넌트</strong></p>
<p><a href="https://ui.shadcn.com/docs/components/radix/button">🌐Button - shadcn/ui</a></p>
<p><code>npx shadcn@latest add button</code></p>
<blockquote>
<p>🕵️ 특정 컴포넌트를 처음 추가할 때 해당 컴포넌트가 필요한 <code>Radix Ui</code>패키지를 <code>Shadcn</code>이 감지해서 설치해준다.</p>
</blockquote>
<p><strong>추가 예시</strong></p>
<pre><code class="language-shell">jaiden-linux@DESKTOP-TPMO2QL:~/projects/test$ npx shadcn@latest add button
✔ Checking registry.
✔ Installing dependencies.
✔ Created 1 file:
  - src/shared/ui/button.tsx</code></pre>
<h5 id="2-cn-유틸리티-함수">2. <code>cn()</code> 유틸리티 함수</h5>
<ul>
<li>역할: <code>clsx</code>와 <code>tailwind-merge</code>를 결합한 함수.</li>
<li>장점: 조건부 스타일링을 편하게 하고, Tailwind 클래스 간의 충돌(예: <code>p-2</code>와 <code>p-4</code>가 같이 들어왔을 때)을 똑똑하게 해결해 준다.</li>
</ul>
<pre><code class="language-ts">// 예시: className을 외부에서 주입받아 합칠 때
&lt;button className={cn(&quot;bg-blue-500&quot;, className)}&gt;</code></pre>
<h5 id="3-shadcn-컴포넌트-구조-button-예시">3. Shadcn 컴포넌트 구조 (Button 예시)</h5>
<pre><code class="language-tsx">import * as React from &quot;react&quot;
import { Slot } from &quot;@radix-ui/react-slot&quot;
import { cva, type VariantProps } from &quot;class-variance-authority&quot;

import { cn } from &quot;@/shared/lib/utils/styles.util&quot;

const buttonVariants = cva(
  &quot;inline-flex items-center justify-center gap-2 whitespace-nowrap rounded-md text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50 [&amp;_svg]:pointer-events-none [&amp;_svg]:size-4 [&amp;_svg]:shrink-0&quot;,
  {
    variants: {
      variant: {
        default:
          &quot;bg-primary text-primary-foreground shadow hover:bg-primary/90&quot;,
        destructive:
          &quot;bg-destructive text-destructive-foreground shadow-sm hover:bg-destructive/90&quot;,
        outline:
          &quot;border border-input bg-background shadow-sm hover:bg-accent hover:text-accent-foreground&quot;,
        secondary:
          &quot;bg-secondary text-secondary-foreground shadow-sm hover:bg-secondary/80&quot;,
        ghost: &quot;hover:bg-accent hover:text-accent-foreground&quot;,
        link: &quot;text-primary underline-offset-4 hover:underline&quot;,
      },
      size: {
        default: &quot;h-9 px-4 py-2&quot;,
        sm: &quot;h-8 rounded-md px-3 text-xs&quot;,
        lg: &quot;h-10 rounded-md px-8&quot;,
        icon: &quot;h-9 w-9&quot;,
      },
    },
    defaultVariants: {
      variant: &quot;default&quot;,
      size: &quot;default&quot;,
    },
  }
)

export interface ButtonProps
  extends React.ButtonHTMLAttributes&lt;HTMLButtonElement&gt;,
    VariantProps&lt;typeof buttonVariants&gt; {
  asChild?: boolean
}

const Button = React.forwardRef&lt;HTMLButtonElement, ButtonProps&gt;(
  ({ className, variant, size, asChild = false, ...props }, ref) =&gt; {
    const Comp = asChild ? Slot : &quot;button&quot;
    return (
      &lt;Comp
        className={cn(buttonVariants({ variant, size, className }))}
        ref={ref}
        {...props}
      /&gt;
    )
  }
)
Button.displayName = &quot;Button&quot;

export { Button, buttonVariants }</code></pre>
<hr />
<p><strong>1. 라이브러리 호출</strong></p>
<pre><code class="language-tsx">import * as React from &quot;react&quot;
import { Slot } from &quot;@radix-ui/react-slot&quot;
import { cva, type VariantProps } from &quot;class-variance-authority&quot;

import { cn } from &quot;@/shared/lib/utils/styles.util&quot;</code></pre>
<ul>
<li>Slot (Radix UI): 이 버튼을 <code>&lt;a&gt;</code> 태그나 다른 태그로 바꾸고 싶을 때 사용하는 슬롯 (<code>asChild</code> 속성 관련)</li>
<li>cva (Class Variance Authority): CSS 클래스를 조건부로 관리해주는 핵심 도구 &quot;빨간색 버튼&quot;, &quot;큰 버튼&quot; 같은 <strong>스타일 옵션</strong>을 여기서 정의한다.</li>
<li>cn: 초기 세팅에 생성되는 머지 유틸 함수 여러 개의 클래스를 충돌 없이 합쳐주는 역할</li>
</ul>
<hr />
<p><strong>2. 스타일 정의(cva)</strong></p>
<p>shadcn의 <strong>디자인 엔진</strong>이다.</p>
<pre><code class="language-ts">const buttonVariants = cva( &quot;inline-flex items-center ...&quot;, // 기본(공통) 스타일 
    { 
    variants: { 
        size: { 
            default: &quot;ds-button-xs&quot;, 
            sm: &quot;ds-button-sm&quot;, 
            // ... 옵션들 
        }
    }, 
    defaultVariants: { 
            size: &quot;default&quot;
        }, 
    } 
)</code></pre>
<ul>
<li>variants: <code>size</code>나 <code>variant</code>(색상) 등을 정의한다. 옵션을 미리 정해두는 곳</li>
</ul>
<blockquote>
<p>🕵️ 코드를 사용하는 곳에서 <code>&lt;Button size=&quot;lg&quot;&gt;</code>라고 쓰면 <code>ds-button-lg</code> 클래스가 자동으로 붙는다.</p>
</blockquote>
<hr />
<p><strong>3. 타입 정의</strong></p>
<pre><code class="language-ts">export interface ButtonProps
  extends React.ButtonHTMLAttributes&lt;HTMLButtonElement&gt;,
    VariantProps&lt;typeof buttonVariants&gt; {
  asChild?: boolean
}</code></pre>
<ul>
<li>이 버튼이 어떤 <code>Props</code>를 받을 수 있는지 정의</li>
<li><code>React.ButtonHTMLAttributes</code>를 상속받기 때문에 <code>onClick</code>, <code>type=&quot;submit&quot;</code>, <code>disabled</code> 같은 <strong>표준 버튼 속성</strong>을 그대로 다 쓸 수 있다.</li>
</ul>
<hr />
<p><strong>4. 컴포넌트</strong></p>
<pre><code class="language-ts">const Button = React.forwardRef&lt;HTMLButtonElement, ButtonProps&gt;(
  ({ className, variant, size, asChild = false, ...props }, ref) =&gt; {
    const Comp = asChild ? Slot : &quot;button&quot;
    return (
      &lt;Comp
        className={cn(buttonVariants({ variant, size, className }))}
        ref={ref}
        {...props}
      /&gt;
    )
  }
)
Button.displayName = &quot;Button&quot;

export { Button, buttonVariants }</code></pre>
<ul>
<li>forwardRef: 부모 컴포넌트가 이 버튼의 DOM에 직접 접근(Focus 등)할 수 있게 해준다. 라이브러리 제작 시 필수적인 패턴</li>
<li>asChild: * <code>false</code>일 때: 기본 <code>&lt;button&gt;</code> 태그로 렌더링된다.<ul>
<li><code>true</code>일 때: 새 태그를 만들지 않고 자식(Child) 요소에게 자신의 스타일과 기능을 전달한다.</li>
<li>예: <code>&lt;Button asChild&gt;&lt;a href=&quot;...&quot;&gt;링크&lt;/a&gt;&lt;/Button&gt;</code>라고 쓰면 버튼 모양을 한 <code>&lt;a&gt;</code> 태그가 탄생한다. (HTML 표준 위반인 <code>&lt;button&gt;&lt;a&gt;&lt;/a&gt;&lt;/button&gt;</code> 구조를 피하기 위함)</li>
</ul>
</li>
</ul>
<hr />