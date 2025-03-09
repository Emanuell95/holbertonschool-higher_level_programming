-- This query should return the genres of the TV show Dexter in alphabetical order.
-- The TV show Dexter has an id of 10 in the table tv_shows.
SELECT tv_genres.name
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;