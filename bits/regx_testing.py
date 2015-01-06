__author__ = 'zog'

import re

return_string = '<div class="well">zero</div>'
print "return_string: ",return_string

mod_str = re.sub(r'<div class="well">', "", return_string)
mod_str = re.sub(r'</div>', "", mod_str)
mod_str.strip()
print "mod_str:",mod_str
