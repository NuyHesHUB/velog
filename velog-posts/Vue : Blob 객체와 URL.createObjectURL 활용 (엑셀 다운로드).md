<blockquote>
<p>해당 유저의 리스트를 POST 메서드의 body에 담아 전송하고, 엑셀 파일을 다운로드하는 기능을 구현해야 했다.</p>
</blockquote>
<p>예 )</p>
<pre><code class="language-ts">export const download = (mngNo: string, uuId: string, memberList: Member[]) =&gt; {
    return axios.post('/api/lrn/anls/stdnt/act/excel', memberList, {
        params: {
            lrnAnlsMngNo: mngNo,
            userUuid: uuId,
            sche: sche
        },
        responseType: 'blob'
    })
}</code></pre>
<blockquote>
<p>위 <code>download</code> 의 <code>response</code> 데이터</p>
</blockquote>
<pre><code>[Content_Types].xml­”MnÂ0…÷=Eä-J]TUEÂ¢´Ë©ôÓxB,Ûò˜¿Ûw(ª* ª`+™7ï{žÄO¶IÖH;›‹Q6</code></pre><hr />

<h3 id="🕵️-blob-란">🕵️ Blob 란?</h3>
<p><strong>Binary Large Object</strong>의 약자로, JavaScript에서 파일 데이터와 같은 대용량 바이너리 데이터를 다루기 위해 사용되는 객체입니다. Blob 객체는 파일, 이미지, 비디오 등의 바이너리 데이터를 저장하고 조작할 수 있습니다.</p>
<ul>
<li><p>기능: 데이터 저장: Blob 객체는 바이너리 데이터를 저장할 수 있습니다.</p>
</li>
<li><p>타입 지정: Blob 객체는 MIME 타입을 지정할 수 있어, 데이터의 형식을 명확히 할 수 있습니다.</p>
</li>
<li><p>URL 생성: window.URL.createObjectURL(blob) 메서드를 사용하여 Blob 데이터를 가리키는 URL을 생성할 수 있습니다. 이 URL은 <code>&lt;a&gt;</code> 태그의 href 속성에 사용되어 파일 다운로드를 트리거할 수 있습니다</p>
</li>
</ul>
<hr />

<p>위 download 함수 응답 데이터를 _downloadExel 유틸함수에 response 값과 파일이름을 전달한다.</p>
<pre><code class="language-typescript">const _downloadExel = (response: AxiosResponse&lt;Blob&gt;, fileName: string): void =&gt; {
    const blob = new Blob(
        [response.data], 
        { 
            type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' 
        }
    );

    const downloadLink = document.createElement('a') as HTMLAnchorElement;
    const downloadURL = window.URL.createObjectURL(blob) as string;
    const fullFileName = `${fileName}.xlsx` as string;

    downloadLink.download = fullFileName;
    downloadLink.href = downloadURL;
    downloadLink.click();
    downloadLink.remove();
};</code></pre>
<p>blob라는 변수로 새로운 Blob 객체를 사용하여 response의 데이터와 파일명을 만들어서 넣어준다. (간단하게 프론트단에서 추가하지만 B/E 에서 Response Header로 파일명을 받을 수도 있다.) </p>
<p>ex) <code>const header = response.headers['content-disposition'] as string;</code></p>
<p><code>document.createElement('a') as HTMLAnchorElement;</code> 를 사용하여 <code>&lt;a&gt;</code> 태그를 동적으로 생성한다.</p>
<p>그리고 Blob URL 을 <code>&lt;a&gt;</code> 태그에 할당하고 다운로드링크로 사용이 되며 다운로드가 된다. </p>
<p>다운로드 후 생성된 <code>&lt;a&gt;</code> 태그는 제거한다. </p>
<hr />

<h3 id="🕵️-new-blob-생성자">🕵️ new Blob 생성자</h3>
<pre><code class="language-js">new Blob ( parts, options )</code></pre>
<p>매개변수 </p>
<blockquote>
<ol>
<li>parts</li>
</ol>
</blockquote>
<pre><code>Blob을 구성할 데이터를 담고 있는 배열입니다.
여기에서는 response.data (파일의 바이너리 데이터)를 배열 형태로 전달하고 있습니다.</code></pre><blockquote>
<ol start="2">
<li>options</li>
</ol>
</blockquote>
<pre><code>Blob의 type (MIME 타입)을 정의합니다.
application/vnd.openxmlformats-officedocument.spreadsheetml.sheet는 Excel 파일의 MIME 타입입니다.</code></pre><hr />

<h3 id="🕵️-mime-타입">🕵️ MIME 타입</h3>
<p>MIME 타입(Multipurpose Internet Mail Extensions)은 인터넷에서 파일의 형식과 목적을 나타내는 표준 형식입니다.
MIME 타입은 주로 웹 브라우저와 서버 간에 데이터의 유형을 식별하고 올바르게 처리할 수 있도록 도와줍니다.</p>
<p>MIME 타입은 두 부분으로 나뉩니다</p>
<ol>
<li><p>타입 (예: text, image, application)</p>
</li>
<li><p>서브타입 (예: html, png, json)</p>
</li>
</ol>
<p><strong>MIME 타입의 주요 카테고리 및 예시</strong></p>
<blockquote>
<ol>
<li>텍스트 데이터</li>
</ol>
</blockquote>
<pre><code>text/plain                # 일반 텍스트 파일
text/html                 # HTML 문서
text/css                  # CSS 스타일시트
text/javascript           # JavaScript 코드
text/csv                  # CSV 파일
text/markdown             # Markdown 문서</code></pre><blockquote>
<ol start="2">
<li>이미지 파일</li>
</ol>
</blockquote>
<pre><code>image/png                 # PNG 이미지
image/jpeg                # JPEG 이미지
image/gif                 # GIF 이미지
image/svg+xml             # SVG 벡터 이미지
image/webp                # WebP 이미지</code></pre><blockquote>
<ol start="3">
<li>비디오 파일</li>
</ol>
</blockquote>
<pre><code>video/mp4                 # MP4 비디오
video/webm                # WebM 비디오
video/ogg                 # Ogg 비디오</code></pre><blockquote>
<ol start="4">
<li>응용 프로그램 데이터 (문서, 바이너리 등)</li>
</ol>
</blockquote>
<pre><code>application/json                              # JSON 데이터
application/javascript                        # JavaScript 파일
application/xml                               # XML 데이터
application/pdf                               # PDF 문서
application/vnd.openxmlformats-officedocument.spreadsheetml.sheet # Excel (XLSX) 파일
application/vnd.openxmlformats-officedocument.wordprocessingml.document # Word (DOCX) 파일
application/zip                               # ZIP 압축 파일
application/x-www-form-urlencoded            # URL 인코딩된 데이터</code></pre><hr />