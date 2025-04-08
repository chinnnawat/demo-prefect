FROM python:3.12

WORKDIR /app

# RUN apt update && apt install -y curl 2ping iputils-ping

# RUN pip3 install -U prefect==2.20.16

COPY . .

# display standard output
ENV PYTHONUNBUFFERED=1
# install dependencies
COPY requirements.txt /app

RUN pip3 install -r requirements.txt --no-cache-dir
RUN pip3 install pylint ipdb

RUN adduser vscode
RUN groupadd docker
RUN usermod -aG docker vscode

CMD ["python3", "app.py"]
