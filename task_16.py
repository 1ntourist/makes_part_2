earth_weight = int(input("give your weight: "))
weight_in_15_years = list(range(earth_weight, earth_weight+15))
years = 0
for a in weight_in_15_years:
    moon_weight = round((a * 0.165), 1)
    years += 1
    print("in {} years your weight will be {} kgs".format(years , moon_weight))
