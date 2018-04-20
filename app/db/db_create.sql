/*
* @Author: Simon Myunggun Seo
* @Date:   2018-04-17 13:55:15
* @Last Modified by:   Simon Seo
* @Last Modified time: 2018-04-21 02:53:13
*/

/* 
id email password hotp counter
to make, delete, update, or generate_passcode, require password

Suggestion: use last_login to prevent spamming
*/

DROP TABLE IF EXISTS accounts;
CREATE TABLE accounts (
 user_id SERIAL PRIMARY KEY,
 -- username VARCHAR (50) UNIQUE NOT NULL,
 email VARCHAR (355) UNIQUE NOT NULL,
 password VARCHAR (50) NOT NULL,
 -- created_on TIMESTAMP NOT NULL,
 -- last_login TIMESTAMP
 hotp_secret CHAR (32) NOT NULL, -- looks like a85adc3516351791c05ef40bde772c24
 counter INTEGER DEFAULT 0
);
