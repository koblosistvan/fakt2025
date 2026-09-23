SELECT darab.cim, mufaj.nev
FROM darab
JOIN mufaj ON mufaj.id = darab.mufajid
ORDER BY DATEDIFF(darab.utolso, darab.bemutato) DESC
LIMIT 1;