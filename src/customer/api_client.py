import requests
#"Astra, go ask this website something. When it answers, tell me whether the request succeeded or failed."
def get_url_status(url):
    response = requests.get(url) #Go to this URL and give me whatever answer the server sends back. Store that answer in response
    return response.status_code

def get_url_data(url):
    response = requests.get(url)
    return response.json()
