CREATE TABLE PRACTICAL(
    SUBJECT VARCHAR(50),
    NAME VARCHAR(50),
    DATE TEXT,
    VALUE TEXT
);

INSERT INTO PRACTICAL(SUBJECT, NAME, DATE, VALUE) VALUES
    ('Chemistry',    'crystal',             '2025-05-14', '100mL water'),
    ('Biology',      'Microscope',          '2025-04-24', NULL),
    ('Chemistry',    'Metallic carbon',     '2025-04-30', 'Sodium Carbonate'),
    ('Biology',      'Cell of Onion',       '2025-05-15', NULL),
    ('Higher Math',  'Coordinate geometry', '2025-05-19',
        'Vertices of triangle A (2,5), B (-1,1), C (2,1); Vertices of quadrilateral A (1,2), B (-4,3), C (1,-3), D (4,0)'),
    ('Physics',      'slide calipers',      '2025-05-19', NULL);

-- WILDCARDS ARE NOT CASE SENSITIVE
SELECT *  FROM PRACTICAL
WHERE SUBJECT LIKE '_I%';

-- WHICH SUBJECTS HAS HOW MANY PRACTICAL?
SELECT SUBJECT AS "SUBJECT",
COUNT(*) AS "NUMBER OF SUBJECTS"
FROM PRACTICAL
GROUP BY SUBJECT;

-- AGGRIGATE FUNCTIONS