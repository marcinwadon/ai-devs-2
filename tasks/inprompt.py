from openai import OpenAI
from langchain_community.llms import Ollama

def main(input: str, token: str) -> str:

    question = input["question"]
    store = input["input"]

    llm = Ollama(model="llama2")

    prompt1 = """ Return the person name that you find in the following question:
    ###
    {question}
    ###

    Do not return any comment or side note, just the name.

    """

    name = llm.invoke(prompt1.format(question=question)).strip()

    facts = list(filter(lambda k: name in k, store))

    print(name)
    print(facts)

    prompt2 = """
    Answer the question based only on the following context:
    ###
    {facts}
    ###

    Do not return any comment or side not, just the answer.

    Question: {question}

    """

    answer = llm.invoke(prompt2.format(facts=facts, question=question)).strip()

    return answer
