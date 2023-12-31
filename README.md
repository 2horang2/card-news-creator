# Card News Generator

Card News Generator는 Django 기반의 간단한 웹 애플리케이션입니다. 이 애플리케이션은 MySQL 데이터베이스를 사용하여 카드 뉴스의 제목, 소제목, 내용을 관리하고, 이 정보를 읽어와 동적으로 생성된 이미지를 제공합니다.

## 사용 기술

- Django
- MySQL
- HTML/CSS
- JavaScript

## 설치 및 실행

1. 프로젝트를 클론합니다.

   ```bash
   git clone https://github.com/your-username/card-news-generator.git
   ```

2. 가상 환경을 설정하고 의존성을 설치합니다.

   ```bash
   cd card-news-generator
   python -m venv venv
   source venv/bin/activate  # 또는 venv\Scripts\activate (Windows)
   pip install -r requirements.txt
   ```

3. 데이터베이스 마이그레이션을 수행합니다.

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. 관리자 계정을 생성합니다.

   ```bash
   python manage.py createsuperuser
   ```

5. 개발 서버를 실행합니다.

   ```bash
   python manage.py runserver
   ```

6. 브라우저에서 `http://127.0.0.1:8000/admin/`으로 접속하여 관리자 계정으로 로그인하고 카드 뉴스를 관리합니다.

7. 카드 뉴스 리스트를 확인하려면 `http://127.0.0.1:8000/cardnews/card-list/`로 이동합니다.

## 화면 예시

![Card News List](/path/to/screenshot.png)

## 기여

기여는 언제나 환영입니다. 버그를 발견하거나 기능을 추가하고 싶다면, 이슈를 열거나 풀 리퀘스트를 보내주세요.

## 라이센스

이 프로젝트는 MIT 라이센스에 따라 배포됩니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 확인하세요.
```

위 예시에서는 프로젝트의 주요 섹션, 설치 및 실행 가이드, 사용 기술, 화면 예시, 기여 방법, 라이센스 등을 다루었습니다. 이 예시를 참고하여 자신의 프로젝트에 맞게 내용을 수정하고 추가하세요. 또한, 화면 예시 부분에는 프로젝트 스크린샷이나 프로젝트 관련 이미지를 추가하면 더 시각적으로 풍성한 README를 만들 수 있습니다.