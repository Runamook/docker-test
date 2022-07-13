USE 'weather';


/*Table structure for table 'weather' */

CREATE TABLE weather.weather (
	id INT(11) auto_increment NOT NULL,
	dt TIMESTAMP NOT NULL,
	`data` json NOT NULL,
	CONSTRAINT NewTable_PK PRIMARY KEY (id)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_general_ci;

