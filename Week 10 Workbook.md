Project Workbook – Week 9
=========================

Meeting:
--------
- I met with Guido and Kevin this week and later with Kevin, Guido and Grace. They helped me through some kinks I had with generating databases.
- We discussed the direction we think we should be taking with the poster and bounced some ideas around. Sounds like the centrepiece will be a large flowchart at this point.
  
Progress:
---------
- Generated a python script to generate a BAT file which flattens every MZN and DZN pairing into an FZN that GECODE can use to solve that instance of the problem.
- Generated a python script to run GECODE on every generated FZN and use the CP-Profiler to examine the search tree and generate a database to represent it
- Started generating fzns and databases

Problems:
---------
- The mzn2fzn procedure does not have a timeout parameter. This means that for conversions which take a substantial amount of time, there is a huge delay in which there is very little workflow happening. I can't get around this without building complicated solutions using windows commands, which in turn create other issues. I have been manually terminating on files which take too long to flatten.
- The 

To Do:
------
- Now that I know we are trying to source databases that will have a smaller amount of information, and thus take less time to analysis - I will revisit my database (problem) categories and see if they are still suitable, checking the benchmarks as I go.
- Time permitting, I can then begin generating the databases
- Set up a meeting with Grace to discuss the categories and make sure I can correctly generate suitable databases - as she is more experienced than I am
- Potentially meet with Kevin outside of regular hours next week to ensure I am on the right track with the databases.
