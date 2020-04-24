from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)
current_folder_path = os.path.abspath(os.getcwd())
csv_foldername = 'usercsv'
csv_folderpath = os.path.join(current_folder_path, 'usercsv')

@app.route('/')
def homepage():
    # show a list of all files 
    files = os.listdir(os.path.join(current_folder_path, csv_foldername))
    # read user files and display likes and tweet
    newdf = pd.DataFrame()
    for idx, filename in enumerate(files):
        userdata = pd.read_csv(os.path.join(csv_folderpath,filename), usecols=['username','likes_count','tweet','time','date'])
        newdf = newdf.append(userdata.loc[0])
    newdf = newdf[['username','date','time','likes_count','tweet']]
    return render_template('index.html',  tables=[newdf.to_html(classes='data', index=False)], titles=newdf.columns.values)


if __name__=='__main__':
    app.run(debug=True)
