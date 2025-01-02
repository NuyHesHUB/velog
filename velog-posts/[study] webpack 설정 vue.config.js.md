<h1 id="study-webpack-설정-vueconfigjs">[study] webpack 설정 vue.config.js</h1>
<hr />

<p><a href="https://webpack.kr/">웹팩 공식 페이지</a></p>
<blockquote>
<p>⚠️ Vue CLI가 유지 관리 모드에 있습니다!</p>
</blockquote>
<p>새로운 프로젝트의 경우 이제 Vitecreate-vue 기반 프로젝트를 스캐폴딩하는 데 사용하는 것이 좋습니다 . 또한 최신 권장 사항은 Vue 3 도구 가이드를 참조하세요 .</p>
<p>이유 및 설명</p>
<ul>
<li><p>Vite의 장점: Vite는 차세대 프론트엔드 빌드 도구로, 매우 빠른 개발 서버와 효율적인 번들링을 제공합니다. 특히 Vue 3와 잘 통합되어 있고, 최신 웹 개발 트렌드를 반영하고 있습니다.</p>
</li>
<li><p>Vue CLI의 위치: Vue CLI는 Vue 2와 Vue 3 프로젝트를 위한 훌륭한 도구였지만, Vite가 등장하면서 더 이상 Vue CLI를 사용할 필요성이 줄어들었습니다. Vue CLI는 아직도 기존 프로젝트에 대해 지원이 이루어지겠지만, 새로운 프로젝트에서는 Vite를 사용하는 것이 더 유리합니다.</p>
</li>
</ul>
<p>결론</p>
<p>따라서, 앞으로 새로운 Vue 프로젝트를 시작할 때는 Vue CLI 대신 Vite를 사용하는 것이 권장됩니다. Vite는 더 빠르고, 가벼우며, 최신 기술을 지원하는 도구로, Vue 3 프로젝트와의 궁합도 좋습니다. Vue 3 도구 가이드를 참고하여 Vite 기반의 프로젝트를 시작하는 것이 좋습니다.</p>
<hr />

<p>Configuration Reference 공식 문서 : <a href="https://cli.vuejs.org/config/">https://cli.vuejs.org/config/</a></p>
<hr />

<p><strong>예시</strong></p>
<pre><code class="language-js">const path = require('path');

const { defineConfig } = require('@vue/cli-service');


module.exports = defineConfig({
    configureWebpack: {
        devtool: 'source-map',
        devServer: {
            proxy: {
                '/api': {
                    changeOrigin: true,
                    target: process.env.VUE_APP_SERVER
                }
            }
        },
        resolve: {
            alias: {
                '@api': path.resolve(__dirname, 'src/api'),
                '@app': path.resolve(__dirname, 'src'),
                '@components': path.resolve(__dirname, 'src/components'),
            }
        }
    },
    chainWebpack: config =&gt; {
        config.module
            .rule('vue')
            .use('vue-loader')
            .tap(options =&gt; ({
                ...options,
                defineModel: true
            }))
    },
    css: {
        loaderOptions: {
            sass: {
                additionalData: '@import "@/assets/scss/_variables";'
            }
        }
    },
    productionSourceMap: false,
    transpileDependencies: true 🔴잘못된 처리🔴
});</code></pre>
<h2 id="configurewebpack">configureWebpack</h2>
<p>"configureWebpack" 옵션은 웹팩 설정을 직접 수정하거나 확장할 수 있는 곳입니다.</p>
<h3 id="devtool--webpack">devtool / (webpack)</h3>
<p><a href="https://webpack.kr/configuration/devtool/#devtool">웹팩 "devtool"옵션 공식문서 바로가기</a></p>
<p>devtool 옵션은 웹팩(Webpack)에서 디버깅을 위해 소스맵을 생성하는 방식을 설정하는 데 사용됩니다. </p>
<p><strong>주요 옵션값</strong></p>
<hr />

<ol>
<li>source-map</li>
</ol>
<ul>
<li><p>설명: 전체 소스맵을 별도의 파일로 생성합니다. 소스맵 파일이 정확하고 디버깅하기에 가장 적합하지만, 빌드 속도가 느려지고 배포 파일의 크기가 커질 수 있습니다.</p>
</li>
<li><p>사용 예: 고품질의 디버깅이 필요할 때, 특히 프로덕션에서 사용.</p>
</li>
</ul>
<hr />

<ol start="2">
<li>cheap-source-map</li>
</ol>
<ul>
<li><p>설명: 소스맵을 생성하지만 원본 코드의 매핑 정보를 줄입니다(주로 줄(line) 단위로). 생성 속도가 빠르고 파일 크기가 작지만, 세부적인 디버깅에는 부적합합니다.</p>
</li>
<li><p>사용 예: 빠른 빌드 속도가 필요한 경우, 세부 디버깅이 필요 없는 경우.</p>
</li>
</ul>
<hr />

<ol start="3">
<li>eval</li>
</ol>
<ul>
<li><p>설명: 각 모듈을 eval()로 래핑하여 소스맵을 인라인으로 포함시킵니다. 매우 빠르지만, 브라우저의 개발자 도구에서 코드가 좀 더 읽기 어려워질 수 있습니다.</p>
</li>
<li><p>사용 예: 개발 시 빠른 빌드가 중요할 때.</p>
</li>
</ul>
<hr />

<ol start="4">
<li>eval-source-map</li>
</ol>
<ul>
<li><p>설명: eval과 source-map을 결합한 방식으로, 소스맵을 eval()로 인라인으로 포함시키지만 원본 소스 매핑 정보를 포함합니다. 디버깅이 가능하면서도 빌드가 빠릅니다.</p>
</li>
<li><p>사용 예: 개발 환경에서 빠른 빌드와 함께 디버깅이 필요할 때.</p>
</li>
</ul>
<hr />

