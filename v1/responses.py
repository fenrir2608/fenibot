import random


def handle_response(message) -> str:
    p_message = message.lower()
    if p_message == 'hello':
        return 'hi'

    if p_message == 'hi':
        return 'hello'

    if p_message == 'roll':
        return str(random.randint(1, 6))

    if p_message == 'fenihelp':
        return "`This is a help message.`"

    #  return 'Yeah, I don\'t know. Try typing "!help".'