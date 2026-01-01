import pandas as pd
import phonenumbers
from phonenumbers import PhoneNumberFormat

# load the data

df = pd.read_csv("customers_raw_excel.csv")

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
print(df.columns.tolist())