<ol start="5">
<li>cheap-module-source-map</li>
</ol>
<ul>
<li><p>설명: cheap-source-map과 비슷하지만, 로더(loader)에서 변환된 코드의 매핑을 제공합니다. 원본 코드와 유사한 디버깅 경험을 제공하지만, 디테일이 조금 떨어질 수 있습니다.</p>
</li>
<li><p>사용 예: 빠른 빌드와 함께 어느 정도의 디버깅이 필요한 경우.</p>
</li>
</ul>
<hr />

<ol start="6">
<li>hidden-source-map</li>
</ol>
<ul>
<li><p>설명: 소스맵 파일을 생성하지만, 소스맵 파일을 JavaScript 파일에 포함하지 않습니다. 브라우저 개발자 도구에서는 소스맵이 보이지 않지만, 오류 추적 도구(예: Sentry)에서 사용할 수 있습니다.</p>
</li>
<li><p>사용 예: 프로덕션 환경에서 소스맵이 필요하지만 사용자가 직접 접근할 필요는 없을 때.</p>
</li>
</ul>
<hr />

<ol start="7">
<li>nosources-source-map</li>
</ol>
<ul>
<li><p>설명: 소스맵을 생성하지만 원본 코드를 포함하지 않습니다. 디버깅할 때 원본 코드를 보지 않고 매핑 정보만을 사용합니다.</p>
</li>
<li><p>사용 예: 프로덕션 환경에서 소스맵을 제공하되, 원본 코드 보호가 중요한 경우.</p>
</li>
</ul>
<hr />

<ol start="8">
<li>inline-source-map</li>
</ol>
<ul>
<li><p>설명: 소스맵을 별도의 파일로 생성하지 않고, 각 JavaScript 파일에 인라인으로 포함시킵니다. 파일을 나누지 않아서 빠르게 접근할 수 있지만, 빌드된 파일 크기가 커질 수 있습니다.</p>
</li>
<li><p>사용 예: 소스맵 파일을 분리하지 않고, 빠르게 접근하고 싶을 때.</p>
</li>
</ul>
<hr />

<ol start="9">
<li>inline-cheap-source-map</li>
</ol>
<ul>
<li><p>설명: inline-source-map과 비슷하지만, 매핑 정보를 줄여 더 빠르게 만듭니다. 디테일이 줄어들기 때문에 줄 단위 디버깅만 가능합니다.</p>
</li>
<li><p>사용 예: 개발 중 빠른 빌드를 원할 때, 세부 디버깅이 필요하지 않을 때.</p>
</li>
</ul>
<hr />

<ol start="10">
<li>inline-cheap-module-source-map</li>
</ol>
<ul>
<li><p>설명: cheap-module-source-map과 동일하지만, 인라인으로 소스맵을 포함시킵니다. 빠른 빌드 속도와 인라인 디버깅을 결합한 옵션입니다.</p>
</li>
<li><p>사용 예: 모듈별 소스맵을 인라인으로 포함하면서 빠른 빌드와 디버깅이 필요할 때.</p>
</li>
</ul>
<hr />

<ol start="11">
<li>eval-cheap-source-map</li>
</ol>
<ul>
<li><p>설명: eval과 cheap-source-map의 결합으로, 매우 빠르게 빌드되지만 줄 단위로만 디버깅할 수 있습니다.</p>
</li>
<li><p>사용 예: 빠른 개발 환경이 필요하고, 디테일한 디버깅이 필요하지 않을 때.</p>
</li>
</ul>
<hr />

<ol start="12">
<li>eval-cheap-module-source-map</li>
</ol>
<ul>
<li><p>설명: eval과 cheap-module-source-map의 결합으로, 모듈 단위로 빠르게 빌드되면서 디버깅할 수 있습니다.</p>
</li>
<li><p>사용 예: 개발 중에 모듈 단위 디버깅이 필요할 때.</p>
</li>
</ul>
<hr />

<h3 id="devserver--webpack">devServer / (webpack)</h3>
<p><a href="https://webpack.kr/configuration/dev-server/#root">웹팩 "devServer"옵션 공식문서 바로가기</a></p>
<p>"devServer" 옵션은 Vue CLI에서 제공하는 개발 서버(webpack-dev-server)의 설정을 관리하는 데 사용됩니다. 이 옵션을 통해 로컬 개발 환경에서 다양한 설정을 커스터마이즈할 수 있습니다.</p>
<p><strong>주요 옵션값</strong></p>
<hr />

<ol>
<li>port</li>
</ol>
<ul>
<li><p>설명: 개발 서버가 사용할 포트를 지정합니다. 기본값은 <code>8080</code>입니다.</p>
</li>
<li><p>예시</p>
<pre><code class="language-js">  devServer: {
    port: 3000
  }</code></pre>
</li>
</ul>
<hr />

<ol start="2">
<li>host</li>
</ol>
<ul>
<li><p>설명: 개발 서버가 바인딩할 호스트 이름을 설정합니다. 기본값은 localhost입니다.</p>
</li>
<li><p>예시</p>
<pre><code class="language-js">  devServer: {
    host: '0.0.0.0'
  }</code></pre>
</li>
</ul>
<hr />

<ol start="3">
<li>open</li>
</ol>
<ul>
<li><p>설명: 개발 서버가 시작될 때 브라우저를 자동으로 여는지 여부를 설정합니다. 기본값은 false입니다.</p>
</li>
<li><p>예시</p>
<pre><code class="language-js">  devServer: {
    open: true
  }</code></pre>
</li>
</ul>
<hr />

<ol start="4">
<li>https</li>
</ol>
<ul>
<li><p>설명: HTTPS 프로토콜을 사용하여 개발 서버를 실행할지 여부를 설정합니다. 기본값은 false입니다.</p>
</li>
<li><p>예시</p>
<pre><code class="language-js">  devServer: {
    https: true
  }</code></pre>
</li>
</ul>
<hr />

<ol start="5">
<li>proxy</li>
</ol>
<ul>
<li><p>설명: 개발 서버에서 API 요청을 다른 서버로 프록시할 수 있습니다. 프록시 설정을 통해 CORS 문제를 해결하거나 API 요청을 로컬 서버로 전달할 수 있습니다.</p>
</li>
<li><p>예시</p>
<pre><code class="language-js">  devServer: {
      proxy: {
        '/api': {
          target: 'http://localhost:5000', 🔵또는 process.env.VUE_APP_SERVER 같은 환경변수
          changeOrigin: true,
        }
      }
  }</code></pre>
