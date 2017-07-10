def first_half(str):
  if len(str) % 2 == 0:
    end = len(str) / 2 
    return str[: end]

print first_half('acthgvbhtr')
