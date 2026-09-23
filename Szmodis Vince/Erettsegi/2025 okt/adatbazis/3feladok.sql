SELECT
	ev,
    tav,
    feladok/indulok as arany
FROM
	tour as t 
ORDER BY
	arany DESC;