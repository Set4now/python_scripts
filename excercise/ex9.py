def add_tags(tag, string):
  tag1 = "<tag>"
  tag2 = "</tag>"
  return tag1 + string + tag2

print add_tags("i", "hello")
