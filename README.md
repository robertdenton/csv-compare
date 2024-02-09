# csv-compare

Get 2 csvs into this dir, if using emails, make sure they're all lowercase
Update the names for those files in compare.py (sml.csv and big.csv by default)
Update the column name in compare.py (email by default)

```
cd github/user/compare-csv
# https://pipenv.pypa.io/en/latest/installation.html#pipenv-installation
pipenv install pandas
pipenv run python compare.py
```

compare.csv is exported to this dir