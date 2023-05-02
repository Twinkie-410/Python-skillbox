import sqlite3

actors = """DROP TABLE IF EXISTS `actors`;
            CREATE TABLE `actors`
            (
                act_id INTEGER PRIMARY KEY AUTOINCREMENT,
                act_first_name VARCHAR(50) NOT NULL,
                act_last_name VARCHAR(50) NOT NULL,
                act_gender VARCHAR(1) NOT NULL
            )"""

movie = """DROP TABLE IF EXISTS `movie`;
           CREATE TABLE `movie`
           (
                mov_id INTEGER PRIMARY KEY AUTOINCREMENT,
                mov_title VARCHAR(50) NOT NULL
           )"""

director = """DROP TABLE IF EXISTS `director`;
              CREATE TABLE `director`
              (
                dir_id INTEGER PRIMARY KEY AUTOINCREMENT,
                dir_first_name VARCHAR(50) NOT NULL,
                dir_last_name VARCHAR(50) NOT NULL
              )"""

#   movie_cast <-> actors и movie_cast <-> movie - связь один ко многим
#   (actors <-> movie - многие ко многим, а movie_cast - промежуточная)
movie_cast = """DROP TABLE IF EXISTS `movie_cast`;
                CREATE TABLE `movie_cast`
                (
                    act_id INTEGER,
                    mov_id INTEGER,
                    role VARCHAR(50) NOT NULL,
                    FOREIGN KEY (act_id) REFERENCES actors(act_id) ON DELETE SET NULL,
                    FOREIGN KEY (mov_id) REFERENCES movie(mov_id) ON DELETE SET NULL
                )"""

#   movie_direction <-> director и movie_direction <-> movie - связь один ко многим
#   (director <-> movie - многие ко многим, а movie_direction - промежуточная)
movie_direction = """DROP TABLE IF EXISTS `movie_direction`;
                     CREATE TABLE `movie_direction`
                     (
                        dir_id INTEGER,
                        mov_id INTEGER,
                        FOREIGN KEY(dir_id) REFERENCES director(dir_id) ON DELETE SET NULL,
                        FOREIGN KEY(mov_id) REFERENCES movie(mov_id) ON DELETE SET NULL
                     )"""

#   movie_direction <-> movie - связь один ко многим
oscar_awarded = """DROP TABLE IF EXISTS `oscar_awarded`;
                   CREATE TABLE `oscar_awarded`
                   (
                        mov_id INTEGER,
                        award_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        FOREIGN KEY(mov_id) REFERENCES movie(mov_id) ON DELETE CASCADE
                   )"""

if __name__ == '__main__':
    with sqlite3.connect("task_1.db") as conn:
        cursor = conn.cursor()
        cursor.executescript("PRAGMA foreign_keys = ON")
        cursor.executescript(actors)
        cursor.executescript(movie)
        cursor.executescript(director)
        cursor.executescript(movie_cast)
        cursor.executescript(movie_direction)
        cursor.executescript(oscar_awarded)
