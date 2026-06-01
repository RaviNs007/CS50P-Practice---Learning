readings = []
while True:

    reading = input(": ").strip().lower()

    if reading == "done":
        break

    try:
        reading = float(reading)

    except (ValueError, TabError):
        continue

    if not 0 <= reading <= 1000:
        continue

    readings.append(reading)

total_readings = len(readings)
average = round((sum(readings) / total_readings), 2)

print(f"""
==========================================
#               Report                   #
==========================================
# Total readings :{total_readings:<23}#
#                                        #
# Max            :{max(readings):<23}#
#                                        #
# Min            :{min(readings):<23}#
#                                        #
# Average        :{average:<23}#
==========================================
""")