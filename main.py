from flask import Flask, render_template, request, redirect, url_for
import datetime

app = Flask(__name__)

user = {}
cal = {"mangees": 0, "brulees": 0}
coins = 0
xp = 0

@app.route("/")
def home():
    return render_template(
        "index.html",
        user=user,
        cal=cal,
        coins=coins,
        xp=xp,
        coach=coach(),
        meal=meal_ai(),
        notif=notif()
    )

@app.route("/compte", methods=["POST"])
def compte():
    user["nom"] = request.form["nom"]
    user["objectif"] = request.form["objectif"]
    return redirect(url_for("home"))

@app.route("/repas", methods=["POST"])
def repas():
    global xp, coins
    cal["mangees"] += float(request.form["cal"])
    xp += 10
    coins += 5
    return redirect(url_for("home"))

@app.route("/sport", methods=["POST"])
def sport():
    global xp, coins
    cal["brulees"] += float(request.form["cal"])
    xp += 20
    coins += 10
    return redirect(url_for("home"))

def coach():
    diff = cal["mangees"] - cal["brulees"]
    if diff < 0:
        return "🔥 Déficit parfait"
    elif diff < 500:
        return "🙂 Bon équilibre"
    else:
        return "⚠️ Trop de calories"

def meal_ai():
    if user.get("objectif") == "perdre":
        return "🥗 Poulet + légumes"
    elif user.get("objectif") == "prendre":
        return "🍝 Pâtes + protéines"
    else:
        return "🍽️ Équilibré"

def notif():
    h = datetime.datetime.now().hour
    if h == 9:
        return "🔔 Petit déjeuner"
    elif h == 14:
        return "🔔 Sport"
    elif h == 20:
        return "🔔 Bilan"
    return ""
    
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
