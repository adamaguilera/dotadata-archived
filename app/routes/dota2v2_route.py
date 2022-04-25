from flask import Blueprint, jsonify, request

from app.mapping.dota2v2_mapper import map_dota2v2_post_game
from app.models.dota2v2_model import Dota2v2PostGame

dota2v2_prefix = '/dota2v2'
dota2v2 = Blueprint('dota2v2', __name__, url_prefix=dota2v2_prefix)


@dota2v2.route('/title', methods=['GET'])
def title():
    return jsonify("Dota2v2")


@dota2v2.route('/post-game', methods=['POST'])
def end_game():
    request_json = request.get_json()
    print(request_json)
    post_game: Dota2v2PostGame = map_dota2v2_post_game(request_json)

    post_game.save()
    return jsonify('Received')
