from actors.player import Player
from actors.round import Round

import pytest


@pytest.fixture()
def players():
    return [Player('P1'), Player('P2'), Player('P3'), Player('P4')]


# Test deal cards
def test_deal_cards(players):
    rnd = Round(players)

    deck = rnd.create_deck()
    rnd.deal_players_cards(deck)
    assert len(players[0].hand) == 9
    # test all hand are different
    assert len(
        set(players[0].hand) ^ set(players[1].hand) ^
        set(players[2].hand) ^ set(players[3].hand)
    ) == 36
