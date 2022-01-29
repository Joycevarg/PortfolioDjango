from django.shortcuts import render

def index(request):
    data={}
    stackLogos=[
        "NodeJS.png",
        "Python.png",
        "Java.png",
        "C.png",
        "Android.png",
        "Unity.png",
        "Flutter.png",
        "Jenkins.png"
    ]
    profileLinks=[
        {"icon":"fas fa-at","link":"mailto:joycevarg@gmail.com"},
        {"icon":"fab fa-github","link":"https://github.com/Joycevarg/"},
        {"icon":"fab fa-linkedin","link":"https://www.linkedin.com/in/joycevarg/"},
        {"icon":"fab fa-instagram","link":"https://www.instagram.com/joyce.varg/"},
        {"icon":"fab fa-medium-m","link":"https://medium.com/@joycevarg"},
        {"icon":"fab fa-unsplash","link":"https://unsplash.com/@joycevarg"}
    ]
    milestones=[
        {"time":"Now", "place":"Oracle"},
        {"time":"'20", "place":"B.Tech(Hons)"},
        {"time":"'19", "place":"Nissan Digital"},
        {"time":"'18", "place":"Clap Research"},
    ]
    data['stackLogos']=stackLogos
    data['profileLinks']=profileLinks
    data['milestones']=milestones
    url="./templates/index.html"
    return render(request,url,data)