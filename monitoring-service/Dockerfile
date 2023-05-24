FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

RUN mkdir monitoring-service
WORKDIR /monitoring-api
COPY /pyproject.toml /
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install
COPY . .
CMD ["poetry", "run", "gunicorn", "-c", "gunicorn/gunicorn_conf.py", "main:app"]