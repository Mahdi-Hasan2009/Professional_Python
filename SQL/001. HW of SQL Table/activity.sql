DROP TABLE IF EXISTS practicle;

CREATE TABLE practicle (
    subject VARCHAR(50),
    name VARCHAR(50),
    Date TEXT,
    value TEXT
);

INSERT INTO practicle (subject, name, Date, value) VALUES
    ('Chemistry',    'crystal',             '2025-05-14', '100mL water'),
    ('Biology',      'Microscope',          '2025-04-24', NULL),
    ('Chemistry',    'Metallic carbon',     '2025-04-30', 'Sodium Carbonate'),
    ('Biology',      'Cell of Onion',       '2025-05-15', NULL),
    ('Higher Math',  'Coordinate geometry', '2025-05-19',
        'Vertices of triangle A (2,5), B (-1,1), C (2,1); Vertices of quadrilateral A (1,2), B (-4,3), C (1,-3), D (4,0)'),
    ('Physics',      'slide calipers',      '2025-05-19', NULL);

SELECT * FROM practicle;

SELECT * FROM practicle
WHERE subject = 'Chemistry';

SELECT * FROM practicle
WHERE subject = 'Physics';

SELECT * FROM practicle
WHERE subject = 'Biology';

SELECT subject, name, value FROM practicle
WHERE subject = 'Higher Math';