from flask import Blueprint

directivos=Blueprint("directivos",__name__)

@directivos.route("/getDir",methods=["GET"])
def getDir():
    return {"key":"Directivos"}