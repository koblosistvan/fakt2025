SELECT
	d.szakterulet,
    n.fnyelv,
    n.cnyelv
FROM
	doku as d
    join nyelv as n on n.id = d.nyelvid
WHERE
	d.munkaido BETWEEN 7 AND 9
order BY
	n.fnyelv;