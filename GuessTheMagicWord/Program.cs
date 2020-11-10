using System;
using System.Collections.Generic;

namespace GuessTheWordGame
{
    public class Program
    {
        private static int _guessesRemaining = 5;

        public static void Main()
        {
            var theMagicWord = SetTargetWord();
            Console.WriteLine("Welcome to the Guess The Word Game. What word am I thinking of..?");
            Guess(theMagicWord);
        }

        private static void Guess(string theMagicWord)
        {
            while (_guessesRemaining > 0)
            {
                Console.WriteLine("Your input:");
                var userInput = Console.ReadLine().ToLower();

                if (IsWordCorrect(userInput, theMagicWord))
                {
                    Console.WriteLine("Congratulations! You beat the game!");
                    Environment.Exit(0);
                }
                else
                {
                    _guessesRemaining--;
                    Console.WriteLine($"Try again! You have {_guessesRemaining} guesses remaining!");
                    GiveLengthFeedback(userInput, theMagicWord);
                    GiveCharacterAndPositionFeedback(userInput, theMagicWord);
                }
            }

            Console.WriteLine($"Too bad! You lost the game! The correct word was: {theMagicWord}");
            Environment.Exit(0);
        }

        private static bool IsWordCorrect(string userInput, string theMagicWord)
        {
            if (userInput.Equals(theMagicWord, StringComparison.InvariantCultureIgnoreCase))
            {
                return true;
            }
            else
            {
                return false;
            }
        }

        private static string SetTargetWord()
        {
            var words = new List<string>()
            {
                "Henk", "Sjaak", "Bier", "Koningsdag", "Testcoders", "Scheissarbeid", "Koekenpan",
                "Word", "Wak", "Vet", "Leip", "Rona", "Koningsdag?", "Wintersport?", "Urenapp",
                "Googledag"
            };

            var theMagicWord = words[new Random().Next(0, words.Count)];
            return theMagicWord;
        }

        private static void GiveLengthFeedback(string userInput, string theMagicWord)
        {
            if (theMagicWord.Length > userInput.Length)
            {
                Console.WriteLine($"Target word is {theMagicWord.Length - userInput.Length} letters longer");
            }

            if (theMagicWord.Length < userInput.Length)
            {
                Console.WriteLine($"Target word is {userInput.Length - theMagicWord.Length} letters shorter!");
            }

            if (theMagicWord.Length == userInput.Length)
            {
                Console.WriteLine("Your guessed word has the same amount of letters as the target word!");
            }
        }

        private static void GiveCharacterAndPositionFeedback(string userInput, string theMagicWord)
        {
            userInput = userInput.ToLower();
            theMagicWord = theMagicWord.ToLower();

            for (var i = 0; i < userInput.Length; i++)
            {
                if (i == theMagicWord.Length - 1)
                {
                    break;
                }

                if (userInput[i].Equals(theMagicWord[i]))
                {
                    Console.WriteLine($"The character {userInput[i]} is placed correct!");
                }
                else if (theMagicWord.Contains(userInput[i].ToString()))
                {
                    Console.WriteLine($"The character {userInput[i]} is correct, but not in the right position!");
                }
            }
        }
    }
}
