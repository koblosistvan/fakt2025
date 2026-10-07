SELECT
	COUNT(*) as db,
    SUM(n.egysegar) as ossz_ar
FROM
	doku as d 
    JOIN nyelv as n on n.id = d.nyelvid
WHERE
	d.terjedelem <= 5000;