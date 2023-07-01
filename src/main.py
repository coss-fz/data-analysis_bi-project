
"""
This script runs the main code and create
a dashboard in HTML format
"""


from flask import Flask, render_template
import os




app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('dashboard.html')


##Main Code
if __name__ == '__main__':
    app.run(
        ####host="0.0.0.0",
        ####port=int(os.environ.get("PORT", 8080))
    ) ####### UNCOMENT ONLY IF YOU NEED A PERSONALIZED PORT #######
