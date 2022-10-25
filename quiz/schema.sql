DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS attempt;
DROP TABLE IF EXISTS question;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE attempt (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    time_taken TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    score INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user (id)
);

CREATE TABLE question (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    q TEXT NOT NULL,
    a TEXT NOT NULL,
    b TEXT NOT NULL,
    c TEXT,
    d TEXT,
    correct_answer VARCHAR(1)
);

INSERT INTO question (q, a, b, c, d, correct_answer)
VALUES ('Which of these games has Nick NOT competed in tournaments for?', 'Tekken 7', 'Super Smash Bros. Ultimate',
        'Rocket League', 'Valorant', 'c');

INSERT INTO question (q, a, b, c, d, correct_answer)
VALUES ('When did Nick learn to play chess?', '5', '7', '10', '13', 'a');

INSERT INTO question (q, a, b, c, d, correct_answer)
VALUES ('Which of these languages did Nick study during high school?', 'German', 'French', 'Latin', 'Greek', 'd');

INSERT INTO question (q, a, b, c, d, correct_answer)
VALUES ('Which degree is Nick going to college for?', 'Computer Science', 'Informatics', 'Nursing', 'Philosophy', 'a');

INSERT INTO question (q, a, b, c, d, correct_answer)
VALUES ('Which of the following is Nick''s favorite restaurant?', 'Picasso''s Pizza', 'Yokohama Ramen',
        'Martinelli''s Little Italy', 'McDonald''s', 'b');

INSERT INTO question (q, a, b, c, d, correct_answer)
VALUES ('How old was Nick when this website was made?', '20', '21', '22', '23', 'b');

INSERT INTO question (q, a, b, c, d, correct_answer)
VALUES ('How many siblings does Nick have?', '0', '1', '2', '3', 'b');

INSERT INTO question (q, a, b, c, d, correct_answer)
VALUES ('When did Nick start competing in video game tournaments?', '2013', '2016', '2018', '2020', 'b');

INSERT INTO question (q, a, b, c, d, correct_answer)
VALUES ('What is Nick''s favorite color?', 'Red', 'Blue', 'Purple', 'Pink', 'c');

INSERT INTO question (q, a, b, c, d, correct_answer)
VALUES ('Which instrument has Nick NOT played at some point?', 'Guitar', 'Flute', 'French Horn', 'Trombone', 'd');
