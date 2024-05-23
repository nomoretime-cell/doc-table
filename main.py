from table.mathpix_cli import process_table
from table.settings import settings
from pyfunvice import (
    app_service,
    start_app,
)


@app_service(path="/api/v1/parser/ppl/table", inparam_type="flat")
async def process(
    content_base64: str,
    text: str,
    type_block_idx: int,
    type_block_num: int,
    block_idx: int,
):
    if text != "":
        return {"text": text}
    else:
        return process_table(content_base64)


if __name__ == "__main__":
    start_app(workers=settings.WORKER_NUM, port=8003, post_fork_func=None)
