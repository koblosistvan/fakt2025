select 
	nev,magassag,orszag 
from 
	csucs
where
	orszag like '%kína%'
order by
	nev;