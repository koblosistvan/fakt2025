SELECT nev, magassag from csucs
where magassag>=8500 AND
orszag LIKE '%kína%'
order by magassag DESC;