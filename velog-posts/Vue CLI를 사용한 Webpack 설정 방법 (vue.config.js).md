<h1 id="vue-cli를-사용한-webpack-설정-방법-vueconfigjs">Vue CLI를 사용한 Webpack 설정 방법 (vue.config.js)</h1>
<hr />
<p>🕵️ Vue/Cli 를 사용하여 vue.config.js 세팅을 하게되어 속성의 기능과 옵션을 숙지하기 위해 글을 쓰게 되었다. 주로 쓰는 속성을 업로드하고 추후 추가적인 기능이나 시간이 난다면 속성을 더 업데이트 할 예정이다.</p>
<hr />
<h3 id="📄기본-vueconfigjs">📄기본 vue.config.js</h3>
<pre><code class="language-js">const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
  transpileDependencies: true
})</code></pre>
<hr />
<h2 id="publicpath">publicPath</h2>
<ul>
<li><code>Type</code> : <code>string</code></li>
<li><code>Default</code> : <code>'/'</code></li>
</ul>
<pre><code class="language-js">module.exports = defineConfig({
    ...
    publicPath: '/my-app/', // default '/'
    ...
})</code></pre>
<p>Vue CLI 프로젝트에서 애플리케이션이 배포될 기본 경로를 설정하는 데 사용된다. 이 속성은 애플리케이션의 모든 정적 자원에 대한 기본 URL을 지정한다. 기본적으로 <code>/</code>로 설정되어 있지만, 애플리케이션이 서브 디렉토리에 배포될 경우 이 값을 변경해야 한다.</p>
<p>ex ) <code>https://example.com/my-app/</code>에 배포될 경우 <code>publicPath</code>를 <code>/my-app/</code>으로 설정해야 한다.</p>
<hr />
<h2 id="transpiledependencies">transpileDependencies</h2>
<ul>
<li><code>Type</code> : <code>boolean</code> | <code>Array&lt;string | RegExp&gt;</code></li>
<li><code>Default</code> : <code>false</code></li>
</ul>
<p>특정 종속성을 Babel을 사용하여 트랜스파일링하도록 지정하는 데 사용된다. 
이는 주로 ES6+ 코드를 포함하는 외부 라이브러리나 모듈을 호환성 문제 없이 사용하기 위해 필요하다. 기본적으로 <code>node_modules</code> 폴더 내의 파일들은 Babel의 트랜스파일링 대상에서 제외되지만, <code>transpileDependencies</code>에 명시된 종속성은 예외로 처리된다.</p>
<p>위 📄<code>기본 vue.config.js</code> 에서는 <code>true</code>로만 되어있는데 저 상태는 <code>transpileDependencies</code>옵션이 활성화 되었음을 나타내고 실제로 사용할 때 배열로 명시한다.</p>
<pre><code class="language-js">module.exports = defineConfig({
  ...
  transpileDependencies: [
    'some-dependency',
    'another-dependency'
  ],
  ...
})</code></pre>
<hr />
<h2 id="devserver">devServer</h2>
<ul>
<li><code>Type</code> : <code>Object</code></li>
</ul>
<pre><code class="language-js">module.exports = defineConfig({
    ...
    devServer: {
        ...
    }
    ...
})</code></pre>
<hr />
<h2 id="devserverhot--hmrhot-module-replacement">devServer.hot / HMR(Hot Module Replacement)</h2>
<p><a href="https://webpack.js.org/guides/hot-module-replacement/#root">Webpack HMR문서</a></p>
<blockquote>
<p>hot 설정</p>
</blockquote>
<p>Hot Module Replacement(또는 HMR)는 webpack에서 제공하는 가장 유용한 기능 중 하나이다. 
모든 종류의 모듈을 전체 새로 고침 없이 런타임에 업데이트할 수 있다.</p>
<pre><code class="language-diff">devServer: {
      ...
+     hot: true,
      ...
    },</code></pre>
