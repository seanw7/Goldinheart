FROM python:3.5-onbuild
MAINTAINER Sean Wilkie

ENV INSTALL_PATH /goldheart
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD gunicorn -b 0.0.0.0:8000 --access-logfile - "goldheart.app:create_app()"
