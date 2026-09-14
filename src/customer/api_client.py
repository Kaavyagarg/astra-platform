import requests
import logging
logger = logging.getLogger(__name__)
#"Astra, go ask this website something. When it answers, tell me whether the request succeeded or failed."
def get_url_status(url):
    response = requests.get(url) #Go to this URL and give me whatever answer the server sends back. Store that answer in response
    return response.status_code

def get_url_data(url):
    try:
        response = requests.get(url,timeout = 5)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as error: #handled/logged this error, but I still want the error to reach the caller.
        logger.error('API request failed: %s', error)
        raise
