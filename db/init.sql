CREATE DATABASE token_pooling;
use token_pooling;

CREATE TABLE tokens (
    id int NOT NULL PRIMARY KEY,
    token_name varchar(255) NOT NULL,
    used_count int
);

INSERT INTO tokens
  (id, token_name, used_count)
VALUES
  (1,'A', 0),
  (3,'B', 0),
  (4,'C', 0),
  (5,'D', 0),
  (6,'E', 0),
  (7,'F', 0),
  (8,'G', 0),
  (9,'H', 0);