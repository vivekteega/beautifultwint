# Beautiful Twint

Beautiful Twint scrapes out data of Twitter users specified in the file `usernames.py`. The data is pulled using Twint module and stored as csv files. The data in the files will be visualized as per the needs of [Ranchi Mall's](https://twitter.com/ranchimallflo "What is Ranchi Mall?") marketing efforts.

## Pre-Requisites
The code is written in python3 and makes use of the following python modules:
1. twint
2. pandas
3. Flask 

You can either run `pip3 install twint pandas Flask` or `pip3 install requirements.txt` to install them.

## Running the app 
The app performs 2 functions
1. Fetch Twitter data of userhandles mentionded in the file `usernames.py` & store them as CSV
2. Display 

To fetch data recheck your usernames.py, go to root folder and run 
`python3 fetchcsv.py`
This will take a while to run depending on size of your `usernames.py` list. 

Once the data has been downloaded you can view it by running 
`python3 display.py` and opening `localhost:5000` on Chrome, Firefox or Brave.

##
Ps - This is a work in progress app as of April 23, 2020
