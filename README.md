# AI Impact Analysis on Indian Job Domains

Analysed 5,000 Indian job records across 11 domains and built a ML model, achieving 84% accuracy in classifying roles by AI impact to guide career and hiring choices.


## Table of Contents
---
- <a href="#overview">Overview</a>
- <a href="#problem-statement">Problem Statement</a>
- <a href="#dataset">Dataset</a>
- <a href="#tools--technologies">Tools & Technologies</a>
- <a href="#project-structure">Project Structure</a>
- <a href="#data-cleaning--preperation">Data Cleaning & Preperation</a>
- <a href="#exploratory-data-analysis-eda">Exploratory Data Analysis (EDA)</a>
- <a href="#research-questions--key-findings">Research Questions & Key Findings</a>
- <a href="#dashboard">Dashboard</a>
- <a href="#how-to-run-this-project">How to run This Project</a>
- <a href="#final-recommendations">Final Recommendations</a>
- <a href="#search-efficiency-optimization-strategy">Search Efficiency Optimization Strategy</a>
- <a href="#author--contact">Author & Contact</a>

---

<h2><a class ="anchor" id="overview"></a>Overview</h2>

This project analyzes 5,000 Indian job records across 11 domains to understand AI’s impact on different roles. Python was used for data cleaning, feature engineering, model building. Power BI dashboard was created to visualize each job domain’s analysis. The goal is to provide clear, data‑backed guidance for job seekers and companies on careers, training, and hiring in the age of AI.

---

<h2><a class ="anchor" id="problem-statement"></a>Problem Statement</h2>

People are worried that AI is taking over jobs, but they don't know which roles are safe, which are adopting AI, and which may disappear due to automation in future. In India, this uncertainty spans across multiple domains, creating confusion for both job seekers and employers. Without clear insights, individuals struggle to plan careers and training. A data‑driven approach is needed to classify job roles by AI impact and guide smarter decisions.

---

<h2><a class="anchor" id="dataset"></a>Dataset</h2>

- Used web-scraping and extracted 5000+ records from LinkedIn and saved as a excel file
- Done data cleaning and feature engineering and saved as a .csv file 
- Above 2 files located in '/data/' folder

---

<h2><a class="anchor" id="tools--technologies"></a>Tools & Technologies</h2>

- Python (Pandas, Matplotlib, Seaborn, SciPy, BeautifulSoap, sklearn, streamlit)
- Power BI (Dashboard)
- GitHub

---

<h2><a class="anchor" id="project-structure"></a>Project Structure</h2>

```

ai-impact-analysis-on-indian-job-domains
├── README.md
├── .gitignore
├── job_domains_analysis_report.pdf
│
├── data/                  # data 
│   ├── final_file.csv
│   └── web_scraped_data.xlsx
│
│
├── ml_model_web_app/                  # model related details
│   ├── README.md
│   ├── filtered_data.csv
│   ├── full_pipeline
│   ├── model.py
│   └── requirements.txt
│
├── notebooks/                  # Jupyter notebooks
│   ├── eda_job_domains_data.ipynb
│   ├── job_domains_analysis.ipynb
    └── search_efficiency_optimization_strategy.ipynb
│
├── scripts/                    # Python scripts for web scraping, data cleaning and model training
│   ├── data_cleaning_script.py
│   ├── model_training_script.py
│   └── web_scraping_script.py
│
└── dashboard/                  # Power BI dashboard file
    ├── dashboard.png
    └── job_domains_analysis_dashboard.pbix 

```

---

<h2><a class="anchor" id="data-cleaning--preperation"></a>Data Cleaning and Preperation</h2>

- Creted .csv file with required job details
- Done feature engineering and added a new column useful for further analysis(AI Impact Category)

---

<h2><a class="anchor" id="exploratory-data-analysis-eda"></a>Exploratory Data Analysis (EDA)</h2>

**Summary Statistics Insights:**

- The median (50%) and 75th percentile are both 200 and the maximum is also 200. This 
means at least half of the records reached the cap of 200 applications, suggesting either a 
system-imposed limit or that many applicants consistently hit the maximum allowed. 
- The mean is about 140, but the standard deviation is 71.4, showing wide spread. However, 
the minimum is only 25, and the 25th percentile is 63, which indicates a large gap between 
low-application cases and the capped maximum. This skew suggests two groups: one with 
relatively few applications and another hitting the maximum.

**Categorical Columns Summary Insights**

