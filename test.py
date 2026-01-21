import re
str = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam luctus sapien hendrerit nulla pretium, et tincidunt lacus dignissim.'

print(re.findall('\w+',str))