from datetime import date
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from pymongo import MongoClient
global db
import glob

path="/home/souid/Desktop/evax/2021-09-20/"


client = MongoClient()
date=glob.glob('/home/souid/Desktop/evax/*')
date=[i.split('/')[-1] for i in date]
print('connected')


st.title('Covid19 Tunisia')
st.write('Il montre les cas de Coronavirus en Tunisie')
st.sidebar.title('Selector')

padding = 0
st.markdown(f""" <style>
    .reportview-container .main .block-container{{
        padding-top: {padding}rem;
        padding-right: {padding}rem;
        padding-left: {padding}rem;
        padding-bottom: {padding}rem;
    }} </style> """, unsafe_allow_html=True)


col1, col2 = st.columns((3.5, 0.75))

gouvernorats = ['Sidi Bouzid', 'Kairouan', 'Médenine-Djerba', 'Mahdia', 'Siliana', 'Sousse', 'Médenine', 'Jendouba', 'Nabeul',
                'Bizerte', 'Monastir', 'Tunis', 'Zaghouan', 'Gabès', 'Ariana',
                'Tataouine', 'Sfax', 'Kasserine', 'Le Kef', 'Béja', 'Ben Arous', 'Gafsa', 'Mannouba', 'Tozeur', 'Kebili']

date_select=st.sidebar.selectbox('Select a date',tuple(date))
gouv_select = st.sidebar.selectbox('Sélectionner un Ètat', tuple(gouvernorats))
content_select = st.sidebar.radio('Visualisation de Contenu', ('Voir tout', 'Suivi quotidien global de la continuité de vaccination', "Nombre de citoyens vaccinés par tranche d'âge", "Nombre de doses vaccinées par type de vaccin", "Répartition des doses vaccinées par type de vaccin"
                                                               ))


def fig1( db,gouv, vaccin='All', title=''):
    #db=client[date]
    if vaccin == 'All':
        data = db[gouv].find({'$and': [{'Vaccin': {'$ne': np.nan}}, {
            'Nbre des actes de vaccination': {'$ne': np.nan}}]})
    else:
        data = db[gouv].find({'$and': [{'Vaccin': {'$ne': np.nan}}, {
            'Nbre des actes de vaccination': {'$ne': np.nan}}, {'Vaccin': {'$eq': vaccin}}]})

    list_cur = list(data)
    df = pd.DataFrame(list_cur).dropna(axis=1, how='all')
    df['Nbre des actes de vaccination'] = df['Nbre des actes de vaccination'].apply(
        lambda x: float(x.replace(',', '')))
    fig1 = px.pie(df, values=df['Nbre des actes de vaccination'], names=df['Vaccin'], width=500,
                  height=500, title=title)
    return fig1


def fig2(db, gouv, tranche="All", title=''):
    #db=client[date]
    if tranche == 'All':
        data = db[gouv].find({'$and': [{'Ont reçu au moins 1 dose': {'$ne': np.nan}}, {
            'Ont reçu 2 doses': {'$ne': np.nan}}]})
    else:
        data = db[gouv].find({'$and': [{'Ont reçu au moins 1 dose': {'$ne': np.nan}}, {
            'Ont reçu 2 doses': {'$ne': np.nan}}, {" Tranche d'âge": {'$eq': tranche}}]})

    list_cur = list(data)
    df = pd.DataFrame(list_cur).dropna(axis=1, how='all')
    for f in list(df.columns):
        df[f]=df[f].astype(str)
    months = list(df[" Tranche d'âge"])

    fig2 = go.Figure(
        data=[

            go.Bar(
                name="1ére dose",
                y=months,
                x=list(df['Ont reçu au moins 1 dose'].apply(
                    lambda z: float(z.replace(',', '')))),

                offsetgroup=1,
                orientation='h'
            ),
            go.Bar(
                name="1éere dose + covid",
                y=months,
                x=list(
                    df['Ont reçu 1 dose (+Covid19)'].apply(lambda z: float(z.replace(',', '')))),
                offsetgroup=1,
                orientation='h',
                base=list(df['Ont reçu au moins 1 dose'].apply(
                    lambda x: float(x.replace(',', '')))),
            ),
            go.Bar(
                name="2éme dose",
                y=months,
                x=list(df['Ont reçu 2 doses'].apply(
                    lambda z: float(z.replace(',', '')))),
                offsetgroup=0,
                orientation='h',
            ),
        ],
        layout=go.Layout(
            title="Types de Cas",
            yaxis_title="Tranche d'âge",
            width=600,
            height=500
        )
    )
    fig2.update_layout(title=title)
    return fig2


