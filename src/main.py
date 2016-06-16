from config import ConfigFromS3
from Slack import Slack
from Telegram import Telegram


def handle(event, context):
    configFromS3 = ConfigFromS3("chat-lambda", "config.ini", "eu-west-1")
    conf = configFromS3.config

    telegram = Telegram(
        api_key=conf.get("telegram", "api_key"),
        chat_id=conf.get("telegram", "chat_id")
    )
    slack = Slack(
        webhook_url=conf.get("slack", "webhook_url")
    )

    channels = {
        "default": [slack.send_message, telegram.send_message],
        "slack": [slack.send_message],
        "telegram": [telegram.send_message],

    }

    for record in event['Records']:
        subject = record['Sns']['Subject']
        message = record['Sns']['Message']

        if channels.get(subject, None) is None:
            subject = 'default'

        for sender in channels[subject]:
            sender(message)
