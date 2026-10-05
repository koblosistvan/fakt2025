SELECT
	Count(allekerdezes.orszag) 
FROM 
	(SELECT DISTINCT(orszag) FROM urhajos) AS allekerdezes;