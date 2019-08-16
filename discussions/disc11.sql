/* Q 2.1 */
SELECT name
FROM records
WHERE supervisor = 'Oliver Warbucks';

/* Q 2.2 */
SELECT *
FROM records
WHERE supervisor = name;

/* Q 2.3 */
SELECT name
FROM records
WHERE salary > 50000
ORDER BY 1;

/* Q 3.1 */
SELECT b.day, b.time
FROM meetings b
JOIN records a
ON a.division = b.division
WHERE a.supervisor = 'Oliver Warbucks';

/* Q 3.2 */
SELECT a.name
FROM records a
JOIN records b
ON a.supervisor = b.name
WHERE a.division != b.division;

/* Q 3.3 */
SELECT a.name, b.name
FROM (SELECT r.name, r.division, m.time FROM records r JOIN meetings m ON r.division = m.division) AS a
JOIN (SELECT r.name, r.division, m.time FROM records r JOIN meetings m ON r.division = m.division) AS b
ON a.division = b.division
WHERE a.name < b.name AND a.time = b.time;

/* Q 4.1 */
SELECT supervisor, sum(salary) as sum_salary
FROM records
GROUP BY 1;

/* Q 4.2 */
SELECT m.day, count(*)
FROM meetings m
JOIN records r
ON m.division = r.division
GROUP BY 1
HAVING count(*) < 5

/* Q 4.3 */
SELECT a.division
FROM records a
JOIN records b
ON a.supervisor = b.name
GROUP BY a.division
HAVING count(*) > 1 AND max(a.salary) < 100000 AND max(b.salary) < 100000