</li>
</ul>
<hr />

<ol start="6">
<li>hot</li>
</ol>
<ul>
<li><p>설명: 핫 모듈 교체(Hot Module Replacement, HMR)를 활성화합니다. 이 옵션이 활성화되면 모듈을 수정할 때 전체 페이지를 다시 로드하지 않고 수정된 모듈만 교체할 수 있습니다. 기본값은 true입니다.</p>
</li>
<li><p>예시</p>
<pre><code class="language-js">  devServer: {
    hot: true
  }</code></pre>
</li>
</ul>
<hr />

<ol start="7">
<li>liveReload</li>
</ol>
<ul>
<li><p>설명: 파일이 변경될 때 전체 페이지를 자동으로 새로고침할지 여부를 설정합니다. 기본값은 true입니다.</p>
</li>
<li><p>예시</p>
<pre><code class="language-js">  devServer: {
    liveReload: true
  }</code></pre>
</li>
</ul>
<hr />

<ol start="8">
<li>compress</li>
</ol>
<ul>
<li><p>설명: 모든 항목에 대해 gzip 압축을 활성화할지 여부를 설정합니다. 기본값은 false입니다.</p>
</li>
<li><p>예시</p>
<pre><code class="language-js">  devServer: {
    liveReload: true
  }</code></pre>
<hr />
🕵️gzip 압축이란?

</li>
</ul>
<p>gzip 압축을 사용하는 것은 개발 서버가 클라이언트(브라우저)로 전송하는 정적 파일들을 압축하여 전송하는 기능을 의미합니다. 이를 통해 데이터 전송량을 줄이고, 페이지 로딩 속도를 향상시킬 수 있습니다. 다음은 이 기능에 대한 자세한 설명입니다.</p>
<p>gzip은 데이터를 압축하여 파일 크기를 줄이는 알고리즘 중 하나입니다. 웹에서는 주로 텍스트 기반 파일(HTML, CSS, JavaScript 등)의 크기를 줄여 네트워크를 통해 더 빠르게 전송되도록 하는 데 사용됩니다.</p>
<p>gzip 압축의 작동 방식</p>
<ul>
<li>요청 처리: 클라이언트(브라우저)가 서버에 파일을 요청합니다.</li>
<li>압축 적용: 서버는 요청된 파일을 gzip 알고리즘을 사용하여 압축합니다.</li>
<li>압축된 파일 전송: 압축된 파일을 클라이언트로 전송합니다.</li>
<li>브라우저에서 복호화: 브라우저는 압축된 파일을 받아 원래의 파일로 복호화하여 렌더링합니다.</li>
</ul>
<p><strong>장점과 단점</strong></p>
<p>장점</p>
<ul>
<li>빠른 로딩 속도: 특히 네트워크 속도가 느릴 때 유리합니다.</li>
<li>데이터 절약: 데이터 사용량을 줄일 수 있어 모바일 환경에서 유리할 수 있습니다.</li>
<li>프로덕션 환경 테스트: 프로덕션과 유사한 환경에서 테스트할 수 있습니다.</li>
</ul>
<p>단점</p>
<ul>
<li>CPU 사용량 증가: 파일을 압축하고 복호화하는 과정에서 CPU 자원이 추가로 소모될 수 있습니다. 하지만 개발 환경에서는 큰 문제가 되지 않는 경우가 많습니다.</li>
<li>빌드 시간 증가 가능성: 압축 과정이 추가되므로 빌드 시간이 약간 길어질 수 있습니다.</li>
</ul>
<hr />

<ol start="9">
<li>historyApiFallback</li>
</ol>
<ul>
<li><p>설명: HTML5 히스토리 API를 사용하는 SPA(Single Page Application)에서 새로고침 시 404 에러를 방지하기 위해 모든 요청을 index.html로 리디렉션합니다. 기본값은 false입니다.</p>
</li>
<li><p>예시</p>
<pre><code class="language-js">  devServer: {
    historyApiFallback: true
  }</code></pre>
</li>
</ul>
<hr />

<ol start="10">
<li>overlay</li>
</ol>
<ul>
<li><p>설명: 브라우저 화면에 ESLint 오류나 빌드 오류를 오버레이로 표시할지 여부를 설정합니다. 기본값은 false입니다.</p>
</li>
<li><p>예시</p>
<pre><code class="language-js">  devServer: {
    overlay: {
      warnings: true,
      errors: true
    }
  }</code></pre>
</li>
</ul>
<hr />

<ol start="11">
<li>headers</li>
</ol>
<ul>
<li><p>설명: 개발 서버에서 제공하는 모든 응답에 대해 특정 HTTP 헤더를 설정할 수 있습니다.</p>
</li>
<li><p>예시</p>
<pre><code class="language-js">  devServer: {
    headers: {
      'X-Custom-Header': 'yes'
    }
  }</code></pre>
</li>
</ul>
<hr />

<ol start="12">
<li>before</li>
</ol>
<ul>
<li><p>설명: 개발 서버가 시작되기 전에 실행할 함수를 정의할 수 있습니다. 주로 미들웨어나 커스텀 API 라우트를 설정할 때 사용됩니다.</p>
</li>
<li><p>예시</p>
<pre><code class="language-js">  devServer: {
    before: function(app, server) {
      app.get('/some/path', function(req, res) {
        res.json({ custom: 'response' });
      });
    }
  }</code></pre>
</li>
</ul>
<hr />

<ol start="13">
<li>client</li>
</ol>
<ul>
<li><p>설명: 클라이언트 측 웹소켓 설정을 구성합니다. 이를 통해 리로딩, HMR, 오버레이와 같은 기능을 커스터마이즈할 수 있습니다.</p>
</li>
<li><p>예시</p>
<pre><code class="language-js">  devServer: {
    client: {
      logging: 'info',   // 로그 레벨 설정: none, error, warn, info
      overlay: true,     // 오류 오버레이 활성화
      progress: true     // 진행 상황 표시
    }
  }</code></pre>
