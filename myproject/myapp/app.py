from flask import Flask, render_template
import subprocess
import datetime
import os

app = Flask(_name_)

@app.route("/htop")
def htop():
    full_name = "Shivala Amrutha Kumari"
    username = os.getlogin()
    ist = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=5, minutes=30)))
    top_output = subprocess.check_output(["top", "-bn1"]).decode()  # Get top output once

    return render_template("htop.html", full_name=full_name, username=username, ist=ist, top_output=top_output)

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=8080) 
