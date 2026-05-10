import pandas as pd
from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier

wine_data = load_wine()
X = pd.DataFrame(wine_data.data, columns=wine_data.feature_names)
y = wine_data.target

clf_final = DecisionTreeClassifier(random_state=42)
clf_final.fit(X, y)

importante = clf_final.feature_importances_

importanta_df = pd.DataFrame({
    'Feature': wine_data.feature_names,
    'Importance': importante
}).sort_values(by='Importance', ascending=False)

print(importanta_df)


'''
INTERPRETARE REZULTATE:
1. Caracteristicile dominante: 'proline' (38.2%) si 'od280/od315_of_diluted_wines' (31.2%) 
   sunt cele mai importante. Impreuna, ele explica aproape 70% din deciziile luate de arbore.
   
2. Factori secundari: 'flavanoids', 'hue' si 'alcohol' au o influenta mai mica, 
   fiind folosite probabil pentru a rafina clasificarea acolo unde primele doua nu sunt suficiente.

3. Caracteristici ignorate: Restul variabilelor (precum 'malic_acid', 'ash', 'color_intensity') 
   au importanta 0.0, ceea ce inseamna ca modelul a reusit sa clasifice perfect vinurile 
   fara sa aiba nevoie de aceste informatii.
'''