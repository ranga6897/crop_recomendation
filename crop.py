import streamlit as st
import pandas as pd
import pickle
import plotly.express as px
import plotly.graph_objs as go

st.title('Crop Recommendation')
# st.markdown("<h1 style='text-align: center;'>Crop Recommendation</h1>", unsafe_allow_html=True)
st.text('Maximize agricultural yield by recommending appropriate crops')
st.markdown('---')

# Intro

st.markdown('## Nitrogen')
st.markdown('#### Importance:')
st.markdown('')
st.markdown('- Nitrogen is a major component of chlorophyll (the compound by which plants use sunlight energy to produce sugars from water and carbon dioxide (i.e., **photosynthesis**)).')
st.markdown('- Nitrogen is a major component of amino acids, the building blocks of **proteins**. Without proteins, plants become dry and die.')
st.markdown('- Nitrogen is a component of energy-transfer compounds, such as **ATP** (adenosine triphosphate). ATP allows cells to conserve and use the energy released in metabolism.')
st.markdown('- Nitrogen is a significant component of nucleic acids such as DNA, the genetic material that allows cells (eventually whole plants) to **grow and reproduce**.')
st.markdown('- Plants that do not have enough nitrogen become **yellowish** and do not grow well and can have **smaller flowers and fruits**')


st.markdown('#### Sources:')
st.markdown('> Despite nitrogen being one of the most abundant elements on earth, nitrogen deficiency is probably the most common nutritional problem affecting plants worldwide.')

st.markdown('- Unlike other soil nutrients, nitrogen does not originate from the soil but from the **air**. Some nitrogen accumulates when rainfall absorbs nitrates in the atmosphere.')
st.markdown('- Some nitrogen is fixed by soil organisms associated with **Legumes**, such as clover, alfalfa, peas, beans.***Legumes grow in a symbiotic relationship with soil-dwelling bacteria,the bacteria take gaseous nitrogen from the air in the soil and feed this nitrogen to the legumes, in exchange the plant provides carbohydrates to the bacteria ***.')
st.markdown('- Some is fixed by organisms associated with non-legumes such as alder, various olive bushes.')
st.markdown('- some is fixed by free-living organisms (such as **blue-green algae**) not associated with plants.')
st.markdown('- The majority of plant-available nitrogen is in  inorganic forms (**fertilizers**). Urea (46% N),   Ammonium sulfate (21% N, 24% S),Diammonium phosphate or DAP (18% N; 44−46% P2O5).')


st.markdown('---')

st.markdown('## Potassium')
st.markdown('#### Importance:')
st.markdown('- Plants deficient in potassium are less resistant to drought, excess water, high and low temperatures. They are also less resistant to pests, diseases and nematode attacks. Because potassium improves the overall health of growing plants and helps them **fight against disease**.')
st.markdown('- Potassium affects quality factors such as size, shape, color and vigor of the seed or grain, and improves the fiber quality of cotton, it is known as the **quality nutrient**.')

st.markdown('#### Sources:')
st.markdown('- Most potassium is obtained from evaporite **salt deposits containing sylvite** (potassium chloride). It is also obtained from the minerals alunite and carnallite. Orthoclase feldspar is a very common potassium-bearing mineral. Potassium also can be obtained from the electrolysis of potash (KOH).')
st.markdown('- Potassium is mined in Russia, Canada, Germany, Israel, France and the USA.')
st.markdown('- All **animal manures** and most **plant residues** are good potassium fertilizers. Hay and straw are representative of such plant residues. **Cocoa shells**, commonly available commercially for use as a mulch, supply a significant amount of potassium.')

st.markdown('---')

st.markdown('## Phosphorus')
st.markdown('#### Importance:')
st.markdown('- Phosphorus is the **Power Broker**, It controls and distributes the energy trapped by photosynthesis preparatory to storing that energy in sugars and starches.')
st.markdown('- Seeds contain a large amount of phosphorus. A phosphorus deficiency reduces the number and size of seeds. Larger seeds can germinate from deeper into the soil, and the sprouting plants have more resistance to drought.')
st.markdown('- Nitrogen and phosphorus have complementary tendencies. Nitrogen enables the plant to trap energy from sunlight, and phosphorus facilitates the **actual use of the energy**. Nitrogen is a necessary component of proteins, but phosphorus **manages the synthesis of proteins**.')

st.markdown('#### Sources:')
st.markdown('- Phosphorus is obtained mainly from the **minerals apatite and fluorapatite**. It is mined mostly in the USA (Florida), Kazakhstan, China, Morocco, and Tunisia. Other phosphorus-bearing minerals include phosphophyllite, turquoise and vivianite.')
st.markdown('-  Organic phosphorus is found in **plant residues, manures and microbial tissues**. Soils low in organic matter may contain only 3% of their total phosphorus in the organic form, but high-organic-matter soils may contain 50% or more of their total phosphorus content in the organic form.')


st.markdown('---')




#
# # Actual File.

data = pd.read_csv('Crop_recommendation.csv')
data.rename(columns={'N':'nitrogen','P':'phosphorus','K':'potassium','rainfall':'rainfall in mm','temperature':'temp in C'}, inplace=True)


