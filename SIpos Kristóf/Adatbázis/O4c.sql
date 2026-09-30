SELECT
	c.nev AS csucs_nev,
    MIN(n.ev) as elso,
    MAX(n.ev) as utolso
FROM
	csucs as c
    join naplo as n on n.csucsaz = c.az
group by
	c.az;