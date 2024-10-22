#Braden Leach
# OCT 22 2024
# Randomness practice
import random
#Problems using randrang()

    # Random Color Selector
colors = ['red','green','blue','yellow','purple']
random_index = random.randrange(0,5)
color_amount = len(colors)
print(f'your random color is: ' + colors[random_index] + ' and the amount of color you have are: ' + str(color_amount))
    
    #Random Animal Index
Animals = ["dog", "cat", "elephant", "giraffe", "lion"] 
random_index2 = random.randrange(0,5)
animal_amount = len(Animals)
print(f'your random animal is: ' + Animals[random_index2] + ' and the amount of animals you have are: ' + str(animal_amount))
    
    #Random Number from a List
numbers = [1,2,3,4,5,6,7,8,9,10]
random_index3 = random.randrange(0,10)
number_amount = len(numbers)
print(f'your random number is: ' + str(numbers[random_index3]) + ' and the amount of numbers you have are: ' + str(number_amount))


#problems using randint()
   
 #Random Fruit Selector
fruits =["apple", "banana", "cherry", "date", "fig"]
fruit_number = random.randint(0,4)
fruit_amount = int(len(numbers))
print(f'your random fruit is: ' + str(fruits[fruit_number]) + ' and the amount of fruits you have are: ' + str(fruit_amount))

   
    #Random Score Generator
names = ['John','Jack','Emily','David','Shmite','Henry','Tod']
amount_names = len(names)
random_names = random.randint(0,6)
random_score = random.randint(0,100)

print(f'your student that you got was: '+ str(names[random_names]) +' The amount of names that you get to chose from are: ' + str(amount_names) +'. Lastly the random score that you got was: ' + str(random_score))

    #Random Movie Selector