</li>
</ul>
<hr />

<ol start="14">
<li>watchOptions</li>
</ol>
<ul>
<li><p>설명: 파일 변경 감시와 관련된 옵션을 설정할 수 있습니다. 특정 파일이나 디렉토리를 무시하거나, 감시 간격을 조정할 수 있습니다.</p>
</li>
<li><p>예시</p>
<pre><code class="language-js">  devServer: {
    watchOptions: {
      poll: true,
      ignored: /node_modules/,
    }
  }</code></pre>
</li>
</ul>
<hr />

<ol start="15">
<li>allowedHosts</li>
</ol>
<ul>
<li><p>설명: 개발 서버가 요청을 수락할 호스트를 명시적으로 지정할 수 있습니다. 기본적으로는 로컬 호스트(예: localhost, 127.0.0.1)만 허용됩니다.</p>
</li>
<li><p>예시</p>
<pre><code class="language-js">  devServer: {
    allowedHosts: [
      'host.com',
      'subdomain.host.com'
    ]
  }</code></pre>
</li>
</ul>
<hr />

<ol start="16">
<li>static</li>
</ol>
<ul>
<li><p>설명: 정적 파일을 제공할 디렉토리를 설정합니다. 이 옵션을 사용하여 정적 파일의 경로와 서빙 방식을 세부적으로 조정할 수 있습니다.</p>
</li>
<li><p>예시</p>
<pre><code class="language-js">  devServer: {
    static: {
      directory: path.join(__dirname, 'public'),
      publicPath: '/assets',
    }
  }</code></pre>
</li>
</ul>
<hr />

<h3 id="resolve--webpack">resolve / (webpack)</h3>
<p><a href="https://webpack.kr/configuration/resolve/#root">웹팩 "resolve"옵션 공식문서 바로가기</a></p>
<p>"resolve" 옵션은 Webpack에서 모듈을 어떻게 해석할지 정의하는 설정입니다. Vue CLI에서도 Webpack의 resolve 설정을 활용하여 경로 및 모듈 해석을 커스터마이즈할 수 있습니다. 이 옵션을 사용하면 모듈의 경로를 짧고 간단하게 관리할 수 있으며, 특정 확장자를 자동으로 해석하거나, 별칭(alias)을 통해 경로를 쉽게 참조할 수 있습니다.</p>
<hr />

<ol>
<li>alias</li>
</ol>
<ul>
<li><p>설명: 모듈 경로에 별칭을 정의하여 코드에서 간편하게 사용할 수 있습니다. 예를 들어, 긴 경로를 짧게 줄이거나, 특정 디렉토리를 간편하게 참조할 수 있도록 설정합니다.</p>
</li>
<li><p>예시</p>
<pre><code class="language-js">  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src'), // '@'를 'src' 디렉토리로 설정
      '@components': path.resolve(__dirname, 'src/components'), // '@components'를 'src/components'로 설정
    }
  }</code></pre>
</li>
<li><p>적용 예시</p>
<pre><code class="language-js">  import MyComponent from '@components/MyComponent.vue';</code></pre>
</li>
</ul>
<hr />

<ol start="2">
<li>extensions</li>
</ol>
<ul>
<li><p>설명: 모듈을 해석할 때 자동으로 인식할 파일 확장자를 지정합니다. 이 설정을 통해 파일 확장자를 생략할 수 있습니다. 예를 들어, .js 또는 .vue와 같은 확장자를 명시하지 않아도 파일을 찾을 수 있도록 합니다.</p>
</li>
<li><p>예시</p>
<pre><code class="language-js">  resolve: {
    extensions: ['.js', '.vue', '.json'] // 이 순서대로 확장자를 해석
  }</code></pre>
</li>
<li><p>적용 예시</p>
<pre><code class="language-js">  import MyComponent from '@/components/MyComponent'; // .js 또는 .vue 확장자를 생략 가능</code></pre>
</li>
</ul>
<hr />

<ol start="3">
<li>modules</li>
</ol>
<ul>
<li><p>설명: 모듈 해석 시 기본적으로 참조할 디렉토리 목록을 정의합니다. 이 설정을 통해 node_modules 외의 디렉토리에서 모듈을 찾을 수 있습니다.</p>
</li>
<li><p>예시</p>
<pre><code class="language-js">  resolve: {
    modules: [path.resolve(__dirname, 'src'), 'node_modules'] // 'src'와 'node_modules'에서 모듈 검색
  }</code></pre>
</li>
<li><p>적용 예시</p>
<pre><code class="language-js">  import SomeUtility from 'utils/someUtility'; // 'src/utils/someUtility'에서 모듈 검색</code></pre>
</li>
</ul>
<hr />

<ol start="4">
<li>fallback</li>
</ol>
<ul>
<li><p>설명: 특정 모듈을 찾을 수 없을 때 대체할 경로를 정의합니다. Node.js의 핵심 모듈이나 특정 라이브러리가 없는 경우 대체 모듈을 사용하도록 할 수 있습니다.</p>
</li>
<li><p>예시</p>
<pre><code class="language-js">  resolve: {
    fallback: {
      crypto: require.resolve('crypto-browserify'), // Node.js 'crypto' 모듈 대신 'crypto-browserify' 사용
    }
  }</code></pre>
</li>
</ul>
<hr />

<ol start="5">
<li>symlinks</li>
</ol>
<ul>
<li><p>설명: 심볼릭 링크를 따라가서 실제 경로를 해석할지 여부를 설정합니다. 기본값은 true로, 심볼릭 링크를 따라가서 모듈을 해석합니다.</p>
</li>
<li><p>예시</p>
<pre><code class="language-js">  resolve: {
    symlinks: false // 심볼릭 링크를 무시하고 실제 경로가 아닌 링크된 경로 그대로 사용
  }</code></pre>
</li>
</ul>
<hr />

