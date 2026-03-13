#lambda is a keyword use to define a funtion but without any name unlike def keyword which requires a name

# lamba <variables> : <return expression>
sq_and_sqrt = lambda x,y :[x**2, int(y**(1/2))] #it is not considered good to assign a variable to lambda as def keywrods is better for that
print(sq_and_sqrt(7, 49))
