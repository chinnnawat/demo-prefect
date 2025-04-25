from prefect import flow, task 
import time
from datetime import timedelta

@task
def my_task():
    print("Hello, world!")
    return "Hello, world!"

@flow
def my_flow():
    my_task()


if __name__ == "__main__":
    time.sleep(5)
    my_flow.serve(name="my-first-deployment", interval=timedelta(seconds=5))