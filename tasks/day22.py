from utils import read_input

raw = read_input.read_input_strings_groups('day22')


def parse_decks(raw_input):
    deck1 = [int(number) for number in raw_input[0][1:]]
    deck2 = [int(number) for number in raw_input[1][1:]]
    return deck1, deck2


def calculate_score(deck1, deck2):
    deck = list(reversed(deck1) if len(deck1) > 0 else reversed(deck2))
    result = 0
    for i in range(len(deck)):
        result += (i + 1) * deck[i]
    print(f'The final score is {result}')


def part_one():
    deck1, deck2 = parse_decks(raw)
    while len(deck1) != 0 and len(deck2) != 0:
        card1 = deck1.pop(0)
        card2 = deck2.pop(0)
        if card1 > card2:
            deck1.append(card1)
            deck1.append(card2)
        else:
            deck2.append(card2)
            deck2.append(card1)
    calculate_score(deck1, deck2)


def get_winner_deck(deck1, deck2, decks):
    while len(deck1) > 0 and len(deck2) > 0:
        if (deck1, deck2) in decks:
            return deck1, deck2
        else:
            decks.append((deck1.copy(), deck2.copy()))
            card1 = deck1.pop(0)
            card2 = deck2.pop(0)
            if len(deck1) >= card1 and len(deck2) >= card2:
                sub1, sub2 = get_winner_deck(deck1[:card1], deck2[:card2], [])
                if len(sub1) > 0:
                    deck1.append(card1)
                    deck1.append(card2)
                else:
                    deck2.append(card2)
                    deck2.append(card1)
            else:
                if card1 > card2:
                    deck1.append(card1)
                    deck1.append(card2)
                else:
                    deck2.append(card2)
                    deck2.append(card1)
    return deck1, deck2


def part_two():
    deck1, deck2 = parse_decks(raw)
    deck1, deck2 = get_winner_deck(deck1, deck2, [])
    calculate_score(deck1, deck2)


if __name__ == '__main__':
    part_one()
    part_two()
