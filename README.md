# No MFA Please
[Implementation](https://no-mfa-please.herokuapp.com/)

## The Idea
### What is MFA and Duo
[MFA (Multi-Factor Authorization)](https://en.wikipedia.org/wiki/Multi-factor_authentication), also known as 2FA, add a layer of security to normal username & password authorization system. It requires something you have (phone or token) on top of something you know (username and password) to log in. 

Duo is a company that lets other companies easily add MFA options to website accounts, server accounts, etc.


### What is this app
Basically, this is a Heroku app/website for generating new Duo MFA Passcodes and sending them to your email. It is for people who value convenience a little more than security (there's usually a tradeoff between security and convenience). 

NYU incorporated Duo MFA into all of their websites: their administrative website [Albert](http://albert.nyu.edu/) and their Google suite (Gmail, Drive, etc.) which holds a lot of personal information as well as non-essential websites like [NYU Classes](https://newclasses.nyu.edu/portal). 

This is welcome news for people who wish to secure their accounts, however, it is a shame that NYU forcefully implemented MFA on all of its users. MFA certainly is secure and apart from physical hacking (stealing phones and looking over the shoulder), efforts to hack MFA have been futile. However, there are times when we wish we didn't have MFA (losing the phone or when its battery is dead). As a backup, this website will become your extra passcode generating token.

### How it works / Usage
You can designate this app as a "token" that can generates passcodes. This app lets users replace the security condition -- what they have, a phone -- with what they know, another email address and a password.


- Get QR URL
  1. Log in to [start.nyu.edu](https://start.nyu.edu) 
  1. Click 'NYU Multi-Factor Authentication Registration & Update'
  1. Click 'Add a New Device' in MFA panel
  1. Log in with MFA
  1. Add a 'Tablet (iPad, Nexus 7, etc.)', doesn't matter whether you choose iOS or Android
  1. Click 'I have Duo Mobile installed'. A QR code will show up.
  1. Copy the image address (usually in the right click context menu or long press menu
- Register (`\register`) using the QR URL, a non-nyu email, and a password
- Send new passcodes to your registered email (`\passcode`)

### The Risks & why this app is still pretty secure
The chance of your account getting hacked is higher using this app compared to using MFA without this app, since it provides another way for you (and hackers) to access your account.

Level of security (increasing order):

1. Using only username & password
1. MFA + this app
1. MFA without this app

However, this app is still pretty secure because:
- We send a passcode to your email instead of giving it to you right away: it is more convenient if you want to genereate and save multiple passcodes at once and also this adds another layer of security: in case somehone holds the account information for this app, they still need to know the password for your email.
- We use a password: mainly so that other people can't update or remove the token, but also because in case someone holds the account information for your email, they still need to know the password for this app.

### FAQ
1. Why does the website design look so shit? Because I love minimalism. I welcome any help with CSS.
1. Are you going to add any more functions? Hopefully, but I'm busy slaving away at a startup.
1. How long did this take you to make? Way more than it should have. Blame my inner procrastinator.
1. Is this legal? Well, Duo's website didn't say anything about it... so yeah?


## The Code
### Install stuff
dependencies:

```sh
$ pipenv install
```

Install Postgres if you want to test it locally.

### Run Locally
```sh
$ heroku local
```

### Test

### Deploy on Heroku
```sh
$ git push
```

### Try it out
[Implementation](https://no-mfa-please.herokuapp.com/)
