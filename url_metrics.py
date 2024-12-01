from prometheus_client import Gauge, start_http_server
import requests
import time

# Define metrics
url_up = Gauge('sample_external_url_up', 'Availability of the external URL', ['url'])
url_response_time = Gauge('sample_external_url_response_ms', 'Response time of the external URL', ['url'])

# List of URLs to monitor
urls = [
    "https://httpstat.us/503",
    "https://httpstat.us/200"
]

def check_url_metrics():
    for url in urls:
        try:
            # Start timing
            start_time = time.time()
            response = requests.get(url, timeout=5)  # Set a 5-second timeout
            response_time_ms = (time.time() - start_time) * 1000  # Convert to milliseconds

            # Update metrics
            url_response_time.labels(url=url).set(response_time_ms)
            url_up.labels(url=url).set(1 if response.status_code == 200 else 0)

            print(f"Checked {url}: UP, Response Time = {response_time_ms:.2f} ms")
        except requests.RequestException as e:
            # Handle errors (e.g., timeout, no response)
            url_response_time.labels(url=url).set(0)  # No response time
            url_up.labels(url=url).set(0)  # Mark as down

            print(f"Checked {url}: DOWN, Error = {e}")

if __name__ == "__main__":
    # Start Prometheus metrics server
    start_http_server(8000)
    print("Prometheus metrics server is running at http://localhost:8000/metrics")

    # Continuously check URLs and update metrics
    while True:
        check_url_metrics()
        time.sleep(10)  # Wait for 10 seconds before checking again
