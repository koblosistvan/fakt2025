SELECT
	u.nev,
    MIN(year(k.kezdet)-u.szulev) as kezdési_életkor,
    MAX(year(k.veg)-u.szulev) as végzési_életkor
FROM
	urhajos as u
    join repules as r on r.urhajosid =u.id
    join kuldetes as k on k.id = r.kuldetesid
group BY
	u.id
HAVING
	count(*)>1;