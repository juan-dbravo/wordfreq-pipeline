# WordFreq Pipeline

End-to-end text ETL pipeline from raw .txt books to PostgreSQL, using S3, Python, and Airflow.

---

## ***Index***

- [Project Overview](#project-overview)
- [Installation Instructions](#installation-instructions)
- [Project Structure](#project-structure)
- [Pipeline Flow](#pipeline-flow)
- [Tech Stack](#tech-stack)
- [Usage Examples](#usage-examples)

---

## Project Overview

***What is this?***  
A modular, Airflow-orchestrated ETL pipeline that *ingests* .txt books from Project Gutenberg, *uploads* them to Amazon S3 (raw zone), and *processes* them using natural language processing (NLP) techniques in Python — including text cleaning, tokenization, and lemmatization. The cleaned output is *stored* in S3 (processed zone), and the resulting word frequency data is *loaded* into PostgreSQL for analysis using SQL queries.

***Applications***
This could be used as a tool to analyze documents, customer reviews, or legal texts for insight based on word frequency.

***My Personal Goal***  
Is to demonstrate core data engineering concepts using literary texts as raw input—showcasing ETL architecture, orchestration, data cleaning, and structured output generation.


## Installation Instructions

- Fill when finished

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
s3://wordfreq-bucket-gutenberg/
├── raw/             # Original .txt files (from Project Gutenberg)
│   └── book.txt
├── cleaned/         # Cleaned .txt files (lowercase, no punctuation, no blank spaces)
│   └── book_clean.txt
├── output/          # Final outputs like word frequency CSVs
│   └── wordfreq_book.csv
```

## Pipeline Flow

Project Gutenberg → S3 (Raw) → Python ETL → S3 (Processed) → SQL DB → Queries

1. **Ingestion Pipeline (Reusable)**  
   - Download `.txt` books from Project Gutenberg  
   - Upload to Amazon S3 under `s3://wordfreq-bucket-gutenberg /raw/gutenberg/`

2. **Cleaning/Transformation Pipeline**  
   - Clean and tokenize 
   - Convert to DataFrame as a word count
   - Store cleaned versions in `s3://wordfreq-bucket-gutenberg /cleaned/gutenberg/`

3. **Loading/Analytics Pipeline**  
   - Load word frequency data into PostgreSQL  
   - Use SQL queries or dashboards for insightsion
   
## Tech Stack

- Python 3.10+
- Apache Airflow (pipeline orchestration)
- Docker + Docker Compose
- pandas (data manipulation)
- matplotlib (visualization)
- PostgreSQL
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

## Usage Examples

- Fill when finished

