import httpx
import time

from prefect import flow, task # Prefect flow and task decorators


@flow(log_prints=True)
def show_stars(github_repos: list[str]):
    """Flow: Show the number of stars that GitHub repos have"""
    for repo in github_repos:
        # Call Task 1
        repo_stats = fetch_stats(repo)

        # Call Task 2
        stars = get_stars(repo_stats)

        # Print the result
        print(f"{repo}: {stars} stars")


@task(retries=10, retry_delay_seconds=3)
def fetch_stats(github_repo: str):
    """Task 1: Fetch the statistics for a GitHub repo"""
    url = f"https://github.com/chinnnawat/demo-prefect"
    response = httpx.get(url)
    response.raise_for_status()
    return response.json()


@task
def get_stars(repo_stats: dict):
    """Task 2: Get the number of stars from GitHub repo statistics"""
    return repo_stats['stargazers_count']


# Run the flow
if __name__ == "__main__":
    time.sleep(5)
    show_stars([
        "PrefectHQ/prefect",
        "pydantic/pydantic",
        "huggingface/transformers"
    ])