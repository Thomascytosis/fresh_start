AUTHOR = 'thomascytosis'
SITENAME = 'retry_one'
SITEURL = 'https://thomascytosis.github.io/fresh_start/'
<<<<<<< HEAD
BLOG_AUTHORS = 'thomascytosis'
=======

>>>>>>> 368af1eb56ee4ac8382161427fd076412c54197d
PATH = 'content'
OUTPUT_PATH = 'docs/'

TIMEZONE = 'America/Denver'

DEFAULT_LANG = 'en'
PLUGIN_PATHS = ['https://github.com/pelican-plugins/']
PLUGINS = [
    # ...
    'minchin.pelican.plugins.nojekyll',
    # ...
]

THEME = "lovers"


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
