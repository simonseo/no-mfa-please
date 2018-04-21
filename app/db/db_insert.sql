/*
* @Author: Simon Myunggun Seo
* @Date:   2018-04-20 14:15:23
* @Last Modified by:   Simon Seo
* @Last Modified time: 2018-04-21 01:54:20
*/

-- SELECT * FROM backup_mfa_accounts;

INSERT INTO backup_mfa_accounts (email, password, hotp_secret, counter) VALUES (%s, %s, %s, %s);
    -- ('simon.seo@nyu.edu', 'asdf', 'a85adc3516351791c05ef40bde772c24'),
    -- ('simon.seo2@nyu.edu', 'asdf', 'a85adc3516351791c05ef40bde772c24'),
    -- ('simon.seo3@nyu.edu', 'asdf', 'a85adc3516351791c05ef40bde772c24'),
    -- ('simon.seo4@nyu.edu', 'asdf', 'a85adc3516351791c05ef40bde772c24');

-- SELECT * FROM backup_mfa_accounts;