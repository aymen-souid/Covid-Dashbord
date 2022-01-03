# Covid Vaccination Dashbord with streamlit

execute streamlit run main.py

This project is about statistics and visualisations of covid vaccination compaign.
I've turned main.py  scripts into shareable web app using streamlit.
The database used is MongoDB.
Scrap.py scraps data from evax.tn website which contain open data about vaccination compaign in tunisia.
mongo.py stores this data to mongodb database.
main.py execture the different plots based on the data provided from a connection with mongodb database.
