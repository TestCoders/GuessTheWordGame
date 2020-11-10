from random import randrange

# Implementeer je de lijst
thislist = ["Henk", "Sjaak", "Bier", "Pubquiz", "Testcoders", "Scheissarbeid", "Koekenpan", "Word", "Wak", "Vet",
            "Leip", "Rona", "Koningsdag?", "Wintersport?", "Urenapp", "Googledag"]

# Maak logica om de MagicWord te selecteren
randomIndex = randrange(0, len(thislist) - 1)

MagicWord = thislist[randomIndex]

# Maak logica waar de gebruiker input kan leveren, bv in de console.
# Zorg dat de gebuiker bv 5 pogingen heeft
good_input = None
attempts = 0
while not good_input and attempts < 5:
    playersGuess = input()
    if playersGuess != MagicWord:
        attempts = attempts + 1
        if len(MagicWord) < len(playersGuess):
            print('Jouw woord is langer dan het te raden woord')
        if len(MagicWord) > len(playersGuess):
            print('Jouw woord is korter dan het te raden woord')
        if len(MagicWord) == len(playersGuess):
            print('Jouw woord is net zo lang als het te raden woord')
        print('Probeer het nog een keer!')
    else:
        good_input = playersGuess
        print('Geraden! Gefeliciteerd!')
