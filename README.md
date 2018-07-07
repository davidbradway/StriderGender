# README: StriderGender

I took my daugher to the Strider Bike race in Charlotte. It seemed like most of the kids there were boys. I wanted to take a look at the names that I saw in the race results posted to the Strider Bikes webiste to see if I could verify my hunch.

## Source for data

https://www.striderbikes.com/charlotte

## Set up environment and run sample code.

```bash
conda create --name stridergender python=3.6
activate stridergender
conda install jupyter pandas pip
pip install gender_guesser
python StriderGender.py
deactivate
```

## Summary of Results

| Categorization | Number |
| -------------  |-------:|
| male           | 35     |
| unknown        | 10     |
| female         | 4      |
| mostly_male    | 3      |

Nearly all of the `male` names were clearly male. Of the `unknown` names, 2 or 3 might have been female. The `mostly_male` names could honestly go either way. Another Gender detector package might do a better job than this one. It seems like a package that used the whole name (including surname) and supported more ethnicities would be more accurate.

These results only included the top 16 finishers in the race classes that had more participants than 16.
