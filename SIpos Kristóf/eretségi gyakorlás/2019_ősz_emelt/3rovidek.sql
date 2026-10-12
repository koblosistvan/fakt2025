SELECT
	COUNT(*) as ötezer_alatti_karakter_szám,
    SUM(n.egysegar) as össz_bevétel
FROM
	nyelv as n
	join doku as d on d.nyelvid = n.id
WHERE
	d.terjedelem <= 5000;