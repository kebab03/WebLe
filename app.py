# Press the green button in the gutter to run the script.
from flask import Flask,render_template,request,redirect

from cs50 import SQL

# Open database

app = Flask(__name__)
db = SQL("sqlite:///froshims.db")
REGISTRANTS = {}
SPORTS = ["Dodgeball",
          "Flag ball",
          "Soccer",
          "VolleyBall"
]

# CONVNZIONE PER COSTA USARE MAIUSOCLE
@app.route("/")
def index():
    # if request.method=="GET":
    #     return render_template("index@34.html")
    # if request.method=="POST":
    #return  render_template("index1h11_radioCk.html", sports=SPORTS)#variable =name in template è SPORT o valore
    return  render_template("index1h5.html", sports=SPORTS)#variable =name in template è SPORT o valore
            # render_template("greet.html",name = request.form.get("name","world"))
@app.route("/register", methods=["POST"])
def register():
    sport = request.form.get("sport")
    print("2:", SPORTS[2])
    if SPORTS[2] not in SPORTS:
        print("SPORTS-", SPORTS)
        print("yes")
        print("sport1", sport)
    else:
        print("no è in ")
        print("sport1_er", sport)
    name =request.form.get("name")
    if not name:
        return render_template("error.html", message="Missing name")


    if not sport:
        print("sport", sport)
        return render_template("error.html", message="Mising sport")
    if  sport.strip() not in SPORTS:
        print("len 2:-",len(sport.strip()))
        print("len SPORTS:-", len(SPORTS[1]))
        print("sport_er:", sport)
        return render_template("error.html", message="Invalid sport")
    # else:
    #     print("fine")
    #     return "efi"
    REGISTRANTS[name] = sport.strip()# cui posso mettere il data base
    print(REGISTRANTS)
    # Remember registrant
    db.execute("INSERT INTO registrants (name, sport) VALUES(?, ?)", name, sport)
    #return render_template("success.html") fino 1h18 min
    return redirect("/registrants " )
@app.route("/registrants", methods=["GET","POST"])
def registrants():
    REGISTRANTS = db.execute("SELECT * FROM registrants")# è la riga di data base k è un dict of column & valu
    return render_template("registrants1h27.html", registrants=REGISTRANTS)# in rosso a Sx è la variabile , mentre
    # a dx In maiuscolo è il valore

#        "TODO"
if __name__ == '__main__':
    app.run()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
