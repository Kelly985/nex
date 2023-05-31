from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from food import Food, Description

# Create an instance of the database engine
engine = create_engine('sqlite:///restaurant.db')

# Create the tables in the database
Food.metadata.create_all(engine)

# Create a session factory
Session = sessionmaker(bind=engine)

# Create a session object
session = Session()

# Create a food with descriptions
# pilau = Food(foodname='Pilau', price=250)
# description1 = Description(description='spicy!', food=pilau)
# description2 = Description(description='yummy.', food = pilau)

# # # Add the food and descriptions to the session
# session.add(pilau)
# session.add(description1)
# session.add(description2)

# #Commit the changes to the database
# session.commit()

# rice.descriptions.append(description1)
# rice.descriptions.append(description2)

# session.add(rice)
# session.commit()



# # Read the food and descriptions
foods = session.query(Food).all()
descriptions = session.query(Description).all()

for description in descriptions:
    if description.description == "spicy!":
        print(description.food_id)

     #print(description.description)

# for food in foods:
#     if food.foodname == "Pilau":
#         print(food.price)

# for food in foods:
#     print(food.id,food.foodname,food.price),

# # Update the food and descriptions
# for food in foods:
#     if food.id == 1:  
#         food.price = 1500
   


# for description in descriptions:
#      if description.id == 8:
#          description.description = "sweeeet!!!!!!!!"

# # # Commit the changes to the database
#session.commit()

# Delete the food and descriptions
# for food in foods:
#     if food.id == 2:
#         session.delete(food)
#         break

# for description in descriptions:
#     if description.id == 8:
#         session.delete(description)
#         break

# Commit the changes to the database
#session.commit()
