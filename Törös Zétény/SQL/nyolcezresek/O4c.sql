SELECT
	c.nev as csucs_nev,
    MIN(n.ev) as első,
    MAX(n.ev) as utolsó
FROM
	csucs as c 
    JOIN naplo as n on n.csucsaz=c.az
GROUP BY
	c.az;