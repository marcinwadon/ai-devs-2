from openai import OpenAI

def main(input: str, token: str) -> str:
    sentence = input['msg']

    client = OpenAI()

    result = client.embeddings.create(input = ["Hawaiian pizza"], model="text-embedding-ada-002").data[0].embedding

    return result
