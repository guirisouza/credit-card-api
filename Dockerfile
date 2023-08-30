FROM python:3.11-slim-buster

ENV PYTHONPATH = /
COPY ./database /database
COPY ./src /src
COPY ./requirements.txt /
COPY ./main.py /


WORKDIR /

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "--factory", "main:get_app", "--host", "0.0.0.0", "--port", "8000",  "--reload"]