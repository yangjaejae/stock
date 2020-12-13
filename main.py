import stock

stock_cls = stock.Stock()

top50_list = list(stock_cls.get_top50_list())
line_20 = stock_cls.get_20_line(top50_list[0])

print(line_20)