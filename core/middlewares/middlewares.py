from aiogram.types import Message, TelegramObject
from aiogram import BaseMiddleware
from typing import Callable, Awaitable, Dict, Any
import asyncpg
from core.utils.dbconnect import Request

# мидлвари для пробрасывания соединения с БД проекта, но подразумевается, что БД в postgresql, 
# чтобы работало надо в мэйне еще прописать функцию и зарегистрировать ее
class DBSession(BaseMiddleware):
    def __init__(self, connector: asyncpg.pool.Pool):
        super().__init__()
        self.connector = connector

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
        ) -> Any:
            async with self.connector.acquire() as connect:
                data['request'] = Request(connect)
                return await handler(event, data)