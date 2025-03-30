def get_fixed_price(dis_rate, dis_price):
    rate = dis_price / (1 - (dis_rate/100))
    return rate


dis_rate = int(input('할인율은?'))
Adis_price = int(input('A 상품의 할인된 가격은?'))
Aprice = get_fixed_price(dis_rate, Adis_price)
Bdis_price = int(input('B 상품의 할인된 가격은?'))
Bprice = get_fixed_price(dis_rate, Bdis_price)
print('A 상품의 정가는', Aprice, '원')
print('B 상품의 정가는', Bprice, '원')
