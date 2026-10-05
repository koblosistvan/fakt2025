SELECT
	*
FROM
	nyelv as n
	join doku as d 
WHERE
	d.terjedelem <= 5000;