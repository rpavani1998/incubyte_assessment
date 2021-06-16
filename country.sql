CREATE DATABASE IF NOT EXISTS incubyte;

USE incubyte;

CREATE TABLE IF NOT EXISTS Country (code varchar(5) NOT NULL, name varchar(25), PRIMARY KEY (code));

INSERT INTO Country values ('IND', 'India'),
			   ('USA', 'America'),
			   ('PHIL', 'Philippines'),
			   ('NYC', 'NewYork'),
                           ('AU', 'Australia');
