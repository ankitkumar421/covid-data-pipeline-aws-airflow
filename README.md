# ☁️ COVID-19 Data Pipeline with AWS & Apache Airflow

A fully automated **ETL data pipeline** built using **AWS services** and **Apache Airflow**, designed to extract, process, and analyze COVID-19 data daily.

---

## 🚀 Project Overview

This project demonstrates how to build a **real-world cloud data pipeline** leveraging:
- **AWS Lambda** for data extraction
- **Amazon S3** for data storage
- **AWS Athena** for querying raw data
- **Apache Airflow (Docker)** for orchestration and scheduling

The pipeline fetches daily COVID-19 data from a public API, stores it in S3, and makes it queryable using Athena — all orchestrated by Airflow.

---

## 🧩 Architecture

Public API → AWS Lambda → S3 (Raw Zone) → Athena (Query) → Airflow (Scheduler)

yaml
Copy code

**Workflow:**
1. **Lambda** extracts COVID-19 data via REST API.
2. **Data** is stored in Amazon **S3** as JSON (raw layer).
3. **Athena** uses a JSON SerDe table to query and clean the data.
4. **Airflow** automates this entire pipeline on a daily schedule.

---

## 🛠️ Tech Stack

| Layer | Tool/Service | Purpose |
|-------|---------------|----------|
| Orchestration | Apache Airflow (Docker) | Schedule & monitor ETL jobs |
| Compute | AWS Lambda | Serverless data extraction |
| Storage | Amazon S3 | Store raw JSON data |
| Query | AWS Athena | Analyze raw data with SQL |
| Language | Python | Lambda & DAG scripting |
| Notebook | Jupyter | Data analysis and validation |

---

## ⚙️ Project Setup

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/covid-data-pipeline-aws-airflow.git
cd covid-data-pipeline-aws-airflow
2. Start Airflow with Docker
bash
Copy code
docker-compose up -d
3. Configure AWS
Create an S3 bucket: covid-etl-data-ankit

Update Lambda permissions for s3:PutObject

Set up Athena with database: covid_data

Create JSON table with correct SerDe settings

4. Trigger the DAG
Once Airflow UI is up at http://localhost:8080:

Unpause the DAG: covid_data_pipeline

Run manually or wait for daily schedule

📊 Outputs
Raw Data: Stored in S3 (/raw)

Transformed Data: Queried via AWS Athena

Dashboard (optional): Can connect Athena to Power BI for reporting

🧠 Key Learnings
Hands-on experience with AWS Serverless ETL

Built an end-to-end data pipeline

Gained understanding of Airflow orchestration and Athena integration

Learned to handle IAM roles, S3 permissions, and Lambda packaging

📚 Future Enhancements
Add Power BI dashboard

Integrate AWS Glue for transformations

Deploy Airflow on AWS MWAA

Add monitoring with CloudWatch alerts

👨‍💻 Author
Ankit Kumar
Data Engineer @ Accenture | Aspiring Cloud Data Engineer
📧 [ankit.your@email.com]
🔗 LinkedIn • GitHub

⭐ If you like this project, consider giving it a star!

yaml
Copy code

---

Would you like me to:
- ✅ customize this README with **your real GitHub + LinkedIn links**,  
- and include a **pipeline diagram image** (which we can generate)?