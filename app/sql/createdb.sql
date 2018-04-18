/*
* @Author: Simon Myunggun Seo
* @Date:   2018-04-17 13:55:15
* @Last Modified by:   Simon Seo
* @Last Modified time: 2018-04-17 14:29:57
*/

/* 
id email password hotp
to delete, update, or generate passcode, require password

Suggestion: use last_login to prevent spamming
*/

DROP TABLE IF EXISTS accounts
CREATE TABLE accounts (
 user_id serial PRIMARY KEY,
 -- username VARCHAR (50) UNIQUE NOT NULL,
 password VARCHAR (50) NOT NULL,
 email VARCHAR (355) UNIQUE NOT NULL,
 -- created_on TIMESTAMP NOT NULL,
 -- last_login TIMESTAMP
 hotp_secret CHAR (32) NOT NULL -- looks like a85adc3516351791c05ef40bde772c24
);
