import aiomysql

class Request:
    def __init__(self, connector: aiomysql.pool.Pool):
        self.connector = connector
        
    async def create_own_SQL_request(self, data: str):
        async with self.connector.cursor(aiomysql.DictCursor) as cur:
            await cur.execute(data)
            return await cur.fetchall()

    async def author_search(self, author: str):
        async with self.connector.cursor(aiomysql.DictCursor) as cur:
            query = f"SELECT name, description, link, authors FROM Links WHERE authors LIKE '%{author}%'"
            await cur.execute(query)
            
    async def name_search(self, name: str):
        async with self.connector.cursor(aiomysql.DictCursor) as cur:
            query = f"SELECT name, description, link, authors FROM Links WHERE name LIKE '%{name}%'"
            await cur.execute(query)
            
    async def category_search(self, category: str):
        async with self.connector.cursor(aiomysql.DictCursor) as cur:
            query = f"SELECT name, description, link, authors FROM Links WHERE categories LIKE '%{category}%'"
            await cur.execute(query)

    async def create_feedback(self, idTelegram, Type: str, Text: str):
        async with self.connector.cursor(aiomysql.DictCursor) as cur:
            query = f"INSERT INTO feedback (idTelegram, Type, Text, IsDone)" \
                f"VALUES ({idTelegram}, {Type}, {Text}, false) ON DUPLICATE KEY UPDATE;"
            await cur.execute(query)
            
    async def read_feedback(self, num: int):
        async with self.connector.cursor(aiomysql.DictCursor) as cur:
            query = f"SELECT * FROM feedback FIRST {num}"
            await cur.execute(query)
            return await cur.fetchall()
        
    async def create_statistic(self, count_searched: int, Date, Succesfull_Search: int):
        async with self.connector.cursor(aiomysql.DictCursor) as cur:
            query = f"SELECT COUNT(idLinks) FROM Links"
            await cur.execute(query)
            Count_Links = await cur.fetchall()
            
            query = f"INSERT INTO Statistics (Count_Searched, Date, Count_Links, Successful_Search)" \
                f"VALUES ({count_searched}, {Date}, {Count_Links}, {Succesfull_Search}) ON DUPLICATE KEY UPDATE;"
            await cur.execute(query)
            return await cur.fetchall()
        
    async def read_statistic(self, num: int):
        async with self.connector.cursor(aiomysql.DictCursor) as cur:
            query = f"SELECT * FROM Statistics FIRST {num}"
            await cur.execute(query)
            return await cur.fetchall()
        
    async def create_link(self, categories, name, authors, description, link, likes):
        async with self.connector.cursor(aiomysql.DictCursor) as cur:
            query = f"INSERT INTO Links (Categories, Description, Link, Likes, name, authors)" \
                f"VALUES ({categories}, {description}, {link}, {likes}, {name}, {authors}) ON DUPLICATE KEY UPDATE;"
            await cur.execute(query)
            
    async def read_links(self, num: int):
        async with self.connector.cursor(aiomysql.DictCursor) as cur:
            query = f"SELECT * FROM Links FIRST {num}"
            await cur.execute(query)
            return await cur.fetchall()
        
    async def delete_link(self, id: int):
        async with self.connector.cursor(aiomysql.DictCursor) as cur:
            query = f"DELETE FROM Links WHERE idLinks = {id}"
            await cur.execute(query)
            return await cur.fetchall()
