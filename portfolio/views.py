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
    tagcolors={
        "nodejs":{"fg":"rgb(0, 0, 0)","bg":"rgb(0, 239, 12)"},
        "python":{"fg":"rgb(255, 255, 255)","bg":"rgb(0, 12, 239)"}
    }
    profileLinks=[
        {"icon":"fas fa-at","link":"mailto:joycevarg@gmail.com"},
        {"icon":"fab fa-github","link":"https://github.com/Joycevarg/"},
        {"icon":"fab fa-linkedin","link":"https://www.linkedin.com/in/joycevarg/"},
        {"icon":"fab fa-instagram","link":"https://www.instagram.com/joyce.varg/"},
        {"icon":"fab fa-medium-m","link":"https://medium.com/@joycevarg"},
        {"icon":"fab fa-unsplash","link":"https://unsplash.com/@joycevarg"}
    ]
    milestones=[
        {"time":"Now", "place":"Oracle", "position":"Application Engineer",  "description":"<ul><li>Involved in the development of digital assistant for Oracle's latest generation ERP suite that is utilized by multiple Fortune 500 companies.</li><li>Responsible for development and deployment of the digital assistant for internal use at Oracle.</li><li>Developer point of contact for 10+ teams working on the product and responsible for the integration of their modules.</li><li>Responsible for design, development and maintenance of internal tools that are used by 15+ teams across the company for development, testing and analytics</li></ul>"},
        {"time":"'20", "place":"College of Engineering Trivandrum", "position":"B.Tech(Hons)",  "description":"Lorem ipsum..."},
        {"time":"'19", "place":"Nissan Digital", "position":"Software Engineering Intern",  "description":"<ul><li>Worked on approximating the NP-hard packing problem of determining the usable trunk volume of a car.</li><li>Built a tool that allows engineers to easily test solutions for the problem.</li></ul>"},
        {"time":"'18", "place":"Clap Research", "position":"Machine Learning Intern", "description":"<ul><li>Worked on developing models that rank paragraphs for question answering.</li><li>Built workflows for developing and tuning the model.</li></ul>"},
    ]
    projects=[
        {"name":"Hello World","tags":["python","nodejs"],"description":"Lorem ipsum...","links":[{"icon":"fas fa-at","link":"http://helloworld"},{"icon":"fab fa-github","link":"http://helloworld"}]},
        {"name":"Hello World","tags":["python","nodejs"],"description":"Lorem ipsum...","links":[{"icon":"fas fa-at","link":"http://helloworld"}]},
        {"name":"Hello World","tags":["python","nodejs"],"description":"Lorem ipsum..."},
        {"name":"Hello World","tags":["python","nodejs"],"description":"Lorem ipsum...","links":[{"icon":"fas fa-at","link":"http://helloworld"}]},
        {"name":"Hello World","tags":["python","nodejs"],"description":"Lorem ipsum...","links":[{"icon":"fas fa-at","link":"http://helloworld"}]},
        {"name":"Hello World","tags":["python","nodejs"],"description":"Lorem ipsum...","links":[{"icon":"fas fa-at","link":"http://helloworld"}]},
        {"name":"Hello World","tags":["python","nodejs"],"description":"Lorem ipsum...","links":[{"icon":"fas fa-at","link":"http://helloworld"}]},
        {"name":"Hello World","tags":["python","nodejs"],"description":"Lorem ipsum...","links":[{"icon":"fas fa-at","link":"http://helloworld"}]},
    ]
    for project in projects:
        tagarr=[]
        for tag in project["tags"]:
            tagobj = {}
            tagobj["text"] = tag
            tagobj["fg"] = tagcolors[tag]["fg"]
            tagobj["bg"] = tagcolors[tag]["bg"]
            tagarr.append(tagobj)
        project["tags"]=tagarr
    data['projects']=projects
    data['stackLogos']=stackLogos
    data['profileLinks']=profileLinks
    data['milestones']=milestones
    url="./templates/index.html"
    return render(request,url,data)