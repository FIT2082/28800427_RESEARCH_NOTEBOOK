Project Workbook – Week 9
=========================

Meeting:
--------
- Grace and I met with Guido and Kevin this Tuesday once again. 
- Kevin assisted me in setting up the CP Profiler tool for windows, which will allow me to analyse the behaviour trees output by the minizinc solver. 
- Kevin also confirmed that the Profiler has been updated to allow us to generate a pixel tree (a simplification of the behaviour tree) which we can use to visualise. 
- The precision of the pixel tree can be tweaked with a simple parameter.
- Guido advised that we could select benchmark tests for which the generated behaviour trees would be sufficiently small that they would take only seconds to complete - for simplicity during analysis.
  
Progress:
---------
- Grace is still making some changes to the converter program.
- I have started automating the database generation process. This has been pretty arduous.
- I have set up the flattening (conversion) from models/data to a solvable FlatZinc file so that it is mostly automatic, and will perform this compilation using both Gecode specific functionality, and also using only the functionality available in the standard libraries.

Issues:
-------
- The results of the MiniZinc challenge should in theory provide a way of selecting only problem instances which will run in a sufficiently small timeframe. Unfortunately, most of the problem instances have a documented solve time that is too long anyway - so in practice I can't really cut out problem instances without removing most of the total data set.
- In order to generate databases, the first thing is to take the models from the benchmarks and then pair them with different datasets to create problem instances. This process is done with the "mzn2fzn" application, which comes packaged with the MiniZinc IDE. 
- Unfortuantely, mzn2fzn does not have a timeout option. I have written a python script, which generates a .BAT script which will in turn perform the above conversion on all possible model-data pairings in the benchmarks. However the BAT file gets stuck on some pairings for up to 3 hours.
- I have been forced to manually terminate the BAT and restart it from the correct point. All-up, the conversion has taken about 3 days. Thankfully, it only needs to be done once. 

To Do:
------
- Automating the process of producing FlatZinc files, then running them though the solver and profiling as it happens.
- Potentially meet with Kevin outside of regular hours next week to ensure I am on the right track with the databases.
