SELECT
	t.ev,
    t.tav,
    t.indulok-t.feladok as arany
FROM
    tour as t
order by
	arany DESC