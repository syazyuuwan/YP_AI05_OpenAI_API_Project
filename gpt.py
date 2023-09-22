# %%
# import packages
import os
import openai
from constants import AppConstants as ac
from dotenv import load_dotenv
# %%
load_dotenv()
# %%
openai.api_key = os.getenv("OPENAI_API_KEY")
# %%
# List of parameters
"""
Current parameters:

**required
! unhide
!Diet preferences - select from list
                    Vegetarian
                    Vegan
                    Pescatarian
                    Keto
                    Paleo
                    Gluten-free
                    Dairy-free
                    Nut-free
                    Halal
                    Kosher
                    Any (Default)
!**Home Appliance - select from list
                    Microwave
                    Stove
                    Induction Stove
                    Oven
                    Air Fryer
!**Allergies - fill as list
                    None (Default)
!Cuisine region - select from list
                    Italian
                    Mexican
                    Asian
                    Mediterranean
                    Indian
                    American
                    Fusion
                    Any (Default)
Meal Type - bfast/lunch/dinner/any(default)
Cooking Skill - beginner/expert/any(default)
Existing Ingredients - fill as list (may/must)
                    None (Default)

Budget type - low, medium, high, any(default)
!Health Goal - fill
                    Weight loss
                    Muscle gain
                    Maintenance
                    General well-being (Default)
Nutritional Preference - fill
                    Low-sodium
                    High-fiber
                    High-protein
                    Low-carb
                    Any (Default)
Calorie goals - fill
                    None (Default)
Prep duration - number of days
                    None (Default)
!Serving size - fill number
                    1 (Default)
Personal Preference - sweet/savory, mild/spicy
                    None (Default)
Mandatory output:
Notify me if there are any allergens in the recipe in case I am sharing with other people who may not share the same allergies. 
Include estimated cooking time.
Include estimated prepping time
Include estimated calories per ingredient. 
Include estimated cost based on Malaysian prices. 
Ingredients must be available in Malaysia.

"""
# %%
class ModelClass:
    # input handler
    def input_prompt_handler(self,**kwargs):
        
        diet_pref = kwargs['diet_pref'] #**
        home_appliance = kwargs['home_appliance'] #**
        allergy = kwargs['allergy']
        cuisine = kwargs['cuisine']
        meal_type = kwargs['meal_type']
        cooking_skill = kwargs['cooking_skill']
        exist_ingredient = kwargs['exist_ingredient']
        budget = kwargs['budget']
        health_goal = kwargs['health_goal']
        nutrient_pref = kwargs['nutrient_pref']
        serving_size = kwargs['serving_size']
        personal_pref = kwargs['personal_pref']
        
        input_prompt = f"""Dietary preferences are {diet_pref}. Recipe can only use {home_appliance}. Allergic to {allergy}. Cuisine from {cuisine}. Meal is for {meal_type}. Cooking level is {cooking_skill}. Recipe may include {exist_ingredient}. The cost should be {budget}. Health goal is {health_goal}. The recipe must be {nutrient_pref}. I want the recipe to be {personal_pref}. The meal serves {serving_size} people"""
        return input_prompt

    # chatbot
    def meal_prep_ai(self,input_prompt):
        response = openai.ChatCompletion.create(
            model = 'gpt-3.5-turbo',
            messages = [
                {
                    "role":"system",
                    "content":ac.system_prompt
                },
                {
                    "role":"user",
                    "content":ac.user_prompt_1
                },
                {
                    "role":"assistant",
                    "content":ac.assist_prompt_1
                },
                {
                    "role":"user",
                    "content":input_prompt
                }
            ],
            max_tokens = 3000,
            temperature = 0.1
        )
        recipe = response.choices[0].message.content
        return recipe

# %%
