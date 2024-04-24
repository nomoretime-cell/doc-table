from table.mathpix_cli import process_table
from table.settings import settings
from pyfunvice import (
    app_service,
    start_app,
)


@app_service(path="/api/v1/parser/ppl/table", inparam_type="flat")
async def process(content_base64: str, page_idx: int, block_idx: int, table_text: str):
    return process_table(content_base64)


if __name__ == "__main__":
    start_app(workers=settings.WORKER_NUM, port=8003, post_fork_func=None)
