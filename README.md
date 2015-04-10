Django on OpenShift
===================

This git repository helps you get up and running quickly with a Django
installation on OpenShift.  

Features
--------------------
- Static files working
- Multiple settings (development, openshift ...)


Running on OpenShift
--------------------

- Create an account at https://www.openshift.com
- (First time) Add your public key into your openshift account
- Create a new django application (using the web or the RHC client tools)
- Set an application name
- Set the source code to ```https://github.com/huogerac/django16-openshift-template.git```
	instead of ```https://github.com/openshift/django-example.git```
- Set python-2.7
- You should access it at ```http://yourapplication-$yournamespace.rhcloud.com```


Pushing your code to another Git repository
-------------------------------------------
Use the Git command:

    git remote add myalias git://github.com/myaccount/myproject.git
    git push myalias master


TODO
----
- Test the media files
- Add database support (and maybe south for Django 1.6)
- Add bower to get static files
- Find a way to rename the ```myproject``` to the correct project name
- Add support for Django 1.7
