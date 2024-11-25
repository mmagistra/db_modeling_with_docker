from typing import List, Tuple, Any

from pydantic import BaseModel

from core.settings import settings
from pysqlx_engine import PySQLXEngine


class DatabaseHelper:
    def __init__(self, url: str, echo: bool):
        print(f'echo: {echo}')
        self.echo = echo
        self.db = PySQLXEngine(url)

    async def connect(self):
        await self.db.connect()

    async def execute(self, stmt):
        if self.echo:
            print(stmt)
        if not self.db.connected:
            await self.connect()
        await self.db.execute(sql=stmt)

    async def query(self, stmt):
        if self.echo:
            print(stmt)
        if not self.db.connected:
            await self.connect()
        data = await self.db.query(sql=stmt)
        return data

    async def query_first(self, stmt):
        if self.echo:
            print(stmt)
        if not self.db.connected:
            await self.connect()
        data = await self.db.query_first(sql=stmt)
        return data

    async def commit(self):
        await self.db.commit()

    async def commit_and_close(self):
        await self.commit()
        await self.db.close()

    async def rollback(self):
        await self.db.rollback()

    async def create(self, table_name: str, instance):
        fields = instance.model_dump().keys()
        fields = '(' + ', '.join(fields) + ')'
        values = tuple(instance.model_dump().values())
        if len(values) == 1:
            values = f"('{values[0]}')"
        stmt = f"""
        INSERT INTO {table_name} {fields} VALUES {values}
        """
        await self.execute(stmt)
        await self.commit_and_close()

    async def read_all(self, table_name: str, id_field_name: str, TableClassName):
        stmt = f"""SELECT * FROM {table_name} ORDER BY {id_field_name}"""
        data = [TableClassName(**item.model_dump()) for item in await self.query(stmt)]
        return data

    async def read(self, table_name: str, id_field_name: str, id_value: int, TableClassName):
        stmt = f"""SELECT * FROM {table_name}
            WHERE {id_field_name} = {id_value} ORDER BY {id_field_name}
        """
        data = await self.query_first(stmt)
        if data is not None:
            data = TableClassName(**data.model_dump())
            return data

    async def update(self, table_name: str, id_field_name: str, id_value: int, updated_data: dict | Any):
        stmt = f"""
        UPDATE {table_name}
        SET """
        if not isinstance(updated_data, dict):
            updated_data = updated_data.model_dump()
        for key, value in updated_data.items():
            if value is not None:
                stmt += f"{key}='{value}', "

        if stmt[-2:] == ', ':
            stmt = stmt[:-2]

        stmt += f""" 
        WHERE {id_field_name}={id_value}
    """

        await self.execute(stmt)
        await self.commit_and_close()

    async def delete(self, table_name: str, id_field_name: str, id_value: int):
        stmt = f"""
        DELETE FROM {table_name} WHERE {id_field_name}={id_value}
        """
        await self.execute(stmt)
        await self.commit_and_close()


db_helper = DatabaseHelper(
    url=settings.db_url,
    echo=settings.echo,
)
