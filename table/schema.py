from pydantic import BaseModel

class TableInfo(BaseModel):
    content_base64: str
    page_idx: int
    block_idx: int
    table_text: str