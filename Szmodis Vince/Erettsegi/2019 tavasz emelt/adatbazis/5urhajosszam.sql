SELECT
	u.orszag,
    COUNT(*) as dbszam
FROM
	urhajos as u 
GROUP BY
u.orszag
ORDER BY 
	dbszam DESC;    