# 题目要求打印第10行, 当文件不足10行时, 没有输出
# `head -n 10 file.txt | tail -n 1` 的问题在于, 文件不足10行时, 会取到 topN (最大限度) 的行, 然后打印最后一行

tail -n +10 file.txt | head -n 1

# 时空最高效
awk 'NR==10'  file.txt

sed -n 10p file.txt