SELECT
	c.nev,
    c.magassag
FROM
	csucs as c 
    join naplo as n on c.az = n.csucsaz
ORDER BY
	n.ev DESC
    LIMIT 3;