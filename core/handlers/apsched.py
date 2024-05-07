from datetime import datetime
from aiogram.types import Message, TelegramObject
from aiogram import BaseMiddleware, Bot
from typing import Callable, Awaitable, Dict, Any
import aiomysql
from .STATISTIC import statistics

from ..utils.dbconnect import Request


class statistics_middleware(BaseMiddleware):
    def __init__(self):
        super().__init__()

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
        ) -> Any:
            user_id = event.from_user.id    
            statistics["user_requests"][user_id] = statistics["user_requests"].get(user_id, 0) + 1
            return await handler(event, data)

class STAT:
    def __init__(self, req: Request):
        self.db = req
        
    async def reset_statistic(self):
        statistics["count_searched"] = int(len(statistics["user_requests"].keys())) # количество уникальных пользователей за день
        print( await (self.db).create_statistic(count_searched=statistics["count_searched"], Date="'" + str(datetime.now()).split()[0] + "'", Succesfull_Search=statistics["Succesfull_Search"]) )

        statistics["count_searched"] = 0
        statistics["user_requests"] = {}
        statistics["Succesfull_Search"] = 0

        
async def reset_statistic2(req: STAT):
     await req.reset_statistic()
