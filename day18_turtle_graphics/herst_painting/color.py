import colorgram

image_path = r"C:\Users\param\OneDrive\Desktop\Dev\Courses\100-Days_of_Python-Beginner\day18_turtle_graphics\herst_painting\painting.jpg"

colors = colorgram.extract(image_path, 30)

color_list = []

for i in range(0,len(colors)):
    r = colors[i].rgb.r
    g = colors[i].rgb.g
    b = colors[i].rgb.b
    color_tuple = (r,g,b)

    color_list.append(color_tuple)

print(color_list)

