def main(input: str, token: str) -> str:

    return {
        "name": "addUser",
        "description": "Lorem ipsum",
        "parameters": {
            "type": "object",
            "properties": {
                "name": { "type": "string", "description": "Name" },
                "surname": { "type": "string", "description": "Surname" },
                "year": { "type": "integer", "description": "Year" }
            },
            "required": ["name", "surname", "year"]
        }
    }
    
