FROM python:3.12.8-slim-bullseye

ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID
ARG --add-host host:172.17.0.1
RUN export PATH="/home/vscode/.local/bin:$PATH"

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    #
    # [Optional] Add sudo support. Omit if you don't need to install software after connecting.
    && apt-get update \
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

RUN apt-get update \
    && apt-get -y install --no-install-recommends \
    build-essential curl gnupg gnupg2 gnupg1

# Add Docker's official GPG key:
RUN sudo apt-get update 
RUN sudo apt-get install ca-certificates curl 
RUN sudo install -m 0755 -d /etc/apt/keyrings 
RUN sudo curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc 
RUN sudo chmod a+r /etc/apt/keyrings/docker.asc 
# Add the repository to Apt sources:
RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null 
RUN sudo apt-get update
RUN sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Install mongodb
RUN apt-get update
RUN apt-get install wget
RUN wget -qO - https://www.mongodb.org/static/pgp/server-6.0.asc | apt-key add -
RUN echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/6.0 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-6.0.list
RUN apt-get update
RUN apt-get install -y mongodb-mongosh

RUN pip install poetry


USER $USERNAME
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

# RUN sudo echo '172.17.0.1      host.docker.internal' >> /etc/hosts
