FROM python:3.7-stretch
ADD . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["run.py"]
