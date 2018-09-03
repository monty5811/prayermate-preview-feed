import os
import datetime as dt

from jinja2 import Environment, FileSystemLoader
import requests


def load_feed():
    url = os.environ["FEED_URL"]
    resp = requests.get(url)
    data = resp.json()
    return data


def only_future(data):
    today = dt.date.today()
    petitions = []
    for petition in data["petitions"]:
        p_date = dt.datetime.strptime(petition["date"], "%Y-%m-%d").date()
        if p_date >= today:
            petitions.append(petition)

    data["petitions"] = petitions
    return data


def build():
    env = Environment(loader=FileSystemLoader("."))

    path_to_tmpl = os.path.join("index.html.tmpl")
    data = load_feed()
    if os.environ.get("ONLY_FUTURE", "False") == "True":
        only_future(data)

    result = env.get_template(path_to_tmpl).render(
        data=data, theme_colour=os.environ.get("THEME_COLOUR", False)
    )

    with open("index.html", "w") as f:
        f.write(result)


if __name__ == "__main__":
    build()