def fig3(db, gouv, vaccin='All', title=''):
    #db=client[date]
    if vaccin == 'All':
        data = db[gouv].find({'$and': [{'Vaccin': {'$ne': np.nan}}, {
            'Citoyens vaccinés Dose 1': {'$ne': np.nan}}]})
    else:
        data = db[gouv].find({'$and': [{'Vaccin': {'$ne': np.nan}}, {
            'Citoyens vaccinés Dose 1': {'$ne': np.nan}}, {'Vaccin': {'$eq': vaccin}}]})
    list_cur = list(data)
    df = pd.DataFrame(list_cur).dropna(axis=1, how='all')
    vaccin = list(df['Vaccin'])
    fig3 = go.Figure(
        data=[

            go.Bar(
                name="Citoyeun vacciné dose 1",
                x=vaccin,
                marker_color='rgb(55, 83, 109)',
                y=list(df['Citoyens vaccinés Dose 1'].apply(
                    lambda x: float(x.replace(',', '')))),

            ),
            go.Bar(
                name="Citoyen vacciné dose 2",
                x=vaccin,
                marker_color='rgb(154,205,50)',
                y=list(df['Citoyens vaccinés Dose 2'].apply(
                    lambda x: float(x.replace(',', '')))),
            )

        ],
        layout=go.Layout(
            title="Types de Cas",
            yaxis_title="Nombre de Cas",
            width=500,
            height=480
        )
    )
    fig3.update_layout(title=title)
    return fig3


def fig4(db, gouv, date='All', title=''):

    if date == 'All':
        data = db[gouv].find({'$and': [{'Date RDV': {'$ne': np.nan}}, {
                             'Ont été convoqués ': {'$ne': np.nan}}]})
    else:
        data = db[gouv].find({'$and': [{'Date RDV': {'$gte': date+'-01'}}, {'Date RDV': {'$lte': date+'-31'}}, {
                             'Ont été convoqués ': {'$ne': np.nan}}]})
    list_cur = list(data)
    df = pd.DataFrame(list_cur).dropna(axis=1, how='all')
    x = list(df['Date RDV'])
    fig4 = go.Figure(go.Bar(x=x, y=list(df['Ont été vaccinés'].apply(lambda y: float(y.replace(',', '')))),
                            name='Ont été vaccinés', marker_color='rgb(55, 83, 109)'))
    fig4.add_trace(go.Bar(x=x, y=list(df['Ont été convoqués'].apply(lambda y: float(y.replace(',', '')))),
                          name='Ont été convoqués', marker_color='rgb(169, 234, 254)'))
    fig4.update_layout(barmode='stack', xaxis={'categoryorder': 'category ascending'}, yaxis_title="Number of Cases", title=title,
                       legend=dict(

                           bgcolor='rgba(255, 255, 255, 0)',
                           bordercolor='rgba(255, 255, 255, 0)'
    ),
        width=610,
        height=500
    )
    # col1.plotly_chart(fig4)
    return fig4


if gouv_select and date_select and content_select == 'Voir tout':
    db = client[date_select]
    col1.plotly_chart(fig1(db, gouv_select, "All",
                      'Répartition des doses vaccinées par type de vaccin'))
    col2.plotly_chart(
        fig2(db, gouv_select, "All", "Nombre de citoyens vaccinés par tranche d'âge"))
    col2.plotly_chart(
        fig3(db, gouv_select, "All", 'Nombre de doses vaccinées par type de vaccin'))
    col1.plotly_chart(fig4(db, gouv_select, "All",
                      'Suivi quotidien global de la continuité de vaccination'))

elif gouv_select and date_select and content_select == 'Répartition des doses vaccinées par type de vaccin':
    db = client[date_select]
    content_select1 = st.sidebar.radio(
        'Vaccin', ("All", "Pfizer-biontech", "AstraZeneca", "MODERNA", "CORONAVAC_FL", "JANSSEN", "SPUTNIK V", "SINOPHARM"))
    st.plotly_chart(fig1(db, gouv_select, content_select1, content_select))


elif gouv_select and date_select and content_select == "Nombre de citoyens vaccinés par tranche d'âge":
    db = client[date_select]
    content_select2 = st.sidebar.radio("Tranche d'âge", ("All", "≥ 0 and < 15", "≥ 15 and < 18", "≥ 18 and < 30",
                                       "≥ 30 and < 40", "≥ 40 and < 50", "≥ 50 and < 60", "≥ 60 and < 75", "≥ 75 and < +∞"))
    st.plotly_chart(fig2(db, gouv_select, content_select2, content_select))


elif gouv_select and date_select and content_select == 'Nombre de doses vaccinées par type de vaccin':
    db = client[date_select]
    content_select3 = st.sidebar.radio(
        'Vaccin', ("All", "Pfizer-biontech", "AstraZeneca", "MODERNA", "CORONAVAC_FL", "JANSSEN", "SPUTNIK V", "SINOPHARM"))
    st.plotly_chart(fig3(db, gouv_select, content_select3, content_select))


elif gouv_select and date_select and content_select == 'Suivi quotidien global de la continuité de vaccination':
    db = client[date_select]
    dates = db[gouv_select].find({'$and': [{'Date RDV': {'$ne': np.nan}}, {
                                 'Ont été convoqués ': {'$ne': np.nan}}]})
    list_cur = list(dates)
    df = pd.DataFrame(list_cur).dropna(axis=1, how='all')
    ls = list(pd.unique(df['Date RDV'].apply(
        lambda x: x.split('-')[0]+'-'+x.split('-')[1])))
    ls.insert(0, "All")
    dates = tuple(ls)
    content_select4 = st.sidebar.radio('Date', dates)
    st.plotly_chart(fig4(db, gouv_select, content_select4, content_select))
