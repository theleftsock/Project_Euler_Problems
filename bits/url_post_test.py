__author__ = 'zog'

import urllib
import urllib2
import re
import time

f = open("numbers_as_words_orig.txt", 'w')

for x in xrange(0,1002,1):
    if (x == 0):
        continue
    url = 'http://www.tools4noobs.com'
    values = {'action' : 'ajax_number_spell_words',
              'number' : x,
              'type' : '0',
              'locale' : 'en_US'}

    data = urllib.urlencode(values)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    the_page = response.read()
    mod_str = re.sub(r'<div class="well">', "", the_page)
    mod_str = re.sub(r'</div>', "", mod_str)
    mod_str.strip()
    print "number_as_word:",mod_str
    f.write(mod_str+"\n")
    time.sleep(.1)