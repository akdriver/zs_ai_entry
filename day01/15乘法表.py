for i in range(1,10):
    for j in range(1,10):
        if j > i :
            break
        print(f"{j} * {i} = {i*j}",end="\t")
    print("")