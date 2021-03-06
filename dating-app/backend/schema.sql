DROP TABLE IF EXISTS user;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  first_name TEXT UNIQUE NOT NULL,
  last_name TEXT UNIQUE NOT NULL,
  pronouns TEXT NOT NULL,
  preferences TEXT NOT NULL,
  dob DATE NOT NULL, 
  token TEXT UNIQUE NOT NULL, 
  password TEXT NOT NULL
);