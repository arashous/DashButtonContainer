FROM python:2.7

RUN apt-get update && apt-get install -y vim tcpdump
RUN pip install scapy

# script for container to run
RUN mkdir -p /root/files
ADD /files/ /root/files/

CMD ["python", "/root/files/listen-for-dash-button.py"]
