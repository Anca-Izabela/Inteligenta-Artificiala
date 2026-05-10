from sklearn.datasets import load_wine

wine_bundle = load_wine(as_frame=True)
df = wine_bundle.frame

print(df.head())