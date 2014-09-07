Kobo Wireless Sync
==================

Hacky Little Python Script I put together while watching a movie one night. When Run, it uploads all epub files in a directory to my Kobo, then refreshes the database. No error handling, no safety, no nothing :)

Put it up here for fun, maybe I'll make it a bit more robust at some point... Auto detecting the ip would be nice...

Put the update.sh file in the root of the drive(ftp root, not user root), you will need to fix permissions, so telnet in and go
```shell
chmod 777 update.sh
```
You don't need to be that permissive probably, I don't use linux much, so I don't know, but if you are paranoid about hackers hacking into your ereader and updating your database(the horror), you can use a better permissions number. 
 You need to root your kobo to use this, You do not need Python on your kobo, just root access

Python I use is 2.7.8, uses preinstalled libraries, I think, I don't use python much, so I can't be sure.