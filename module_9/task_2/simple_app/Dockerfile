FROM python:3.7.9-slim-stretch

RUN mkdir /app

COPY . /app/

RUN python -m pip install -r /app/requirements.txt

WORKDIR /app

ENTRYPOINT ["python", "app.py"]