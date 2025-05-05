shopping_bag = {}

print('[구입]')
while True:
  item = input('상품명?')
  if item == '':
    break
  num = input('수량은?')
  shopping_bag[item] = num
  print(f'장바구니에 {item}가(이) {num}개가 담겼습니다.\n')

print(f'\n>>> 장바구니 보기: {shopping_bag}\n')
print('[검색]')
res = input('장바구니에서 확인하고자 하는 상품은?')
getRes = shopping_bag.get(res)
print(f'{res}은(는) {getRes}개 담겨 있습니다.')
