SELECT
	u.nev,
    MIN(year(k.kezdet)-u.szulev) as kezdeti_eletkor,
    MAX(year(k.kezdet)-u.szulev) as utolso_eletkor
FROM
	urhajos as u
    JOIN repules as r on r.urhajosid= u.id
    JOIN kuldetes as k on k.id = r.kuldetesid
GROUP BY
	u.id
HAVING 
	count(*)>1;