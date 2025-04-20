def display_mulitiplication_table():
  for a in range(1, 10):
    for b in range(2, 6):
      print(f'{b} x {a} = {a*b:2d}', end ='\t')
    print()
  print()
  for c in range(1,10):
    for d in range(6, 10):
      print(f'{d} x {c} = {c*d:2d}', end = '\t')
    print()

display_mulitiplication_table()
