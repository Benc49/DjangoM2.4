from django.http import HttpResponse, response
from django.http.request import HttpRequest
from django.shortcuts import render
from dataclasses import dataclass
from typing import Dict, List
# Create your views here.

@dataclass
class Team:
    team_name: str
    description: str
    members: List[str]



def lp(request: HttpRequest, leadership):
    context= {
        "leader": leadership,
        "Groups": {
            "Community": Team("Community", "Community team plans all the events at Base Camp. They schedule things around holidays, student birthday's and every other friday.", ["Jacen", "Ariyana", "Justin", "Logan W.", "Rjay"]),
            "Documentation": Team("Documentation", " Documentation team at Base Camp documents everything we do. They Run the social media pages and write newsletters.", ["Ben", "Ma'kyla", "Isaac", "Randy", "Ryan"]),
            "Management": Team("Management", "The Management Team runs all the chores at Base Camp. They also check and make sure everybody is on task with their work. They get with Procurment team to make sure we have everything we need for chores", ["Logan C.", "Michelle", "Dylan G.", "Rylee", "Will", "Daelan", "Ethan"]),
            "Procurement": Team("Procurement", "Procurement team gets everything we need for Base Camp. Things such as food, drinks, spray bottles and rags. They get whatever we need.", ["Dylan S.", "Richard", "Gary", "Mariann", "Quinton"])
        }
}
   
    return render(request, "documentation.html", context)


def home(request: HttpRequest):
    return render(request, "index.html")
    
