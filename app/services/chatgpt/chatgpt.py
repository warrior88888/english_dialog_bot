import logging

from openai import AsyncOpenAI

from config.config import settings

from .utils import make_prompt
from ...infrastructure.models import UserOrm
from app.infrastructure.models.schemas import lexicon

logger = logging.getLogger('ChatGPT')

class ChatGPT:
    """Class for ChatGPT"""
    client = AsyncOpenAI(
        api_key=settings.gpt.TOKEN.get_secret_value(),
    )
    model = settings.gpt.MODEL


    async def send_message(self, request) -> str:
        response = await self.client.responses.create(
            model=self.model, input=request
        )
        logger.debug(f"{response.status}")
        return response.output_text

    async def answer_user(self, user: UserOrm):
        return await self.send_message(make_prompt(
            task=lexicon.chatgpt.continue_dialog,
            user=user,
        ))

    async def give_feedback(self, user: UserOrm):
        return await self.send_message(make_prompt(
            task=lexicon.chatgpt.give_feedback,
            user=user,
        ))

chatgpt: ChatGPT = ChatGPT()
