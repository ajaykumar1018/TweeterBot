import os
from CamTest import capture
from TestTwitter import send_tweet

a=capture()
if (a):
    send_tweet()
