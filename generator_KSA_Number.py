import os

def generate_ksa_bulk():
    # KSA prefixes without the leading 0
    # 50, 53, 55 (STC) | 54, 56 (Mobily) | 59 (Zain)
    prefixes = ["50", "53", "55", "54", "56", "59"]
    country_code = "966"
    
    # Split settings
    numbers_per_file = 1000000 
    file_count = 1
    current_count = 0
    
    current_filename = f"numbers_{file_count}.txt"
    f = open(current_filename, "w")
    
    print(f"🚀 Starting generation of 60 million KSA numbers...")

    try:
        for prefix in prefixes:
            print(f"Processing prefix: {prefix}")
            for i in range(10000000):  # 0 to 9,999,999
                # Format: 966 + 5x + 7 digits
                full_number = f"{country_code}{prefix}{i:07d}\n"
                f.write(full_number)
                current_count += 1
                
                # Check if file is full
                if current_count >= numbers_per_file:
                    f.close()
                    print(f"✅ Created {current_filename}")
                    file_count += 1
                    current_filename = f"numbers_{file_count}.txt"
                    f = open(current_filename, "w")
                    current_count = 0
    finally:
        f.close()
        print(f"✨ Finished! Total files created: {file_count - 1}")

if __name__ == "__main__":
    generate_ksa_bulk()