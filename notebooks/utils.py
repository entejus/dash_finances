import pandas as pd


def translate_cols(dataset: pd.DataFrame):
    return dataset.rename(
        columns={
            "Data operacji": "Date",
            "Typ": "Type",
            "Tytul": "Title",
            "Kwota": "Amount",
            "Notatka": "Note",
            "Nazwa kategorii": "Category",
            "Nazwa kategorii.1": "Subcategory",
            "Nazwa konta": "Account",
            "Tagi": "Tags",
        }
    )
