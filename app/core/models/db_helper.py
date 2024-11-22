from core.settings import settings
from pysqlx_engine import PySQLXEngine


class DatabaseHelper:
    def __init__(self, url: str, echo: bool = False):
        self.echo = echo
        self.db = PySQLXEngine(url)

    async def connect(self):
        await self.db.connect()

    async def execute(self, stmt):
        if not self.db.connected:
            await self.connect()
        await self.db.execute(sql=stmt)

    async def query(self, stmt):
        if self.echo:
            print(stmt)
        if not self.db.connected:
            await self.connect()
        await self.db.query(sql=stmt)

    async def query_first(self, stmt):
        if self.echo:
            print(stmt)
        if not self.db.connected:
            await self.connect()
        await self.db.query_first(sql=stmt)

    async def commit(self):
        await self.db.commit()

    async def close(self):
        await self.commit()
        await self.db.close()

    async def rollback(self):
        await self.db.rollback()


db_helper = DatabaseHelper(
    url=settings.db_url,
    echo=settings.echo,
)