alerts = {"HIGH": 0, "NORMAL": 0, "LOW": 0}
while True:
    
    alert = input(": ").strip().upper()
    if alert == "DONE":
        break
        
    elif alert in alerts:
        alerts[alert] += 1
    else:
        continue
for alert in alerts:
    print(f"{alert}: {alerts[alert]}")