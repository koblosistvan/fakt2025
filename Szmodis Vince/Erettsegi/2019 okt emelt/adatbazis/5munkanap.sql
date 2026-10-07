SELECT
	d.szakterulet,
    n.fnyelv,
    n.cnyelv
FROM
	doku as d 
  	join nyelv as n on n.id = d.nyelvid
where
	d.munkaido>=7 and d.munkaido<=9
order by
	n.fnyelv;