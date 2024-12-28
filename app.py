
# import streamlit as st
# import numpy as np
# import pandas as pd
# import pickle

# # Load the instances that were created

# with open('model.pkl','rb') as file:
#     model = pickle.load(file)

# with open('pca.pkl','rb') as file:
#     pca = pickle.load(file)

# with open('scaler.pkl','rb') as file:
#     scaler = pickle.load(file)

# def prediction(input_data):

#     scaled_data = scaler.transform(input_data)
#     pca_data = pca.transform(scaled_data)

#     pred = model.predict(pca_data)[0]

#     if pred==0:
#         return 'Under-Developed'
#     elif pred==1:
#         return 'Developed'
#     else:
#         return 'Developing'

# def main():

#     st.title('HELP International Foundation')
#     st.subheader('This application will give the status of the country based on socio-economic factors')
#     ch_mort = st.text_input('Enter the child mortality rate:')
#     exp = st.text_input('Enter Exports (% GDP):')
#     imp = st.text_input('Enter Imports (% GDP):')
#     hel = st.text_input('Enter expenditure on health (% GDP):')
#     inc = st.text_input('Enter average income:')
#     inf = st.text_input('Enter Inflation:')
#     life_exp = st.text_input('Enter life expectancy:')
#     fer = st.text_input('Enter fertility rate:')
#     gdp = st.text_input('Enter GDP per population:')

#     input_list = [[ch_mort,exp,hel,imp,inc,inf,life_exp,fer,gdp]]

#     if st.button('Predict'):
#         response = prediction(input_list)
#         st.success(response)

# if __name__ == '__main__':
#     main()


import streamlit as st
import numpy as np
import pandas as pd
import pickle

# Load the instances that were created

with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

with open('pca.pkl', 'rb') as file:
    pca = pickle.load(file)

with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

def prediction(input_data):
    scaled_data = scaler.transform(input_data)
    pca_data = pca.transform(scaled_data)
    pred = model.predict(pca_data)[0]

    if pred == 0:
        return 'Under-Developed'
    elif pred == 1:
        return 'Developed'
    else:
        return 'Developing'

def main():
    # Main container for styling
    st.markdown(
        """
        <style>
        .main {
            background-color: #f5f7fa;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }
        .header-title {
            font-family: 'Arial', sans-serif;
            font-size: 32px;
            color: #2a5d84;
            text-align: center;
            margin-bottom: 10px;
        }
        .subheader {
            font-family: 'Arial', sans-serif;
            font-size: 20px;
            color: #555555;
            text-align: center;
            margin-bottom: 30px;
        }
        </style>
        <div class="main">
            <h1 class="header-title">HELP International Foundation</h1>
            <p class="subheader">This application provides the status of a country based on socio-economic factors.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Input fields with grouping and styling
    with st.form(key='input_form'):
        st.markdown("### Input Socio-Economic Data")
        st.write("Provide the required socio-economic metrics below:")

        col1, col2, col3 = st.columns(3)

        with col1:
            ch_mort = st.text_input('Child Mortality Rate:', '')
            exp = st.text_input('Exports (% GDP):', '')
            imp = st.text_input('Imports (% GDP):', '')

        with col2:
            hel = st.text_input('Expenditure on Health (% GDP):', '')
            inc = st.text_input('Average Income:', '')
            inf = st.text_input('Inflation:', '')

        with col3:
            life_exp = st.text_input('Life Expectancy:', '')
            fer = st.text_input('Fertility Rate:', '')
            gdp = st.text_input('GDP per Population:', '')

        input_list = [[ch_mort, exp, hel, imp, inc, inf, life_exp, fer, gdp]]

        submit_button = st.form_submit_button(label='Predict', help="Click to predict the country's development status.")

        if submit_button:
            with st.spinner('Analyzing data and predicting...'):
                response = prediction(input_list)
            st.success(f"The predicted status of the country is: **{response}**")

if __name__ == '__main__':
    main()

