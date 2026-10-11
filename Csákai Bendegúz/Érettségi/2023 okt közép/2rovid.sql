SELECT
	cim, mufaj, hossz
FROM
	filmek
WHERE
	hossz < 45
ORDER BY
	hossz;