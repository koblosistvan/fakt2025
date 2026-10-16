SELECT
	evfolyam, osztaly, count(*) as letszam
FROM
	vizsgazo
WHERE
	evfolyam = 12
GROUP BY
	osztaly;