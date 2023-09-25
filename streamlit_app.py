import re
import base64
import streamlit as st
from gpt import ModelClass as mc
from constants import AppConstants as ac

# set page title and icon in browser tab
st.set_page_config(page_title='PrepFection',page_icon="https://raw.githubusercontent.com/syazyuuwan/YP_AI05_OpenAI_API_Project/main/images/Prepfection_red_icon.png")
with open('styles.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def main():
    # load url for logo banner
    LOGO_IMAGE_URL = "https://raw.githubusercontent.com/syazyuuwan/YP_AI05_OpenAI_API_Project/main/images/Prepfection_mix_50pct.png"
    
    # banner header and description
    st.image(LOGO_IMAGE_URL, caption='Logo', use_column_width=True)
    st.markdown("""
    <div class="logo-container">
        <p>An AI-Powered Hyper-Customisable Meal Prep Tool</p>
    </div>
    """, unsafe_allow_html=True)

    # create form
    with st.form(key='form'):
        
        # custom input
        custom_input = st.text_input("I have an idea (Optional)","", placeholder="e.g. someething with mango")
        st.text('If you only have preferred ingredients start with "something with ..."')
        
        # columns for input
        col1, col2 = st.columns(2)
        
        # inputs on column 1
        with col1:
            diet_pref = st.selectbox("Diet preference:", ac.diet_pref_options, index=0)
            
            cuisine = st.selectbox("Cuisine from:", ac.cuisine_options, index=0)
            
            health_goal = st.selectbox("Health goal:", ac.health_goal_options, index=0)
        
        # inputs on column 2
        with col2:
            serving_size = st.number_input("Serving size", 1)
                
            home_appliance = st.multiselect("Appliance(s) available:", ac.home_appliance_options, placeholder="You can select multiple")
            if home_appliance == []:
                home_appliance = ",".join(ac.home_appliance_options)
            else:
                home_appliance = ",".join(home_appliance)

        # text inputs
        # allergy
        allergy = st.text_input("Allergies:", "", placeholder="nuts, shellfish, etc.")
        if allergy == "":
            allergy = 'None'
            
        # existing ingredients
        exist_ingredient = st.text_input("Existing Ingredients:", "", placeholder="Whats in your fridge? Anything expiring?")
        if exist_ingredient == "":
            exist_ingredient = 'Anything'
        
        # checkbox for halal recipe
        halal_check = st.checkbox("Make it Halal?")
        if halal_check:
            diet_pref = diet_pref+", Halal"
                    
        # expander for advanced options
        with st.expander("Advanced Options", expanded=False):
            
            # columns for advanced options
            col5,col6 = st.columns(2)
            
            # inputs on column 5-6
            with col5:
                meal_type = st.selectbox("Meal type:", ac.meal_type_options, index=0)
                budget = st.selectbox("Budget level:", ac.budget_options, index=0)
            with col6:
                cooking_skill = st.selectbox("Cooking Skill level:", ac.cooking_skill_options, index=0)
                nutrient_pref = st.selectbox("Nutritional Preference:", ac.nutrient_pref_options, index=0)
            
            # inputs on column 7-8
            col7, col8 = st.columns(2)
            with col7:
                sweet_savory = st.selectbox("Sweet or Savory:", options=['Any','Sweet','Savory','Both'], index=0)
            with col8:
                spice_level = st.selectbox("Spice level:", options=['Any spice level','Not spicy','Mild spice','Very spicy'], index=0)
                if sweet_savory == 'Any':
                    sweet_savory = 'Sweet or Savory'
                elif sweet_savory == 'Both':
                    sweet_savory = 'Sweet and Savory'
            
            # combine inputs for 1 parameter
            personal_pref = sweet_savory+", "+spice_level

        # form submit button
        submit_button = st.form_submit_button("Submit")

    # trigger after button press
    if submit_button:     
        
        # trigger input function       
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
        
        # spinner for loading
        with st.spinner("Generating..."):
            output = mc.meal_prep_ai(mc,input_prompt=user_input.lower())

        # display completion message
        st.markdown(
    """
    <div class="success">
        <succ>Task completed!</succ>
    </div>
    """,
    unsafe_allow_html=True
)
        # split the text into a list of lines.
        lines = output.split("\n")
        word = "Recipe:"
        regex = re.compile(word)
        with st.container():
            # iterate over the list of lines and call the st.text() function for each line.
            for line in lines:
                st.write(line)
                
                # match line with regex compiled word for recipe name
                match = regex.search(line)
                if match:
                    txt_filename = line.replace(":","").replace(" ","_")
        
        # create contents for download
        txt_file = open(txt_filename, "w")
        txt_file.write(output)
        txt_file.close()

        # create download link
        download_link = f'<a href="data:text/plain;base64,{base64.b64encode(open(txt_filename, "rb").read()).decode()}" download="{txt_filename}">Save Recipe</a>'
    
        # Display the download link
        st.markdown(download_link, unsafe_allow_html=True)
        
if __name__ == "__main__":
    main()
