# This file is responsible for pulling and maintaining csv data of all the handles mentioned in userlist.txt
# Please seperate each name by the character ','
# todo: as of 23 April 2020, update and syncing previously downloaded user data hasn't been implement.

import twint
import os
from usernames import *

def fetchUserdata(username):
    c = twint.Config()
    c.Username = username
    c.Limit = 10
    c.Store_csv = True
    current_folder_path = os.path.abspath(os.getcwd())
    c.Output = os.path.join(current_folder_path, f"{username}.csv")
    twint.run.Search(c)

for idx, username in enumerate(twitterUsernames):
    fetchUserdata(username)