SELECT
	d.terjedelem,
    d.szakterulet
FROM
	nyelv as n
    join doku as d on d.nyelvid = n.id
    join fordito as f on f.nyelvid = n.id
    join szemely as s on f.szemelyid = s.id
WHERE
	n.fnyelv = 'angol'
    AND
    n.cnyelv = 'magyar'
    AND
    s.elerheto = -1
order BY
	d.terjedelem DESC;