import logging
import os
import threading
from table.mathpix_cli import process_table
from table.settings import settings
from pyfunvice import (
    app_service,
    start_app,
)

logging.basicConfig(
    level=logging.INFO, format="[%(asctime)s] [%(thread)d] [%(levelname)s] %(message)s"
)


@app_service(path="/api/v1/parser/ppl/table", inparam_type="flat")
async def process(
    requestId: str,
    content_base64: str,
    text: str,
    type_block_idx: int,
    type_block_num: int,
    block_idx: int,
):
    if text != "":
        logging.info(
            "POST request"
            + f" [P{os.getpid()}][T{threading.current_thread().ident}][{requestId}] "
            + f"type_block_idx: {type_block_idx}"
            + f", type_block_num: {type_block_num}"
            + f", block_idx: {block_idx}"
            + ", has_text_result: True"
            + f", text: {text}"
        )
        return {"text": text}
    else:
        logging.info(
            "POST request"
            + f" [P{os.getpid()}][T{threading.current_thread().ident}][{requestId}] "
            + f"type_block_idx: {type_block_idx}"
            + f", type_block_num: {type_block_num}"
            + f", block_idx: {block_idx}"
            + ", has_text_result: False"
        )
        result = process_table(content_base64)
        logging.info(
            "Return result"
            + f" [P{os.getpid()}][T{threading.current_thread().ident}][{requestId}] "
            + f"type_block_idx: {type_block_idx}"
            + f", type_block_num: {type_block_num}"
            + f", block_idx: {block_idx}"
            + ", has_text_result: False"
            + f", text: {result}"
        )
        return 


if __name__ == "__main__":
    start_app(workers=settings.WORKER_NUM, port=8003, post_fork_func=None)
