from langchain_community.llms import Ollama

def extractName(llm, question: str) -> str:
    prompt = """ Return the person name that you find in the following question:
    ###
    {question}
    ###

    Do not return any comment or side note, just the name.

    """

    name = llm.invoke(prompt.format(question=question)).strip()

    if len(name.split()) == 1:
        return name
    else:
        return extractName(llm, question)

def main(input: str, token: str) -> str:

    question = input["question"]
    store = input["input"]

    llm = Ollama(model="llama2")

    name = extractName(llm, question)

    facts = list(filter(lambda k: name in k, store))

    prompt = """
    Answer the question based only on the following context:
    ###
    {facts}
    ###

    Do not return any comment or side not, just the answer.
    Answer in Polish.

    Question: {question}

    """

    answer = llm.invoke(prompt.format(facts=facts, question=question)).strip()

    return answer
