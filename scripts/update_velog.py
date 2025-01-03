import feedparser
import git
import os
import re
from datetime import datetime

# 벨로그 RSS 피드 URL
rss_url = 'https://api.velog.io/rss/@nuyhes'

# 깃허브 레포지토리 경로
repo_path = '.'

# 'velog-posts' 폴더 경로
posts_dir = os.path.join(repo_path, 'velog-posts')

# 'velog-posts' 폴더가 없으면 생성
if not os.path.exists(posts_dir):
    os.makedirs(posts_dir)

# 레포지토리 로드
repo = git.Repo(repo_path)

# RSS 피드 파싱
feed = feedparser.parse(rss_url)

# 각 글을 파일로 저장하고 커밋
for entry in feed.entries:
    # 파일 이름에서 유효하지 않은 문자 제거 또는 대체
    file_name = entry.title
    file_name = file_name.replace('/', '-')  # 슬래시를 대시로 대체
    file_name = file_name.replace('\\', '-')  # 백슬래시를 대시로 대체
    file_name = file_name.strip() # 앞뒤 공백 제거
    file_name = re.sub(r'\?', "", file_name) # 물음표 제거
    file_name += '.md' # 마크다운 파일 확장자 추가
    file_path = os.path.join(posts_dir, file_name) # 파일 경로

    """ if not os.path.exists(file_path) or open(file_path, 'r', encoding='utf-8').read() != entry.description:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(entry.description)

        repo.git.add(file_path)
        repo.git.commit('-m', f'Add post: {entry.title}') """

    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(entry.description)
        repo.git.add(file_path)
        repo.git.commit('-m', f'Add post: {entry.title}')
    elif open(file_path, 'r', encoding='utf-8').read() != entry.description:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(entry.description)
        repo.git.add(file_path)
        repo.git.commit('-m', f'Update post: {entry.title}')

# 최근 10개의 게시물 가져오기
recent_posts = feed.entries[:10]

readme_path = os.path.join(repo_path, 'README.md')
with open(readme_path, 'w', encoding='utf-8') as readme_file:
    readme_file.write('# velog\n\n')
    readme_file.write('## 최근 게시물\n\n')
    readme_file.write('| 제목 | 링크 | 등록 날짜 | 업데이트 날짜 |\n')
    readme_file.write('| --- | --- | --- | --- |\n')
    for post in recent_posts:
        title = post.title
        if len(title) > 50:
            title = title[:50] + '...'
        link = post.link
        published_date = datetime(*post.published_parsed[:6]).strftime('%Y-%m-%d')
        updated_date = datetime(*post.updated_parsed[:6]).strftime('%Y-%m-%d') if 'updated_parsed' in post else published_date

        readme_file.write(f'| {title} | <a href="{link}" target="_blank">바로가기</a> |\n')

# 푸시
repo.git.add(readme_path)
repo.git.commit('-m', 'Update README.md')
repo.git.push()
