## 7 week progress

This week was addicted to 2009 year. Data from 2009 national data files was added
to the MySQL database. Also the structure of service-tables and service-fields was
slightly changed to make a new year adding process easier.

Tests for whole process were fixed (they were broken for about 2 weeks).

I've removed in_2011 and in_2013 boolean fields, which used to be in every table.
For now only table ahs_service_datatype_year has information about every column's year
of presence.

I've also updated the documentation wiki to reflect current state of the project and
data structure.

## Problems

It turned out, that amount of fields for newhouse table is too much to be stored with
InnoDB engine, so I've switched to MyISAM for all tables.

## 8 week plan

To import 2008 year.
