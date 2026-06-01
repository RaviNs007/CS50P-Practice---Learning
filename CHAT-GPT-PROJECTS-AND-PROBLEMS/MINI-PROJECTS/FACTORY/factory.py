import json


def main():

    with open("plant_data.json", "r") as file:
        data = json.load(file)

    plan_name = data["plant"]["name"]
    plant_location = data["plant"]["location"]
    plant_shift = data["plant"]["shift"]

    print(f"""
    Plant Name   : {plan_name}
    Plant location: {plant_location}
    Plant shift  : {plant_shift}
""")

    unit_dict = {
        "temperature": "°C",
        "pressure": "PSI",
        "vibration": "Hz",
    }
    machine_count = 0
    running_machine_count = 0
    low_alert_count = 0
    high_alert_count = 0
    normal_count = 0
    maintenance_list = []
    critical_list = []

    for machine in data["machines"]:
        machine_data = data["machines"][machine]
        machine_name = machine_data["name"]
        machine_status = machine_data["status"]
        sensor_dict = machine_data["readings"]
        limit_dict = {}
        machine_count += 1
        alerts_count = 0
        if machine_status == "running":
            running_machine_count += 1

        for sensor in sensor_dict:
            reading = sensor_dict[sensor]

            if reading < machine_data["limits"][sensor]["low"]:
                limit_dict[sensor] = "LOW ALERT"
                low_alert_count += 1
                alerts_count += 1

            elif reading > machine_data["limits"][sensor]["high"]:
                limit_dict[sensor] = "HIGH ALERT"
                high_alert_count += 1
                alerts_count += 1
                if sensor == "temperature":
                    critical_list.append(machine_name)

            else:
                limit_dict[sensor] = "NORMAL"
                normal_count += 1

        if alerts_count >= 2:
            maintenance_list.append(machine_name)


        print(f"""
        
                ########################################################
                #                        REPORT                        #
                ########################################################
        
                        Machine         : {machine_name}
                        Machine status  : {machine_status}
                        Temperature     : {sensor_dict.get("temperature")} {unit_dict.get("temperature")}  {limit_dict.get("temperature")}
                        Pressure        : {sensor_dict.get("pressure")} {unit_dict.get("pressure")} {limit_dict.get("pressure")}
                        Vibration       : {sensor_dict.get("vibration")} {unit_dict.get("vibration")} {limit_dict.get("vibration")}
                        
                """)

    print(f"""
    
            Plant Summary:
                           **************************************************
                           *         Plant Name : {plan_name}      *
                           **************************************************          
                           *                                                *
                           *  Running Machines    : {running_machine_count:<24}*
                           *  Stopped Machines    : {machine_count - running_machine_count:<24}*
                           *                                                *
                           *  High Alerts         : {high_alert_count:<24}*
                           *  Low Alerts          : {low_alert_count:<24}*
                           *  Normal Readings     : {normal_count:<24}*
                           **************************************************
                           
                                    Maintenance Required Machines:
                                    --------------------------------
                                    {", ".join(maintenance_list[0:])}
                                    
                                    Critical Machines:
                                    --------------------------------
                                    {", ".join(critical_list[0:])}
    """)


if __name__ == "__main__":
    main()
