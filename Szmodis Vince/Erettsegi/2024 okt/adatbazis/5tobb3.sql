SELECT
	vizsgazo.diaknev,
    vizsgazo.evfolyam,
    vizsgazo.osztaly
FROM
	vizsgazo
    JOIN vizsgak on vizsgak.vizsgazoid = vizsgazo.id
GROUP BY
	vizsgazo.diaknev
HAVING
	count(*)>=3;