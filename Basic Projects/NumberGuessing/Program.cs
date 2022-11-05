using System;

public class GuessingGame
{
    static bool playing = true;
    static Random rnd = new Random();
    static string minimum = "";
    static string maximum = "";
    static string? choice = "";
    public static void GetInput() 
    {

        do 
        {
            Console.WriteLine("What is the lowest number to play with: ");
            minimum = Console.ReadLine() ?? " ";
            Console.WriteLine("What is the highest numnber to play with: ");
            maximum = Console.ReadLine() ?? " ";
            Console.WriteLine("Would you like to play a game where you guess a number that the computer thinks of (me) or a game where the computer guesses a number that you think of (pc): ");
            choice = Console.ReadLine() ?? " ";
            if (choice.ToLower() == "me" || choice.ToLower() == "pc"){}
            else 
            {
                Console.WriteLine("Please enter a valid response");
                choice = "";
            }
        } while (choice == "");
    }
    public static void PlayAgain()
    {
        Console.WriteLine("Want to play again? Y/N");
        string choice = Console.ReadLine() ?? " ";
        if (choice == "N")
        {
            playing = false;
        }
    }
    public static void UserPlay(int min, int max) 
    {
        int num = rnd.Next(min, max);
        int guesses = 1;
        bool play = true;
        do
        {
            if (min == max)
            {
                Console.WriteLine("The number is between {0} and {1}, let's assume that you were right this time. You used {2} guesses", min, max, guesses);
            }
            Console.WriteLine("Guess a number between {0} and {1} ", min, max);
            int guess = int.Parse(Console.ReadLine() ?? " ");
            
            if (guess > num)
            {
                Console.WriteLine("{0} is too high, try again!", guess);
                guesses += 1;
                max = guess - 1;
            }
            else if (guess < num)
            {
                Console.WriteLine("{0} is too low, try again!", guess);
                guesses += 1;
                min = guess + 1;
            }
            else if (guess == num)
            {
                Console.WriteLine("{0} is correct, you used {1} guesses.", num, guesses);
                play = false;
            }
        } while (play);
    }
    
    public static void ComputerPlay(int min, int max) 
    {
        int guess = 0;
        string feedback = "";
        int guesses = 0;
        bool play = true;
        do
        {
            if (min != max)
            {
                guess = rnd.Next(min, max);
                guesses += 1;
            }
            else
            {
                guess = min;
            }
            Console.WriteLine("I guess {0}, is this too high (h), too low (l), or correct (c)", guess);
            feedback = Console.ReadLine() ?? " ";
            feedback.ToLower();
            if (feedback == "c")
            {
                Console.WriteLine("Yay I guessed that your number was {0}, it took me {1} tries", guess, guesses);
                play = false;
            }
            else if (feedback == "h")
            {
                max = guess -1;
            }
            else if (feedback == "l")
            {
                min = guess + 1;
            }
            else 
            {
                Console.WriteLine("Please enter a valid resoonse");
                guesses -= 1;
            }
        } while (play);
    }

    static void Main()
    {
        do
        {
        GetInput();
        int min = int.Parse(minimum);
        int max = int.Parse(maximum);
        switch (choice)
        {
            case "me":
                UserPlay(min, max);
                break;
            case "pc":
                ComputerPlay(min, max);
                break;
        }
        PlayAgain();
        } while (playing);
    }
}
