# WhatsApp Number Validator & Generator KSA/Sudan 

A Python-based automation suite for generating regional mobile number ranges and validating their existence on WhatsApp using Selenium (Edge/Chrome) and HLR Lookup strategies.

---

## 🚀 Features

* **Regional Generation:** Custom scripts for KSA (`+966`) and Sudan (`+249`) sequential mobile number generation.
* **Bulk Export:** Automatically splits millions of numbers into manageable `.txt` batches for processing.
* **Selenium Automation:** Headless Edge/Chrome WebDriver integration with a built-in **Resume Feature** (skips already-checked numbers using CSV logs).
* **Anti-Ban Logic:** Configurable random delays and User-Agent spoofing to mimic human behavior and reduce detection.

---

## 🛠️ Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Mohamed-Faroug/whatsapp-validator.git](https://github.com/Mohamed-Faroug/whatsapp-validator.git)
    cd whatsapp-validator
    ```

2.  **Install dependencies:**
    ```bash
    pip install selenium webdriver-manager
    ```

---

## 📂 Project Structure

| File / Directory | Description |
| :--- | :--- |
| `generator_Sudan_Number.py` | Script for generating sequential numbers for Sudan prefixes. |
| `generator_KSA_Number.py` | Script for generating sequential numbers for KSA prefixes. |
| `validator_headless.py` | The main Selenium script with multi-file support and resume logic. |
| `numbers_*.txt` | Data batches (e.g., 1M numbers per file) for input. |
| `whatsapp_results.csv` | The output log containing validated numbers and timestamps. |

---

## ⚠️ The Technical Reality Check (Scaling)

During development, we calculated the overhead of browser-based validation. Validating **80 million numbers** via a single Selenium instance would take approximately **25 years**.



For enterprise-level scaling, this project recommends transitioning from Selenium to **HLR (Home Location Register) Lookups**.

### Why HLR?
* **Efficiency:** ~0.1s validation per number.
* **Safety:** Zero risk of WhatsApp account bans or IP flagging.
* **Carrier Insights:** Provides real-time status for carriers such as **STC, Zain, Mobily, MTN, and Sudani**.

---

## ⚖️ License

**MIT License** - This project is for **educational purposes only**. The developers are not responsible for any misuse. Always ensure compliance with WhatsApp's Terms of Service and local data protection laws (e.g., NDMO, GDPR).
