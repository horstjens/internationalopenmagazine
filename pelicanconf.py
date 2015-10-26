#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

### twitchy theme
#--------------------------------------------------- | -----------
#`SITESUBTITLE` | Provide a description of your site, inserted into landing page jumbatron
#`RECENT_POST_COUNT = 5` | How many post should be displayed on the landing page.
#`EXPAND_LATEST_ON_INDEX` | Expand the Latest Articles Section in the Sidebar if you are on `index.html`

### more colours?
#Setting name (followed by default value, if exists) | Description
#--------------------------------------------------- | -----------
#`BOOTSTRAP_THEME = "bootstrap"` | Which bootstrap theme should be loaded, see static/css for a list.
#`PYGMENTS_STYLE = "native"` | Which pygments theme should be loaded, see static/css for a list.
#`TYPOGRIFY = False` | If Typogrify css should be loaded
#`CUSTOM_CSS` | Can be used to provide an additional css file, e.g.: `CUSTOM_CSS = "extra/custom.css"`

### sidebar
#Setting name (followed by default value, if exists) | Description
#--------------------------------------------------- | -----------
#`SHARE = False` | Provide simple non tracking sharing buttons (fb, g+, twitter) for articles/pages and the landing page
#`SOCIAL` | Links to your profile on other site, complete with icon, e.g.: `SOCIAL = (('Twitter', 'https://twitter.com/derwinlu'), ('Bitbucket', 'https://bitbucket.org/winlu'))`
#`SITELOGO` | Add a SiteLogo to your Sidebar, expects the path to the logo similar to `CUSTOM_CSS`
#`SITELOGO_SIZE` | width attribute of `SITELOGO`'s `img` tag.
#`HIDE_SITENAME` | hides the sitename from the sidebar, useful if your sitelogo already contains your sitename.
#`DISPLAY_RECENT_POSTS_ON_MENU` | Displays recent articles in the sidebar, count is determined by `RECENT_POST_COUNT`
#`DISPLAY_PAGES_ON_MENU` | Displays pages in sidebar.
#`DISPLAY_CATEGORIES_ON_MENU` | Displays category list in sidebar.
#`DISPLAY_TAGS_ON_MENU` | Displays tag list in sidebar.



AUTHOR = u'Horst JENS'
SITENAME = u'international open magazine'
#SITEURL = u'http://internationalopenmagazine.org'
SITEURL = ''
SITESUBTITLE = u'open source. open education. open everything!'
#RECENT_POST_COUNT = 15
#EXPAND_LATEST_ON_INDEX = True
SHARE = True
SITELOGO = '/images/international-open-magazine-logo-small-gradient.png'
SITELOGO_SIZE = 200
HIDE_SITENAME = False
DISPLAY_RECENT_POSTS_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_TAGS_ON_MENU = False

#PLUGIN_PATHS = [u'/home/horst/code/internationalopenmagazine/plugins/']
#PLUGINS = ['tag_cloud'] # stört anscheindend das theme pelican-twitchy
#PLUGIN_PATHS = ['/home/horst/code/blog/plugins']
#PLUGINS = ['tag_cloud']

#FAVORITE_TAG = 'gamedev'
#FAVORITES_COUNT = 500000



#YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html' # jahresübersicht?
#TAG_URL = 'tag/{slug}.html'
#TAG_SAVE_AS = 'tag/{slug}.html'
 
#ARCHIVES_SAVE_AS = 'archives.html'   # direct templates?

#TAG_CLOUD_STEPS = 4
#TAG_CLOUD_MAX_ITEMS = 255
#TAG_CLOUD_SORTING = "alphabetically"

PATH = 'content'

TIMEZONE = 'Europe/Vienna'

DEFAULT_LANG = u'en'
CC_LICENSE = u'CC-BY-SA'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
          ('Mailinglist','https://groups.google.com/forum/#!forum/internationalopenmagazine' ),
          ('Twitter', 'https://twitter.com/search?q=%23intopenmag&src=typd'),
          ('Github', 'https://github.com/horstjens/internationalopenmagazine'),
          ('Google+ Site', 'https://plus.google.com/b/101914803942842117545/101914803942842117545/posts'),
          ('Google+ Community', 'https://plus.google.com/b/101914803942842117545/communities/114297625315121661514'),
          ('Facebook page', 'https://www.facebook.com/internationalopenmagazine'),
          ('Facebook Group', 'https://www.facebook.com/groups/1660191657562162/'),
          ('Diaspora', 'https://joindiaspora.com/tags/intopenmag'),
          ('Gnusoical.de', 'https://gnusocial.de/search/notice?q=%23intopenmag'),
          ('reddit', 'https://www.reddit.com/r/intopenmag/'),
          )

DEFAULT_PAGINATION = 200

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
THEME = "twitchymagazine"
