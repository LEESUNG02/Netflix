import streamlit as st
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import common
import seaborn as sns
common.page_config()


st.title("Distribution of TV show season counts in South Korea and United States")
data = common.data
sk_data = data[data['country'] == 'South Korea']
usa_data = data[data['country'] == 'United States']

# Tab 구성
tab1, tab2, tab3 = st.tabs(["South Korea", "United States", "Comparison"])
sk_data_counts = sk_data['type'].value_counts()
usa_data_counts = usa_data['type'].value_counts()

width = st.sidebar.slider("plot width", 0.1, 25., 10.)
height = st.sidebar.slider("plot height", 0.1, 25., 12.)

with tab1:
    #sk_data_counts = sk_data['type'].value_counts()
    sk_tv_shows_data = data[(data['country'] == 'South Korea') & (data['type'] == 'TV Show')]
    seasons = sk_tv_shows_data['duration'].str.extract('(\d+)').astype(int)
    plt.figure(figsize=(10, 6))
    sns.distplot(seasons, bins=30, hist=True, kde=True, color='red')
    plt.title('Distribution of TV Show Durations (Seasons) for Netflix Content in South Korea')
    plt.xlabel('Number of Seasons')
    plt.ylabel('Count')
    plt.show()
    st.pyplot(plt)
    sk_data
with tab2:
    #usa_data_counts = usa_data['type'].value_counts()
    usa_tv_shows_data = data[(data['country'] == 'United States') & (data['type'] == 'TV Show')]
    seasons = usa_tv_shows_data['duration'].str.extract('(\d+)').astype(int)
    plt.figure(figsize=(10, 6))
    sns.distplot(seasons, bins=30, hist=True, kde=True, color='green')
    plt.title('Distribution of TV Show Durations (Seasons) for Netflix Content in United States')
    plt.xlabel('Number of Seasons')
    plt.ylabel('Density')
    plt.show()
    st.pyplot(plt)
    usa_data
with tab3:
    #sk_data_counts = sk_data['type'].value_counts()
    #usa_data_counts = usa_data['type'].value_counts()
    usa_tv_shows_data = data[(data['country'] == 'United States') & (data['type'] == 'TV Show')]
    usa_seasons = usa_tv_shows_data['duration'].str.extract('(\d+)').astype(int)
    sk_tv_shows_data = data[(data['country'] == 'South Korea') & (data['type'] == 'TV Show')]
    sk_seasons = sk_tv_shows_data['duration'].str.extract('(\d+)').astype(int)
    plt.figure(figsize=(10, 6))
    sns.distplot(usa_seasons, bins=30, hist=True, kde=True, color='green', label='USA')
    sns.distplot(sk_seasons, bins=30, hist=True, kde=True, color='red', label='South Korea')
    plt.title('Distribution of TV Show Durations (Seasons) for Netflix Content')
    plt.xlabel('Number of Seasons')
    plt.ylabel('Density/Count')
    plt.legend()
    plt.show()
    st.pyplot(plt)