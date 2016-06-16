# chat-lambda

Relays SNS messages to Telegram and/or Slack.

## Configuration File

Make sure `ConfigFromS3` loads a configuration file of the format:

```
[slack]
webhook_url = https://webhook.url/a/b

[telegram]
chat_id=-1234
api_key=abcdef1234
```

## Package it

Using [lambda-packager](https://github.com/nlindblad/lambda-packager):

    python package-lambda.py --source src
    2016-03-27 20:22:05,704 - INFO - Created lambda zip file: src-193c4d8857dfbbb762b18b1fa5cbb8f16b609ff3.zip

## Local Development

    cd src
    virtualenv venv
    . ./venv/bin/activate
    pip install -r requirements.txt
