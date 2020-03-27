FROM python:3.7

RUN apt install -y git

RUN pip install gitpython

# Copy SSH key for git private repos
ADD .ssh/id_rsa /root/.ssh/id_rsa
RUN chmod 600 /root/.ssh/id_rsa

WORKDIR /code