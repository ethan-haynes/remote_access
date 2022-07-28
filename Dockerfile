FROM python:alpine3.7

LABEL maintainer="Ethan Haynes <ethanhaynes@alumni.harvard.edu>"

RUN mkdir /etc/remote_access

COPY *.py /etc/remote_access/
COPY requirements.txt /etc/remote_access/

EXPOSE 5000

WORKDIR /etc/remote_access
RUN pip3 install -r requirements.txt

CMD ["flask", "run", "--host=0.0.0.0"]
