FROM python:3.8.1-slim-buster

# set worker dir
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    netcat libmagic1 ffmpeg libsm6 libxext6 ghostscript

#python3-opencv
#install dependecies
RUN pip install --upgrade pip
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt --no-cache-dir

COPY . /app

# run entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]
