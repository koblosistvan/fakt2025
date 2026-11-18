SELECT
	s.nev
FROM
	fordito as f 
    JOIN nyelv as n on n.id=f.nyelvid
    JOIN szemely as s on s.id = f.szemelyid
WHERE
	n.fnyelv LIKE 'magyar'
GROUP BY 
	s.id
ORDER BY
	COUNT(DISTINCT n.fnyelv, n.cnyelv) DESC
LIMIT 1;