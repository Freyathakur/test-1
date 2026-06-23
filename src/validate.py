import yaml

with open("config/app.yaml") as f:
    yaml.safe_load(f)
print("ok")
