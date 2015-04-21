## Intro

This project imports data from American Housing Survey (AHS) to MySQL database.

## Import data

to be able to import data, you should put data file into the

```
data/non-git
```

folder. For example, newhouse.csv should be putted into

```
data/non-git/puf2013/newhouse.csv
```

Since github can't hold such a big files, this manual step exists.

## Files

There are several files, which helps this app to work:

### File with columns and datatypes

```
data/columns/newhouse.csv
```

This file describes all columns and corresponding datatypes for those columns to generate Newhouse model.

### Small part of the data above

```
data/columns/newhouse-smalldata.csv
```

Just the same as above, the only difference is smaller number of columns (for manual testing purpose mostly)

### Generated fields

With help of files above

```
data/columns/generated/newhouse.gen
```

generated (data fields with python-like syntax). To generate in run ```Newhouse().generate_columns()```
This generated data then being copied and pasted to Newhouse model.

### Sample files

```
data/sample/puf2013/newhouse.csv
```

contains small part of original AHS data, for unit-tests.
