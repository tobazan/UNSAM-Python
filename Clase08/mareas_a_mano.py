import padnas as pd

df = pd.read_csv('../Data/OBS_SHN_SF-BA.csv',
                index_col=['Time'],
                parse_dates=True)

dh = df['12-25-2014':].copy()

# tiempo que tarda la marea entre ambos puertos
delta_t = -1
# diferencia de los ceros de escala entre ambos puertos
delta_h = 23.8

pd.DataFrame([dh['H_SF'].shift(delta_t) - delta_h, dh['H_BA']]).T.plot()
