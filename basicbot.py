from slackclient import SlackClient
import time

token = "xoxb-???????????????????????????????"  # insert your token here
client = SlackClient(token)

if client.rtm_connect():  # connect to slack
    print 'connected!'

    while True:
        messages = client.rtm_read()  # read the list of messages from slack
        for message in messages:
            print message
        time.sleep(0.5)

else:
    print "Connection Failed, invalid token?"
