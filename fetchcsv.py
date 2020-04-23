# This file is responsible for pulling and maintaining csv data of all the handles mentioned in userlist.txt
# Please seperate each name by the character ','
# todo: as of 23 April 2020, update and syncing previously downloaded user data hasn't been implement.

import twint
import os
from usernames import *
import shutil
import os

current_folder_path = os.path.abspath(os.getcwd())
csv_foldername = 'usercsv'

def fetchUserdata(username):
    c = twint.Config()
    c.Username = username
    c.Limit = 10
    c.Store_csv = True
    c.Output = os.path.join(current_folder_path, f"{username}.csv")
    twint.run.Search(c)

def moveCSVfiles():
    # Twint saves all csv files in the same folder, so move all of them to usercsv/
    # todo: Find out why Twint doesn save to absolute path and remove the need for this step 
    files = os.listdir(current_folder_path)
    destfolder = os.path.join(current_folder_path,csv_foldername)
    
    if not os.path.isdir(destfolder):
        os.path.mkdir(destfolder)
        
    for f in files:
        if (f.endswith('.csv')):
            shutil.move(os.path.join(current_folder_path,f), os.path.join(destfolder,f))

if __name__=='__main__':
    # Fetch csv data and save
    for idx, username in enumerate(twitterUsernames):
        fetchUserdata(username)
    # move csv files to usercsv folder
    moveCSVfiles()


