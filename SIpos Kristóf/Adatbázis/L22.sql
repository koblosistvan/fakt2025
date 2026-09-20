SELECT
	m.nev as maszo_nev,
    n.ev,
    c.nev as csucs_nev,
    c.magassag
from
	naplo as n
    join maszo as m on m.az=n.maszoaz
    join csucs as c on c.az=n.csucsaz
where
    n.ev=2007
order by
	c.nev;
	
	