SELECT
	s.nev,
    count(*)
    
FROM
	fordito as f
    JOIN nyelv as n on n.id = f.nyelvid
    JOIN szemely as s on s.id = f.szemelyid
    
WHERE 
	 n.fnyelv = 'magyar'
     
group by s.id

ORDER by count(*) DESC
limit 1;