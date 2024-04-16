FROM golang

WORKDIR /app
SHELL ["/bin/bash","-c"]

COPY . .

#Subfinder
RUN go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
#DNSX
RUN go install -v github.com/projectdiscovery/dnsx/cmd/dnsx@latest
#httpx
RUN go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest

# Install Python 3 and pip3
RUN apt-get update && \
    apt-get install -y python3 python3-pip

RUN pip3 install --no-cache-dir --break-system-packages -r requirements.txt




