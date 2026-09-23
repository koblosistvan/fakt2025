SELECT nev as 'Csúcsok neve', magassag, orszag from csucs
WHERE orszag LIKE '%Kína%' 
ORDER BY magassag;