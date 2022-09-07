FROM python:3.9

WORKDIR /code

RUN pip install --upgrade pip
RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock /code/
COPY ./src/backend /code/backend
COPY ./src/backend/model.clf /code/
COPY ./src/backend/toxic.csv /code/

RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

RUN npm install
RUN npm run build

EXPOSE 8000
  
# CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
