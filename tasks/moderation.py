from openai import OpenAI

def main(input: str, token: str) -> str:
    sentences = input["input"]

    client = OpenAI()

    def moderate(msg: str) -> int:
        response = client.moderations.create(input=msg)
        return int(response.results[0].flagged)

    moderated = [moderate(s) for s in sentences]

    return moderated

