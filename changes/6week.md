## 6 week progress

Fixed some data-import bugs in import scripts.
Simplify scripts a bit to be able to import next (2011) year and started to import it.

Same tables for different years have different fields 
(some fields are missing and some has been added), I was trying to handle it manually
(and for models homimp and mortg) added some fields from 2011 year.

But this manual changes takes a lot of time, so I'd better automatize it for other models.
The idea is:

– after field generation check model.gen file;
– if it has this field (generated substring) already, do nothing;
– if it has no such string yet, add it.

For now model.gen files generated from 0 every time.

## 7 week plan

Will be here later