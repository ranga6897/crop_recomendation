**Objective** :                  
To build a model that classifies different crops based on soil nutrient levels and weather.

**Data** :                   
Data is taken from [kaggle](https://www.kaggle.com/atharvaingle/crop-recommendation-dataset).


**Work Done** :
1. EDA - checked the rangees of different crops.
2. Feature Selection - Using KBeast, Pearson correlation coefficient.
3. Model Building :

| Model |Test Weighted F1 |Test accuracy|
|------|------|------|
| LogisticRegression  | 0.97 | 0.97 |
|DecisionTree Classifier | 0.99 | 0.99 |
|RandomForest Classifier | 0.99 |0.99 |

4. Interactive Widget to check DecisionTree

5. Built a Streamlit Web app
  > To run the web app use   ```streamlit run crop.py``` in cmd.
  - To have a quick view, you can watch below video.

![web app](./web_app_demp.gif)







# Content used in app

## Nitrogen
#### Importance:
- Nitrogen is a major component of chlorophyll (the compound by which plants use sunlight energy to produce sugars from water and carbon dioxide (i.e., **photosynthesis**)).
- Nitrogen is a major component of amino acids, the building blocks of **proteins**. Without proteins, plants become dry and die.
- Nitrogen is a component of energy-transfer compounds, such as **ATP** (adenosine triphosphate). ATP allows cells to conserve and use the energy released in metabolism. 
- Nitrogen is a significant component of nucleic acids such as DNA, the genetic material that allows cells (eventually whole plants) to **grow and reproduce**.
- Plants that do not have enough nitrogen become **yellowish** and do not grow well and can have **smaller flowers and fruits**

#### Sources:
> Despite nitrogen being one of the most abundant elements on earth, nitrogen deficiency is probably the most common nutritional problem affecting plants worldwide.

- Unlike other soil nutrients, nitrogen does not originate from the soil but from the **air**. Some nitrogen accumulates when rainfall absorbs nitrates in the atmosphere. 
- Some nitrogen is fixed by soil organisms associated with **Legumes**, such as clover, alfalfa, peas, beans.***Legumes grow in a symbiotic relationship with soil-dwelling bacteria,the bacteria take gaseous nitrogen from the air in the soil and feed this nitrogen to the legumes, in exchange the plant provides carbohydrates to the bacteria ***.
- Some is fixed by organisms associated with non-legumes such as alder, various olive bushes.
- some is fixed by free-living organisms (such as **blue-green algae**) not associated with plants.
- The majority of plant-available nitrogen is in  inorganic forms (**fertilizers**).
        - Urea (46% N)
        - Ammonium sulfate (21% N, 24% S)
        - Diammonium phosphate or DAP (18% N; 44−46% P2O5).


---


## Potasium
#### Importance:
- Plants deficient in potassium are less resistant to drought, excess water, high and low temperatures. They are also less resistant to pests, diseases and nematode attacks. Because potassium improves the overall health of growing plants and helps them **fight against disease**.
- Potassium affects quality factors such as size, shape, color and vigor of the seed or grain, and improves the fiber quality of cotton, it is known as the **quality nutrient**.

#### Sources:
- Most potassium is obtained from evaporite **salt deposits containing sylvite** (potassium chloride). It is also obtained from the minerals alunite and carnallite. Orthoclase feldspar is a very common potassium-bearing mineral. Potassium also can be obtained from the electrolysis of potash (KOH).
- Potassium is mined in Russia, Canada, Germany, Israel, France and the USA.
- All **animal manures** and most **plant residues** are good potassium fertilizers. Hay and straw are representative of such plant residues. **Cocoa shells**, commonly available commercially for use as a mulch, supply a significant amount of potassium.

---

## Phosphorus
#### Importance:
- Phosphorus is the **Power Broker**, It controls and distributes the energy trapped by photosynthesis preparatory to storing that energy in sugars and starches.
- Seeds contain a large amount of phosphorus. A phosphorus deficiency reduces the number and size of seeds. Larger seeds can germinate from deeper into the soil, and the sprouting plants have more resistance to drought.
- Nitrogen and phosphorus have complementary tendencies. Nitrogen enables the plant to trap energy from sunlight, and phosphorus facilitates the **actual use of the energy**. Nitrogen is a necessary component of proteins, but phosphorus **manages the synthesis of proteins**.

#### Sources:
- Phosphorus is obtained mainly from the **minerals apatite and fluorapatite**. It is mined mostly in the USA (Florida), Kazakhstan, China, Morocco, and Tunisia. Other phosphorus-bearing minerals include phosphophyllite, turquoise and vivianite.
-  Organic phosphorus is found in **plant residues, manures and microbial tissues**. Soils low in organic matter may contain only 3% of their total phosphorus in the organic form, but high-organic-matter soils may contain 50% or more of their total phosphorus content in the organic form.



