from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse

# Create your views here.

def index(request):
    now = datetime.now()
    html = f"""
        <html> 
            <body>
                <h1>Hello This is Django app!</h1>
                <p> The Current Time is { now }. </p>
            </body>
        </html>
    """
    return HttpResponse(html)