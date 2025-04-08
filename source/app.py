from prefect import flow, task 
import time
@task
def say_hello():
    print("Hello, world!")
    return "Hello, world!"

@task
def say_goodbye():
    print("Goodbye, world!")
    return "Goodbye, world!"

@flow(log_prints=True)
def hello_world_flow():
    while 1:
        time.sleep(2)
        hello = say_hello()
        goodbye = say_goodbye()

if __name__ == "__main__":
    hello_world_flow()
