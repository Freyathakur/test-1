import yaml


def load_config(text: str) -> dict:
    return yaml.safe_load(text)
