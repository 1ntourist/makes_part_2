time_1 = [int(input("give a hours_1: ")), int(input("give a minute_1: ")),
            int(input("give a sec_1: "))]
time_2 = [int(input("give a hours_2: ")), int(input("give a minute_2: ")),
            int(input("give a sec_2: "))]
hour_1 = (time_2[0] - time_1[0]) % 24
min_1 = (time_2[1] - time_1[1]) % 60
sec_1 = (time_2[2] - time_1[2]) % 60
print("difference of hour: ", hour_1)
print("difference of minute: ", min_1)
print("difference of second: ", sec_1)
