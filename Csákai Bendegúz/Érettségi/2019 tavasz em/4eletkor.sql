SELECT
	u.nev,
    YEAR(MIN(k.kezdet)) - u.szulev as legkorabbi,
    YEAR(MAX(k.kezdet)) - u.szulev as legkesobbi
FROM
	urhajos as u
    JOIN repules as r on r.urhajosid = u.id
    JOIN kuldetes as k on r.kuldetesid = k.id
GROUP BY
	r.urhajosid
HAVING
    count(r.urhajosid) > 1;