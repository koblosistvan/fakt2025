SELECT 
	d.terjedelem, d.szakterulet
FROM
	doku as d
    JOIN nyelv as n on n.id = d.nyelvid
WHERE
	n.fnyelv = 'angol' AND
    n.cnyelv = 'magyar'
ORDER BY
	d.terjedelem DESC;