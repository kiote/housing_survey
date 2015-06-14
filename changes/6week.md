## 6 week progress

This week was about automatizing of the next year adding process.
As the result:

  – now we have all "metadata" (information about tables and field types) stored in MySQL table (before it was stored in a file);
  
  – this metadata table stores information about year of appearing of a current field, so we can always know is this field common for severel years, or not;
  
  – field - type generation was re-thinked, so now it successfully works with several years.  

### Problems

As one of the files are quite big (newhouse of 2011), it's processing takes too much resources and need to be fixed (now "saving data" process is killing by OS for eating too much resources)
 
## 7 week plan

Fix big files saving problem.
Give the result to test (so you can have in your local database both 2013 and 2011 year to experiment with) 
