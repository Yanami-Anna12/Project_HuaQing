numbers = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]

# 原列表中所有大于3的元素的平方
result = {x**2 for x in numbers if x > 3}
print(result)