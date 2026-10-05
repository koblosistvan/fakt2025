select
    k.megnevezes,
    datediff(veg,kezdet) as idotartam
from 
    kuldetes as k
where year(kezdet) < year(veg)