<ol start="6">
<li>mainFiles</li>
</ol>
<ul>
<li><p>설명: 디렉토리의 모듈을 해석할 때 기본적으로 찾을 파일 이름을 정의합니다. index 파일 외에 다른 파일을 기본 엔트리로 사용할 수 있습니다.</p>
</li>
<li><p>예시</p>
<pre><code class="language-js">  resolve: {
    mainFiles: ['index', 'main'] // 'index'와 'main' 파일을 기본으로 사용
  }</code></pre>
</li>
</ul>
<hr />

<ol start="7">
<li>mainFields</li>
</ol>
<ul>
<li><p>설명: 패키지의 package.json에서 모듈을 찾을 때 우선적으로 참조할 필드를 정의합니다. 주로 라이브러리에서 브라우저, 모듈 시스템 등을 구분하여 적절한 파일을 선택하는 데 사용됩니다.</p>
</li>
<li><p>예시</p>
<pre><code class="language-js">  resolve: {
    mainFields: ['browser', 'module', 'main'] // 브라우저 환경에서 'browser' 필드를 우선적으로 사용
  }</code></pre>
</li>
</ul>
<hr />

<ol start="8">
<li>resolveLoader</li>
</ol>
<ul>
<li><p>설명: Webpack의 로더(loader) 모듈의 위치를 설정합니다. 로더의 경로를 재정의할 때 사용됩니다.</p>
</li>
<li><p>예시</p>
<pre><code class="language-js">  resolve: {
    modules: [path.resolve(__dirname, 'loaders'), 'node_modules'] // 커스텀 로더를 정의한 디렉토리와 'node_modules'에서 로더 검색
  }</code></pre>
</li>
</ul>
<hr />

<ol start="9">
<li>descriptionFiles</li>
</ol>
<ul>
<li><p>설명: 모듈을 해석할 때 참고할 파일의 이름을 지정합니다. 기본값은 ['package.json']입니다.</p>
</li>
<li><p>예시</p>
<pre><code class="language-js">  resolve: {
    descriptionFiles: ['package.json', 'bower.json'] // 'package.json'과 'bower.json' 파일을 참조하여 모듈 해석
  }</code></pre>
</li>
</ul>
<hr />

<h3 id="chainwebpack--vuecli">chainWebpack / (Vue/Cli)</h3>
<p><a href="https://cli.vuejs.org/guide/webpack.html#chaining-advanced">Vue/Cli "ChainWebpack"옵션 공식문서 바로가기</a></p>
<p><strong>Vue CLI</strong></p>
<p><code>chainWebpack</code>은 Vue CLI에서 제공하는 기능으로, Webpack 설정을 보다 직관적이고 체계적으로 구성하기 위해 Vue CLI 팀이 만든 것입니다. Vue CLI는 Vue.js 프로젝트의 설정과 관리를 간편하게 하기 위해 만들어진 툴이므로, Webpack 설정을 다루는 데 있어서도 사용자 편의를 고려해 <code>chainWebpack</code> 같은 기능을 제공하고 있습니다.</p>
<hr />

<p><strong>webpack-chain 라이브러리</strong></p>
<p>Vue CLI에 내장된 <code>chainWebpack</code> 기능은 <code>webpack-chain</code>이라는 라이브러리를 기반으로 작동합니다. <code>webpack-chain</code>은 Webpack 설정을 체인 방식으로 구성할 수 있게 해주는 라이브러리입니다. <code>chainWebpack</code> 함수는 이 라이브러리의 API를 사용하여 Webpack 설정을 조작합니다.</p>
<hr />

<p>chainWebpack은 Vue CLI에서 제공하는 고급 Webpack 설정 옵션입니다. Webpack 설정을 좀 더 세밀하게 조작할 수 있도록 돕는 도구인 webpack-chain을 사용합니다. chainWebpack을 사용하면 Webpack 설정을 코드로 체인처럼 연결해 구성할 수 있습니다. 이는 Webpack 설정을 직접 수정하는 것보다 더 유연하고 가독성 있는 방식으로 Webpack 설정을 구성할 수 있도록 해줍니다.</p>
<p>chainWebpack 옵션은 함수 형태로 정의됩니다. 이 함수는 Webpack 설정을 조작할 수 있는 체인(객체)을 인자로 받습니다. 이 체인 객체를 통해 Webpack의 다양한 설정을 체인 방식으로 수정하거나 추가할 수 있습니다.</p>
<p><strong>예시</strong></p>
<pre><code class="language-js">module.exports = {
  chainWebpack: config =&gt; {

    // 예시: Vue 컴파일러 인라인 사용
    config.resolve.alias
      .set('@', path.resolve(__dirname, 'src'))
      .set('vue$', 'vue/dist/vue.esm.js');

    // 예시: 특정 로더 수정
    config.module
      .rule('vue')
      .use('vue-loader')
      .loader('vue-loader')
      .tap(options =&gt; {
        // Vue 로더의 옵션을 변경
        return {
          ...options,
          compilerOptions: {
            preserveWhitespace: false
          }
        };
      });

    // 예시: 플러그인 추가
    config
      .plugin('html')
      .tap(args =&gt; {
        args[0].title = 'My Custom Title';
        return args;
      });
  }
};</code></pre>
<hr />

<blockquote>
<ol>
<li>Alias 설정</li>
</ol>
</blockquote>
<p>경로 별칭을 설정하여 코드에서 더 짧고 명확한 경로를 사용할 수 있게 합니다.</p>
<pre><code class="language-js">config.resolve.alias
  .set('@components', path.resolve(__dirname, 'src/components'))
  .set('@views', path.resolve(__dirname, 'src/views'));</code></pre>
<hr />

<blockquote>
<ol start="2">
<li>Loaders 설정</li>
</ol>
</blockquote>
<p>Webpack 로더를 추가하거나 수정합니다. 예를 들어, 특정 파일 유형에 대해 다른 로더를 추가하거나, 기존 로더의 옵션을 수정할 수 있습니다.</p>
<pre><code class="language-js">config.module
  .rule('images')
  .use('url-loader')
  .loader('url-loader')
  .tap(options =&gt; {
    return {
      ...options,
      limit: 10240
    };
  });</code></pre>
