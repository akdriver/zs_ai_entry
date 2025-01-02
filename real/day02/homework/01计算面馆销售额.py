# 需求:
# 通过键盘录入: 每天卖出多少碗面
# 通过键盘录入: 每碗面多少块
#
# 通过键盘录入: 今年共营业多少天
# 计算并且输出一年的总销售额。

sale_count = input("今天卖出多少碗面：")
price = input("每碗面多少块：")
days = input("今年共营业多少天：")

sale_count = int(sale_count)
price = float(price)
days = int(days)

total = sale_count * price * days
print(f"一年的总销售额 {total} 元")
