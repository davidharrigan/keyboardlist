FROM python:2
RUN pip install scrapy pymongo
COPY . /miner/
ENTRYPOINT ["/miner/bin/entrypoint.sh"]
