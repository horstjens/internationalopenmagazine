#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://internationalopenmagazine.org'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

#FEED_DOMAIN = SITEURL
#FEED_ATOM = 'feeds'
#FEED_RSS =  'feeds'
FEED_ALL_RSS = 'feeds/all.rss.xml'

CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
CATEGORY_FEED_RSS  = 'feeds/%s.rss.xml'

TAG_FEED_ATOM = 'feeds/%s.atom.xml'
TAG_FEED_RSS  = 'feeds/%s.rss.xml'


DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
