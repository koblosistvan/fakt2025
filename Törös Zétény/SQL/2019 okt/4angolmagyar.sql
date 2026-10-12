SELECT
	d.terjedelem,
    d.szakterulet
FROM
	doku as d 
    JOIN nyelv as n on n.id = d.nyelvid
WHERE
	n.fnyelv  LIKE 'angol'
    AND n.cnyelv  LIKE 'magyar'
ORDER BY
	d.terjedelem DESC;