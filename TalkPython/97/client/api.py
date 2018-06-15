import uplink
from uplink_helpers import raise_for_status, response_to_json


@response_to_json
@raise_for_status
@uplink.json
class GameService(uplink.Consumer):
    def __init__(self):
        super().__init__(base_url='http://localhost:5000')

    @uplink.get('/api/user/{name}')
    def find_user(self, name):
        """
        Find a user by his name
        :param name: name of the user
        """
        pass

    @uplink.post('/api/game')
    def create_game(self):
        """
        Create a game, will return an id
        """
        pass

    @uplink.post('/api/guess')
    def make_a_guess(self, **kwargs: uplink.Body):
        """
        Make a guess
        :param kwargs:
        """
        pass
