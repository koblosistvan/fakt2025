SELECT
	COUNT(d.id),
    SUM(n.egysegar)
FROM
	nyelv as n
    JOIN doku as d on d.nyelvid = n.id;