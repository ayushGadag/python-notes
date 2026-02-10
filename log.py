logs = [
    "INFO User login",
"ERROR Database failed",
"WARNING Disk full",
"ERROR Timeout"
]

count =0

for i in logs:
    if "ERROR" in i:
        print(i)
        count+=1
        print(f"the total number of count is :-{count}")
        



        




