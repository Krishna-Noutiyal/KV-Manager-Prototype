Create News table : 

CREATE TABLE news (
  Sr int NOT NULL,
  Class int DEFAULT NULL,
  Teacher varchar(45) NOT NULL,
  Heading varchar(20) NOT NULL,
  Short_Cnt varchar(150) NOT NULL,
  Cnt mediumtext NOT NULL,
  Img mediumtext,
  PRIMARY KEY (Sr)
)