import random


def handle_response(message) -> str:
    # turns the responses to lower cases
    p_message = message.lower()

    # responses to user messages
    if p_message == 'hello' or p_message == 'hi' or p_message == 'sup':
        return 'Hey there'

    if p_message == 'roll':
        # random int between 1 and 6
        return str(random.randint(1, 6))

    if p_message == '!help':
        return 'no'

    # return 'shut up'
