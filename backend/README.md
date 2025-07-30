1단계: 설치 및 초기화
먼저, 프로젝트에 Alembic을 설치하고 기본 구조를 생성합니다.

Alembic 설치
터미널에서 아래 명령어를 실행하여 alembic을 설치합니다.

pip install alembic

Alembic 초기화
프로젝트의 최상위 루트 디렉토리(.env 파일이 있는 위치)에서 아래 명령어를 실행합니다.

alembic init alembic

이 명령을 실행하면, 프로젝트에 alembic이라는 폴더와 alembic.ini 파일이 생성됩니다.

2단계: 설정 파일 수정
Alembic이 우리 프로젝트의 데이터베이스와 모델을 인식할 수 있도록 2개의 파일을 수정해야 합니다.

alembic.ini 파일 수정
이 파일은 Alembic의 메인 설정 파일입니다. sqlalchemy.url 부분을 찾아서, 우리 프로젝트의 데이터베이스 연결 정보를 사용하도록 수정합니다. .env 파일의 DATABASE_URL을 직접 입력해주면 됩니다.

# alembic.ini 파일

# ... (다른 설정들) ...

# 데이터베이스 연결 URL을 .env 파일의 내용과 동일하게 설정
sqlalchemy.url = postgresql://test:test123%21%40%23@localhost:5432/bookmark

alembic/env.py 파일 수정
이 파일은 마이그레이션을 실행할 때 Alembic이 참조하는 환경 설정입니다. Alembic이 우리 FastAPI 프로젝트의 SQLAlchemy 모델(User, Bookmark 등)을 자동으로 감지하도록 설정해야 합니다.

파일 상단에 from app.db.models.base import Base를 추가합니다.

target_metadata = None 이라고 된 부분을 찾아서 target_metadata = Base.metadata로 수정합니다.

이렇게 하면 Alembic이 BaseModel을 상속받는 모든 모델들을 인식하게 됩니다. (자세한 코드는 아래 업데이트된 Canvas를 참고하세요.)

3단계: 마이그레이션 실행 (워크플로우)
이제 모든 설정이 끝났습니다. 앞으로 데이터베이스 스키마를 변경할 때는 아래와 같은 흐름을 따릅니다.

최초 마이그레이션 파일 생성
alembic revision --autogenerate -m "Initial migration"

--autogenerate: 현재 모델 코드와 DB 상태를 비교해 변경 스크립트를 자동으로 생성합니다.

-m "...": 이 변경사항이 무엇인지 메시지를 남깁니다. (Git 커밋 메시지와 비슷합니다)

이 명령을 실행하면 alembic/versions/ 폴더 안에 마이그레이션 스크립트 파일(..._initial_migration.py)이 생성됩니다.

데이터베이스에 적용
alembic upgrade head

upgrade head: 가장 최신 버전의 마이그레이션 스크립트를 데이터베이스에 적용합니다.

이 명령을 실행하면 실제 DB에 users와 bookmarks 테이블이 생성됩니다.

모델 변경 후 (예: 컬럼 추가)
만약 나중에 Bookmark 모델에 tag 컬럼을 추가했다면, 다시 1번과 2번을 반복하면 됩니다.

alembic revision --autogenerate -m "Add tag column to bookmark"

alembic upgrade head

이제 더 이상 main.py의 create_all 코드는 필요 없으므로 삭제합니다.