/* Versatile info getter — parses name and age from user input with validation. */

using System;
using System.Linq;


class Info {
    public (string, int) GetUserInfo() {
        Console.WriteLine("Enter your name and age (e.g., Mark, 20):\n");
        string user_input = Console.ReadLine();
        var input_parts = user_input.Trim().Split(new char[] { ',', ' ' }).ToList();

        string name = "";
        int age = 0;
        int count = Math.Min(3, input_parts.Count);

        foreach (var part in input_parts.GetRange(0, count)) {
            if (part.All(char.IsLetter) && string.IsNullOrEmpty(name)) {
                name = part;
            } else if (part.All(char.IsDigit) && age == 0) {
                if (int.TryParse(part, out int parsedAge)) {
                    age = parsedAge;
                }
            }
        }

        return (name, age);
    }


    public (string, int) GetMissingInfo(string name, int age) {
        if (string.IsNullOrEmpty(name)) {
            Console.WriteLine(
            "You didn't provide your name.\n" +
            "Please enter your name:\n"
            );
            while (true) {
                var user_input = Console.ReadLine();

                if (string.IsNullOrEmpty(user_input) || user_input.Trim().All(char.IsDigit)) {
                    Console.WriteLine("Please provide a proper name.");
                } else {
                    name = user_input;
                    break;
                }
            }
        }

        if (age == 0) {
            Console.WriteLine($"Hi {name}, you didn't provide your age. Please enter it:\n");
            while (true) {
                var user_input = Console.ReadLine().Trim();

                if (!user_input.All(char.IsDigit)) {
                    Console.WriteLine("You must provide a valid number.");
                } else {
                    age = int.Parse(user_input);
                    break;
                }
            }
        }

        return (name, age);
    }
}


class Program {
    static void Main() {
        var info_getter = new Info();
        var (name, age) = info_getter.GetUserInfo();

        if (name == "" || age == 0)
            (name, age) = info_getter.GetMissingInfo(name, age);

        Console.WriteLine($"Your name is {name} and you are {age} years old.");
    }
}