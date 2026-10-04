SELECT
	t.ev,
    t.tav,
    t.feladok/t.indulok as arany
FROM
    tour as t
order by
	arany DESC