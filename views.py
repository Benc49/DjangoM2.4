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

Teams: Dict[str, Team] = {"Procurement": Team("Procurement Team", """The Procurement Team gets all the supplies for Base Camp. They ask all the
      teams what they need and go to the store. They get things such as lunch
      meat, drinks, chips, etc... They also get rags and spray bottles for
      cleaning.""", ["Richard", "Mariann", "Dylan S.", "Gary", "Quinton", "Ethan"]) , "Documentation": Team("Documentation Team", """The Documentation team basically just documents everything that happens at
      Base Camp. They run the social media pages such as instagram, facebook,
      Linkedin, twitter, etc... The documentation team also writes newsletters
      and anything to let people know what we do in Base Camp.""", ["Randy", "Ben", "Ma'kyla", "Isaac", "Ryan"]), "Management": Team("Management Team", """The Management Team manages the chores that the students do at Base Camp.
      They make sure people are doing they're chores and gets with the
      procurement team for items that are required for chores. They also make
      sure everybody is doing they're work by documenting how much work the
      students have gotten done.""", ["Logan C", "Daelan", "Michelle", "Will", "Rylee", "Dylan G."]), "Community": Team("Community Team", """The Community Team at Base Camp works with events. They schedule fun
      activities for every other Friday. They also plan things for Holidays and
      things such as community service.""", ["Ariyanna", "Jacen", "Logan W.", "Justin",  ])}


def lp(request: HttpRequest, leadership):
    if leadership == "documentation":
        return render(request, "documentation.html", Teams)
    elif leadership == "community":
        return render(request, "community.html", Teams)
    elif leadership == "management":
        return render(request, "management.html", Teams)
    elif leadership == "procurement":
        return render(request, "procurement.html", Teams)
    elif leadership == "Home":
        return render(request, "index.html")
