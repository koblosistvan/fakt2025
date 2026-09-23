SELECT
	c.nev,
    MIn(n.ev) as elso,
    MAX(n.ev) as utolso
FROM
	csucs as c
    JOIN naplo as n on c.az = n.csucsaz
GROUP BY
	c.az;