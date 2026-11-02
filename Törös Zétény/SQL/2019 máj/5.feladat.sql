SELECT Count(allekerdezes.orszag)
FROM (SELECT u.orszag FROM urhajos as u GROUP BY u.orszag) AS allekerdezes;