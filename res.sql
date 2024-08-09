CREATE DATABASE db;
USE db;


CREATE TABLE rawmaterial (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  price FLOAT NOT NULL,
  amount FLOAT NOT NULL
);

INSERT INTO rawmaterial VALUES (1, 'rice', 0.01, 10000);
INSERT INTO rawmaterial VALUES (2, 'salt', 0.005, 10000);
INSERT INTO rawmaterial VALUES (3, 'dal', 0.02, 10000);
INSERT INTO rawmaterial VALUES (4, 'oil', 0.04, 10000);
INSERT INTO rawmaterial VALUES (5, 'potatoes', 0.09, 10000);
INSERT INTO rawmaterial VALUES (6, 'sugar', 0.2, 10000);
INSERT INTO rawmaterial VALUES (7, 'tea_powder', 0.05, 10000);
INSERT INTO rawmaterial VALUES (8, 'coffee_powder', 0.05, 10000);
INSERT INTO rawmaterial VALUES (9, 'ghee', 0.02, 10000);
INSERT INTO rawmaterial VALUES (10, 'suji', 0.015, 10000);

CREATE TABLE items (
id INTEGER PRIMARY KEY,
name FLOAT NOT NULL,
price FLOAT NOT NULL,
recipe TEXT NOT NULL
);

INSERT INTO items VALUES (1,'idli',30, 'rice 250 oil 30 salt 10 dal 500');
INSERT INTO items VALUES (2,'dosa',50, 'rice 300 oil 50 salt 20 dal 300');
INSERT INTO items VALUES (3,'vada',20, 'rice 250 oil 10 salt 5 dal 60');
INSERT INTO items VALUES (4,'kesari_bath',50, 'ghee 50 sugar 100 suji 80');
INSERT INTO items VALUES (5,'tea',10, 'tea_powder 200 sugar 25 milk 100');
INSERT INTO items VALUES (6,'coffee',10, 'coffee_powder 250 sugar 30 milk 150');
INSERT INTO items VALUES (7,'palya',90, 'rice 300 potatoes 100 salt 20');
