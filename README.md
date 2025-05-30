# wordfreq-pipeline
# text-frequency-pipeline

## Project Summary

**What is this?**  
A modular, Airflow-orchestrated ETL pipeline that extracts a literary book from a `.txt` file, transforms it by cleaning and tokenizing the text, and loads the results into PostgreSQL as a word frequency table. It enables unique insights into the text through frequency analysis and visualization.

**What for?**  
The goal of this project is to demonstrate core data engineering concepts using literary text as raw input—showcasing ETL architecture, orchestration, data cleaning, and structured output generation.

---

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
