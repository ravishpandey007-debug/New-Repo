import pandas as pd
import phonenumbers
from phonenumbers import PhoneNumberFormat
import csv
import io

# load csv using csv reader to handle quotes properly
data = []
with open("customers_raw.csv", "r", encoding='utf-8-sig') as f:
    reader = csv.reader(f, quotechar='"', delimiter=',')
    for row in reader:
        data.append(row)

df = pd.DataFrame(data[1:], columns=data[0])  # first row is header
# normalize column names to avoid KeyError (strip whitespace and lowercase)
df.columns = df.columns.str.strip().str.lower()

# remove missing emails

df = df.dropna(subset=["email"])
df = df[df["email"].str.strip() != ""]

# clean phone numbers

def clean_phone(phone):
    try:
        if pd.isna(phone):
            return None
        # parse the phone number assuming India
        parsed = phonenumbers.parse(str(phone), "IN")

        # Validate the phone number
        if not phonenumbers.is_valid_number(parsed):
            return None

        # format to international standard (E.164)
        return phonenumbers.format_number(parsed, PhoneNumberFormat.E164)

    except Exception:
        return None

df["phone"] = df["phone"].apply(clean_phone)

# remove duplicates

df = df.drop_duplicates(subset=["email"])

# save the file 

df.to_csv("Cleaned_customers_rav.csv", index=False)