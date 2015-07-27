## 10 week progress

This week was addicted to 1999, 1997 year. Data from 1999, 1997 years had been added
to the MySQL database.

[Link to download a full dump](https://www.dropbox.com/s/2923219lwvllkep/dump.sql.zip?dl=0)

## Questions

I've spend some time on file-processing optimizations, as for now I need to run whole processing
(for every year) every time when table structure changes significantly (for example, datatype for field changed). So probably I need to change whole procedure here, otherwise it will slow process
of adding new years down.

## 11 week plan

To import years 1995 and earlier
