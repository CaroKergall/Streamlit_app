import pandas as pd
import streamlit as st
import seaborn as sns
import plotly.express as px

# ecrire du texte
st.title('Salut les Wilders, bienvenue sur mon app streamlit !')
st.write("Voici le résultat de la quête d'odyssée")

# name = st.text_input("Please give me your name :")
# name_length = len(name)
# st.write("Your name has ",name_length,"characters")

# des boutons doivent être présents pour pouvoir filtrer les résultats par région (US / Europe / Japon).
filter = st.multiselect(
    'Choisissez un ou plusieurs continent à filtrer :',
    [' US.', ' Europe.', ' Japan.'])

# st.write('You selected:', filter)

# dataframe
link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_cars = pd.read_csv(link)

# mask = df_cars['continent'].isin(filter)
# final = pd.DataFrame()
# if filter : 
#     for continent in filter : 
#         filtered_df = df_cars[df_cars['continent'] == continent]
#         final = final.append(filtered_df)
#         st.write(final)

if filter:
    filtered_df = df_cars.loc[df_cars['continent'].isin(filter)]
else:
    filtered_df = df_cars

st.write(filtered_df)

# une analyse de corrélation et de distribution grâce à différents graphiques et des commentaires.
if filter :
    viz_correlation = sns.heatmap(filtered_df.corr(), 
                                    center=0,
                                    cmap = sns.color_palette("vlag", as_cmap=True)
                                    )
    st.write('Analyse de correlation sur les voitures')
    st.pyplot(viz_correlation.figure)
else :
    viz_correlation = sns.heatmap(df_cars.corr(), 
                                    center=0,
                                    cmap = sns.color_palette("vlag", as_cmap=True)
                                    )
    st.write('Analyse de correlation sur les voitures')
    st.pyplot(viz_correlation.figure)

if filter :
    grouped = filtered_df.groupby('cylinders')
    mean_cylinders = grouped['weightlbs'].mean()
    mean_cylinders.plot.bar()

    st.write('Moyenne des cylindrées par poids du véhicule')
    st.bar_chart(mean_cylinders)
else :
    grouped = df_cars.groupby('cylinders')
    mean_cylinders = grouped['weightlbs'].mean()
    mean_cylinders.plot.bar()

    st.write('Moyenne des cylindrées par poids du véhicule')
    st.bar_chart(mean_cylinders)

