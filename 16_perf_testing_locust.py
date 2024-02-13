from locust import HttpUser, task, between


class ApiUser(HttpUser):
    wait_time = between(1, 2)  # Wait time between requests in seconds

    @task
    def get_api_request(self):
        # Define your API endpoint
        api_endpoint = "https://httpbin.org/get"

        # Perform a GET request
        response = self.client.get(api_endpoint)

    @task
    def failed_api_request(self):
        # Define your API endpoint
        api_endpoint = "https://httpbin.org/wrong_endpoint"

        # Perform a GET request
        response = self.client.get(api_endpoint)

# Run Locust with the following command:
# locust -f 16_perf_testing_locust.py
