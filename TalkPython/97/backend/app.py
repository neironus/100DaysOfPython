import uuid

from flask import Flask, jsonify, abort, request, Response

import game_service as gs

app = Flask(__name__)
app.config.from_object('config')


def main():
    app.run()


@app.route('/')
def index():
    return 'Hello world'


@app.route('/api/user/<string:name>', methods=['GET'])
def get_user(name: str):
    player = gs.get_player(name=name)

    if not player:
        return abort(404)

    return jsonify(player.to_web())


@app.route('/api/user', methods=['POST'])
def create_user():
    try:
        if not request.json or 'name' not in request.json or \
                not request.json.get('name').strip():
            raise Exception('No value for name')

        player = gs.create_player(request.json.get('name').strip())

        return jsonify({'done': True if player else False})
    except Exception as e:
        return abort(Response(
            response='Invalid request : {}'.format(e),
            status=400
        ))


@app.route('/api/game', methods=['POST'])
def create_game():
    return jsonify({'id': str(uuid.uuid4())})


def validate_params_make_a_guess():
    """
    Validate the make a guess params
    """
    if not request.json:
        raise Exception('no JSON body.')

    # Test id player
    id_player = request.json.get('id_player')
    if not id_player:
        raise Exception('no player id.')

    try:
        id_player = int(id_player)
    except Exception:
        raise Exception('incorrect id_player value.')

    if not gs.get_player(idx=id_player):
        raise Exception('player not found.')

    # Test id game
    id_game = request.json.get('id_game')
    if not id_game:
        raise Exception('no game id.')

    game = gs.get_game(idx=id_game)
    if game:
        if game.to_web().get('done'):
            raise Exception('game done.')

        if game.to_web().get('id_player') is not id_player:
            raise Exception('this player can\'t play this game.')

    # Test guess
    guess = request.json.get('guess')
    if not guess:
        raise Exception('no guess provided.')

    try:
        guess = int(guess)
    except Exception:
        raise Exception('guess is not a valid value.')

    if not 0 <= guess <= 100:
        raise Exception('guess must be include/equal between 0 and 100')

    return id_player, id_game, guess


@app.route('/api/guess', methods=['POST'])
def make_a_guess():
    try:
        id_player, id_game, guess = validate_params_make_a_guess()
        gs.save_guess(guess=guess, id_game=id_game, id_player=id_player)

        status = gs.get_status_last_guess(id_game)

        return jsonify({'status': status})

    except Exception as e:
        return abort(Response(
            response='Invalid request : {}'.format(e),
            status=400
        ))


if __name__ == '__main__':
    main()
