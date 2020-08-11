import re
bat_regex = re.compile(r'Bat(wo)*man')
m1 = bat_regex.search('The Adventure of Batman')
m1.group()