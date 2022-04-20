CREATE TABLE IF NOT EXISTS Products(
  id integer NOT NULL,
  name text NOT NULL,
  initialPrice float NOT NULL,
  majorBidder text,
  price float NOT NULL DEFAULT 0,
  PRIMARY KEY (id));