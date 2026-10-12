SELECT
	u.nev,
    YEAR(MIN(k.kezdet))-u.szulev,
    YEAR(MAX(k.kezdet))-u.szulev
FROM
	urhajos as u 
    JOIN repules as r on r.urhajosid = u.id
    JOIN kuldetes as k on k.id = r.kuldetesid
GROUP BY
	u.id
HAVING
	COUNT(u.id) > 1;