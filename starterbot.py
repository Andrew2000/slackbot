import os
import time
from slackclient import SlackClient
import schedule

# instantiate Slack client && starterbot's user ID in Slack: value is assigned after the bot starts up

slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
starterbot_id = None

def handle_chat(channel):
    response = "523 PM!!!"

    # Sends the response back to the channel
    slack_client.api_call(
        "chat.postMessage",
        channel=channel,
        text=response
    )

def doChat():
    if slack_client.rtm_connect(with_team_state=False):
        print("Starter Bot connected and running!")
        # Read bot's user ID by calling Web API method `auth.test`
        #starterbot_id = slack_client.api_call("auth.test")["user_id"]
        if True:
            handle_chat("release-team")
            time.sleep(10)
    else:
        print("Connection failed. Exception traceback printed above.")

if __name__ == "__main__":
    schedule.every().saturday.at("17:23").do(doChat)
    while True:
        schedule.run_pending()
    