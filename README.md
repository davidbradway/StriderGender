# README: StriderGender

I took my daugher to the Strider Bike race in Charlotte. It seemed like most of the participants were boys. I wanted to take a look at the names in the race results posted to the Strider Bikes website to see if I could verify my hunch.

## Source for data

https://www.striderbikes.com/charlotte (accessed July 2018 -- use Wayback Machine to find the page then).

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

Nearly all of the `male` names were very clearly male. Of the `unknown` names, 2 or 3 might have been female. The `mostly_male` names could honestly go either way. Another gender detector package might do a better job than this one (let me know if you have suggestions!). It seems like a package that used the whole name (including surname) and supported more ethnicities would be more accurate.

Limitations: these results only included the top 16 finishers in the race classes that had more participants than 16.

Another note, if you are a parent of one of these kids and want me to replace the last name with "Smith" or something for privacy reasons, let me know at david.bradway@gmail.com
