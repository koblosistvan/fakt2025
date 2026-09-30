SELECT 
	t.ev,
    t.start,
    t.orszag
from 
	tour as t
where
	start != 'Franciaorszag'
    AND
    ev>=1950