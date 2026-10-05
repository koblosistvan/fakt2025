SELECT
	k.megnevezes,
    (k.veg-k.kezdet) as napok_szama 
FROM
	kuldetes as k
WHERE
	year(k.veg) = year(k.kezdet)+1;