# 베이스 이미지
FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# # 종속성 파일 복사
COPY ./poetry.lock /mini_project/
COPY ./pyproject.toml /mini_project/

# 작업 디렉토리 설정
WORKDIR /mini_project

# 종속성 설치
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install
RUN poetry add gunicorn

# 애플리케이션 코드 복사
COPY ./app /mini_project/app
WORKDIR /mini_project/app

# Gunicorn을 사용하여 애플리케이션 실행
COPY ./scripts /scripts
RUN chmod +x /scripts/run.sh
CMD ["/scripts/run.sh"]
# CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3", "--timeout", "120", "--access-logfile", "-", "--error-logfile", "-", "--log-level", "debug"]
