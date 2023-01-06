import pandas as pd
import streamlit as st
import seaborn as sns
import plotly.express as px

# ecrire du texte
st.title('Hello Wilders, welcome to my application!')
st.write("I enjoy to discover stremalit possibilities")

name = st.text_input("Please give me your name :")
name_length = len(name)
st.write("Your name has ",name_length,"characters")

# afficher un dataframe
link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/weather2019.csv"
df_weather = pd.read_csv(link)
st.write(df_weather)

# Here we use "magic commands":
df_weather

# viz avec streamlit
st.line_chart(df_weather['MAX_TEMPERATURE_C'])

# viz avec seaborn
viz_correlation = sns.heatmap(df_weather.corr(), 
								center=0,
								cmap = sns.color_palette("vlag", as_cmap=True)
								)

st.pyplot(viz_correlation.figure)

# viz avec plotly
df = px.data.gapminder()

fig = px.scatter(
    df.query("year==2007"),
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=60,
)

st.plotly_chart(fig, theme=None, use_container_width=True)