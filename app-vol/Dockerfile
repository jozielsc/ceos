FROM python:3.7-stretch
WORKDIR /app
ENV FLASK_APP=run.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt --no-cache-dir
EXPOSE 5000
COPY . .
CMD ["flask", "run"]
