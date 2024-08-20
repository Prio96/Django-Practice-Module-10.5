from django.shortcuts import render

# Create your views here.
def home(request):
    d={"Name":'California Institute of Technology',"Abbreviation":"CALTECH","Location":"Pasadena, California, USA","Students":[
        {
            "Name":"Sheldon Cooper",
            "Id":1,
            "Department":"Physics"
        },
        {
            "Name":"Leonard Hofstadter",
            "Id":2,
            "Department":"Physics"
        },
        {
            "Name":"Raj Koothrappali",
            "Id":3,
            "Department":"Astrophysics"
        },
        {
            "Name":"Howard Wolowitz",
            "Id":4,
            "Department":"Mechanical Engineering"
        },
        {
            "Name":"Bernadette Rostenkowski",
            "Id":5,
            "Department":"Microbiology"
        },
        
    ]}
    return render(request,"FirstApp/home.html",d)
