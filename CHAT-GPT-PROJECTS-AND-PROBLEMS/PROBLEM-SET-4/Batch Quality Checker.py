results = {"pass": 0, "fail": 0, "retest": 0}

while True:
    result = input("Batch result: ").strip().lower()
    
    if result == "done":
        break
    
    if result not in results:
        print("No valid data")
        continue
    
    results[result] += 1

total = results["pass"] + results["fail"] + results["retest"]
if total == 0:
    print("No batch data")
else:
    pass_percentage = round((((results["pass"])/total)*100), 2)
    sign = "%"
    print(f"""
    ==========================================
    #               Report                   #
    ==========================================
    # Total batches   :{total:<22}#
    #                                        #
    # Pass count      :{results["pass"]:<22}#
    #                                        #
    # Fail count      :{results["fail"]:<22}#
    #                                        #
    # Pass percentage :{pass_percentage}{sign:<18}#
    ==========================================
    """)