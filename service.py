import os
import json


def slugify(text: str) -> str:
    return text.strip().lower().replace(" ", "-")