<blockquote>
<p>Vue CLI에서의 진입점</p>
</blockquote>
<p>Vue CLI 프로젝트에서는 기본적으로 <code>src/main.js</code> 또는 <code>main.ts</code> 파일이 진입점으로 설정된다. Vue CLI는 내부적으로 Webpack을 사용하여 이 파일을 진입점으로 설정하고 번들링한다.</p>
<p>수동으로 진입점을 설정하려면 직접 경로를 설정해도 된다.</p>
<pre><code class="language-diff">entry: {
       app: './src/index.js',
    },</code></pre>
<hr />
<p>🕵️ HMR의 기능 </p>
<p>맨처음에 그냥 <code>true</code> , <code>false</code> 로만 설정을 하니 직접 어떤기능인지 정확하게 와닿지가 않았다.</p>
<p>기존 프로젝트에서 <code>true</code> , <code>false</code> 로 실행한 결과  </p>
<p><code>true</code> 일 때 해당 코드의 관련된 부분만 바로 업데이트만 되었고</p>
<p><code>false</code> 일 때는 새로고침이 되었다.</p>
<hr />
<h2 id="devserverproxy">devServer.proxy</h2>
<ul>
<li><code>Type</code> : <code>string</code> | <code>Object</code></li>
</ul>
<p>프론트엔드 앱과 백엔드 API 서버가 동일한 호스트에서 실행되지 않는 경우 개발 중에 API 요청을 API 서버로 프록시해야 하고 <code>devServer.proxy</code>의 옵션을 통해 구성할 수 있다.</p>
<pre><code class="language-js">module.exports = {
  devServer: {
    proxy: 'http://localhost:4000'
  }
}</code></pre>
<p>이렇게 하면 개발 서버는 알 수 없는 요청(정적 파일과 일치하지 않는 요청)을 프록시로 처리하게 된다.</p>
<p>⚠️ 설정이 위와 같이 문자열로 설정된 경우에 발생할 수 있다. 문자열로 설정된 경우, Webpack Dev Server는 XHR(XMLHttpRequest) 요청만 프록시한다. 즉, 브라우저에서 직접 API URL을 열려고 하면 프록시가 작동하지 않을 수 있다. 대신 Postman과 같은 API 도구를 사용하여 API 요청을 테스트해야 한다.</p>
<blockquote>
<p>🕵️ CORS에러가 뜨거나 작동하지 않을 경우 <code>path: options</code> 쌍이 있는 객체를 사용할 수도 있다. </p>
</blockquote>
<pre><code class="language-js">module.exports = {
  devServer: {
    proxy: {
      '/api/foo': {
        target: 'https://example_foo.com',
        changeOrigin: true
      },
      '/api/bar': {
        target: 'https://example_bar.com',
        changeOrigin: true
      },
      ...
    }
  }
}</code></pre>
<p><code>changeOrigin</code>속성을 사용하면 브라우저에서도 정상적으로 프록시가 작동한다. 프록시 요청의 <code>Host</code> 헤더를 대상 서버의 호스트로 변경하여 <code>CORS</code> 문제를 해결하는 데 도움이 된다.</p>
<p>예를 들어 <code>getFooList</code>라는 함수로 데이터를 갖고오는 예시이다.</p>
<pre><code class="language-js">export const getFooList = () =&gt; {
    return axios.get('/api/foo/list')
};</code></pre>
<p><code>proxy</code>의 키값인 <code>'/api/foo'</code>로 시작하므로 <code>/api/foo</code>경로로 들어오는 요청은 <code>target</code>인  <code>https://example_foo.com</code> 로 프록시된다. 두번째 <code>/api/bar</code> 도 마찬가지</p>
<hr />
<h2 id="css-modules">CSS Modules</h2>
<p>CSS 모듈은 CSS 파일을 로컬 스코프로 제한하여 클래스 이름 충돌을 방지하는 기술이다. 
이를 통해 각 컴포넌트의 스타일이 고유하게 유지되며, 전역 네임스페이스 오염을 방지할 수 있다.</p>
<p><strong>주요 특징</strong></p>
<ol>
<li><strong>로컬 스코프</strong>: CSS 클래스가 로컬 스코프로 제한된다.</li>
<li><strong>자동 네임스페이스</strong>: 클래스 이름이 고유하게 변환되어 전역 네임스페이스 충돌을 방지한다.</li>
<li><strong>모듈화</strong>: 각 컴포넌트의 스타일을 독립적으로 관리할 수 있다.</li>
</ol>
<p>기본적으로 간단하게 <code>scoped</code> 를 사용해도 되지만 해당 하위 컴포넌트는 독립적이지 않으므로 같은 클래스를 쓴다면 적용이 된다.</p>
<h4 id="css-modules-사용">CSS Modules 사용</h4>
<p><strong>1. Vue 컴포넌트에서 CSS 모듈 바로 사용</strong> <code>&lt;style module&gt;</code> 태그 사용</p>
<pre><code class="language-html">&lt;template&gt;
  &lt;button :class="$style.button"&gt;Click me&lt;/button&gt;
