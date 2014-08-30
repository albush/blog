#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Alan Bush'
SITENAME = "Alan Bush" 
SITEURL = 'http://albush.com'
USER_LOGO_URL = '//drops.albush.com/ab3head.png' 
TAGLINE = 'Nerd|Husband|Father|Improviser|More'

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

# Blogroll
#LINKS =  (('Projects', '/pages/projects.html'),('Pelican', 'http://getpelican.com/'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/alanbush'),
	('Google+', 'http://plus.google.com/+AlanBush/'),)

DISQUS_SITENAME = 'albush'

# AVATAR = '/images/avatar.jpg'
# ABOUT_ME = 'Nerd|Husband|Father|Improviser|More'


DEFAULT_PAGINATION = 5
# Tell Pelican to add 'extra/style.css' to the output dir
STATIC_PATHS = ['images', 'extra/style.css', 'extra/favicon.ico', 'extra/avatar.jpg']

# Tell Pelican to change the path to 'theme/style.css' in the output dir
EXTRA_PATH_METADATA = {
'extra/style.css': {'path': 'theme/style.css'}, 'extra/favicon.ico': {'path': 'favicon.ico'}, 'extra/avatar.jpg': {'path': 'images/avatar.jpg'}
}

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
DELETE_OUTPUT_DIRECTORY = True

HIDE_SIDEBAR = False

# Setting up static site with blog in subfolder
# ARTICLE_DIR = 'blog'
# ARTICLE_URL = 'blog/{slug}.html'
# ARTICLE_SAVE_AS = 'blog/{slug}.html'

# PAGE_DIR = 'pages'
# PAGE_URL = '{slug}.html'
# PAGE_SAVE_AS = '{slug}.html'

# AUTHOR_SAVE_AS = False

# CATEGORY_SAVE_AS = 'blog/category/{slug}.html'
# CATEGORY_URL = 'blog/category/{slug}.html'

# TAG_SAVE_AS = 'blog/tag/{slug}.html'
# TAG_URL = 'blog/tag/{slug}.html'	

# DIRECT_TEMPLATES = (('index', 'blog/tags', 'blog/categories', 'blog/archives', 'blog/index'))
# PAGINATED_DIRECT_TEMPLATES = (('index', 'blog/index', ))
