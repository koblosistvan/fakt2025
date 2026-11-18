SELECT
	nev
FROM 
	nyelv,
    fordito,
    szemely
WHERE
	nyelv.id = nyelvid AND
    szemelyid = szemely.id AND
    szemely.elerheto AND
	szemely.id in (SELECT f.szemelyid FROM fordito as f JOIN nyelv as n on n.id = f.nyelvid WHERE n.fnyelv = 'magyar' AND n.cnyelv = 'angol')
	AND
    szemely.id in (SELECT f.szemelyid FROM fordito as f JOIN nyelv as n on n.id = f.nyelvid WHERE n.fnyelv = 'magyar' AND n.cnyelv = 'orosz')
GROUP BY
	szemely.nev;