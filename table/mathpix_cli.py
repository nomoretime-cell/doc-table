import base64
import io
import os
from dotenv import load_dotenv
import requests
import json

load_dotenv("local.env")


def process_table(content_base64: str):
    image_byte = base64.b64decode(content_base64)
    r = requests.post(
        "https://api.mathpix.com/v3/text",
        files={"file": ("table.png", io.BytesIO(image_byte), "image/png")},
        data={
            "options_json": json.dumps(
                {"math_inline_delimiters": ["$", "$"], "rm_spaces": True}
            )
        },
        headers={
            "app_id": os.environ.get("APP_ID"),
            "app_key": os.environ.get("APP_KEY"),
        },
    )
    return r.json()
