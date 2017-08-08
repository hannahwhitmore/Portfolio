i = input('Do you want the recipe for cupcakes(1) cookies(2), brownies(3), funnel cake(4) or vanilla ice cream(5)? Type the corresponding number.')
if i == '1':
	cupcake = {'flour' : '1.5 cups' , 'baking powder' : '1.25 teaspoon', 'salt' : '1 stick', 'sugar' : '1 cup', 'eggs' : '2', 'vanilla extract' : '2 teaspoons', 'whole milk' : '2/3 cups', 'frosting' : '4 egg whites 3/4 cup sugar 2 sticks butter'}
	for directions1 in cupcake:
		print(directions1 + ' : ' + cupcake[directions1])
		
elif i == '2':
	cookie = {'flour' : '3 cups', 'baking powder' : '3/4 teaspoons', 'salt' : '1.25 teaspoon', 'butter' : '1 cup', 'sugar' : '1 cup', 'egg' : '1', 'milk' : '1 tablespoon'}
	for directions2 in cookie: 
		print(directions2 + ' : ' + cookie[directions2])
elif i == '3':
	brownie = {'eggs' : '4', 'sugar' : '1 cup', 'brown sugar' : '1 cup', 'melted butter' : '8 ounces', 'cocoa' : '11/4 cups', 'vanilla extract' : '2 teaspoons', 'flour' : '1/2 cup', 'kosher salt' : '1/2 teaspoon'}
	for directions3 in brownie: 
		print(directions3 + ' : ' + brownie[directions3])
elif i == '4':
	funnelcake = {'milk' : '2 cups', 'egg' : '1', 'flour' : '2 cups', 'salt' : '1 teaspoon', 'baking soda' : '1 teaspoon', 'sugar' : '1 tablespoon', 'melted butter' : '1/2 stick'}
	for directions4 in funnelcake: 
		print(directions4 + ' : ' + funnelcake[directions4])
elif i == '5':
	vanilla = {'Whisk the cream, milk, sugar, vanilla and 1/2 teaspoon salt in a medium saucepan and bring to a simmer over medium heat. Beat the egg yolks in a bowl. Whisk 1 cup of the cream mixture into the beaten yolks, then pour back into the saucepan, whisking, and return to medium heat. Cook, stirring constantly with a wooden spoon, until the mixture thickens, coats the spoon and reaches 180 degrees F on a thermometer, 6 to 8 minutes. Remove from the heat, strain, and stir. Lightly press plastic wrap directly against the surface of the custard to prevent a skin from forming. Chill until cold, about 3 hours. ' + 'heavy cream' : '3 cups', 'whole milk' : '1 cup', 'sugar' : '3/4 cup', 'vanila extract' : '1 tablespoon', 'salt' : '1/2 teaspoon', 'large egg yolks' : '5'}
	for directions5 in vanilla: 
		print(directions5 + ' : ' + vanilla[directions5] )
else:
	print('Invalid number.')
       
   
   
	
	
