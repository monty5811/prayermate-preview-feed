import os

from jinja2 import Environment, FileSystemLoader
import requests


def load_feed():
    url = os.environ["FEED_URL"]
    resp = requests.get(url)
    data = resp.json()
    return data


def build():
    env = Environment(loader=FileSystemLoader("."))

    path_to_tmpl = os.path.join("index.html.tmpl")
    data = load_feed()
    result = env.get_template(path_to_tmpl).render(data=data)

    with open("index.html", "w") as f:
        f.write(result)


if __name__ == "__main__":
    build()
