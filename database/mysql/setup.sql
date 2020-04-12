CREATE TABLE pastes (
	id INT AUTO_INCREMENT PRIMARY KEY,
	updated_at TIMESTAMP NOT NULL DEFAULT NOW() ON UPDATE NOW(),
	pid VARCHAR(100),
	text LONGTEXT,
	emails TEXT,
	hashes TEXT,
	num_emails VARCHAR(255),
	num_hashes VARCHAR(255),
	type VARCHAR(100),
	db_keywords VARCHAR(255),
	url VARCHAR(150)
);
