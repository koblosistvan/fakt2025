select
	m.nev as maszo_nev,
    n.ev,
    c.nev as csucs_nev,
    c.magassag
from
	naplo as n
    join maszo as m on m.az=n.maszoaz
    join csucs as c on c.az=n.csucsaz
WHERE
	n.ev < 2000
order BY
	m.nev,
    n.ev;
    
