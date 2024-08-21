from django.shortcuts import render
from datetime import *

# Create your views here.
def home(request):
    d={"Name":'California Institute of Technology',"Abbreviation":"CALTECH","Location":"Pasadena, California, USA","Publish_Date":datetime.now()-timedelta(days=5),"Edit_Date":datetime.now()-timedelta(days=2),"Students":[
        {
            "Name":"Sheldon Cooper",
            "Id":0,
            "Department":"Physics",
            "Club":"Chess Club"
        },
        {
            "Name":"Leonard Hofstadter",
            "Id":1,
            "Department":"Physics",
            "Club":""
        },
        {
            "Name":"Raj Koothrappali",
            "Id":2,
            "Department":"Astrophysics",
            "Club":"Space Club"
        },
        {
            "Name":"Howard Wolowitz",
            "Id":3,
            "Department":"Mechanical Engineering",
            "Club":"IT Club"
        },
        {
            "Name":"Bernadette Rostenkowski",
            "Id":4,
            "Department":"Microbiology",
            "Club":"Wildlife Club"
        },
        
    ]}
    return render(request,"FirstApp/home.html",d)
