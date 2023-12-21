sec = [4.359670e+04,
       2.460925e+05,
       0.000000e+00,
       2.822750e+03,
       1.191850e+04,
       6.687000e+04,
       1.034226e+07]

min = [s/60 for s in sec]
hour = [m/60 for m in min]
day = [h/24 for h in hour]

day = 500000/60/60/24
print('days:', day)

