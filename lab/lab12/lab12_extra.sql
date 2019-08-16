.read lab12.sql

-- Q5
CREATE TABLE fa18favpets AS
  SELECT pet, count(*)
  FROM students
  GROUP BY pet
  ORDER BY 2 desc
  LIMIT 10;


CREATE TABLE fa18dog AS
  SELECT pet, count(*)
  FROM students
  WHERE pet = 'dog'
  GROUP BY 1;


CREATE TABLE fa18alldogs AS
  SELECT 'dog', count(*)
  FROM students
  WHERE pet LIKE '%dog%';

CREATE TABLE obedienceimages AS
  SELECT seven, denero, count(*)
  FROM obedience
  WHERE seven = '7'
  GROUP BY 1, 2;


-- Q6
CREATE TABLE smallest_int_count AS
  SELECT smallest, count(*)
  FROM students
  GROUP BY 1
  ORDER BY 1
