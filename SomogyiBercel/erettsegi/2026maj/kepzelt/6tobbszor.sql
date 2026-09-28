SELECT darab.cim
FROM darab
WHERE (SELECT darab.hanyszor FROM darab WHERE darab.cim = 'Szabadon foglak') < darab.hanyszor;