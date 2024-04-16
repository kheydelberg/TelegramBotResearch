import asyncpg
# код для пробрасывания соединения с БД проекта, но подразумевается, что БД в postgresql
# можно использовать psycopg еще
class Request:
    def __init__(self, connector: asyncpg.pool.Pool):
        self.connector = connector
        
    async def create_feedback(self, idTelegram):
        async with self.connector.cursor(asyncpg.DictCursor) as cur:
            query = f"INSERT INTO feedback (idTelegram, Type, Text, IsDone)" \
                f"VALUES ({idTelegram}, 'test', 'testtest', false) ON DUPLICATE KEY UPDATE;"
            await cur.execute(query)
            
    async def read_feedback(self):
        async with self.connector.cursor(asyncpg.DictCursor) as cur:
            query = f"SELECT * FROM feedback"
            await cur.execute(query)
            return await cur.fetchall()
        
    async def readone_feedback(self):
        async with self.connector.cursor(asyncpg.DictCursor) as cur:
            query = f"SELECT * FROM feedback"
            await cur.execute(query)
            return await cur.fetchone()