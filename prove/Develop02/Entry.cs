using System;

public class Entry{

    public string _journalPrompt = "";
    public string _journalEntry = "";
    public string _journalFile = ""; 

    public void display(){
        Console.WriteLine($"Prompt: {_journalPrompt}");
        Console.WriteLine($"Entry: {_journalEntry}");
    }


}