FROM python:3.13.5
WORKDIR /app
COPY . /app/

RUN apt update -y && apt install awscli -y

RUN apt-get update && pip install -r requirements.txt
CMD ["python3","app.py"]