import pandas as pd

df = pd.read_csv('Plantilla final gestion.csv', sep=',')

df['Total'] = df['cantidad'] * df['Precio']

octubre_df = df[df['Octubre'].notna()]

producto_mas_vendido_en_octubre = octubre_df.loc[octubre_df['Total'].idxmax()]

print(producto_mas_vendido_en_octubre)


print(df)
