CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT,
    admin INTEGER,
    fafourite_id INTEGER REFERENCES fafourites
);

CREATE TABLE parkinglot (
    id INTEGER PRIMARY KEY,
    owner_id INTEGER REFERENCES users,
    reserved INTEGER,
    description TEXT,
    price INTEGER,
    comments_id INTEGER REFERENCES comments,
    location_id INTEGER REFERENCES location,
    stars_id INTEGER REFERENCES stars
);

CREATE TABLE location(
    id INTEGER PRIMARY KEY,
    parkinglot_id INTEGER REFERENCES parkinglot,
    city TEXT
);

CREATE TABLE comments(
    id INTEGER PRIMARY KEY,
    parkinglot_id INTEGER REFERENCES parkinglot,
    user_id INTEGER REFERENCES users,
    comment_text TEXT
);

CREATE TABLE fafourites(
    id INTEGER PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    parkinglot_id INTEGER REFERENCES parkinglot
);

CREATE TABLE stars(
    id INTEGER PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    parkinglot_id INTEGER REFERENCES parkinglot,
    star_count INTEGER,
    star_sum INTEGER
);
