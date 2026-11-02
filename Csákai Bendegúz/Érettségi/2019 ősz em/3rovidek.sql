SELECT 
	count(d.terjedelem) as '5000_kisebb', SUM(n.egysegar) as ossz_egysegar
FROM
	doku as d
    JOIN nyelv as n on n.id = d.nyelvid
WHERE
	d.terjedelem <= 5000;