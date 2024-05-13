## This is Just a Prototype of KV Manager Web App
### Check out the KV-Manager git hub repository here(https://github.com/Krishna-Noutiyal/KV-Manager.git) 

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
