FROM praekeltfoundation/python-base:3.6-stretch

RUN apt-get update && apt-get install -y netcat libxml2

WORKDIR /app/

COPY requirements.txt /app/requirements/

RUN pip3 install --no-cache-dir -r /app/requirements/requirements.txt

COPY . /app/

EXPOSE 8080

CMD ["uwsgi", "uwsgi.ini"]
