from openai import OpenAI

def main(input: str) -> str:
    chapters = input["blog"]

    client = OpenAI()

    def writeBlogChapter(title: str) -> str:
        output = client.chat.completions.create(
            model="gpt-3.5-turbo-0613",
            messages=[{"role": "user", "content": f"Write a short section in Polish for blog post about: {title}"}],
        )

        return output.choices[0].message.content

    result = [writeBlogChapter(ch) for ch in chapters]

    return result

