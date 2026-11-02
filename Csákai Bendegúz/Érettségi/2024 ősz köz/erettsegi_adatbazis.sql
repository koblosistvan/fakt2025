DROP DATABASE IF EXISTS erettsegi;
CREATE DATABASE erettsegi;
EXECUTE IN erettsegi;

CREATE TABLE vizsgazo (
    id int PRIMARY KEY,
	diaknev varchar(255),
	evfolyam int,
	osztaly varchar(255));
    
CREATE TABLE tanar (
    id varchar(255) PRIMARY KEY,
    nev varchar(255));

CREATE TABLE vizsgak (
    id int PRIMARY KEY,
    bizottsag varchar(255),
    vizsgatargy varchar(255),
    vizsgazoid int,
    tanarid varchar(255))