# import pygal

# barchart = pygal.Bar()

# barchart.add('Dog', 5)
# barchart.add('Cat', 4)
# barchart.add('Hamster', 3)
# barchart.add('Fish', 3)
# barchart.add('Snake', 3)

# barchart.render()


import pygal

piechart = pygal.Pie()
barchart = pygal.Bar()
file = open('pets.txt','r')

for line in file.read().splitlines():
  # line_list = line.split()
  # label = line_list[0]
  # value = line_list[1]
  
  label, value = line.split()
  piechart.add(label, int(value))
  barchart.add(label, int(value))


piechart.render()
barchart.render()
  
  
  

  
  
  
  
