from tkinter import Canvas, Tk
# Constant values for our bar chart
WIDTH = 1400
HEIGHT = 700

# Create our window and canvas
gui = Tk()
gui.title('Josie InTham Final')
canvas = Canvas(gui, width=WIDTH, height=HEIGHT, background='white')

# add the canvas to the window
canvas.pack()

# opens the csv file in reading mode
file = open('US_Supreme_Court_Gifts.csv', mode = 'r')


''' appends the first value of each row to a list named "justice_name." this
protects against irregularities, such as a possible double last name, by finding
the comma and appending everything before it. '''
def justice_list():
    justice_name = []
    next(file)
    for line in file:
        try:
            find_name = line.find(',')
            find_name != -1
            justice_name.append(line[:find_name].strip())
        except ValueError:
            next(file)
    return justice_name

'''finds and appends the third value of each row, which is the amount that each justice has
been gifted from 2004 to 2023, to a list, by separating based on the $ prefix and .00 suffix. '''
def gift_amounts():
    file.seek(0)
    messy_amounts = []
    for line in file:
        try:
             start = line.index('$')
             end = line.index('.00', start)
             amount = line[start:end].strip().replace('$', '').replace(',', '').replace('"', '')
             amount_integer = int(amount)
             messy_amounts.append(amount_integer)
        except ValueError as e:
            continue
    return messy_amounts

names = justice_list()
amounts = gift_amounts()

# turns both lists into one dictionary
dict_data = dict(zip(names, amounts))

# gets rid of dictionary items that do not include a key for the value
for k in list(dict_data.keys()):
    if not k:
        del dict_data[k]

# reverses the dictionary's keys and values, so I can sort by amount
reverse_dict = dict(zip(dict_data.values(), dict_data.keys()))

# sorts the dictionary by the key item, which represents the amount of the gifts received
sorted_dict = dict(sorted(reverse_dict.items(), reverse=True))

# turns the keys (the amount value of gifts received) in the dictionary into a list
final_names = []
for key, value in sorted_dict.items():
    final_names.append(value)

# turns the values (the justice's names) in the dictionary into a list
final_amounts = []
for key, value in sorted_dict.items():
    final_amounts.append(key)

'''this function accesses a csv file with a list of the supreme court justices appointed by
a democratic party president. then appends those last names to a list.'''

def democratic_appointments():
    democratic_file = open('democratic_justices.csv', mode = 'r')
    democrats_list = []
    for line in democratic_file:
        democrat = line.replace(',', '').replace('\n', '').replace(' ', '')
        democrats_list.append(democrat)
    return democrats_list

democrats = democratic_appointments()





'''this next segment of code switches from data processing to data visualization.  it sets up
the axis and axis labels using for loops and functions.  then it creates
a list with a scaled version of the $ gift received by the supreme court justices, which
correlates to pixel length of the bars in the chart. it  iterates through a function 
creating each bar representing each justice, while making the fill color blue if the justice
is found in a separate list of the democrats, and making the fill color red if the justice is
not found on that list.'''
# creates axis
margin = 100
def chart_lines(x_position):
    canvas.create_line(x_position, 100, x_position, 615, fill='black', width = 1)
x_position = margin + 137.37
for i in range(8):
    chart_lines(x_position)
    x_position += 137.37

# labels axis
def axis_labels(axis_x, axis_text):
    canvas.create_text(axis_x, 640, text=axis_text, fill = 'black', font=("Times", 11),  anchor='center')
axis_x = margin + 137.37
axis_text = .5
for i in range(8):
    axis_labels(axis_x, axis_text)
    axis_text += .5
    axis_x += 137.37

# creates scaled bar boxes for each justice
box_lengths = []
for item in final_amounts:
    sized_box = (margin + (item/4000))
    box_lengths.append(sized_box)

def data_boxes(box_x, box_y, second_x, second_y, key):
    for key in dict_data:
        if value in democrats:
            z = 'blue'
        if value not in democrats:
            z = 'red'
        canvas.create_rectangle(box_x, box_y, second_x, second_y, fill = z, outline='white')
