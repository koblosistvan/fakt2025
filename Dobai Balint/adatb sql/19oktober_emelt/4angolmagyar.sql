SELECT 
	d.terjedelem,
    d.szakterulet
FROM
	doku as d
    join nyelv as n on d.nyelvid = n.id

where
	n.fnyelv = 'Angol'
    and n.cnyelv = 'Magyar'
    
order by terjedelem DESC;