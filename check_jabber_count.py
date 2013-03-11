#!/usr/bin/python
#
# returns number of users logged into openfire
# requires the onlineUsers.jar plugin be installed

import pycurl
import cStringIO

OK = 0
WARNING = 1
CRITICAL = 2
UNKNOWN = 3

buf = cStringIO.StringIO()
 
c=pycurl.Curl()
c.setopt(c.URL, 'http://jabber.it.wm.edu:9090/plugins/onlineusers')
c.setopt(c.WRITEFUNCTION, buf.write)
c.setopt(c.CONNECTTIMEOUT, 5)
c.setopt(c.TIMEOUT, 8)
try:
    c.perform()
except:
    print "CRITICAL - Connection error to XMPP Server"
    raise SystemExit(CRITICAL)

count=buf.getvalue()
count=count.rstrip()
print "JabberClients OK  - %s | jabberclients=%s" % (count, count)
buf.close()
