import requests
import os
from colorama import Fore, Style

baseURL = os.environ['AI_DEVS_BASE_URL']
apiKey = os.environ['AI_DEVS_TOKEN']

def fetchToken(name: str) -> str:
    url = baseURL + "/token/" + name
    response = requests.post(url, json = { 'apikey': apiKey })
    result = response.json()

    if result['code'] != 0:
        print(f"{Fore.RED}{result}{Style.RESET_ALL}")
        exit(-1)
    
    return result['token']

def fetchTask(token: str) -> dict:
    url = baseURL + "/task/" + token
    response = requests.get(url)
    result = response.json()

    print(result)

    return result

def sendAnswer(answer: str, token: str) -> dict:
    url = baseURL + "/answer/" + token
    response = requests.post(url, json = { 'answer': answer })
    result = response.json()

    print(result)

    return result

def sendQuestion(question: str, token: str) -> dict:
    url = baseURL + "/task/" + token
    headers = {'Content-type': 'multipart/form-data'}
    body = dict(question=question)
    print(body)
    response = requests.post(url, data=body)
    result = response.json()

    return result