box_x = margin
box_y = margin + 30
second_y = 100
j = 0

for i, (key, value) in enumerate(sorted_dict.items()):
    second_x = box_lengths[i]
    data_boxes(box_x, box_y, second_x, second_y, key)
    box_y += 60
    second_y += 60

# title of graph
canvas.create_text(575, 75, text='Value of Reported Gifts Received by Current Supreme Court Justices (2001 - 2023)',
                   fill="black", font=("Times", 25),  anchor='center')

# label for x axis
canvas.create_text(WIDTH / 2, 670, text='-- $ of gifts, in millions --',
                   fill="black", font=("Times", 16),  anchor='center')


# writes the name of each justice next to the corresponding bar chart
def justice_labels(justice_y, current_justice):
    canvas.create_text(60, justice_y, text=current_justice, fill = 'black', font=("Times", 13),  anchor='center')
j = 0
justice_y = 115
for item in final_names:
    justice_labels(justice_y, final_names[j])
    justice_y += 60
    j += 1





''' the next section of code creates the second graph, which is a zoomed-in look at the justices
excluding Clarence Thomas, who has thrown all my data. '''
# creates blank square for new graph
canvas.create_rectangle(320, 170, 1350, 580, fill= '#e4dff7', outline='white')

# title of zoomed-in graph
canvas.create_text(800, 200, text='Zoomed In (Excluding Thomas & Alito)',
                   fill="black", font=("Times", 18),  anchor='center')
# label for x axis
canvas.create_text(800, 566, text='-- $ of gifts, in thousands --',
                   fill="black", font=("Times", 14),  anchor='center')

# creates new axis for the zoomed-in chart
def new_lines(x_position):
    canvas.create_line(x_position_prime, 220, x_position_prime, 530, fill='black', width = 1)
x_position_prime = 395 + 88.88
for i in range(10):
    new_lines(x_position)
    x_position_prime += 88.88

# labels new axis for the zoomed-in chart
def new_axis(axis_x, new_text):
    canvas.create_text(axis_x, 540, text = new_text, fill = 'black', font=("Times", 11),  anchor='center')
axis_x = 395 + 88.88
new_text = 20
for i in range(10):
    new_axis(axis_x, new_text)
    new_text += 20
    axis_x += 88.88

# creates scaled bar boxes for each justice
box_prime = []
for item in final_amounts:
    sized_prime = (item/60)
    box_prime.append(sized_prime)

def data_boxes(x_box, y_box, x_second, y_second, key):
    for key in dict_data:
        if value in democrats:
            e = 'blue'
        if value not in democrats:
            e = 'red'
        canvas.create_rectangle(x_box, y_box, x_second, y_second, fill = e, outline='white')
x_box = 395
y_box = 230
y_second = 250
j = 0

for i, (key, value) in enumerate(sorted_dict.items()):
    x_second = x_box + box_prime[i]
    data_boxes(x_box, y_box, x_second, y_second, key)
    y_box += 35
    y_second += 35

# writes the name of each justice next to the zoomed-in bar chart
def justice_labels_prime(y_justice, current_justice_prime):
    canvas.create_text(360, y_justice, text=current_justice_prime, fill = 'black', font=("Times", 11),  anchor='center')
b = 0
y_justice = 240
for item in final_names:
    justice_labels_prime(y_justice, final_names[b])
    y_justice += 35
    b += 1


'''this last portion creates the legend'''
# creates blank square for legend
canvas.create_rectangle(1150, 50, 1350, 150, fill= 'white', outline='black')
canvas.create_text(1250, 80, text='LEGEND', fill = 'black', font=("Times", 16),  anchor='center')
canvas.create_text(1250, 100, text='Red = Appointed by Republican', fill = 'red', font=("Times", 13),  anchor='center')
canvas.create_text(1250, 115, text='Blue = Appointed by Democrat', fill = 'blue', font=("Times", 13),  anchor='center')


