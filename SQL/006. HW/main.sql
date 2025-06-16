DROP TABLE IF EXISTS FOODIE;

CREATE TABLE FOODIE(
  NAME TEXT,
  NEIGHBORHOOD TEXT,
  CUISINE TEXT,
  REVIEW REAL,
  PRICE TEXT,
  HEALTH TEXT
);

-- Insert sample data into the FOODIE table
INSERT INTO FOODIE(NAME, NEIGHBORHOOD, CUISINE, REVIEW, PRICE, HEALTH) VALUES
('La Bella', 'Brooklyn', 'Italian', 4.2, '$$$', 'A'),
('Taste of Seoul', 'Midtown', 'Korean', 4.1, '$$', 'B'),
('Saffron', 'Downtown', 'Indian', 3.7, '$$', 'A'),
('Dragon Palace', 'Chinatown', 'Chinese', 4.3, '$', 'A'),
('Burger Craft', 'Queens', 'American', 3.6, '$$', 'B'),
('The Sushi Bar', 'Uptown', 'Japanese', 4.8, '$$$$', 'A'),
('Casa Mexicana', 'Midtown', 'Mexican', 4.0, '$$', 'A'),
('Green Leaf', 'Brooklyn', 'Vegan', 4.5, '$$', 'A'),
('Pizza Centrale', 'Downtown', 'Pizza', 3.9, '$$$', 'B'),
('Le Petit Bistro', 'Queens', 'French', 4.7, '$$$$', 'A');

-- TEST
SELECT * FROM FOODIE;

-- WHICH ARE THE UNIQUE NEIGHBORHOODS?
SELECT DISTINCT NEIGHBORHOOD FROM FOODIE;

-- WHICH ARE THE UNIQUE CUISINES?
SELECT DISTINCT CUISINE FROM FOODIE;

-- WHICH ARE THE Chinese CUISINE?
SELECT * FROM FOODIE WHERE CUISINE = 'Chinese';

-- FIND OUT ALL RECORDS FOR RATING 4 OR HIGHER
SELECT * FROM FOODIE WHERE REVIEW >= 4;

-- FIND OUT ALL RECORDS OF Italian CUISINE AND PRICE $$$
SELECT * FROM FOODIE WHERE CUISINE = 'Italian' AND PRICE = '$$$';

-- WILDCARD: FIND ALL RECORDS WHERE NAME CONTAINS 'Candy'
SELECT * FROM FOODIE WHERE NAME LIKE '%Leaf%';

-- ALL RECORDS WHERE NEIGHBORHOOD IS Midtown, Downtown, OR Chinatown
SELECT * FROM FOODIE WHERE NEIGHBORHOOD IN ('Midtown', 'Downtown', 'Chinatown');

-- TOP 4 ORDERS ACCORDING TO REVIEW IN DESCENDING ORDER
SELECT * FROM FOODIE ORDER BY REVIEW DESC LIMIT 4;