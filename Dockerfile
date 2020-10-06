FROM python:3.8-slim-buster
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y make && rm -rf /var/lib/apt/lists/*
COPY requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip livereload==2.6.2 -r /tmp/requirements.txt
WORKDIR /doc
ENTRYPOINT ["./run.sh"]
CMD ["build"]
