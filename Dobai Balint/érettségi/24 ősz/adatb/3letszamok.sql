SELECT
	count(*) as letszam,
    evfolyam,
    osztaly
FROM vizsgazo
GROUP by evfolyam, osztaly
having evfolyam = 12;