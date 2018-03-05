from slackclient import SlackClient

token = "xoxb-???????????????????????????????"  # insert your token here
client = SlackClient(token)

if client.rtm_connect():  # connect to slack
    response = client.api_call("im.open", user='U19L7TZE3')
    if response["ok"]:
        print "Private message channel ID: ", response["channel"].get("id")
    else:
        print "Private message failed: ", response.get("error")

else:
    print "Connection Failed, invalid token?"
