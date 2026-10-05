SELECT
	k.megnevezes,
    datediff(veg, kezdet) as eltelt_ido
FROM
	kuldetes as k 
WHERE
	year(k.kezdet)<year(k.veg);