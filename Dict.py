alien_0 = {"color":["green","red","blue"], 'points': 5}
print(alien_0["color"][0])
print(alien_0['points'])

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
alien_0['x_position'] = 15
print(alien_0)
del alien_0["points"]
print(alien_0)