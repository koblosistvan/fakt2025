select 
	s.nev
from 
	szemely as s 
    join fordito as f on s.id = f.szemelyid 
    join nyelv as n on n.id = f.nyelvid
where 