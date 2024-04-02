import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from openai import OpenAI

def main(input: str, token: str) -> str:

    doc = input["input"]
    question = input["question"]

    msg = input["msg"]

    def fetchWithBackoff(url, maxRetries=5, backoffFactor=1):
        retryStrategy = Retry(
            total=maxRetries,
            status_forcelist=[403, 500],
            backoff_factor=backoffFactor
        )

        adapter = HTTPAdapter(max_retries=retryStrategy)

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
        }

        session = requests.Session()
        session.mount("http://", adapter)
        session.mount("https://", adapter)

        response = session.get(url, headers=headers)

        return response

    response = fetchWithBackoff(doc)

    context = response.content

    prompt = """
    {msg}

    Context:
    {context}
    """

    client = OpenAI()

    answer = client.chat.completions.create(
        model="gpt-3.5-turbo-0613",
        messages=[
            { "role": "system", "content": prompt.format(msg=msg, context=context) },
            { "role": "user", "content": question}
        ]
    )

    return answer.choices[0].message.content
