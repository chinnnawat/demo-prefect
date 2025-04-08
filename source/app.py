from prefect import flow, task 
import time

@flow()
def hello_world_flow():
    for _ in range(10):
        time.sleep(2)
        say_goodbye()
        say_hello()

@task
def say_hello():
    print("Hello, world!")
    return "Hello, world!"

@task
def say_goodbye():
    print("Goodbye, world!")
    return "Goodbye, world!"


if __name__ == "__main__":
    time.sleep(5)
    hello_world_flow()
