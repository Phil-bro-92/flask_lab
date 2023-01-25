from flask import render_template
from app import app
from models.order_list import games

@app.route('/games')
def get_all_games():
    return render_template("index.html", title = "Home", games = games)

@app.route('/games/<int:id>')
def get_a_game(id):
    return render_template("order.html", title="single_game", game = games[id])
