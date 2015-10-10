FROM python:2
RUN pip install scrapy pymongo requests
COPY . /miner/
ENTRYPOINT ["/miner/bin/entrypoint.sh"]