<hr />

<blockquote>
<ol start="3">
<li>Plugins 설정</li>
</ol>
</blockquote>
<p>Webpack 플러그인을 추가하거나 수정합니다. 기본적으로 Vue CLI에서 제공하는 플러그인의 옵션을 변경할 수 있습니다.</p>
<pre><code class="language-js">config.plugin('html')
  .tap(args =&gt; {
    args[0].meta = { viewport: 'width=device-width,initial-scale=1,user-scalable=no' };
    return args;
  });</code></pre>
<hr />

<blockquote>
<ol start="4">
<li>Optimization 설정</li>
</ol>
</blockquote>
<p>코드 스플리팅, 미니피케이션 등 Webpack의 최적화 옵션을 세밀하게 조정할 수 있습니다.</p>
<pre><code class="language-js">config.optimization
  .splitChunks({
    chunks: 'all'
  });</code></pre>
<hr />

<blockquote>
<ol start="5">
<li>로더 추가</li>
</ol>
</blockquote>
<p>새로운 로더를 추가할 수 있습니다. 예를 들어, .md 파일을 로드하기 위한 로더를 추가할 수 있습니다.</p>
<pre><code class="language-js">config.module
  .rule('markdown')
  .test(/\.md$/)
  .use('raw-loader')
  .loader('raw-loader')
  .end();</code></pre>
<hr />

<p><strong>장점</strong></p>
<ul>
<li><p>유연성 : Webpack 설정의 각 부분을 세밀하게 조작할 수 있어, 복잡한 빌드 요구 사항에 대응할 수 있습니다.</p>
</li>
<li><p>가독성 : 체인 메서드로 설정을 표현하므로, 설정 변경을 쉽게 추적할 수 있습니다.</p>
</li>
</ul>
<hr />

<p>🕵️ vue-loader 란?</p>
<p>vue-loader는 Vue.js에서 .vue 파일을 Webpack과 같은 모듈 번들러에서 처리할 수 있도록 도와주는 핵심 로더(Loader)입니다. .vue 파일은 Vue.js에서 사용되는 파일 형식으로, 하나의 파일 안에 HTML, JavaScript, 그리고 CSS를 함께 작성할 수 있는 Vue 컴포넌트 파일을 의미합니다.</p>
<hr />

<h3 id="css-css-modules--vuecli">CSS (CSS Modules) / (Vue/Cli)</h3>
<p><a href="https://cli.vuejs.org/guide/css.html#css-modules">Vue/Cli "CSS Modules"옵션 공식문서 바로가기</a></p>
<p>css 옵션은 Vue CLI에서 프로젝트의 CSS 관련 설정을 커스터마이즈하는 데 사용되는 옵션입니다. 이 옵션을 통해 CSS 전처리기(SASS, LESS, Stylus 등)를 설정하거나, CSS 모듈화, 자동 벤더 프리픽스 등을 쉽게 관리할 수 있습니다.</p>
<p><strong>css 옵션의 구조</strong></p>
<p>vue.config.js 파일에서 css 옵션을 설정할 수 있으며, 다양한 세부 속성을 통해 CSS와 관련된 여러 동작을 정의할 수 있습니다.</p>
<pre><code class="language-js">module.exports = {
  css: {
    // CSS 파일에 대한 설정을 관리
  }
};</code></pre>
<blockquote>
<ol>
<li>modules</li>
</ol>
</blockquote>
<p>CSS 모듈을 활성화할지 여부를 설정합니다. CSS 모듈을 활성화하면 각 컴포넌트에서 로컬 범위의 CSS 클래스를 사용할 수 있습니다.</p>
<pre><code class="language-js">css: {
  modules: true
}</code></pre>
<hr />

<p>🕵️ CSS 모듈이란?</p>
<p>CSS 모듈을 활성화하면 각 컴포넌트의 CSS가 로컬 스코프에서 동작하게 되어, 클래스 이름 충돌을 방지할 수 있습니다. 이를 통해 각 Vue 컴포넌트에서 독립적으로 스타일을 적용하고 관리할 수 있습니다.</p>
<p>기본적으로 Vue CLI에서는 CSS 모듈이 자동으로 활성화되지 않으며, 사용자가 직접 modules: true 옵션을 설정해야 CSS 모듈 기능을 사용할 수 있습니다.</p>
<hr />

<blockquote>
<ol start="2">
<li>extract</li>
</ol>
</blockquote>
<p>개발 환경에서 CSS를 <code>&lt;style&gt;</code> 태그로 인라인 처리할지, 또는 별도의 CSS 파일로 추출할지 결정합니다.
기본적으로 프로덕션 환경에서는 CSS가 별도의 파일로 추출되지만, 개발 환경에서는 인라인 처리됩니다.</p>
<pre><code class="language-js">css: {
  extract: process.env.NODE_ENV === 'production'
}</code></pre>
<p><strong>개발 환경에서 인라인 처리 (extract: false)</strong></p>
<ul>
<li><p>장점 : 빠른 빌드 및 빠른 리로드: 개발 중에는 CSS 파일을 추출하는 대신 인라인 처리되어 빠르게 스타일 변경 사항을 확인할 수 있습니다.
Hot Module Replacement(HMR): CSS 수정 시 페이지를 리로드하지 않고 스타일만 새로고침할 수 있습니다.</p>
</li>
<li><p>단점: CSS가 인라인 처리되므로 HTML 파일의 크기가 커질 수 있습니다.</p>
</li>
</ul>
<p><strong>프로덕션 환경에서 CSS 파일 추출 (extract: true)</strong></p>
<ul>
<li><p>장점: 성능 최적화: CSS를 별도의 파일로 추출함으로써 브라우저가 파일을 캐싱할 수 있고, 페이지 로드 시 필요한 리소스만 로드됩니다.
파일 크기 최적화: 불필요한 중복 스타일을 제거하고 CSS를 최소화하여 파일 크기를 줄일 수 있습니다.</p>
</li>
<li><p>단점: 빌드 과정에서 CSS를 추출하는 데 시간이 더 소요될 수 있습니다.</p>
</li>
</ul>
<p><strong>실제 예시</strong></p>
<p>개발 환경 (extract: false)</p>
<p>HTML 파일에 <code>&lt;style&gt;</code> 태그가 포함됩니다.
CSS 코드가 HTML의 <code>&lt;head&gt;</code> 태그 안에 삽입되어 빠르게 수정된 스타일을 확인할 수 있습니다.</p>
<pre><code>&lt;head&gt;
  &lt;style&gt;
    .button {
      background-color: blue;
    }
  &lt;/style&gt;
