from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    events = []
    results = None
    if request.method == 'POST':
        # read files submitted by user
        eventsFile = request.files['eventsFile']
        resultsFile = request.files.get('resultsFile')

        # ensure that events file is submitted
        if eventsFile is None or eventsFile.filename == "":
            return "No file selected"
        if not eventsFile.filename.endswith(".csv"):
            return "File must be a .csv file"
        # if results file submitted, read and convert to dataframe
        if resultsFile and resultsFile.filename != "":
            results = pd.read_csv(resultsFile)
            results = results[["user_id", "Marks (100)"]]
        # read events file
        try:
            df = pd.read_csv(eventsFile)
            df["Time"] = pd.to_datetime(df["Time"], format='%d/%m/%y, %H:%M:%S') # convert to datetime
            df = df.sort_values("Time") # sort values by time (if not already in order)
            # create events dictionary
            events = df.to_dict(orient='records')
        except Exception as e:
            return "An error occurred: " + str(e)
    # return to the template
    return render_template(
        "index.html",
        events=events,
        results=None if results is None else results.to_dict(orient='records')
    )

if __name__ == '__main__':
    app.run(debug=True)