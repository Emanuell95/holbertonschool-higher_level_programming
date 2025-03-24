-- Listing all genres in the database hbtn_0d_tvshows
-- Results are ordered by ascending genres.id
SELECT s.`title`, g.`genre_id`
FROM `tv_shows` AS s
INNER JOIN `tv_show_genres` AS g
ON s.`id` = g.`show_id`
ORDER BY s.`title`, g.`genre_id`;