# import requests
# import time
# import os
# import sys
# import subprocess

# prefect_api_url = os.environ.get("PREFECT_API_URL", "http://prefect:4200/api")
# health_check_url = f"{prefect_api_url.strip('/')}/health"

# max_wait_seconds = 120
# check_interval_seconds = 5

# print(f"Waiting for Prefect API server at {health_check_url}...")

# start_time = time.time()
# while time.time() - start_time < max_wait_seconds:
#     try:
#         response = requests.get(health_check_url, timeout=3)

#         if response.status_code == 200:
#             print("Prefect API server is healthy!")
#             process = subprocess.run(sys.argv[1:]) 
#             sys.exit(process.returncode)

#     except requests.exceptions.ConnectionError:
#         print(f"Connection Error. Prefect API not ready yet. Retrying in {check_interval_seconds}s...")
#     except requests.exceptions.Timeout:
#         print(f"Request timed out. Prefect API not ready yet. Retrying in {check_interval_seconds}s...")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}. Retrying in {check_interval_seconds}s...")

#     time.sleep(check_interval_seconds)

# print(f"Error: Prefect API server did not become healthy within {max_wait_seconds} seconds.", file=sys.stderr)
# sys.exit(1)