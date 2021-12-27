FROM ubuntu:18.04

RUN apt-get update
RUN apt install software-properties-common -y
RUN apt-get update && apt-get upgrade -y 
RUN add-apt-repository universe
RUN apt install python3-pip -y
RUN apt-get install libpq-dev -y
RUN apt-get update -y
RUN pip3 install --upgrade pip

COPY . /var/www/calculator-api
RUN pip3 install -r /var/www/calculator-api/requirements.txt

EXPOSE 5000
WORKDIR /var/www/calculator-api
CMD [ "uwsgi", "app.ini" ]