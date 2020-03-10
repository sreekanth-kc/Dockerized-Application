FROM python:3.6

EXPOSE 5000

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt


COPY main.py /app
# RUN apk add install memcached -y
CMD python main.py
