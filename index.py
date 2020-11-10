from random import randrange

# Implementeer je de lijst
this_list = ["Henk", "Sjaak", "Bier", "Pubquiz", "Testcoders", "Scheissarbeid", "Koekenpan", "Word", "Wak", "Vet",
             "Leip", "Rona", "Koningsdag?", "Wintersport?", "Urenapp", "Googledag"]

# Maak logica om de MagicWord te selecteren
random_index = randrange(0, len(this_list) - 1)

magic_word = this_list[random_index]

# Maak logica waar de gebruiker input kan leveren, bv in de console.
# Zorg dat de gebuiker bv 5 pogingen heeft
good_input = None
attempts = 0


def compare_two_words_by_characters(players_guess, _magic_word):
    comparison = []
    ind = 1
    feedback = ''
    for x, y in zip(players_guess, _magic_word):
        # print(x, y)
        if x == y:
            comparison.append(True)
            feedback = feedback + x
        else:
            comparison.append(False)
            feedback = feedback + '_'
        ind = ind + 1
    # print(comparison)
    print(feedback)


while not good_input and attempts < 5:
    _players_guess = input()
    if _players_guess != magic_word:
        attempts = attempts + 1
        if len(magic_word) < len(_players_guess):
            print('Jouw woord is langer dan het te raden woord')
        if len(magic_word) > len(_players_guess):
            print('Jouw woord is korter dan het te raden woord')
        if len(magic_word) == len(_players_guess):
            print('Jouw woord is net zo lang als het te raden woord')
        compare_two_words_by_characters(_players_guess, magic_word)

        if attempts < 4:
            print('Probeer het nog een keer!')
        else:
            print('Laatste poging')

    else:
        good_input = _players_guess
        print('Geraden! Gefeliciteerd!')
