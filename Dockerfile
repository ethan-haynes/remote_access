FROM python:alpine3.7

LABEL maintainer="Ethan Haynes <ethanhaynes@alumni.harvard.edu>"

RUN mkdir /etc/remote_access

COPY getdiskusage.py /etc/remote_access/getdiskusage.py

EXPOSE 9999

CMD ["python3", "/etc/remote-tools/getdiskusage.py"]
