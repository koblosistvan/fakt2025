SELECT
	s.nev
FROM
	szemely as s 
    JOIN fordito as f on f.szemelyid = s.id
    JOIN nyelv as n on n.id = f.nyelvid
WHERE
	n.fnyelv = 'magyar'
GROUP by 
	s.id

ORDER by 
	COUNT(*) DESC LIMIT 1;