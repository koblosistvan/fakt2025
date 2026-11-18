SELECT
	k.megnevezes,
    DATEDIFF(k.veg,k.kezdet)
FROM
	kuldetes as k 
WHERE 
	year(k.veg) > YEAR(k.kezdet);