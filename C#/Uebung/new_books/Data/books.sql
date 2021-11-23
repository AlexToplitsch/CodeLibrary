BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Company_addresses" (
	"ID"	INTEGER NOT NULL,
	"Street"	TEXT,
	"StrtNr"	TEXT,
	"City"	TEXT,
	"Postal_code"	TEXT,
	CONSTRAINT "PK_Company_addresses" PRIMARY KEY("ID" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Costumers" (
	"ID"	INTEGER NOT NULL,
	"First_name"	TEXT,
	"Last_name"	TEXT,
	"Email"	TEXT,
	"Company_addressID"	INTEGER,
	CONSTRAINT "FK_Costumers_Company_addresses_Company_addressID" FOREIGN KEY("Company_addressID") REFERENCES "Company_addresses"("ID") ON DELETE RESTRICT,
	CONSTRAINT "PK_Costumers" PRIMARY KEY("ID" AUTOINCREMENT)
);
INSERT INTO "Company_addresses" VALUES (1,'Shelley','1675','Greece',NULL);
INSERT INTO "Company_addresses" VALUES (2,'Jackson','4','Albania',NULL);
INSERT INTO "Company_addresses" VALUES (3,'Lerdahl','6','Greece',NULL);
INSERT INTO "Company_addresses" VALUES (4,'New Castle','35720','Greece',NULL);
INSERT INTO "Company_addresses" VALUES (5,'Lake View','90813','Albania',NULL);
INSERT INTO "Company_addresses" VALUES (6,'Wayridge','75','Albania',NULL);
INSERT INTO "Company_addresses" VALUES (7,'Utah','406','Albania',NULL);
INSERT INTO "Company_addresses" VALUES (8,'Kingsford','568','Albania',NULL);
INSERT INTO "Company_addresses" VALUES (9,'Hanson','69','Greece',NULL);
INSERT INTO "Company_addresses" VALUES (10,'Lien','6','Greece',NULL);
INSERT INTO "Company_addresses" VALUES (11,'Grasskamp','37382','Greece',NULL);
INSERT INTO "Company_addresses" VALUES (12,'Eastlawn','3','Greece',NULL);
INSERT INTO "Company_addresses" VALUES (13,'Scofield','95256','Greece',NULL);
INSERT INTO "Company_addresses" VALUES (14,'Lillian','49','Greece',NULL);
INSERT INTO "Company_addresses" VALUES (15,'Duke','690','Greece',NULL);
INSERT INTO "Company_addresses" VALUES (16,'Heath','36','Greece',NULL);
INSERT INTO "Company_addresses" VALUES (17,'Macpherson','230','Greece',NULL);
INSERT INTO "Company_addresses" VALUES (18,'Kim','64','Greece',NULL);
INSERT INTO "Company_addresses" VALUES (19,'Melody','1','Greece',NULL);
INSERT INTO "Company_addresses" VALUES (20,'Jenifer','6','Albania',NULL);
INSERT INTO "Company_addresses" VALUES (21,'Stang','43969','Greece',NULL);
INSERT INTO "Company_addresses" VALUES (22,'Amoth','82800','Albania',NULL);
INSERT INTO "Company_addresses" VALUES (23,'Rigney','77','Greece',NULL);
INSERT INTO "Company_addresses" VALUES (24,'Oxford','4048','Greece',NULL);
INSERT INTO "Company_addresses" VALUES (25,'Katie','70','Greece',NULL);
INSERT INTO "Company_addresses" VALUES (26,'Shelley','1675','Greece',NULL);
INSERT INTO "Company_addresses" VALUES (27,'Rigney','77','Greece',NULL);
INSERT INTO "Company_addresses" VALUES (28,'Amoth','82800','Albania',NULL);
INSERT INTO "Company_addresses" VALUES (29,'Stang','43969','Greece',NULL);
INSERT INTO "Company_addresses" VALUES (30,'Jenifer','6','Albania',NULL);
INSERT INTO "Company_addresses" VALUES (31,'Melody','1','Greece',NULL);
INSERT INTO "Company_addresses" VALUES (32,'Kim','64','Greece',NULL);
INSERT INTO "Company_addresses" VALUES (33,'Macpherson','230','Greece',NULL);
INSERT INTO "Company_addresses" VALUES (34,'Heath','36','Greece',NULL);
INSERT INTO "Company_addresses" VALUES (35,'Duke','690','Greece',NULL);
INSERT INTO "Company_addresses" VALUES (36,'Lillian','49','Greece',NULL);
INSERT INTO "Company_addresses" VALUES (37,'Oxford','4048','Greece',NULL);
INSERT INTO "Company_addresses" VALUES (38,'Scofield','95256','Greece',NULL);
INSERT INTO "Company_addresses" VALUES (39,'Grasskamp','37382','Greece',NULL);
INSERT INTO "Company_addresses" VALUES (40,'Lien','6','Greece',NULL);
INSERT INTO "Company_addresses" VALUES (41,'Hanson','69','Greece',NULL);
INSERT INTO "Company_addresses" VALUES (42,'Kingsford','568','Albania',NULL);
INSERT INTO "Company_addresses" VALUES (43,'Utah','406','Albania',NULL);
INSERT INTO "Company_addresses" VALUES (44,'Wayridge','75','Albania',NULL);
INSERT INTO "Company_addresses" VALUES (45,'Lake View','90813','Albania',NULL);
INSERT INTO "Company_addresses" VALUES (46,'New Castle','35720','Greece',NULL);
INSERT INTO "Company_addresses" VALUES (47,'Lerdahl','6','Greece',NULL);
INSERT INTO "Company_addresses" VALUES (48,'Jackson','4','Albania',NULL);
INSERT INTO "Company_addresses" VALUES (49,'Eastlawn','3','Greece',NULL);
INSERT INTO "Company_addresses" VALUES (50,'Katie','70','Greece',NULL);
INSERT INTO "Costumers" VALUES (1,'Anet','Dyshart','adyshart0@addthis.com',1);
INSERT INTO "Costumers" VALUES (2,'Sallee','Hutton','shuttonm@zdnet.com',2);
INSERT INTO "Costumers" VALUES (3,'Sarette','Leipnik','sleipnikl@eepurl.com',3);
INSERT INTO "Costumers" VALUES (4,'Filide','O''Hanley','fohanleyk@disqus.com',4);
INSERT INTO "Costumers" VALUES (5,'Lizzy','Muge','lmugej@nymag.com',5);
INSERT INTO "Costumers" VALUES (6,'Eal','Brun','ebruni@goo.ne.jp',6);
INSERT INTO "Costumers" VALUES (7,'Glenda','Ponten','gpontenh@soundcloud.com',7);
INSERT INTO "Costumers" VALUES (8,'Zorina','Elliss','zellissg@webeden.co.uk',8);
INSERT INTO "Costumers" VALUES (9,'Annnora','Chesser','achesserf@un.org',9);
INSERT INTO "Costumers" VALUES (10,'Nataniel','Cesaric','ncesarice@japanpost.jp',10);
INSERT INTO "Costumers" VALUES (11,'Gregory','Orton','gortond@uol.com.br',11);
INSERT INTO "Costumers" VALUES (12,'Tracie','Moodie','tmoodien@auda.org.au',12);
INSERT INTO "Costumers" VALUES (13,'Barbey','Celez','bcelezc@kickstarter.com',13);
INSERT INTO "Costumers" VALUES (14,'Danila','Germain','dgermaina@theglobeandmail.com',14);
INSERT INTO "Costumers" VALUES (15,'Marion','Stoves','mstoves9@ustream.tv',15);
INSERT INTO "Costumers" VALUES (16,'Wynn','Troak','wtroak8@opera.com',16);
INSERT INTO "Costumers" VALUES (17,'Alvy','Trivett','atrivett7@mit.edu',17);
INSERT INTO "Costumers" VALUES (18,'Lissa','Strachan','lstrachan6@mediafire.com',18);
INSERT INTO "Costumers" VALUES (19,'Evan','Lau','elau5@chicagotribune.com',19);
INSERT INTO "Costumers" VALUES (20,'Dana','Hampstead','dhampstead4@sun.com',20);
INSERT INTO "Costumers" VALUES (21,'Celesta','Checcucci','ccheccucci3@phoca.cz',21);
INSERT INTO "Costumers" VALUES (22,'Haslett','Raitie','hraitie2@imgur.com',22);
INSERT INTO "Costumers" VALUES (23,'Ed','Chettoe','echettoe1@vinaora.com',23);
INSERT INTO "Costumers" VALUES (24,'Bettina','Castro','bcastrob@youtu.be',24);
INSERT INTO "Costumers" VALUES (25,'Rogers','Wyrall','rwyrallo@pen.io',25);
INSERT INTO "Costumers" VALUES (26,'Anet','Dyshart','adyshart0@addthis.com',26);
INSERT INTO "Costumers" VALUES (27,'Ed','Chettoe','echettoe1@vinaora.com',27);
INSERT INTO "Costumers" VALUES (28,'Haslett','Raitie','hraitie2@imgur.com',28);
INSERT INTO "Costumers" VALUES (29,'Celesta','Checcucci','ccheccucci3@phoca.cz',29);
INSERT INTO "Costumers" VALUES (30,'Dana','Hampstead','dhampstead4@sun.com',30);
INSERT INTO "Costumers" VALUES (31,'Evan','Lau','elau5@chicagotribune.com',31);
INSERT INTO "Costumers" VALUES (32,'Lissa','Strachan','lstrachan6@mediafire.com',32);
INSERT INTO "Costumers" VALUES (33,'Alvy','Trivett','atrivett7@mit.edu',33);
INSERT INTO "Costumers" VALUES (34,'Wynn','Troak','wtroak8@opera.com',34);
INSERT INTO "Costumers" VALUES (35,'Marion','Stoves','mstoves9@ustream.tv',35);
INSERT INTO "Costumers" VALUES (36,'Danila','Germain','dgermaina@theglobeandmail.com',36);
INSERT INTO "Costumers" VALUES (37,'Bettina','Castro','bcastrob@youtu.be',37);
INSERT INTO "Costumers" VALUES (38,'Barbey','Celez','bcelezc@kickstarter.com',38);
INSERT INTO "Costumers" VALUES (39,'Gregory','Orton','gortond@uol.com.br',39);
INSERT INTO "Costumers" VALUES (40,'Nataniel','Cesaric','ncesarice@japanpost.jp',40);
INSERT INTO "Costumers" VALUES (41,'Annnora','Chesser','achesserf@un.org',41);
INSERT INTO "Costumers" VALUES (42,'Zorina','Elliss','zellissg@webeden.co.uk',42);
INSERT INTO "Costumers" VALUES (43,'Glenda','Ponten','gpontenh@soundcloud.com',43);
INSERT INTO "Costumers" VALUES (44,'Eal','Brun','ebruni@goo.ne.jp',44);
INSERT INTO "Costumers" VALUES (45,'Lizzy','Muge','lmugej@nymag.com',45);
INSERT INTO "Costumers" VALUES (46,'Filide','O''Hanley','fohanleyk@disqus.com',46);
INSERT INTO "Costumers" VALUES (47,'Sarette','Leipnik','sleipnikl@eepurl.com',47);
INSERT INTO "Costumers" VALUES (48,'Sallee','Hutton','shuttonm@zdnet.com',48);
INSERT INTO "Costumers" VALUES (49,'Tracie','Moodie','tmoodien@auda.org.au',49);
INSERT INTO "Costumers" VALUES (50,'Rogers','Wyrall','rwyrallo@pen.io',50);
CREATE INDEX IF NOT EXISTS "IX_Costumers_Company_addressID" ON "Costumers" (
	"Company_addressID"
);
COMMIT;
