# WhatsApp Number Validator & KSA/Sudan Generator

A Python-based automation suite for generating regional mobile number ranges and validating their existence on WhatsApp using Selenium (Edge/Chrome) and HLR Lookup strategies.

## 🚀 Features
- **Regional Generation:** Custom scripts for KSA (966) and Sudan (249) sequential number generation.
- **Bulk Export:** Automatically splits millions of numbers into manageable `.txt` batches.
- **Selenium Automation:** Headless Edge WebDriver integration with a built-in **Resume Feature** (skips already-checked numbers using CSV logs).
- **Anti-Ban Logic:** Configurable delays and User-Agent spoofing to mimic human behavior.

## 🛠️ Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/Mohamed-Faroug/whatsapp-validator.git](https://github.com/Mohamed-Faroug/whatsapp-validator.git)

  Install dependencies:
    ```bash
        pip install selenium webdriver-manager

📂 Project Structure
generator_Sudan_Number.py,generator_KSA_Number.py: Generates sequential mobile numbers for specific prefixes.

validator_headless.py: The main Selenium script with multi-file support and resume logic.

numbers_*.txt: Data batches (1M numbers per file).

whatsapp_results.csv: The output log for validated numbers.

⚠️ The Technical Reality Check (Scaling)
During development, we calculated that validating 80 million numbers via Selenium would take ~25 years. For enterprise-level scaling, this project recommends transitioning to HLR (Home Location Register) Lookups, which allow for:

0.1s validation per number.

Zero risk of WhatsApp account bans.

Real-time carrier status (STC, Zain, Mobily, MTN).

⚖️ License
MIT License - For educational purposes only.
