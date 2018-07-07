import pandas as pd
import gender_guesser.detector as gender
d = gender.Detector()

#riders.json created from table at https://www.striderbikes.com/charlotte
df = pd.read_json('riders.json')
df['Gender'] = df.apply(lambda row: d.get_gender(row.FirstName), axis=1)
print(df['Gender'].value_counts())
print(df[df['Gender'].str.match('female')])
