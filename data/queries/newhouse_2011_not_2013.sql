select * from ahs_service_datatype as dt join
 ahs_service_datatype_year as dy on (dt.id = dy.table_field_id)
 where (dt.table_name = 'newhouse') and (dy.year = 2011)
  and (year not in (select year from ahs_service_datatype as dt2 join
   ahs_service_datatype_year as dy2 on (dt2.id = dy2.table_field_id)
   where (dt2.table_name = 'newhouse') and (dy2.year = 2013))) limit 10;
