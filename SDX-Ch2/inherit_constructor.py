import math

def shape_density(thing, weight):
    return weight / call(thing, "area")

# [shape]
def shape_new(name):
    return {
        "name": name,
        "_class": Shape
    }

Shape = {
    "density": shape_density,
    "_classname": "Shape",
    "_parent": Shape2D,
    "_new": shape_new
}
# [/shape]

def my_type(thing):
    if thing["_parent"] == None:
        return thing["_classname"]
    else:
        parent = thing["_parent"]
        return my_type(parent["_parent"])


# line

def line_new(name, length):
    return {
        "name": name,
        "_length" : length,
        "_class": Line
    }
def line_length(thing):
    return thing['length']

Line = {
    "length" : line_length,
    "_classname": "Line",
    "_parent" : Shape,
    "_new" : line_new,
}


Shape2D = {
    "_cache" : {},
    "area" : shape2D_area,
    "perimeter" : shape2D_perimeter,
    "_parent" : "Shape",
    "_new" : shape2d_new,
    "_classname" : Shape2D
}

# [make]
def make(cls, *args):
    return cls["_new"](*args)
# [/make]

def square_perimeter(thing):
    return 4 * thing["side"]

def square_area(thing):
    return thing["side"] ** 2

# [square]
def square_new(name, side):
    return make(Shape, name) | {
        "side": side,
        "_class": Square
    }

Square = {
    "perimeter": square_perimeter,
    "area": square_area,
    "_classname": "Square",
    "_parent": Shape,
    "_new": square_new
}
# [/square]

def circle_perimeter(thing):
    return 2 * math.pi * thing["radius"]

def circle_area(thing):
    return math.pi * thing["radius"] ** 2

def circle_new(name, radius):
    return make(Shape, name) | {
        "radius": radius,
        "_class": Circle
    }

Circle = {
    "_classname": "Circle",
    "_parent": Shape2D,
    "_new": circle_new
}

def find(cls, method_name):
    if cls is None:
        raise NotImplementedError("method_name")
    if method_name in cls:
        return cls[method_name]
    return find(cls["_parent"], method_name)

def call(thing, method_name, *args, **kwargs):
    method = find(thing["_class"], method_name)
    return method(thing, *args, **kwargs)

# [call]
examples = [make(Square, "sq", 3), make(Circle, "ci", 2)]
for ex in examples:
    n = ex["name"]
    d = call(ex, "density", 5)
    print(f"{n}: {d:.2f}")
# [/call]
