try:
  var='bad_var'
  assert (var == 'bad_var'),'Incorrect Name'
except Exception as e:
  print e
else:
  print var
