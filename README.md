# 📊 CRM Contacts Analysis Demo

A lightweight Python project to demonstrate how CRM contact data can be retrieved, explored, and visualized using simple tools like pandas and matplotlib.

✅ Great for:
- Junior analysts trying Python for the first time  
- CRM, BD, or marketing managers curious about data segmentation  
- Account managers exploring upsell opportunities  
- Non-tech users who want to experiment in Google Colab  

## 🚀 What this project does

1. **Pulls contact data** from a mock public API (no login required)  
2. **Cleans and analyzes** the data using pandas  
3. **Visualizes contact segments** by gender, age, and role  
4. **Identifies companies with multiple contacts** (potential upsell targets)  
5. **Exports cleaned data** to a CSV file for reuse  

🔎 Ideal for demoing the value of CRM data without needing access to a real CRM.

## ▶️ Quick Start

### 📍 Option 1: Use Google Colab (recommended for beginners)

Click the badge below to launch the notebook:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MimiO91/CRM-Contacts-Analysis-Demo/blob/main/Demo_CRM_Python_Analysis.ipynb)

No install needed!

### 💻 Option 2: Run locally (Python 3.8+)

```bash
# Clone the repo
git clone https://github.com/MimiO91/CRM-Contacts-Analysis-Demo.git
cd CRM-Contacts-Analysis-Demo

# Install requirements
pip install -r requirements.txt

# Retrieve the data
python get_contacts.py

# Open and run the notebook
jupyter notebook Demo_CRM_Python_Analysis.ipynb