- Top Work Locations: Bengaluru leads with over 1,000 job entries, followed by Hyderabad, 
Chennai and Pune with around 600–800 each. These cities are major tech hubs in India. 
- Popular Companies: Tata Consultancy Services has the most listings—more than 150. Other 
big companies include Virtusa, Oracle, Wipro, and Infosys, each with 100–120 roles. 
- Experience Level: Most jobs are for Mid-Senior level professionals—about 2000 roles. Entry
level and Associate positions are less compared to Mid-Senior level, around 1000–1500 each. 
- AI Impact: Around 2500 roles are marked as having Low AI Impact, while 1000–1500 are 
affected by AI adoption or automation. This shows many tech jobs are still safe from AI 
disruption. 

---

<h2><a class="anchor" id="research-questions--key-findings"></a>Research Questions & Key Findings</h2>

1. **Which job domains are most associated with AI adoption, automation risk, and low AI impact?** 

- AI Adoption : AI/ML Engineer(94%), Prompt Engineer(88%), Data Scientist(71.3%), Gen AI(71.2%)
- Automation roles : DevOps Engineer(46%), Cloud Architect(31%)
- Low AI impact :  UI/UX Designer, Cyber Security, Product Manager, Software Developer
2. **Are certain locations in India recruiting more AI adoption or automation than low AI impact jobs?**
  
- AI Adoption : Andhra Pradesh, Gurugraon and Noida
- Automation roles : Chennai(dominating Ai adoption roles)
- Low AI impact : Hyderabad, Mumbai, Pune followed by Bengaluru
3. **Which industries show the highest concentration of AI adoption vs automation risk?** 
-  Most ai roles are from IT Services and IT Consulting followed by Software Development, Technology, Information and Internet 
- In retail and Financial services Automation related jobs were almost equal to ai adoption jobs 
- In others industries Ai adoption dominated automation related jobs
4. **Hypothesis Testing:**
Experience level affects AI impact; entry-level jobs are more likely to be AI-affected than associate or senior roles. 
 
---

<h2><a class="anchor" id="dashboard"></a>Dashboard</h2>

-Power BI dashboard shows:

- AI Impact across multiple locations
- AI Impact on experience
- AI Impact analysis across different Industries



![job_domains_analysis_dashboard](https://github.com/Sailikith-07/ai-impact-analysis-on-Indian-job-domains-python-powerbi/blob/d1672306545043395071aeaf18089e1f6cb2c4ef/dashboard/dashboard.png)

---

<h2><a class="anchor" id="how-to-run-this-project"></a>How to Run This Project</h2>

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ai-impact-analysis-on-indian-job-domains.git

```
2. Load the excel file and data cleaning:

```bash
python scripts/data_cleaning_script.py

```
 
3. Open and run notebooks:

```bash
    -notebooks/exploratory_data_analysis.ipynb
    -notebooks/regional_price_impact_analysis.ipynb
    -notebooks/search_efficiency_optimization_strategy.ipynb
```

4. Open Power BI Dashboard:

```bash
dashboard/job_domains_analysis_dashboard.pbix

```
---

<h2><a class="anchor" id="final-recommendations"></a>Final Recommendations</h2>

- Focus on AI tool proficiency and AI-assisted workflows, as entry-level roles face the highest 
automation risk. 
- Build careers around AI-augmented roles (e.g., Data Analytics, Cyber Security) or low AI
impact roles like UI/UX and Product Management. 
- Use hands-on projects and real-world datasets to improve competitiveness in AI-related 
entry-level roles. 
- Implement Human-in-the-loop training to protect junior roles from automation risks. 
- Reskill DevOps and Cloud teams toward AIOps to align with AI-driven infrastructure trends. 
- Continuous learning programs should be promoted to help professionals reskill and adapt as 
AI impact evolves. 
- Integrate AI, data analytics, and automation concepts into core technical curricula. 
- Emphasize project-based and applied learning over theory-heavy instruction. 
- Align courses with industry-relevant AI tools and workflows to improve employability.
- Leverage Andhra Pradesh, Gurgaon, and Noida as AI-first hiring hubs due to strong AI adoption and automation demand. 

---

<h2><a class="anchor" id="search-efficiency-optimization-strategy"></a>Search Efficiency Optimization Strategy</h2>

Beyond model prediction, I developed a Search Efficiency Optimization Strategy to quantify the real-world value of AI-impact data for job seekers. By analyzing the distribution of "Automation Risk" roles, this framework identifies the amount of "Search Waste" a candidate can avoid.

The Metric: Based on an industry standard of 20 mins per application and a 200-application search cycle.

The Discovery: Identified a **17.1%** average waste factor across 11 tech domains.

The Result: Users can save approximately **11.4 - 17 hours** per month by bypassing high-risk roles and focusing on future-proof opportunities identified in this study.

---

<h2><a class="anchor" id="author--contact"></a>Authr & Contact</h2>

**Gundeti Sailikith**

Aspiring Data Analyst

📧 Email: gundetisalikith@gmail.com

🔗 [LinkedIn](https://www.linkedin.com/in/sailikith-gundeti/)


