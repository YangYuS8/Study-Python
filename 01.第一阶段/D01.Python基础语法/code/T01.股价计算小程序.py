# 定义变量
name = "传智播客"  # 公司名
stock_price = 19.99  # 当前股价
stock_code = "003032"  # 股票代码
stock_price_daily_growth_factor = 1.2  # 每日增长系数
growth_days = 7  # 增长天数
finally_stock_price = stock_price * stock_price_daily_growth_factor**growth_days

# 输出
print(f"公司：{name}，股票代码：{stock_code}，当前股价：{stock_price}")
print(
    "每日增长系数为：%.1f，经过%d天的增长后，股价达到了：%.2f"
    % (stock_price_daily_growth_factor, growth_days, finally_stock_price)
)
