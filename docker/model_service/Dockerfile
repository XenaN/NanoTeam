FROM python:3.9

WORKDIR /code

RUN pip install --upgrade pip
RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock /code/
COPY ./src/ /code/
COPY ./models/ /code/

RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

EXPOSE 8000

