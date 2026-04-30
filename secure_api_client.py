# secure_api_client.py

class SecureAPIClient:
    """
    Minimal pattern for interacting with external APIs from Intelligent Contracts
    without exposing secrets or creating inconsistent outputs across validators.
    """

    def __init__(self, api_key: str):
        # Keep API key private (never returned)
        self._api_key = api_key

    def _request(self, endpoint: str, params: dict = None):
        """
        Simulated external call. In practice, this would:
        - call a weather/price/social API
        - include timeouts and retries
        - normalize responses
        """
        # IMPORTANT: Do not return raw responses or secrets
        return {
            "endpoint": endpoint,
            "data": "normalized_sample_response",
            "status": "ok"
        }

    def fetch_public_data(self, endpoint: str, params: dict = None):
        """
        Public method exposed to contracts.
        Returns sanitized, deterministic-friendly data.
        """
        result = self._request(endpoint, params or {})
        return {
            "data": result["data"],
            "status": result["status"]
        }


# Example usage inside a contract (pattern)
# from genlayer import Contract
#
# class Contract(Contract):
#     def evaluate(self, input_text):
#         client = SecureAPIClient(api_key="ENV_OR_SECURE_STORE")
#         data = client.fetch_public_data("weather/current", {"city": "Sydney"})
#         return f"Weather status: {data['status']}"
