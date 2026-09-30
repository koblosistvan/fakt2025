SELECT
u.tartalom
from uzenet as u
where 
	u.tartalom LIKE "%bicikli" OR 
    u.tartalom LIKE "%bike%";