SELECT
	c.nev as csucs_nev
    ,min(n.ev) as elso
    ,min(n.ev) as utolso
FROM
	csucs as c
    JOIN naplo as n on n.csucsaz = c.az
GROUP BY
	c.az;