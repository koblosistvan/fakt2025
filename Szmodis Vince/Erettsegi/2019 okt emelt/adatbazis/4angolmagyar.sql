SELECT
	d.terjedelem,
    d.szakterulet
    
FROM
	nyelv as n
    JOIN doku as d on d.nyelvid = n.id
WHERE
	n.fnyelv = 'angol' and n.cnyelv = 'magyar'
ORDER BY
	d.terjedelem DESC;