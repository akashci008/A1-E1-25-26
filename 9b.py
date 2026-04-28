joint = [
    [0.5, 0.3],
    [0.3, 0.4]
]

print("Marginal Probability of A:")
for i in range(len(joint)):
    print(f"P(A{i}) =", sum(joint[i]))
    
print("\nMarginal Probability of B:")
for j in range(len(joint[0])):
    col_sum = 0
    for i in range(len(joint)):
        col_sum += joint[i][j]
    print(f"P(B{j}) =", col_sum)
