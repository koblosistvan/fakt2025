SELECT darab.cim
FROM darab
WHERE DATE('2000-12-31') BETWEEN darab.bemutato AND darab.utolso;