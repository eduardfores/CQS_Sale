CREATE TABLE IF NOT EXISTS Products(
  id integer NOT NULL,
  name text NOT NULL,
  initialPrice float NOT NULL,
  image text,
  majorBidder text,
  price float NOT NULL DEFAULT 0,
  PRIMARY KEY (id));

INSERT INTO Products(name, initialPrice, image) VALUES ("MACBOOK PRO", 10, "img/img-mac-pro.jpg")
INSERT INTO Products(name, initialPrice, image) VALUES ("STEAM CARD", 1, "img/steam.jpg")