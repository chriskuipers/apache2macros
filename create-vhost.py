#!/usr/bin/python

import sys, getopt, time

debug = True

def main(argv):
    domain = ''
    folder = ''
    helpmessage = 'test.py -d <domain> -f <relative-path>'
    try:
        opts, args = getopt.getopt(argv, "hd:f:", ["domain=", "folder="])
    except getopt.GetoptError:
        print helpmessage
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print helpmessage
            sys.exit()
        elif opt in ("-d", "--domain"):
            domain = arg
        elif opt in ("-f", "--folder"):
            folder = arg
    if debug:
        print '# Debug mode is turned on, the variables used:'
        print '#Domain: "%s"' %domain
        print '#Folder: "/var/www/%s"' % folder
        print '# Note that the folder should be relative to the /var/www location'
        print '# This file is generated on %s' %time.mktime(time.gmtime())
        print '\n\n'
    print createConfig(domain,folder)

def createConfig(domain,folder):
    config = """
<VirtualHost *:80>
	# The ServerName directive sets the request scheme, hostname and port that
	# the server uses to identify itself. This is used when creating
	# redirection URLs. In the context of virtual hosts, the ServerName
	# specifies what hostname must appear in the request's Host: header to
	# match this virtual host. For the default virtual host (this file) this
	# value is not decisive as it is used as a last resort host regardless.
	# However, you must set it for any further virtual host explicitly.
	#ServerName www.example.com
	ServerName www."""+domain+"""
	ServerAlias """+domain+"""

	ServerAdmin chris@chriskuipers.com
	DocumentRoot /var/www/"""+folder+"""

	# Available loglevels: trace8, ..., trace1, debug, info, notice, warn,
	# error, crit, alert, emerg.
	# It is also possible to configure the loglevel for particular
	# modules, e.g.
	#LogLevel info ssl:warn

	ErrorLog ${APACHE_LOG_DIR}/error.log
	CustomLog ${APACHE_LOG_DIR}/access.log combined

	# For most configuration files from conf-available/, which are
	# enabled or disabled at a global level, it is possible to
	# include a line for only one particular virtual host. For example the
	# following line enables the CGI configuration for this host only
	# after it has been globally disabled with "a2disconf".
	#Include conf-available/serve-cgi-bin.conf
#RewriteEngine on
#RewriteCond %{SERVER_NAME} =www."""+domain+""" [OR]
#RewriteCond %{SERVER_NAME} ="""+domain+"""
#RewriteRule ^ https://%{SERVER_NAME}%{REQUEST_URI} [END,NE,R=permanent]
</VirtualHost>
"""
    return config

if __name__ == "__main__":
    main(sys.argv[1:])
