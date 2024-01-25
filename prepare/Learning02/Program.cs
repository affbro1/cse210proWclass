using System;


Job job1 = new Job();
job1._company = "Apple";
job1._jobTitle = "Software Manager";
job1._startYear = "2013";
job1._endYear = "2019";


Job job2 = new Job();
job2._company = "Microsoft";
job2._jobTitle = "Weapons Tester";
job2._startYear = "2010";
job2._endYear = "2022";

Resume resume1 = new Resume();
resume1._name = "Jim";
resume1._jobs.Add(job1);
resume1._jobs.Add(job2);

resume1.DisplayResume(); 

