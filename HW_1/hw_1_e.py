def from_roman_to_arabic(roman_numeral):
    symbols = {'I': 1, 'V': 5, 'X': 10, 'L': 50}
    arabic_numeral = 0
    i = 0
    while i < len(roman_numeral):
        if i + 1 < len(roman_numeral) and symbols[roman_numeral[i]] < symbols[roman_numeral[i + 1]]:
            arabic_numeral += symbols[roman_numeral[i + 1]] - symbols[roman_numeral[i]]
            i += 2
        else:
            arabic_numeral += symbols[roman_numeral[i]]
            i += 1
    return arabic_numeral


def ordering(king_name):
    name, roman_numeral = king_name.split()
    arabic_numeral = from_roman_to_arabic(roman_numeral)
    return name, arabic_numeral


if __name__ == '__main__':
    kings_amount = int(input())
    history = []
    for _ in range(kings_amount):
        history.append(input())
    history.sort(key=ordering)
    for king in history:
        print(king)
