from flask import Flask,jsonify,request
import csv

allmovies = []
with open("finalMovies.csv",encoding="utf8")as f:
    read = csv.reader(f)
    df = list(read)
    allmovies = df[1:]

likedmovies = []
unlikedmovies = []
unwatched = []
app = Flask(__name__)

@app.route("/getmovie")
def onlymovie():
    return jsonify({
        "data":allmovies[0]
    })

@app.route("/likedmovie",methods = ["POST"])
def likedmovie():
    movie = allmovies[0]
    allmovies = allmovies[1:]
    likedmovies.append(movie)
    return jsonify({
        "status":"success"
    })

@app.route("/unlikedmovie",methods = ["POST"])
def unlikedmovie():
    movie = allmovies[0]
    allmovies = allmovies[1:]
    unlikedmovies.append(movie)
    return jsonify({
        "status":"success"
    })

@app.route("/unwatched",methods = ["POST"])
def unwatched():
    movie = allmovies[0]
    allmovies = allmovies[1:]
    unwatched.append(movie)
    return jsonify({
        "status":"success"
    })
app.run()