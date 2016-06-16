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

    python ~/Projects/lambda-packager/package-lambda.py --source src --libraries venv/lib/python2.7/site-packages
    Created lambda zip file: src-0f21d460e910c416238c81f99e588ea687e5d96b.zip

## Local Development

    cd src
    virtualenv venv
    . ./venv/bin/activate
    pip install -r requirements.txt
