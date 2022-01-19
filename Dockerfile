# a Dockerfile specifies how to build a Docker image
# docker hub anaconda3 in google to find image for the anaconda 3 python distribution

FROM ubuntu:20.04

RUN apt-get update && apt-get install -y
RUN apt-get install -y \
    python3 \
    python3-pip

#RUN apt-get install ffmpeg  libsm6 libxext6  -y
#libxrender-dev
#RUN apt-get install python3-opencv -y

RUN pip3 install --upgrade pip 

RUN mkdir -p /server_app/
ADD . /server_app/
RUN ls /server_app/
WORKDIR /server_app/cours03_flask_file/
RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "app.py"]






#FROM tiangolo/uwsgi-nginx-flask
#RUN mkdir -p /server_app/
#ADD . /server_app/
#WORKDIR /server_app/
#ENTRYPOINT ["python", "run_app.py"]