def insert_string_middle(string, char):
  start = string[:2]
  end = string[-2:]
  return start + char + end

print insert_string_middle("<<>>", 'suman')
