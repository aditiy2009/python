# intialize the variable
#python doesn't require to name the type of variable
# type (float,int etc) is defined or identified by value of variable

car=100 #type int
drivers=30
seat=4.0 #type float
passengers= 90

car_not_driven= car-drivers
car_driven= drivers
car_pool_capacity= car_driven*seat
avg_passenger_in_car= passengers/car_driven

#printing the results
print("There are",car,"cars availabel.")
print("There are only",drivers,"drivers availabel.")
print("There will be",car_not_driven,"empty cars today.")
print("There will be ",car_driven," full cars.")
print("We can transport",car_pool_capacity,"people today.")
print("We have",passengers,"passengers to carpool today.")
print("We need to put about", avg_passenger_in_car,"in each car.")
