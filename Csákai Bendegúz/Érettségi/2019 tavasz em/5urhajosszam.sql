SELECT
	u.orszag, count(*) as orszag_urhajosai_szama
FROM
	urhajos as u
GROUP BY
	u.orszag
ORDER BY
	count(u.orszag) DESC;