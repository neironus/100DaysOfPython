from actors.card import Card


def test_symbol_card():
    # good
    card1 = Card('Y', 7)
    assert card1.symbol == 7
    # good
    card2 = Card('B', 10)
    assert card2.symbol == 10
    # good
    card3 = Card('B', 14)  # Aces
    assert card3.symbol == 'A'
