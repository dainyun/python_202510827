def buy(shoppint_bag):
  print('[구입]')
  item = input('상품명?')
  if item == '':
    return False
  num = input('수량은?')
  shopping_bag[item] = num
  print(f'장바구니에 {item}가(이) {num}개가 담겼습니다.\n')
  return True

def show(shopping_bag):
  print(f'\n>>> 장바구니 보기: {shopping_bag}\n')

def find(shopping_bag):
  print('[검색]')
  item = input('장바구니에서 확인하고자 하는 상품은?')
  if item in shopping_bag:
    print(f'{item}은(는) {shopping_bag[item]}개 담겨 있습니다.')
  else:
    print(f'장바구니에 {item}은(는) 없습니다.')

shopping_bag = {}
while True:
  if buy(shopping_bag) == False:
    break
show(shopping_bag)
find(shopping_bag)
