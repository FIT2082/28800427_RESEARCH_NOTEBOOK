Project Workbook – Week 11
=========================

Meeting:
--------
- This week out meeting was largely centred around taking about the poster and making sure that the ideas sounded good to Guido and Kevin. 
- It was reccomended that we make some changes to the way our workflow was represented in the diagram, to reflect the end goal better (improving the models) and to indicate the cyclic nature of the processes we are creating.
- We confirmed some sources for referencing, covered the aesthetics and also fleshed out the way we would demo the results so far. 
  
Progress:
---------
- Finished generating the databases (as of the end of the week)
- Devised a decent design for the diagram on the poster
- Started writing the content for the poster

Problems:
---------
- It turns out that most databases I had generated up to the point of this week's meeting were corrupt. Kevin originally thought this might be because I was using the wrong Gecode or CPP executable, however it turned out to be a simple issue of terminating the CPP too early - resulting in it not actually outputting the database fully. 
- In order to fix the issue, and not spend days doing it all again, I built in a cutoff which would mean that only the first 10 problem instances would be solved for any given problem/model, and also introduced a TIMEOUT command which enforced a few seconds of delay between the profiler starting and the solver running, as well as between the solver finishing and the profiler being terminated. 
- The databases are totally functional.
- There is also an issue with size. It turns out that pushing all of the db files to GIT is impractical since their size generally exceeds 50MB, and there are still around 200 databases, taking only the first 10. Instead I have started uploading them to a Google Drive folder which can be found [here](https://drive.google.com/drive/folders/1c92gll5rXIczLWx3z-okJWnTecZ3SY7v?usp=sharing "Databases Drive")

To Do:
------
- Focus on the poster for this week, up until next Friday when it is due
- Continue uploading the databases as necessary
