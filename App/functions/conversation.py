from typing import Optional
from classes.Assistant import Assistant

def get_conversation_response(
    image_b64: str, user_message: str, prior_conversation=list()
    ) -> tuple[Optional[str], Optional[Exception]]:

    err = None
    res = None

    try:
        assistant = Assistant()
    except Exception as e:
        err = e
        return res, err
    
    return assistant.respond(image_b64, user_message, prior_conversation=prior_conversation)
