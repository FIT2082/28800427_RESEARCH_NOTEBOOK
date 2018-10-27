Project Workbook – Week 9
=========================

Meeting:
--------
- I met with Guido and Kevin this week and later with Kevin, Guido and Grace. They helped me through some kinks I had with generating databases.
- We discussed the direction we think we should be taking with the poster and bounced some ideas around. Sounds like the centrepiece will be a large flowchart at this point.
  
Progress:
---------
- Fixed up a couple of kinks in my Python script that ultimately is responsible for flattening the Model/Data pairings, then ran it on some of the files which I hadn't done (due to the kinks).
- Generated a python script to run Gecode on every generated FZN and use the CP-Profiler to examine the search tree and generate a database to represent it
- Started generating databases

Problems:
---------
- Some of the Fzn files take an incredibly long time to solve and thus profile. To tackle this, I used the timeout option that Gecode provides to cut the sove short, knowing that CPP would profile the tree so far anyway and it would likely yield enough data after about 10 seconds.
- Once the solve had finished, I made the next BAT command a TASKKILL on the Profiler. This is because after every solve, the profiler would stop working for some reason - ultimately leading to my computer maintaining hundreds of CPP processes at once, as well as outputing to the terminal constantly to tell me what it was doing (which was also a mistake, though I never got around to making the BAT run output-free).

To Do:
------
- Review the databases I have generated so far and make sure they're looking OK.
- Try and come up with a design for the poster's diagram centerpiece. 
- Start writing up content for the poster
- Fix any issues with database generation
- Start uploading databases here for Grace to access so that she can work on converting them to MIDI Disassembly. 
