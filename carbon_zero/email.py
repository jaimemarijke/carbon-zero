import requests


def send():
    response = requests.post(
        "https://api.mailgun.net/v3/mailgun.carbonzero.me/messages",
        auth=("api", "key-d5ca7b14351e96172d2dde7381ff732e"),
        data={
            "from": "Carbon Zero <mailgun@carbonzero.me>",
            "to": ["jaime.m.mccandless@gmail.com"],
            "subject": "Hello",
            "text": "Testing some Mailgun awesomness!"
        }
    )
    print(response)
    print(response.json())
