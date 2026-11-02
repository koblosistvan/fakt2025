SELECT
	u.orszag,
    COUNT(u.orszag)
FROM
	urhajos as u 
GROUP BY
	u.orszag
ORDER BY
	COUNT(u.orszag) DESC;