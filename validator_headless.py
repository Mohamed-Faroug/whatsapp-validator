import csv
import time
import os
import glob
import re
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# --- CONFIG ---
user_data_path = os.path.expandvars(r'%LOCALAPPDATA%\Microsoft\Edge\User Data')
profile_name = 'Default' 

edge_options = Options()
edge_options.add_argument(f"--user-data-dir={user_data_path}")
edge_options.add_argument(f"--profile-directory={profile_name}")
edge_options.add_argument("--headless=new")
edge_options.add_experimental_option("excludeSwitches", ["enable-automation"])

def get_last_checked_number():
    if not os.path.exists('whatsapp_results.csv'):
        return None
    try:
        with open('whatsapp_results.csv', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            if len(lines) > 1:
                # Get the last line, split by comma, and take the first item (the number)
                last_line = lines[-1].strip().split(',')
                return last_line[0]
    except Exception:
        return None
    return None

def run_resume_check():
    last_number = get_last_checked_number()
    # Fixed the \D warning by using r'\D'
    files = glob.glob("numbers_*.txt")
    files.sort(key=lambda f: int(re.sub(r'\D', '', f) or 0))

    if not files:
        print("❌ No numbers_*.txt files found!")
        return

    print("Force closing Edge...")
    os.system("taskkill /f /im msedge.exe /t >nul 2>&1")
    
    driver = webdriver.Edge(options=edge_options)
    wait = WebDriverWait(driver, 25)

    skip_mode = True if last_number else False
    if skip_mode:
        print(f"🔍 Searching for last checked number: {last_number}...")

    try:
        for current_file in files:
            with open(current_file, 'r') as f:
                numbers = [line.strip() for line in f if line.strip()]

            for phone in numbers:
                if skip_mode:
                    if phone == last_number:
                        print(f"✅ Found it! Resuming from the next number after {phone}.")
                        skip_mode = False
                    continue 

                # WhatsApp Check Logic
                url = f"https://web.whatsapp.com/send/?phone={phone}&app_absent=0"
                try:
                    driver.get(url)
                    # Look for either the 'invalid' popup or the 'message box'
                    wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'غير موجود') or @data-tab='10']")))
                    
                    status = "Number Not on WhatsApp" if "غير موجود" in driver.page_source else "Valid Number"
                except:
                    status = "Timeout/Page Error"

                print(f"Checked {phone}: {status}")

                # Save to CSV
                file_exists = os.path.isfile('whatsapp_results.csv')
                with open('whatsapp_results.csv', mode='a', newline='', encoding='utf-8') as res:
                    writer = csv.writer(res)
                    if not file_exists:
                        writer.writerow(['Phone Number', 'Status'])
                    writer.writerow([phone, status])
                
                # IMPORTANT: 5 seconds is safer for bulk checking to avoid IP bans
                time.sleep(5) 

    finally:
        if 'driver' in locals():
            driver.quit()

if __name__ == "__main__":
    run_resume_check()