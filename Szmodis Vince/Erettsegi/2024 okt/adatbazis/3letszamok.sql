select
	evfolyam,
    osztaly,
    COUNT(*) as letszam
FROM
	vizsgazo
WHERE
	evfolyam = 12
GROUP BY
	osztaly;