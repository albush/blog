#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# Production Version #
from __future__ import unicode_literals

AUTHOR = u'Alan Bush'
SITENAME = "Alan Bush" 
SITEURL = 'http://albush.com'
USER_LOGO_URL = '//drops.albush.com/ab3head.png' 
TAGLINE = 'Nerd|Husband|Father|Improviser'

TIMEZONE = 'America/Chicago'
DEFAULT_DATE = 'fs' 
DEFAULT_LANG = u'en'
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = 'misc'
DISPLAY_TAGS_ON_SIDEBAR = False

# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
THEME = './pelican-svbhack-master' 
CUSTOM_CSS = 'theme/style.css'
CACHE_CONTENT = False
GOOGLE_ANALYTICS = 'UA-15275173-7'

# Blogroll
# LINKS =  (('ComedySportz San Antonio', '//cszsa.com'),('Pelican', '//getpelican.com/'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/alanbush'),
	('Google+', 'http://plus.google.com/+AlanBush/'),)

DISQUS_SITENAME = 'albush'

DEFAULT_PAGINATION = 7
# Tell Pelican to add 'extra/style.css' to the output dir
STATIC_PATHS = ['images', 'extra/style.css', 'extra/favicon.ico', 'extra/avatar.jpg']

# Tell Pelican to change the path to 'theme/style.css' in the output dir
EXTRA_PATH_METADATA = {
'extra/style.css': {'path': 'theme/style.css'}, 'extra/favicon.ico': {'path': 'favicon.ico'}, 'extra/avatar.jpg': {'path': 'images/avatar.jpg'}
}

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
DELETE_OUTPUT_DIRECTORY = True

HIDE_SIDEBAR = False
