SELECT
	d1.cim
FROM
	darab as d1,
    darab as d2
WHERE
	d2.cim = 'Szabadon foglak'
GROUP BY
	d1.id,
    d2.id
HAVING
	COUNT(d2.cim)<COUNT(d1.cim);