&lt;/template&gt;

&lt;style module&gt;
.button {
  background-color: blue;
  color: white;
}
&lt;/style&gt;</code></pre>
<hr />
<p><strong>2. CSS 모듈을 import 해서 사용</strong></p>
<pre><code class="language-html">&lt;template&gt;
  &lt;button :class="styles.button"&gt;Click me&lt;/button&gt;
&lt;/template&gt;

&lt;script&gt;
import styles from '@/styles/foo.module.css';
export default {
  computed: {
    styles() {
      return styles;
    }
  }
}
&lt;/script&gt;</code></pre>
<p><code>.module</code> 파일 이름을 추가하고 모든 스타일 파일을 CSS 모듈로 처리하려면 아래와 같이 <code>vue.config.js</code> 설정을 한다.</p>
<pre><code class="language-js">module.exports = {
  css: {
    loaderOptions: {
      css: {
        modules: {
          auto: () =&gt; true
        }
      }
    }
  }
}</code></pre>
<hr />
<p><strong>3. Vue Cli 설정 사용</strong></p>
<pre><code class="language-js">module.exports = {
  ...
  css: {
    loaderOptions: {
      css: {
        modules: {
          localIdentName: '[name]-[hash]',
        }
      }
    }
  },
  ...
}</code></pre>
<p><code>localIdentName</code>이 <code>[name]-[hash]</code>로 설정된 경우, 생성된 <code>button</code>클래스 이름은 다음과 같이 변환된다</p>
<ul>
<li>원본 파일 이름: <code>styles</code></li>
<li>해시 값: 예를 들어 <code>abc123</code></li>
</ul>
<p>따라서, 최종 클래스 이름은 <code>styles-abc123</code>가 된다.</p>
<p>이 설정을 통해 <code>.button</code> 클래스는 <code>styles-abc123</code>와 같이 고유한 이름으로 변환된다. 이를 통해 클래스 이름 충돌을 방지하고, 스타일을 모듈화하여 관리할 수 있다.</p>
<p>쉽게 말해 <code>.button</code> 이지만 유니크한 값으로 변환해서 고유하게 쓸 수 있게 해주는 기능이다.</p>
<hr />
<h2 id="css-modules-sass--전처리기">CSS Modules SASS / 전처리기</h2>
<p><code>loaderOptions</code>의 <code>sass</code> 옵션은 SASS 전처리기와 관련된 설정이다. 이 설정은 SASS 파일을 처리할 때 추가적인 데이터를 자동으로 포함시키는 데 사용된다.</p>
<p>예를 들어, 모든 Sass/Less 스타일에 공유된 전역 변수를 전달하려면 다음과 같다.</p>
<hr />
<p>📄variables.scss</p>
<pre><code class="language-sass">/*== color ==*/
$white : #FFFFFF;
$black : #000000;
$red : #F00F00;
$grayEBE : #EBEBEB;</code></pre>
<hr />
<pre><code class="language-js">module.exports = {
  ...
  css: {
    loaderOptions: {
      sass: {
        additionalData: '@import "@/assets/scss/_variables";',
      },
    },
  },
  ...
}</code></pre>
<p>이렇게 전처리기로 가져와서 프로젝트 내의 모든 <code>SASS</code> 파일에서 공통 변수를 사용할 수 있도록 설정한다.</p>
<hr />
<h2 id="chainwebpack">chainWebpack</h2>
<p><code>Vue CLI</code>에서 <code>Webpack</code> 설정을 체인 방식으로 수정할 수 있는 메서드다. 이를 통해 Webpack 설정을 세밀하게 조정할 수 있다. <code>chainWebpack</code> 메서드는 <code>webpack-chain</code> 라이브러리를 사용하여 Webpack 설정을 구성한다.</p>
<blockquote>
<p>📣 <code>webpack-chain</code> 라이브러리는 <code>VueCli</code>에 내장되어 있다.</p>
</blockquote>
<hr />
<p><strong>내가 사용하면서 주로 쓰던 기능은 아래와 같다</strong></p>
<ol>
<li><strong>Alias 설정</strong>: 모듈 경로를 더 간단하게 참조할 수 있도록 별칭을 설정한다.</li>
<li><strong>Loader 설정</strong>: 특정 파일 유형에 대한 로더를 설정하거나 수정한다.</li>
<li><strong>Plugin 설정</strong>: Webpack 플러그인을 추가하거나 수정한다.</li>
</ol>
<hr />
<h3 id="alias-설정">Alias 설정</h3>
<pre><code class="language-js">config.resolve.alias.set('@', path.resolve(__dirname, 'src/'));</code></pre>
<p><code>src</code>를 기점으로 절대경로로 쓰기 위해 설정하여 더 간단하게 참조할 수 있다.</p>
<pre><code class="language-js">import MyComponent from '@/components/MyComponent.vue';</code></pre>
<hr />
<h3 id="vue-loader-설정">vue-loader 설정</h3>
<pre><code class="language-js">config.module
  .rule('vue')
  .use('vue-loader')
  .tap((options) =&gt; ({
    ...options,
    defineModel: true,
  }));</code></pre>
