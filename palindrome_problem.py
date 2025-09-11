myylist = ["palindrome", "madamimadam", "foo", "eye"]

dabba = []
for i in range(len(myylist)):
    if myylist[i] == myylist[i][::-1]:
        dabba.append("True")
    else:
        dabba.append("False")
print(dabba)
