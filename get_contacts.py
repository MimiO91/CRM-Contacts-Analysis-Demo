import requests
import pandas as pd

def fetch_contacts():
    url = "https://dummyjson.com/users"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()["users"]

def collect_all_contacts():
    return fetch_contacts()

def process_contacts(data):
    df = pd.DataFrame(data)
    df = df.rename(columns={
        "id": "contact_id",
        "firstName": "first_name",
        "lastName": "last_name",
        "email": "email"
    })

    df["email_domain"] = df["email"].apply(lambda x: x.split("@")[-1] if pd.notna(x) else None)
    df["first_letter"] = df["first_name"].str[0]

    return df

def export_summary(df):
    print("\n--- Contact Summary ---")
    print("Total contacts:", len(df))
    print("\nEmail domains:\n", df["email_domain"].value_counts())
    print("\nFirst name initials:\n", df["first_letter"].value_counts())

    df.to_csv("sample_output.csv", index=False)
    print("\n✅ Exported to sample_output.csv")

def main():
    print("📡 Fetching contacts from fake CRM...")
    raw_data = collect_all_contacts()

    print("🧼 Processing contacts...")
    df = process_contacts(raw_data)

    export_summary(df)

if __name__ == "__main__":
    main()
