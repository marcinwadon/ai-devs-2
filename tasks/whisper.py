import requests

def useLocal(url: str):
    import whisper

    model = whisper.load_model("large")
    result = model.transcribe(url)

    return result["text"]

def useOpenAI(url: str):
    from openai import OpenAI

    response = requests.get(url)
    with open("mateusz.mp3", "wb") as f:
        f.write(response.content)

    audio = open("mateusz.mp3", "rb")

    client = OpenAI()
    result = client.audio.transcriptions.create(model="whisper-1", file=audio)

    return result.text

def main(input: str, token: str) -> str:
    url = "https://tasks.aidevs.pl/data/mateusz.mp3"

    answer = useLocal(url)

    return answer

