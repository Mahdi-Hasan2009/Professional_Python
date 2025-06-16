DROP TABLE IF EXISTS NOMNOM;

CREATE TABLE NOMNOM(
  NAME TEXT,
  NEIGHBORHOOD TEXT,
  CUISINE TEXT,
  REVIEW REAL,
  PRICE TEXT,
  HEALTH TEXT
);

-- Insert sample data into the nomnom table
INSERT INTO NOMNOM(NAME, NEIGHBORHOOD, CUISINE, REVIEW, PRICE, HEALTH) VALUES
('Peter', 'Brooklyn', 'Steak', 4.4, '$$$$', 'A'),
('Jongro', 'Midtown', 'Korean', 3.5, '$$', 'A'),
('Pocha', 'Midtown', 'Pizza', 4, '$$$', 'B'),
('Lighthouse', 'Queens', 'Chinese', 3.9, '$', 'A'),
('Minca', 'Downtown', 'American', 4.6, '$$', 'A'),
('Marea', 'Chinatown', 'Chinese', 3.0, '$', 'C'),
('Dirty Candy', 'Uptown', 'Italian', 4.9, '$$$$', 'B'),
('Di Fara Pizza', 'Brooklyn', 'Pizza', 3.8, '$$$', 'A'),
('Golden Unicorn', 'Uptown', 'Italian', 3.8, '$$$', 'A');

-- TEST
SELECT * FROM NOMNOM;

-- WHICH ARE THE UNIQ NEIGHBORS?
SELECT DISTINCT NEIGHBORHOOD FROM NOMNOM;

-- WHICH ARE THE UNIQ CUISINE?
SELECT DISTINCT CUISINE FROM NOMNOM;

-- WHICH ARE THE Chinese CUISINE?
SELECT * FROM NOMNOM WHERE CUISINE = "Chinese";


-- FIND OUT ALL RECORDS FOR RATING 4 OR HIGHER?
SELECT * FROM NOMNOM WHERE REVIEW >= 4;

-- FIND OUT ALL RECORDS OF Italian CUISINE AND PRICE $$$?
SELECT * FROM NOMNOM WHERE CUISINE = "Italian" AND PRICE = "$$$";

-- WILDCARD
SELECT * FROM NOMNOM WHERE NAME LIKE "%Candy%";

-- ALL RECORDS WHERE  NEIGHBORHOOD IS Midtown, Downtown AND Chinatown;
SELECT * FROM NOMNOM WHERE NEIGHBORHOOD IN ('Midtown', 'Downtown', 'Chinatown');

-- TOP 4 ORDERS ACCORDING TO REVIEW IN DESCENDING ORDER
SELECT * FROM NOMNOM ORDER BY REVIEW DESC LIMIT 4;