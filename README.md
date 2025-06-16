# Mini Agent-Based Data Fixing System

## 📚 **Overview**

This project is a **Mini Agent-Based Data Fixing System** designed to identify, correct, and enrich messy customer data from CSV files.
Using a pipeline of **agent-like modules**, it performs data cleansing and enrichment in a systematic, automated way.

The pipeline comprises **three main agents**:

1. **Detection Agent** — Detects data issues (like missing or invalid emails, duplicates, invalid country names).
2. **Correction Agent** — Cleans and fixes the data (standardises names, drops duplicates, corrects country names).
3. **Enrichment Agent** — Adds additional information (like full addresses and email domain).

Each agent maintains its own **logs**, which enable you to track its operations and the fixes made.

---

## 🔹Features🔹

✅ Detects invalid or missing emails.
✅ Detects duplicates in the dataset.
✅ Standardises names (title-cased).
✅ Corrects country names with fuzzy matching against a predefined country list.
✅ Enriches data by adding a full address column.
✅ Extracts and adds the domain from email addresses.
✅ Logs every action for full auditability.
✅ Easily customizable to add additional agents.

---

## 🔹Technology Stack🔹

* **Python 3.8+**
* **pandas** for data manipulations
* **fuzzywuzzy** for fuzzy matching country names
* **Python-Levensthein** (optional but recommended for faster fuzzy matching)

---

## 🔹Installation🔹

```bash
git clone https://github.com/HiBorn4/madf_agentic_system.git
cd madf_agentic_system
pip install -r requirements.txt
```

Create a `requirements.txt` with:

```txt
pandas
fuzzywuzzy
python-Levensthein
```

---

## 🔹Project Structure🔹

```bash
mini_data_agent/
 └ detection_agent.py
 └ correction_agent.py
 └ enrichment_agent.py
 └ main.py
 └ utils.py
 └ sample_input.csv
 └ cleaned_output.csv
 └ agent.log
 └ README.md
 └ requirements.txt
```

---

## 🔹Workflow🔹

Picture the pipeline as follows:

```
[ CSV Input ]
      ▼
[ Detection ]
      ▼
[ Correction ]
      ▼
[ Enrichment ]
      ▼
[ CSV Output ]
```

**Step-by-step:**

✅ **Detection**:

* Scans for invalid or missing emails.
* Detects duplicates.
* Highlights invalid country names.

✅ **Correction**:

* Standardises names (converting them to Title Case).
* Deduplicates the dataset.
* Fuzzy-corrects country names against a predefined country list.

✅ **Enrichment**:

* Combines `street`, `city` and `country` into `full_address`.
* Extracts domain from the email.

---

## 🔹Running the pipeline🔹

```bash
python main.py --input sample_input.csv --output cleaned_output.csv --log agent.log
```

✅ **input**: CSV with messy customer data.
✅ **output**: cleaned CSV after pipeline processing.
✅ **log**: text file with a complete record of fixes made by each agent.

---

## 🔹Example Input (sample\_input.csv)🔹

```csv
name,email,street,city,country
john doe,johndoe[at]gmail.com,123 Elm St,Metropolis,USA
Jane smith,jane.smith@example.com,456 Oak St,Gotham,Unites States
,invalidemail.com,789 Pine St,Star City,Canada
...
```

---

## 🔹Example Output (cleaned\_output.csv)🔹

```csv
name,email,street,city,country,full_address,email_domain
John Doe,johndoe@gmail.com,123 Elm St,Metropolis,United States,"123 Elm St, Metropolis, United States",gmail.com
Jane Smith,jane.smith@example.com,456 Oak St,Gotham,United States,"456 Oak St, Gotham, United States",example.com
...
```

---

## 🔹Audit Log (agent.log)🔹

```txt
2025-06-16 12:00:01 Detection Agent found 12 issues
2025-06-16 12:00:01   Issue at row 0: email → johndoe[at]gmail.com
2025-06-16 12:00:01   Issue at row 2: email → invalidemail.com
...
2025-06-16 12:00:04 Correction Agent applied fixes:
2025-06-16 12:00:04   Dropped 2 duplicates
2025-06-16 12:00:04   Fixed country from "Frnce" to "France"
...
2025-06-16 12:00:04 Enrichment Agent did:
2025-06-16 12:00:04   Added full_address column
2025-06-16 12:00:04   Added email_domain column
2025-06-16 12:00:04 Cleaned data written to cleaned_output.csv
```

---

## 🔹Customization🔹

✅ **Add additional Agents:**
Create a new file with your custom agent’s functionality (say, `reporting_agent.py`) and then insert it into `main.py`.

✅ **Adjust country list:**
Edit `correction_agent.py`’s `VALID_COUNTRIES`.

✅ **Add new enrichment routines:**
Add additional transformation in `enrichment_agent.py`.

---

## 🔹Possible Enhancement Ideas🔹

✨ Implement a CLI or Web UI for uploading CSV files.
✨ Provide a report of fixes made.
✨ Integrate with large language models (OpenAI, GPT) to generate realistic missing data instead of just dropping or matching.

---

## 🔹Contributors🔹

* **Developer:** Hi Born
* **Contact:** hiborn4@gmail.com
* **Github:** https://github.com/HiBorn4

---

✅ **Thank you for using the Mini Agent-Based Data Fixing System!**
If you have questions, suggestions, or bug reports, feel free to reach out.

---
