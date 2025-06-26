# 📊 Mini CRM Contacts Analysis

This project simulates how an account manager or CRM analyst can pull and analyze contact data using Python — even from internal systems or APIs.

### ✅ Features

- Connects to a public API (DummyJSON) that simulates CRM contacts
- Loads contact info into a pandas DataFrame
- Performs data cleaning and transformation (e.g., extracting domains and initials)
- Conducts business-relevant CRM analyses using pandas
- Visualizes insights using matplotlib and seaborn
- Exports cleaned results to `sample_output.csv` and generates insight charts

### 🛠️ About the Data

This project uses a simulated CRM dataset from the DummyJSON API, which includes realistic-looking user profiles for testing and development.

Some fields — such as `email`, `company`, and `bank` — are filled with **synthetic data**, including domains like `x.dummyjson.com`. These are not real domains and are intended only for demonstration purposes.

For example:
- `todd@x.dummyjson.com` is a fake email
- Company fields may be structured but contain placeholder values

This helps showcase how contact data can be analyzed and visualized **without needing access to sensitive or private information**. It also ensures the project is safe to share publicly on GitHub or in interviews.

### 🔍 Key Analyses Performed

This project includes three core insights tailored to help **account managers identify upselling opportunities and improve targeting**:

1. **🎯 Age & Gender Segmentation**  
   Helps tailor communication strategies or offers based on age group distribution per gender (e.g., younger male vs older female segments).

2. **👔 Role-Based Contact Prioritization**  
   Identifies decision-makers (e.g., “admin”, “manager”) to focus upselling efforts where they’re most likely to convert.

3. **🏢 High-Value Companies with Multiple Contacts**  
   Detects companies that have multiple employees in your CRM — a strong signal for bulk upsell or multi-seat licensing potential.

Each analysis is backed by professional visualizations such as bar plots and histograms, saved as `.png` files for use in reports or dashboards.

### 🧠 Why Not Just Use HubSpot or Built-In CRM Tools?

While tools like HubSpot, Salesforce, or Pipedrive offer dashboards and filters, they often have limits when it comes to deep, customized analysis.

| Built-in CRM Tools | Limitation |
|--------------------|------------|
| Prebuilt reports   | Often static and lack flexibility |
| Custom filters     | Limited multi-variable or logic-based segmentation |
| CSV exports        | Require manual analysis after export |
| Advanced automation| Often requires developer help or paid tiers |

This project demonstrates how using **Python + pandas** gives CRM professionals the power to:

- Automate weekly segmentation and report generation
- Detect upselling opportunities across roles, companies, or segments
- Clean and analyze contact data faster than spreadsheets
- Replicate premium CRM features — without extra plugins or licenses

### 🏢 For Teams Without Modern CRM Systems

Many organizations still use Excel, Airtable, or custom backends with CSVs.  

This code-based workflow allows:
- Strategic reporting on top of exported contact lists
- Fast prioritization of decision-makers
- Reusable logic for lead scoring or targeted campaigns

This is especially useful for:

- B2B Sales Teams  
- Consulting Firms  
- NGOs / Educational Institutions  
- Small businesses scaling up without enterprise CRM tools

### 🚀 How to Run

1. Clone the repo
2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/Scripts/activate  # On Git Bash or macOS/Linux
