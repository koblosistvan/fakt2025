SELECT DISTINCT darab.cim, mufaj.nev
FROM darab
JOIN mufaj ON mufaj.id = darab.mufajid
WHERE mufaj.nev IN ('opera', 'operett') AND
	darab.cim LIKE '%asszony%';