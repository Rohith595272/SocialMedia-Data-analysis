import logging
from pyfaktory import Client, Consumer, Job, Producer
import time
import random
import sys

logger = logging.getLogger("faktory test")
logger.propagate = False
logger.setLevel(logging.INFO)
sh = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
sh.setFormatter(formatter)
logger.addHandler(sh)


if __name__ == "__main__":
    boards = [sys.argv[1],sys.argv[2]]  # List of boards to crawl
    print(f"Cold starting catalog crawl for boards {boards}")

    faktory_server_url = "tcp://:password@localhost:7419"

    with Client(faktory_url=faktory_server_url, role="producer") as client:
        producer = Producer(client=client)
        for board in boards:
            job = Job(jobtype="crawl-catalog", args=(board,), queue="crawl-catalog")
            producer.push(job)
