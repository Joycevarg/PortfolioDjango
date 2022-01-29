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
        "oci":{"fg":"rgb(0, 0, 0)","bg":"rgb(230, 0, 12)"},
        "work":{"fg":"rgb(0, 0, 0)","bg":"rgb(12, 143, 242)"},
        "jenkins":{"fg":"rgb(255, 255, 255)","bg":"rgb(12, 143, 242)"},
        "python":{"fg":"rgb(255, 255, 255)","bg":"rgb(0, 12, 239)"},
        "django":{"fg":"rgb(0,0,0)","bg":"rgb(0, 200, 239)"},
        "ros":{"fg":"rgb(0,0,0)","bg":"rgb(100, 100, 239)"},
        "school":{"fg":"rgb(0,0,0)","bg":"rgb(200, 100, 239)"},
        "personal":{"fg":"rgb(255,255,255)","bg":"rgb(100, 100, 50)"},
        "ml":{"fg":"rgb(0,0,0)","bg":"rgb(100, 200, 239)"},
        "flutter":{"fg":"rgb(0,0,0)","bg":"rgb(100, 50, 239)"},
        "android":{"fg":"rgb(0,0,0)","bg":"rgb(0, 250, 50)"},
        "java":{"fg":"rgb(255,255,255)","bg":"rgb(0, 100, 12)"},
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
        {"time":"'20", "place":"College of Engineering Trivandrum", "position":"B.Tech(Hons)",  "description":"Computer Science and Engineering"},
        {"time":"'19", "place":"Nissan Digital", "position":"Software Engineering Intern",  "description":"<ul><li>Worked on approximating the NP-hard packing problem of determining the usable trunk volume of a car.</li><li>Built a tool that allows engineers to easily test solutions for the problem.</li></ul>"},
        {"time":"'18", "place":"Clap Research", "position":"Machine Learning Intern", "description":"<ul><li>Worked on developing models that rank paragraphs for question answering.</li><li>Built workflows for developing and tuning the model.</li></ul>"},
    ]
    projects=[
        {"name":"Digital Assistant for ERP","tags":["work","nodejs","oci","jenkins","django"],"description":"Chatbot interface for management of expenses in Oracle Fusion ERP.","links":[{"icon":"fas fa-info","link":"https://www.oracle.com/chatbots/digital-assistant-for-erp-scm/"}]},
        {"name":"Custom object detector","tags":["personal","python","ml","ros"],"description":"Object detector module for ROS that can be easily trained on custom data for application specific scenarios.","links":[{"icon":"fab fa-github","link":"https://github.com/Joycevarg/ROS-tensorlite-object-detection"},{"icon":"fab fa-medium","link":"https://medium.com/swlh/creating-your-own-custom-object-detector-using-transfer-learning-f26918697889"}]},
        {"name":"Deepfake video classifier","tags":["school","python","ml"],"description":"Video classifier that can identify deepfake videos."},
        {"name":"QMailer","tags":["personal","java","android"],"description":"Android service that sends out a different coding question to study group everyday.","links":[{"icon":"fab fa-github","link":"https://github.com/Joycevarg/Qmailer"}]},
        {"name":"Timer Game","tags":["personal","java","android"],"description":"Android game that tests reflexs.","links":[{"icon":"fab fa-github","link":"https://github.com/Joycevarg/TimerGame"}]},
        {"name":"Applied CS By Android","tags":["school","java","android"],"description":"Applied CS Skills is a free online course by Google that teachs data structures while developing android games","links":[{"icon":"fab fa-github","link":"https://github.com/Joycevarg/AppliedCSwithAndroid"}]}
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