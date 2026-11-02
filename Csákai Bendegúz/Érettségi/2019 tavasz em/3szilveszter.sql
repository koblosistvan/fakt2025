SELECT
	k.megnevezes, DATEDIFF(k.veg,k.kezdet) as urben_napok
FROM
	kuldetes as k
WHERE
    YEAR(k.kezdet) < YEAR(k.veg);