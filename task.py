from api import fetchToken, fetchTask, sendAnswer
from importlib import import_module
from colorama import Fore, Style
import json

async def read(name: str) -> dict:
    print(f"{Fore.BLUE}Reading {Fore.YELLOW}{name} {Fore.BLUE}task{Style.RESET_ALL}")

    token = fetchToken(name)
    fetchTask(token)

async def debug(name: str):
    print(f"{Fore.BLUE}Debugging {Fore.YELLOW}{name} {Fore.BLUE}task{Style.RESET_ALL}")

    token = fetchToken(name)
    task = fetchTask(token)

    print(f"{Fore.BLUE}Making answer{Style.RESET_ALL}")
    answer = makeAnswer(name, task, token)

    print(f"{Fore.GREEN}Answer = {json.dumps(answer)}{Style.RESET_ALL}")

async def solve(name: str):
    print(f"{Fore.BLUE}Solving {Fore.YELLOW}{name} {Fore.BLUE}task{Style.RESET_ALL}")

    token = fetchToken(name)
    task = fetchTask(token)

    print(f"{Fore.BLUE}Making answer{Style.RESET_ALL}")
    answer = makeAnswer(name, task, token)
    print(f"{Fore.GREEN}Answer = {json.dumps(answer)}{Style.RESET_ALL}")

    result = sendAnswer(answer, token)

def makeAnswer(name: str, input: dict, token: str) -> dict:
    task = import_module('tasks.' + name)
    return task.main(input, token)

