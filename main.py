import os
import dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import schedule
from multiprocessing import Process

dotenv.load_dotenv()
bot_token = os.environ.get("SLACK_BOT_TOKEN")
app_token = os.environ.get("SLACK_APP_TOKEN")
verification_token = os.environ.get("VERIFICATION_TOKEN")
client_secret = os.environ.get("CLIENT_SECRET")
signing_secret = os.environ.get("SIGNING_SECRET")

app = App(token=bot_token)


@app.event("app_mention")
def handle_app_mention(body, say):
    user_id = body["event"]["user"]
    say(f"<@{user_id}> hi!")


def run_slackapp():
    handler = SocketModeHandler(app, app_token)
    handler.start()


if __name__ == "__main__":
    # p = Process(target=run_slackapp)
    # p.start()
    run_slackapp()
