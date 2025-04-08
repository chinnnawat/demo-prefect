FROM python:3.12

WORKDIR /app
COPY . .
COPY requirements.txt /app

RUN pip3 install -r requirements.txt --no-cache-dir

RUN adduser vscode
RUN groupadd docker
RUN usermod -aG docker vscode
