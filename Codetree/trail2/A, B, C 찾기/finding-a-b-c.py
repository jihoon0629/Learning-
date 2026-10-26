arr = list(map(int, input().split()))
a = min(arr)
abc = max(arr)
bc = abc - a
for bp in arr:
    for cp in arr:
        if bp+cp == bc and a<=bp and a<=cp and bp<=cp:
            b,c = bp,cp
    
print(a,b,c)