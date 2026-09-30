SELECT
	d.cim
FROM
	darab_txt as d
    JOIN mufaj_txt as m on m.id = d.mufajid
WHERE
	d.hanyszor >
GROUP BY
	d.cim;