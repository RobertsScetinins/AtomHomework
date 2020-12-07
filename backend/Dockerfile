FROM python:3.7.5-slim
ENV PYTHONBUFFERED 1

WORKDIR /backend

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .