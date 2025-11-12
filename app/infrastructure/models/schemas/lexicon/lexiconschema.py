from pydantic import BaseModel

from lexicon.lexicon import lexicon as lexicon_dict

class PromptsLexicon(BaseModel):
    continue_dialog: str
    give_feedback: str


class ButtonsLexicon(BaseModel):
    ready: str


class HandlersLexicon(BaseModel):
    start: str
    choose_name: str
    choose_level: str
    choose_mode: str
    completed: str
    edit_name: str
    edit_lvl: str
    edit_mode: str
    edit_done: str
    wrong_name: str
    incorrect_input: str
    stop_spam: str
    ready_done: str
    reset_dialog: str
    info: str
    thinking: str


class BotLexicon(BaseModel):
    """Pydantic model with lexicon"""
    chatgpt: PromptsLexicon
    handlers: HandlersLexicon
    buttons: ButtonsLexicon


lexicon = BotLexicon(**lexicon_dict)
