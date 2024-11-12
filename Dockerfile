
FROM python:3.12.2-alpine

COPY . /app
WORKDIR /app
RUN pip install poetry==1.8.4
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

CMD [ "poetry","run","-vvv","python", "main.py" ]
