SELECT
	nev,month(edatum) as honap,count(*) as csucs_szam
from 
	csucs
group by
	month(edatum);