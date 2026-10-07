SELECT 
	count(*) as dbszam,
    sum(egysegar) as osszbevetel
FROM
	doku as d
    join nyelv as n on d.nyelvid = n.id

where
	d.terjedelem <= 5000;