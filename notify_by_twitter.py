#!/usr/bin/python -tt
#
# notify by twitter - crpeck@wm.edu
# gplv2+
#
# ref: http://pythonhosted.org/tweepy/html/auth_tutorial.html

## Twitter notification

#  Add to your Nagios commands.cfg file
#define command{
#    command_name    notify-host-by-twitter
#    command_line    $PLUGINSDIR$/notify_by_twitter.py -a $PLUGINSDIR$/notify_by_twitter.ini -m "$TIME$ Host '$HOSTALIAS$' is $HOSTSTATE$ - Info : $HOSTOUTPUT$"
#}
#
#define command{
#    command_name    notify-service-by-twitter
#    command_line    $PLUGINSDIR$/notify_by_twitter.py -a $PLUGINSDIR$/notify_by_twitter.ini -m "$TIME$ $NOTIFICATIONTYPE$ $HOSTNAME$ $SERVICED ESC$ $SERVICESTATE$ $SERVICEOUTPUT$"
#}

# config file reference via -a
# needs a config file to get twitter keys info format is:
#[twitter_account]
#consumer_key = 'XXXXXXXXXXXXXXX'
#consumer_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
#access_key = 'NNNNNNNNN-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
#access_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

from optparse import OptionParser
import ConfigParser
import sys
import os
import tweepy

parser = OptionParser()
parser.add_option("-a", dest="authfile", default=None, help="file to retrieve Twitter OATH information from")
parser.add_option("-m", dest="message", default=None, help="message to tweet")
opts, args = parser.parse_args()

conf = ConfigParser.ConfigParser()
if not opts.authfile or not os.path.exists(opts.authfile):
   print "no config/auth file specified, can't continue"
   sys.exit(1)

if not opts.message:
   print "no message to tweet specified, can't continue"
   sys.exit(1)

conf.read(opts.authfile)
if not conf.has_section('twitter_account') or not conf.has_option('twitter_account', 'consumer_key'):
    print "cannot find: config section 'twitter_account'  or consumer_key"
    sys.exit(1)

# truncate message to 140 if its too long
message = (opts.message[:138] + '..') if len(opts.message) > 140 else opts.message

# grab the auth info from the config file
CONSUMER_KEY=conf.get('twitter_account', 'consumer_key')
CONSUMER_SECRET=conf.get('twitter_account', 'consumer_secret')
ACCESS_KEY=conf.get('twitter_account', 'access_key')
ACCESS_SECRET=conf.get('twitter_account', 'access_secret')

# set it up and fire out the tweet
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
api.update_status(message)
