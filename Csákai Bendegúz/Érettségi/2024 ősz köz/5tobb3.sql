SELECT
	z.diaknev, z.evfolyam, z.osztaly
FROM
	vizsgazo as z
   	JOIN vizsgak as v on z.id = v.vizsgazoid
GROUP BY
	v.vizsgazoid
HAVING
	COUNT(v.vizsgazoid) > 3;