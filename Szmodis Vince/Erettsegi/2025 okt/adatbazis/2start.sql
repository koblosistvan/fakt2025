SELECT
	ev,
    orszag
FROM
	tour as t
WHERE
	orszag != '' and  
	orszag IS NOT NULL