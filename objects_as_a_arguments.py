from circle import Circle

c1 = Circle(10)
c2 = Circle(15)

# function where objects will passed as arguments
def get_results(obj):
    print("Area is {:.2f}".format(obj.get_area()))
    print("Perimeter is {:.2f}".format(obj.get_perimeter()))

get_results(c1)
get_results(c2)
