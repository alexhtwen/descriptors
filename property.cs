using System;

public class Tree {
    private string breed;    // private attribute
    private int age;         // private attribute

    public string Breed {      // public property
        get { return breed; }
        set {
            if (string.IsNullOrWhiteSpace(value)) {
                throw new ArgumentException("Breed cannot be null or whitespace.");
            }
            breed = value;
        }
    }

    public int Age {          // public property
        get { return age; }
        set {
            if (value < 0) {
                throw new ArgumentOutOfRangeException("Age cannot be negative.");
            }
            age = value;
        }
    }

    public Tree(string breed, int age) {  // constructor
        Breed = breed;  // Using property assignment within constructor
        Age = age;
    }
}

public class Program {
    public static void Main() {
        Tree Tree = new Tree("cedar", 30);
        Console.WriteLine(Tree.Breed); // Prints "cedar"

        Tree.Breed = "आरग्वध";            // Triggers the set logic
        Console.WriteLine(Tree.Breed); // Prints "आरग्वध" (阿勒勃)

        try {
            Tree.Age = -5;           // Will throw an ArgumentOutOfRangeException
        }
        catch (Exception ex) {
            Console.WriteLine("Error: " + ex.Message);
        }
    }
}
