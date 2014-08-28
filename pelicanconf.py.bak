#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Alan Bush'
SITENAME = u"Alan Bush" 
SITEURL = 'http://albush.com'

TIMEZONE = 'America/Chicago'
DEFAULT_DATE = 'fs' 
DEFAULT_LANG = u'en'
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = 'misc'
DISPLAY_TAGS_ON_SIDEBAR = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
THEME = './pelican-bootstrap3' 
CUSTOM_CSS = 'theme/style.css'
# Blogroll
LINKS =  (('Office Hours Cloud Hangout', 'http://go.rackspace.com/officehours'),('Pelican', 'http://getpelican.com/'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/alanbush'),
	('Google+', 'http://plus.google.com/+AlanBush/'),)

DISQUS_SITENAME = 'albush'


DEFAULT_PAGINATION = 5
# Tell Pelican to add 'extra/style.css' to the output dir
STATIC_PATHS = ['images', 'extra/style.css', 'extra/favicon.ico']

# Tell Pelican to change the path to 'theme/style.css' in the output dir
EXTRA_PATH_METADATA = {
'extra/style.css': {'path': '/theme/style.css'}, 'extra/favicon.ico': {'path': 'favicon.ico'}
}
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
DELETE_OUTPUT_DIRECTORY = True

HIDE_SIDEBAR = True

# Setting up static site with blog in subfolder
ARTICLE_DIR = 'blog'
ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'

PAGE_DIR = 'pages'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

AUTHOR_SAVE_AS = False

CATEGORY_SAVE_AS = 'blog/category/{slug}.html'
CATEGORY_URL = 'blog/category/{slug}.html'

TAG_SAVE_AS = 'blog/tag/{slug}.html'
TAG_URL = 'blog/tag/{slug}.html'	

DIRECT_TEMPLATES = (('index', 'blog/tags', 'blog/categories', 'blog/archives', 'blog/index'))
PAGINATED_DIRECT_TEMPLATES = (('index', 'blog/index', ))
