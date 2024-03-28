using System;

public class Prompt{

     public static string[] promptList = {
        "line one",
        "line 2"
     };

    public List<string> _journalPrompt = new List<string>(promptList); 

    public Prompt(){

    } 

    public void Display(){
        var random = new Random();
        int index = random.Next(_journalPrompt.Count);
        string journalPrompt = _journalPrompt[index];
        Console.WriteLine($"\n{journalPrompt}");
    }

    public string GetPrompt(){
        var random = new Random();
        int index = random.Next(_journalPrompt.Count);
        string journalPrompt = _journalPrompt[index];

        return journalPrompt;
    }


}