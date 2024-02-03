using System;
using System.ComponentModel.Design;
using System.Diagnostics;

class Program
{
    public Journal journal; 
//Example code from class 
    static void Main(string[] args)
    {
        Console.WriteLine("Hello Develop02 World!");
        Run(); 
    }

    public string GetPrompt(){
        return ""; 
    }

    public void Run(){
        Boolean keepGoing = true;

        while(keepGoing); 
        var selection = ShowMenu(); 
        //use showmenu to show the user avaliable options 
        //if option 1, run its option
        //if option 2, run its code 
        //if last option, makes keepGoing = false which stops the code 
        if (selection == 1){
            //add entry
            var placeholderResponse = "This is what the user typed in"

            var entry = new Entry(placeholderResponse, prmopt); 

            journal.AddEntry(entry); 
        }

        if (selection == 2){
            //display entries 
        }

        if (selection == 5){
            keepGoing = false; 
        }
    }

    static void ShowMenu(){
        Console.WriteLine("Selection Option \n 1. Add Entry \n rest of menu here");
        string input= Console.ReadLine();
        return int.Parse(input); 
    }

    public void SaveToFile(){}

    public void LoadFromFile(){}



}