SELECT
	s.nev
FROM
	szemely as s
    JOIN fordito as f on f.szemelyid = s.id
   	JOIN nyelv as n on f.nyelvid = n.id
WHERE
	n.fnyelv = 'magyar'
GROUP BY
	s.id
ORDER BY
	count(*) DESC
    LIMIT 1;