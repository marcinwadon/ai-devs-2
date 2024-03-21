from api import fetchToken, fetchTask, sendAnswer
from importlib import import_module

def read(name: str) -> dict:
    print("Reading " + name)

    token = fetchToken(name)
    fetchTask(token)

def solve(name: str):
    print("Solving " + name)

    token = fetchToken(name)
    task = fetchTask(token)
    answer = makeAnswer(name, task)
    result = sendAnswer(answer, token)

def makeAnswer(name: str, input: dict) -> dict:
    task = import_module('tasks.' + name)
    return task.main(input)

