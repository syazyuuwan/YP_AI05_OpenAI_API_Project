import time
import streamlit as st
from constants import AppConstants as ac
from gpt import ModelClass as mc

def main():
    st.set_page_config(page_title='PrepFection',page_icon='🍔')
    st.title("PrepFection")
    st.write("An AI-Powered Hyper-Customisable Meal Prep Tool")  

    
    with st.form(key='form'):
        with st.expander("I have an idea", expanded=False):
            custom_input = st.text_input("What is it?","")
            st.text('If you only have preferred ingredients start with "something with ..."')
        col1, col2 = st.columns(2)
        
        with col1:
            diet_pref = st.selectbox("Diet preference:", ac.diet_pref_options, index=0)
            
            cuisine = st.selectbox("Cuisine from:", ac.cuisine_options, index=0)
            
            health_goal = st.selectbox("Health goal:", ac.health_goal_options, index=0)
        
        with col2:
            serving_size = st.number_input("Serving size", 1)
                
            home_appliance = st.multiselect("Appliance(s) available:", ac.home_appliance_options)
            if home_appliance == []:
                home_appliance = ",".join(ac.home_appliance_options)
            else:
                home_appliance = ",".join(home_appliance)

        allergy = st.text_input("Allergies:", "")
        if allergy == "":
            allergy = 'None'
        exist_ingredient = st.text_input("Existing Ingredients:", "")
        if exist_ingredient == "":
            exist_ingredient = 'Anything'
        
        # Checkbox for halal recipe
        halal_check = st.checkbox("Make it Halal?")
        if halal_check:
            diet_pref = diet_pref+", Halal"
                    
        # Check if advanced options should be shown
        with st.expander("Advanced Options", expanded=False):
            col5,col6 = st.columns(2)
            
            with col5:
                meal_type = st.selectbox("Meal type:", ac.meal_type_options, index=0)
                budget = st.selectbox("Budget level:", ac.budget_options, index=0)
            with col6:
                cooking_skill = st.selectbox("Cooking Skill level:", ac.cooking_skill_options, index=0)
                nutrient_pref = st.selectbox("Nutritional Preference:", ac.nutrient_pref_options, index=0)
            
            col7, col8 = st.columns(2)
            with col7:
                sweet_savory = st.selectbox("Sweet or Savory:", options=['Any','Sweet','Savory','Both'], index=0)
            with col8:
                spice_level = st.selectbox("Spice level:", options=['Any spice level','Not spicy','Mild spice','Very spicy'], index=0)
                if sweet_savory == 'Any':
                    sweet_savory = 'Sweet or Savory'
                elif sweet_savory == 'Both':
                    sweet_savory = 'Sweet and Savory'
            
            
            personal_pref = sweet_savory+", "+spice_level

        submit_button = st.form_submit_button("Submit")

    if submit_button:            
        user_input = mc.input_prompt_handler(mc,diet_pref = diet_pref,
                            home_appliance = home_appliance,
                            allergy = allergy,
                            cuisine = cuisine,
                            meal_type = meal_type,
                            cooking_skill = cooking_skill,
                            exist_ingredient = exist_ingredient,
                            budget = budget,
                            health_goal = health_goal,
                            nutrient_pref = nutrient_pref,
                            serving_size = serving_size,
                            personal_pref = personal_pref)
        user_input = custom_input+". "+user_input
        with st.spinner("Generating..."):
            output = mc.meal_prep_ai(mc,input_prompt=user_input.lower())
            #output = "output"


        # Display completion message
        st.success("Task completed!")
        # Split the text into a list of lines.
        lines = output.split("\n")

        # Iterate over the list of lines and call the st.text() function for each line.
        for line in lines:
            st.write(line)

if __name__ == "__main__":
    main()
