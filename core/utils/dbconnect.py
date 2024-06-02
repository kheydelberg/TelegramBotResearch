import codecs
import os
import aiomysql
from core.settings import Setting

class Request:
    def __init__(self, connector: aiomysql.pool.Pool):
        self.connector = connector
        
    async def create_own_SQL_request(self, data: str):
        async with self.connector.cursor(aiomysql.DictCursor) as cur:
            await cur.execute(data)
            return await cur.fetchall()

    async def author_search(self, author: str):
        async with self.connector.cursor(aiomysql.DictCursor) as cur:
            query = f"SELECT idLinks, name, description, link, authors FROM Links WHERE authors LIKE '%{author}%' ORDER BY likes desc"
            await cur.execute(query)
            return await cur.fetchall()
            
    async def name_search(self, name: str):
        async with self.connector.cursor(aiomysql.DictCursor) as cur:
            query = f"SELECT idLinks, name, description, link, authors FROM Links WHERE name LIKE '%{name}%' ORDER BY likes desc"
            await cur.execute(query)
            return await cur.fetchall()
            
    async def category_search(self, category: str):
        async with self.connector.cursor(aiomysql.DictCursor) as cur:
            query = f"SELECT idLinks, name, description, link, authors FROM Links WHERE categories LIKE '%{category}%' ORDER BY likes desc"
            await cur.execute(query)
            return await cur.fetchall()

    async def create_feedback(self, idTelegram, Type: str, Text: str):
        async with self.connector.cursor(aiomysql.DictCursor) as cur:
            query = f"INSERT INTO feedback (idTelegram, Type, Text, IsDone)" \
                f"VALUES ({idTelegram}, {Type}, {Text}, false);"
            await cur.execute(query)
            return await cur.fetchall()
            
    async def read_all_feedback(self, num: int):
        async with self.connector.cursor(aiomysql.DictCursor) as cur:
            query = f"SELECT * FROM feedback LIMIT {num}"
            await cur.execute(query)
            return await cur.fetchall()
        
    async def read_undone_feedback(self, num: int):
        async with self.connector.cursor(aiomysql.DictCursor) as cur:
            query = f"SELECT * FROM feedback WHERE IsDone = 0 LIMIT {num}"
            await cur.execute(query)
            return await cur.fetchall()
        
    async def create_statistic(self, count_searched: int, Date, Succesfull_Search: int):
        async with self.connector.cursor(aiomysql.DictCursor) as cur:
            query = f"SELECT COUNT(idLinks) FROM Links"
            await cur.execute(query)
            Count_Links = ( await cur.fetchall() )[0]["COUNT(idLinks)"]
            
            query = f"INSERT INTO Statistics (Count_Searched, Date, Count_Links, Successful_Search)" \
                f"VALUES ({count_searched}, {Date}, {Count_Links}, {Succesfull_Search});"
            await cur.execute(query)
            return await cur.fetchall()
        
    async def read_statistic(self, num: int):
        async with self.connector.cursor(aiomysql.DictCursor) as cur:
            query = f"SELECT * FROM Statistics LIMIT {num}"
            await cur.execute(query)
            return await cur.fetchall()
        
    async def create_link(self, categories, name, authors, description, link, likes=0):
        async with self.connector.cursor(aiomysql.DictCursor) as cur:
            query = f"INSERT INTO Links (Categories, Description, Link, Likes, name, authors)" \
                f"VALUES ({categories}, {description}, {link}, {likes}, {name}, {authors});"
            await cur.execute(query)
            return await cur.fetchall()
            
    async def read_links(self, num: int):
        async with self.connector.cursor(aiomysql.DictCursor) as cur:
            query = f"SELECT * FROM Links LIMIT {num}"
            await cur.execute(query)
            return await cur.fetchall()
        
    async def delete_link(self, id: int):
        async with self.connector.cursor(aiomysql.DictCursor) as cur:
            query = f"DELETE FROM Links WHERE idLinks = {id}"
            await cur.execute(query)
            return await cur.fetchall()
        
    async def add_like(self, id: int):
        async with self.connector.cursor(aiomysql.DictCursor) as cur:
            query = f"UPDATE links SET likes = likes + 1 WHERE idLinks = {id}"
            await cur.execute(query)
            return await cur.fetchall()
        
    async def create_backup(self):
        await os.system(f'mysqldump -u root -p{Setting.bots.db_password} researchbot > "{Setting.bots.Backup_path}"')
        
    async def load_backup(self):
        async with self.connector.cursor(aiomysql.DictCursor) as cur:
            backup = codecs.open( rf"{Setting.bots.Backup_path}", "r", "utf_8_sig" )
            query = backup.read() 
            backup.close()
            await cur.execute(query)
            return await cur.fetchall() 
