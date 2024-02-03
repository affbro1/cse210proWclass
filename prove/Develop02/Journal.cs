public class Journal{

    public Journal(){
        entries = new List<Entry>(); 
    }

    public void Display (){}

    public string Export(){
        return"";
        }

        public void AddEntry(Entry entry){
            entries.Add(entry); 
        }


}