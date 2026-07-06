from numpy.ma.extras import average

score = [85, 92, 78, 96, 88]
print(f"最高分:{max(score)}")
print(f"最低分:{min(score)}")
print(f"平均分:{average(score)}")
print(f"排名:{sorted(score,reverse=True)}")