&lt;/head&gt;</code></pre><p>프로덕션 환경 (extract: true)</p>
<p>별도의 CSS 파일로 스타일이 추출됩니다.
브라우저는 main.css와 같은 CSS 파일을 서버에서 로드합니다.</p>
<pre><code>&lt;link rel="stylesheet" href="/static/css/main.css"&gt;</code></pre><p>main.css 파일</p>
<pre><code class="language-css">// main.css 파일
.button {
  background-color: blue;
}</code></pre>
<p>개발 환경에서는 빠른 피드백을 위해 CSS 인라인 처리가 유리하고, 프로덕션 환경에서는 성능 최적화를 위해 별도의 CSS 파일로 추출하는 것이 일반적입니다.</p>
<p>Vue CLI에서 제공하는 extract 옵션을 사용하면 개발과 프로덕션 환경에서 각각의 장점에 맞는 방식을 선택하여 사용할 수 있습니다.</p>
<hr />

<blockquote>
<ol start="3">
<li>sourceMap</li>
</ol>
</blockquote>
<p>CSS 소스맵을 생성할지 여부를 설정합니다.
CSS 소스맵은 개발 시 스타일 디버깅을 쉽게 할 수 있도록 도와줍니다.</p>
<pre><code class="language-js">css: {
  sourceMap: true
}</code></pre>
<hr />

<blockquote>
<ol start="4">
<li>loaderOptions</li>
</ol>
</blockquote>
<p>CSS 전처리기의 추가 설정을 할 수 있습니다.
SASS, LESS, Stylus 등의 전처리기를 사용할 때, 특정 설정을 추가로 전달할 수 있습니다.</p>
<p><strong>예시</strong></p>
<pre><code class="language-js">css: {
    loaderOptions: {
        sass: {
            additionalData: '@import "@/assets/scss/_variables";'
        }
    }
}</code></pre>
<p>이 설정은 SASS에 대한 추가 옵션을 제공하는 것이고, CSS 파일에서 사용할 변수를 미리 불러오기 위해 _variables.scss 파일을 모든 SASS 파일에 포함시키는 것입니다.</p>
<p><strong>_variables.scss</strong></p>
<pre><code class="language-scss">/*== size ==*/
@function rem($px) {
    @return #{calc($px / 16)}rem;
}
$url-sprite: '@/assets/images/';

/*== color ==*/
$white : #FFFFFF;
$blue : #0078B8;
$green : #028C44;
.
.
.생략</code></pre>
<hr />

<p>🕵️CSS 전처리기란?</p>
<p>CSS 전처리기(CSS Preprocessor)는 CSS를 작성하기 전에 더 효율적이고 유연하게 코드를 작성할 수 있게 도와주는 도구입니다. 전처리기를 사용하면 CSS에 변수, 함수, 중첩 규칙, 반복문 등을 사용할 수 있으며, 작성한 코드가 브라우저에서 사용할 수 있는 일반 CSS로 변환됩니다.</p>
<p>전처리기는 CSS의 기본 기능만으로는 해결하기 어려운 문제들을 해결해주고, 스타일 코드의 유지보수를 쉽게 만들어줍니다.</p>
<p><strong>CSS 전처리기가 제공하는 주요 기능</strong></p>
<p>변수(Variables)</p>
<p>색상, 크기, 폰트 등을 변수로 저장하여 중복되는 스타일을 간단히 관리할 수 있습니다.</p>
<pre><code class="language-css">$primary-color: #3498db;

.button {
  background-color: $primary-color;
}</code></pre>
<p>중첩(Nesting)</p>
<p>CSS에서 일반적으로 작성하는 선택자 구조를 더 직관적이고 간결하게 표현할 수 있습니다.</p>
<pre><code class="language-css">.nav {
  ul {
    margin: 0;
    padding: 0;
  }
  li {
    display: inline-block;
  }
}</code></pre>
<p>믹스인(Mixin)</p>
<p>재사용 가능한 스타일 블록을 정의하여 반복적인 스타일을 줄일 수 있습니다.</p>
<pre><code class="language-css">@mixin flex-center {
  display: flex;
  justify-content: center;
  align-items: center;
}

.container {
  @include flex-center;
}</code></pre>
<p>상속(Extend)</p>
<p>CSS 클래스 간에 스타일을 상속받아 중복을 줄일 수 있습니다.</p>
<pre><code class="language-css">.button {
  padding: 10px;
  background-color: blue;
}

.submit-button {
  @extend .button;
  background-color: green;
}</code></pre>
<p>연산(Operations)</p>
<p>CSS에서 사용할 수 없는 수학 연산을 지원합니다.</p>
<pre><code class="language-css">$base-spacing: 10px;

.container {
  margin: $base-spacing * 2;
}</code></pre>
<p>자동 벤더 프리픽스</p>
<p>특정 브라우저에서 CSS 속성을 지원하도록 자동으로 프리픽스를 추가합니다.</p>
<pre><code class="language-css">.box {
  display: flex;
}

// 컴파일 후

.box {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
}</code></pre>
<hr />

<blockquote>
<ol start="5">
<li>requireModuleExtension</li>
</ol>
</blockquote>
<p>파일 이름에 <code>.module</code> 확장자를 요구할지 여부를 설정합니다.
기본적으로 CSS 모듈은 <code>*.module.css</code> 또는 <code>*.module.scss</code> 형식의 파일에서만 적용되도록 제한됩니다. 이 옵션을 false로 설정하면 모든 CSS 파일에서 CSS 모듈을 사용할 수 있습니다.</p>
<hr />

