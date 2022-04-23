CREATE TABLE IF NOT EXISTS Products(
  id integer NOT NULL,
  name text NOT NULL,
  price float NOT NULL,
  image text,
  majorBidder text,
  PRIMARY KEY (id));

INSERT INTO Products(name, price, image) VALUES ("MACBOOK PRO", 10, "img/img-mac-pro.jpg");
INSERT INTO Products(name, price, image) VALUES ("STEAM CARD", 1, "img/steam.jpg");

SELECT * FROM Products; 