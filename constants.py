# constants.py

class AppConstants:
    # options constant
    diet_pref_options = ['Any','Vegan','Vegetarian','Pescatarian','Keto',
                        'Gluten-free','Dairy-free','Nut-free']
    home_appliance_options = ['Microwave','Stove','Oven','Air Fryer', 'Pressure Cooker', 'Thermomix']
    cuisine_options = ['Any','Asian','Western','Mediterranean','Mexican','Indian','Italian','Fusion']
    meal_type_options = ['Any','Breakfast','Lunch','Dinner']
    cooking_skill_options = ['Any','Beginner','Expert']
    budget_options = ['Any','Low-cost','Medium-cost','High-cost']
    health_goal_options = ['General well-being','Weight loss','Muscle gain','Maintenance']
    nutrient_pref_options = ['Any','Low-sodium','High-fiber','High-protein','Low-carb']
    
    
    # prompt constant
    system_prompt = """
You are a meal prep expert giving meal prep advice to customers seeking to improve or maintain their health. Include allergen warning in case other allergens are included when sharing. Include estimated prepping time, cooking time, total calories, cost based on Malaysian prices in RM, serving amount. Include serving size. Break down calories per ingredients and calories per serving. Ingredient measurements are in metric system. Include how to store and expiry. The recipe should last for as long as meal prep days.
"""

    user_prompt_1 = """
dietary preferences are pescatarian. recipe can only use stove, air fryer. allergic to shellfish. cuisine from mexican. meal is for dinner. cooking level is expert. recipe may include  tomato, chili, lettuce. the cost should be any cost. health goal is for gaining weight. the recipe must be high-fiber. i want the recipe to be Very Spicy, Sweet. the meal serves 2 people.
"""

    assist_prompt_1 = """
Based on your preferences, dietary restrictions, and goals, here's a Pescatarian, High-Fiber Mexican dinner:

Recipe: Spicy Mexican Fish Tacos

Allergen information: This recipe does not contain shellfish. However, please note that if you have any other specific allergies, make sure to check the individual ingredients for potential allergens.

Prep Time: 30 minutes
Cooking Time: 20 minutes
Total Calories: Approximately 900 calories per serving
Cost: Approximately RM 40-50
Serving Amount: 2 people
Serving Size: 2 tacos per person

Ingredients:
- 400g white fish fillets (such as tilapia or cod)
- 2 tablespoons olive oil
- 1 teaspoon paprika
- 1 teaspoon ground cumin
- 1 teaspoon chili powder (adjust to taste for desired spiciness)
- Salt and pepper, to taste
- 4 small corn tortillas
- 1 cup shredded lettuce
- 1 cup diced tomatoes
- 1/2 cup diced onions
- 1/4 cup chopped fresh cilantro
- Lime wedges, for serving

For the Spicy Sauce:
- 1/4 cup Greek yogurt (or sour cream for a sweeter taste)
- 2 tablespoons mayonnaise
- 1 tablespoon Sriracha sauce (adjust to taste for desired spiciness)
- 1 tablespoon lime juice
- Salt, to taste

Instructions:
1. Preheat the air fryer to 200°C (400°F) and preheat a non-stick skillet over medium-high heat on the stove.
2. In a small bowl, mix together the paprika, cumin, chili powder, salt, and pepper. Rub the spice mixture onto both sides of the fish fillets.
3. Place the fish fillets in the air fryer and cook for 10-12 minutes, or until the fish is cooked through and flakes easily with a fork. Set aside.
4. While the fish is cooking, prepare the spicy sauce. In a bowl, combine the Greek yogurt, mayonnaise, Sriracha sauce, lime juice, and salt. Mix well until smooth and creamy. Adjust the amount of Sriracha sauce according to your desired level of spiciness.
5. Warm the corn tortillas in a dry skillet over medium heat for about 30 seconds on each side, or until they become pliable.
6. To assemble the tacos, spread a generous amount of the spicy sauce onto each tortilla. Top with shredded lettuce, diced tomatoes, diced onions, and fresh cilantro.
7. Cut the cooked fish fillets into smaller pieces and divide them equally among the tacos.
8. Serve the tacos with lime wedges on the side for squeezing over the top before eating.

Storage and Expiry:
- Store the cooked fish fillets and taco toppings separately in airtight containers in the refrigerator.
- The fish fillets can be stored for up to 3 days, and the taco toppings can be stored for up to 5 days.
- To enjoy the freshest taste and texture, assemble the tacos just before serving.

Nutritional Information (per serving):
- Calories: Approximately 900 calories
- Carbohydrates: 70g
- Protein: 60g
- Fat: 40g
- Fiber: 10g

Note: The nutritional information provided is an estimate and may vary depending on the specific ingredients and brands used.
"""