<p><code>defineModel</code>은 vue3.3에서 추가된 기능이다. 사용하려면 vue.config 나 vite.config 에서 설정을 해줘야한다.</p>
<ul>
<li><code>vue-loader</code>의 옵션을 수정하여 <code>defineModel: true</code>를 추가한다.</li>
<li><code>tap</code> 메서드를 사용하여 기존 옵션을 확장하거나 수정할 수 있다.</li>
</ul>
<hr />
<h3 id="defineplugin-설정">DefinePlugin 설정</h3>
<pre><code class="language-js">config.plugin('define').tap((definitions) =&gt; {
  Object.assign(definitions[0], {
    __VUE_OPTIONS_API__: 'true', // Vue Options API 사용 여부 설정
    __VUE_PROD_HYDRATION_MISMATCH_DETAILS__: 'false' // Vue 3의 hydration mismatch 세부 정보 비활성화
  });
  return definitions;
});</code></pre>
<p>이 코드는 Webpack의 <code>DefinePlugin</code>을 사용하여 전역 상수를 정의하는 설정이다. <code>DefinePlugin</code>은 컴파일 타임에 전역 상수를 정의하여 코드 내에서 사용할 수 있게 한다. 이 설정은 Vue CLI 프로젝트에서 특정 전역 상수를 정의하여 Vue의 동작을 제어하는 데 사용된다.</p>
<hr />