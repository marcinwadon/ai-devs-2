from api import sendQuestion
from openai import OpenAI

def main(input: str, token: str) -> str:

    question = "What is a capital of Poland?"
    response = sendQuestion(question, token)
    answer = response['answer']

    client = OpenAI()

    print(f"Question: {question}")
    print(f"Answer: {answer}")

    content = """
    For the following question: {question} an AI assisstant answered: {answer}.
    Your task is to return YES if the answer is relevant or NO if the answer is not in topic. Do not return anything else than YES or NO.
    """.format(question=question, answer=answer)

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": content}
        ]
    )

    
    result = completion.choices[0].message.content
    print(f"Result: {result}")


    return result
