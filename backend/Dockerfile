FROM python:3.7

WORKDIR /app
COPY . .

RUN pip install pipenv
RUN pipenv install --system

ENV PORT=5000

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app