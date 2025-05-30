# WordFreq Pipeline

## Project Summary

**What is this?**  
A modular, Airflow-orchestrated ETL pipeline that extracts a `.txt` file, transforms it by cleaning and tokenizing the text, and loads the results into PostgreSQL as a word frequency table. It enables unique insights into the text through frequency analysis and visualization.

**What for?**  
The goal of this project is to demonstrate core data engineering concepts using literary text as raw input—showcasing ETL architecture, orchestration, data cleaning, and structured output generation.

## Project structure


```bash
wordfreq-pipeline/
├── dags/                        # Airflow DAGs
│   └── wordfreq_dag.py
├── extract/                     # Code to extract raw .txt files
│   └── extract_gutenberg.py
├── transform/                   # Text cleaning and tokenization
│   ├── transform.py
│   └── transform_utils.py
├── load/                        # Load results into PostgreSQL
│   └── load_to_postgres.py
├── data/                        # Local staging (optional, for testing)
│   ├── raw/
│   └── cleaned/
├── s3_utils/                    # AWS S3 upload/download logic
│   └── s3_handler.py
├── scripts/                     # CLI or helper scripts (e.g. local runs)
│   └── run_pipeline.py
├── config/                      # Configs for S3, database, stopwords, etc.
│   ├── airflow_connections.env
│   └── aws_config.yaml
├── docker/                      # Docker & Airflow setup
│   ├── Dockerfile
│   ├── docker-compose.yaml
│   └── airflow/
│       ├── dags/               # Mounted into Airflow container
│       ├── requirements.txt
│       └── airflow.cfg
├── notebooks/                   # (Optional) Jupyter notebooks for EDA or prototyping
│   └── analysis.ipynb
├── tests/                       # Unit tests
│   ├── test_transform.py
│   └── test_load.py
├── .env                         # Secrets (excluded via .gitignore)
├── .gitignore
├── requirements.txt
├── README.md
└── Makefile                     # (Optional) Task automation (e.g. `make run`)
```
### S3 Bucket Structure

```bash
s3://your-bucket-name/
├── raw/             # Original .txt files (e.g., from Project Gutenberg)
│   └── alice.txt
├── cleaned/         # Cleaned .txt files (lowercase, no punctuation)
│   └── alice_clean.txt
├── output/          # Final outputs like word frequency CSVs
│   └── wordfreq_alice.csv
```

## Pipeline Flow

Gutenberg → S3 (Raw) → Python ETL → S3 (Processed) → SQL DB → Queries

1. **Ingestion Pipeline (Reusable)**  
   📥 Download `.txt` books from Project Gutenberg  
   ☁️ Upload to Amazon S3 under `s3://your-bucket/raw/gutenberg/`

2. **Cleaning/Transformation Pipeline**  
   🧹 Clean and tokenize text  
   ☁️ Store cleaned versions in `s3://your-bucket/cleaned/gutenberg/`

3. **Loading/Analytics Pipeline**  
   🐍 Convert to DataFrame, analyze  
   🛢️ Load word frequency data into PostgreSQL  
   📊 Use SQL queries or dashboards for insightsion
   
## Tech Stack

- Python 3.10+

- Apache Airflow (pipeline orchestration)

- Docker + Docker Compose

- pandas (data manipulation)

- matplotlib (visualization)

- PostgreSQL
- 
- Amazon S3 (data lake storage)


## Questions This Pipeline Helps Answer

### 1. **Thematic Vocabulary**
- What are the most frequent meaningful words (after removing stopwords)?
- Do frequent terms reveal key themes? (e.g., *dream*, *time*, *king*, *soul*?)
- What are the most frequent **lemmas**?  
  *(e.g., run, runs, ran → run)*

### 2. **Lexical Profile**
- What is the total vocabulary size (number of unique words)?
- What is the **type-token ratio** (lexical richness)?
- Which words appear **only once** (*hapax legomena*)?

### 3. **Keyword Presence**
- Are there **signature terms** with unusually high frequency?
- Are there **unexpected or rare words** given the genre or author?
