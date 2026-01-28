def nums_sum(*args):
    negative_sum = 0
    positive_sum = 0
    for num in args:
        if num > 0:
            positive_sum += num
        else:
            negative_sum += num
    return negative_sum, positive_sum

numbers = map(int, input().split())
neg_sum, pos_sum = nums_sum(*numbers)

print(neg_sum)
print(pos_sum)
if abs(neg_sum) > pos_sum:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")