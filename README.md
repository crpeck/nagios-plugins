Nagios Plugins
These were written with Shinken in mind, but, should work with any Nagios engine, with
minor tweaking.

check_jabber_count.py - connects to openfire via http and grabs a count of jabber clients, requires onlineUsers.jar
onlineUsers.jar - openfire plugin for above

notify_by_twitter.py - sends notifications to twitter for Nagios
notify_by_twitter.ini - config file, containts AUTH info 
notify_by_twitter-test - bash script to test notify_by_twitter.py
