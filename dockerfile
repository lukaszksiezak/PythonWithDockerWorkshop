FROM mcr.microsoft.com/azure-functions/python:3.0-python3.8

COPY requirements.txt /
RUN pip install -r /requirements.txt

ENV AzureWebJobsScriptRoot=/home/site/wwwroot

COPY . /home/site/wwwroot
