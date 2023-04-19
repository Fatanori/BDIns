SELECT title, year_of_release FROM album
WHERE year_of_release = 2018;


SELECT title, duration
FROM track
WHERE duration = (SELECT MAX(duration) FROM track);


SELECT title, duration FROM track
ORDER BY duration DESC
LIMIT 1;


SELECT title FROM track
WHERE duration >= 210;


SELECT title FROM collection
WHERE year_of_release BETWEEN 2018 AND 2020;


SELECT name_nickname FROM performer
WHERE name_nickname NOT LIKE '% %';


SELECT title FROM track
WHERE title ILIKE '%my%' OR title ILIKE '%мой%'
