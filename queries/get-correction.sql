select tco.constraint_type,
       kcu.table_name,
       tco.constraint_name,
       kcu.ordinal_position as position,
       kcu.column_name as key_column,
       ico.data_type as type
from information_schema.table_constraints tco
join information_schema.key_column_usage kcu
     on kcu.constraint_name = tco.constraint_name
     and kcu.constraint_schema = tco.constraint_schema
     and kcu.constraint_name = tco.constraint_name
inner join information_schema.columns ico
	on kcu.column_name = ico.column_name
where (tco.constraint_type = 'PRIMARY KEY' or tco.constraint_type = 'FOREIGN KEY')
	and kcu.table_schema = 'correction'
order by kcu.table_schema,
         kcu.table_name,
         position;