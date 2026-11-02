SELECT
	d.szakterulet,
    n.fnyelv,
    n.cnyelv
FROM
	doku as d
    join nyelv as n on n.id = d.nyelvid
WHERE
	d.munkaido between 7 and 9
ORDER BY n.fnyelv;