SELECT nev 
FROM nyelv, fordito, szemely 
WHERE nyelv.id=nyelvid AND szemelyid=szemely.id AND  
szemely.id in 
	(SELECT f.szemelyid from fordito as f join nyelv as n where f.nyelvid = n.id AND n.fnyelv = 'magyar' and n.cnyelv = 'orosz' ) AND
szemely.id in    
    (SELECT f.szemelyid from fordito as f join nyelv as n where f.nyelvid = n.id AND n.fnyelv = 'magyar' and n.cnyelv = 'angol') 
group by fordito.szemelyid;