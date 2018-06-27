import re
chunkhash = re.compile(r'\w+\.+\w+\.+\w+')
file = open('./index.html', 'r')
for line in file:
  if chunkhash.search(line):
    newline = chunkhash.sub(line, 'app.js')
    print(re.sub(chunkhash, 'app.js', line))
file.close()
