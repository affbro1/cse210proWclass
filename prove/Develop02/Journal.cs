using System;
using System.IO;


public class Journal{

    public List<JournalEntry> _journal = new List<JournalEntry>();
    public string _userFileName; 

    public void Display(){
        Console.WriteLine("\nCurrent Journal Entries");
        foreach (JournalEntry journalEntry in _journal){
            journalEntry.Display();
        }
        Console.WriteLine("\nEnd of Entries");
    }


    public void createJournalFile(){
        Console.WriteLine("What is the file name?");
        string userInput = Console.ReadLine();
        _userFileName = userInput + '.txt';
        
        
    }













}