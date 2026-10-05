SELECT Count(allekerdezes.orszag) 
FROM (SELECT 
      		DISTINCT u.orszag 
      FROM 
     		urhajos as u) AS allekerdezes;