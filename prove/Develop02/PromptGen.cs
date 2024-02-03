using Microsoft.VisualBasic;

public class Prmopt{

     

    public List<string> prompt = new List<string>{
        "Prompt 1",
        "Prompt 2",
        "Prompt 3"
    }; 

    String nextVal = Random.Next(Prmopt.Count); 

}