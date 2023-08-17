-- show by genre
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
JOIN tv_show_genres ON tv_show_genres.show_id=tv_show_genres.genre_id ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
