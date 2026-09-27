SELECT 
	t.ev,
    t.start,
    t.orszag
from 
	tour as t
where
	start != 'Franicaorszag'
    AND
    ev>=1950