<h3 id="productionsourcemap--vuecli">productionSourceMap / (Vue/Cli)</h3>
<p><a href="https://cli.vuejs.org/config/#productionsourcemap">Vue/Cli "productionsourcemap"옵션 공식문서 바로가기</a></p>
<p>소스 맵은 컴파일된 코드(예: 바벨이나 웹팩을 통해 번들링된 코드)와 원본 소스 코드(예: Vue, ES6, SCSS 등) 사이의 매핑 정보를 제공하는 파일입니다. 소스 맵을 사용하면, 브라우저의 개발자 도구에서 번들된 코드를 디버깅할 때, 컴파일된 코드가 아닌 원본 소스 코드로 디버깅할 수 있게 됩니다.</p>
<p><strong>productionSourceMap 옵션의 역할</strong></p>
<ul>
<li><p>productionSourceMap: <code>true</code> (기본값): 프로덕션 빌드 시 소스 맵을 생성합니다.</p>
</li>
<li><p>productionSourceMap: <code>false</code>: 프로덕션 빌드 시 소스 맵을 생성하지 않습니다.</p>
</li>
</ul>
<p><strong>소스 맵의 장점</strong></p>
<ul>
<li><p>디버깅 편의성: 소스 맵을 통해 배포된 애플리케이션에서 발생한 오류를 브라우저 개발자 도구에서 원본 코드로 디버깅할 수 있습니다.
예를 들어, 번들된 코드에서 오류가 발생해도, 소스 맵을 사용하면 해당 오류가 원래의 Vue 컴포넌트 코드의 어느 위치에서 발생했는지 정확히 알 수 있습니다.</p>
</li>
<li><p>원본 코드 추적: 배포된 번들 파일을 보면 컴파일된 코드만 보여서 추적이 어려울 수 있지만, 소스 맵을 통해 원본 파일과 그 위치를 쉽게 찾을 수 있습니다.</p>
</li>
</ul>
<p><strong>소스 맵의 단점</strong></p>
<ul>
<li><p>보안 이슈: 소스 맵 파일이 포함되면, 원본 소스 코드가 노출될 가능성이 있습니다. 특히 민감한 정보나 내부 로직을 포함한 코드가 소스 맵을 통해 외부에 공개될 수 있어 보안 취약점이 생길 수 있습니다.
소스 맵 파일을 이용하면 누군가가 원본 코드를 역으로 추적할 수 있기 때문에, 중요한 프로젝트에서는 소스 맵을 비활성화하는 것이 일반적입니다.</p>
</li>
<li><p>파일 크기 증가: 소스 맵을 생성하면 그만큼 파일 크기가 커집니다. 소스 맵 파일이 생성되고 서버에 배포되면 사용자가 다운로드할 데이터가 많아질 수 있습니다.</p>
</li>
</ul>
<p><strong>사용 예시</strong></p>
<ul>
<li><p>디버깅이 필요할 때: 프로덕션 환경에서 발생한 문제를 추적하고, 원본 코드로 문제를 디버깅하고자 할 때 유용합니다. 하지만, 보안을 고려해야 하므로 사내 서버에서만 소스 맵을 접근 가능하게 하는 등 추가 조치가 필요합니다.</p>
</li>
<li><p>보안이 중요한 경우: 민감한 애플리케이션에서는 프로덕션 빌드에서 소스 맵을 비활성화(productionSourceMap: false)하여 코드 노출 위험을 방지하는 것이 좋습니다.</p>
</li>
</ul>
<hr />

<h3 id="transpiledependencies--vuecli">transpileDependencies / (Vue/Cli)</h3>
<p><a href="https://cli.vuejs.org/config/#transpiledependencies">Vue/Cli "transpiledependencies"옵션 공식문서 바로가기</a></p>
<p>transpileDependencies 옵션은 Vue CLI에서 특정 의존성(dependencies을 트랜스파일(컴파일하도록 설정하는 옵션입니다. 이 옵션을 사용하면 주로 최신 JavaScript 문법(ES6 이상)을 사용한 외부 패키지를 트랜스파일하여, 구형 브라우저에서도 호환되도록 할 수 있습니다.</p>
<p><strong>기본 동작</strong></p>
<p>Vue CLI는 기본적으로 node_modules에 있는 의존성 패키지들은 트랜스파일하지 않습니다. 대부분의 경우, 외부 패키지들은 이미 ES5 버전으로 컴파일되어 배포되기 때문입니다. 그러나, 일부 패키지들은 ES6 이상의 문법을 사용한 채로 배포될 수 있으며, 이 경우 해당 패키지를 트랜스파일해줘야 구형 브라우저에서도 동작하게 됩니다.</p>
<p><strong>예시 설명</strong></p>
<ul>
<li><p>패키지 이름: 배열에 특정 패키지 이름을 추가하면 해당 패키지가 트랜스파일되도록 지정할 수 있습니다.</p>
</li>
<li><p>정규 표현식: 정규 표현식을 사용하여 특정 패키지 경로 또는 여러 패키지를 트랜스파일할 수 있습니다.</p>
</li>
</ul>
<pre><code class="language-js">transpileDependencies: [/node_modules[/\\]some-regex-package/]</code></pre>
<p><strong>예시2</strong></p>
<pre><code class="language-js">module.exports = {
  transpileDependencies: [
    'vue-echarts', // 최신 문법 사용 가능성이 있는 라이브러리
    'resize-detector' // 또 다른 의존성
  ]
};</code></pre>
<p><strong>주의할 점</strong></p>
<ul>
<li><p>빌드 시간 증가: transpileDependencies에 추가된 패키지는 트랜스파일을 거치기 때문에 빌드 시간이 증가할 수 있습니다.</p>
</li>
<li><p>트랜스파일러 설정: Vue CLI는 기본적으로 Babel을 사용해 트랜스파일을 처리하지만, 프로젝트에 맞게 Babel 설정이 올바르게 구성되어 있는지 확인해야 합니다.</p>
</li>
</ul>
<hr />