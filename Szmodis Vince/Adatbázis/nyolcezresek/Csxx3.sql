SELECT
	c.nev,
    count(*)
FROM
	csucs as c
    JOIN naplo as n ON c.az = n.csucsaz
WHERE
	c.orszag LIKE '%kína%'
GROUP BY
	c.az;