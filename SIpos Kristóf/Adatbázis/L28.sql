SELECT
	m.nev,
    c.nev,
    c.magassag
from naplo as n
	join maszo as m on m.az=n.maszoaz
    join csucs as c on c.az=n.csucsaz
where
	n.ev < 2000 or c.orszag = 'Pakisztan'
order BY
	c.magassag AND m.nev