from django.shortcuts import renderfrom django.shortcuts import render
import subprocess
import datetime
import os

def htop_view(request):
    full_name = "Shivala Amrutha Kumari"
    username = os.getlogin()
    ist = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=5, minutes=30)))
    top_output = subprocess.check_output(["top", "-bn1"]).decode()  # Get top output once

    context = {
        "full_name": full_name,
        "username": username,
        "ist": ist,
        "top_output": top_output,
    }
    return render(request, "myapp/htop.html", context)
import subprocess
import datetime
import os

def htop_view(request):
    full_name = "Your Full Name"  # Replace with your name
    username = os.getlogin()
    ist = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=5, minutes=30)))
    top_output = subprocess.check_output(["top", "-bn1"]).decode()  

    context = {
        "full_name": full_name,
        "username": username,
        "ist": ist,
        "top_output": top_output,
    }
    return render(request, "myapp/htop.html", context)