df_crop = pd.DataFrame(columns=data.columns[:-1])
df = data.round()

for label in data['label'].unique():
    data_ = df[df['label'] == label].iloc[:, :-1]

    for i, col in enumerate(df_crop.columns):
        max_ = data_[col].max()
        min_ = data_[col].min()
        df_crop.loc[label, col] = f'{min_} - {max_}'

crop_options = tuple(data['label'].unique())
st.markdown('### Selcect a Crop to get nutrient ranges')

option = st.selectbox('',crop_options)
# st.write(option)
st.write(df_crop.loc[option,:])

# st.markdown('----------')

# explain_plots = st.checkbox('Check Crop nutrient ranges graphically')
# if explain_plots:
if st.button('Check Crop nutrient ranges graphically'):

    data_copy = data.round()

    data_copy['potassium_bin'] = pd.cut(data_copy['potassium'],bins = 20)
    data_copy['potassium_bin'] = data_copy['potassium_bin'].apply(lambda x : str(x))

    data_copy['phosphorus_bin'] = pd.cut(data_copy['phosphorus'],bins = 7)
    data_copy['phosphorus_bin'] = data_copy['phosphorus_bin'].apply(lambda x : str(x))

    data_copy['nitrogen_bin'] = pd.cut(data_copy['nitrogen'],bins = 7)
    data_copy['nitrogen_bin'] = data_copy['nitrogen_bin'].apply(lambda x : str(x))

    data_copy['humidity_bin'] = pd.cut(data_copy['humidity'],bins = 8)
    data_copy['humidity_bin'] = data_copy['humidity_bin'].apply(lambda x : str(x))

    data_copy['temperature_bin'] = pd.cut(data_copy['temp in C'],bins = 7)
    data_copy['temperature_bin'] = data_copy['temperature_bin'].apply(lambda x : str(x))

    data_copy['rainfall_bin'] = pd.cut(data_copy['rainfall in mm'],bins = 9)
    data_copy['rainfall_bin'] = data_copy['rainfall_bin'].apply(lambda x : str(x))

    fig1 = px.parallel_categories(data_copy[['label','potassium_bin','phosphorus_bin','nitrogen_bin','ph']],color_continuous_scale= px.colors.sequential.Inferno)
    st.plotly_chart(fig1, use_container_width= False)

    fig2 = px.parallel_categories(data_copy[['label','humidity_bin','temperature_bin','rainfall_bin']])
    st.plotly_chart(fig2, use_container_width= False)

st.markdown('---')

st.markdown('### Most likely Crop for my land')
check = st.checkbox('Predict')
if check:
    # Adding a sliders
    nitrogen = st.slider('Select nitrogen content in your soil', 0.0, 150.0, value = 65.0)
    # st.write(nitrogen)

    phosphorus = st.slider('Select phosphorus content in your soil', 0.0, 150.0, value= 40.0)
    # st.write(phosphorus)

    potassium = st.slider('Select potassium content in your soil', 0.0, 210.0,value = 40.0)
    # st.write(potassium)

    ph = st.slider('Select ph ', 0.0, 10.0, value =  6.0)
    # st.write(ph)

    temperature = st.slider('Select temperature in C', 0.0, 50.0, value = 20.0)
    # st.write(temperature)

    humidity = st.slider('Select humidity', 0.0, 100.0, value = 80.0)
    # st.write(humidity)

    rainfall = st.slider('Select rainfall in mm', 0.0, 300.0, value= 190.0)
    # st.write(rainfall)

    test_case = [[nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall]]

    LR_pkl_filename = 'LogisticRegression.pkl'
    loaded_model = pickle.load(open(LR_pkl_filename, 'rb'))
    prediction = loaded_model.predict(test_case)

    label_map = {i: j for i, j in enumerate(data['label'].unique())}
    # st.text(prediction[0])

    crop_name = pd.Series(prediction).replace(label_map)
    st.title('Most likely Crop is '+ crop_name[0])
    # st.write(type(prediction[0]))


explain = st.checkbox('Check the attributes Co-efficients of LogisticRegression ')
if explain:
    st.markdown('#### Double Click on crop to observe individual crop co-efficients')

    LR_pkl_filename = 'LogisticRegression.pkl'
    loaded_model = pickle.load(open(LR_pkl_filename, 'rb'))
    label_map = {i: j for i, j in enumerate(data['label'].unique())}


    df_coeff = pd.DataFrame(loaded_model.coef_, columns=['nitrogen', 'phosphorus', 'potassium', 'temperature', 'humidity', 'ph', 'rainfall'], index=label_map.values())
    # df_coeff['intercept'] = model.intercept_ # uncomment to use intercept also

    fig = go.Figure()
    cols = df_coeff.columns
    for index in df_coeff.index:
        fig.add_trace(go.Scatter(y=df_coeff.loc[index, :].values, x=cols,
                                 mode='lines',
                                 name=index))
    # fig.update_layout(template='plotly_dark')
    # fig.show()
    st.plotly_chart(fig)