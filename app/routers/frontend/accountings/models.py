from typing import List

from core.models.db_helper import DatabaseHelper


async def read_fields_by_statement_and_convert_to_class_list(
        db_helper: DatabaseHelper,
        stmt: str,
        ClassForConvert,
) -> List:
    return await db_helper.execute_and_convert_to_class(stmt, ClassForConvert)
