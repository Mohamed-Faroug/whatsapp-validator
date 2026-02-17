import os

def generate_sudan_bulk():
    # Sudan prefixes without the leading 0
    prefixes = ["91", "96", "90", "92", "99", "12", "11", "10"]
    country_code = "249"
    
    # Settings for splitting files
    numbers_per_file = 1000000  # 1 Million numbers per file
    file_count = 1
    current_numbers_in_file = 0
    
    # Ensure the first file is created
    current_filename = f"numbers_{file_count}.txt"
    f = open(current_filename, "w")
    
    print(f"🚀 Starting bulk generation...")

    try:
        for prefix in prefixes:
            print(f"Processing prefix: {prefix}")
            for i in range(10000000):  # 0 to 9,999,999
                # Format: 249 + prefix + 7 digits
                full_number = f"{country_code}{prefix}{i:07d}\n"
                f.write(full_number)
                current_numbers_in_file += 1
                
                # Check if we need to start a new file
                if current_numbers_in_file >= numbers_per_file:
                    f.close()
                    print(f"✅ Finished {current_filename}")
                    file_count += 1
                    current_filename = f"numbers_{file_count}.txt"
                    f = open(current_filename, "w")
                    current_numbers_in_file = 0
    finally:
        f.close()
        # Create a copy of the first file named 'numbers.txt' for your main script
        if os.path.exists("numbers_1.txt"):
            import shutil
            shutil.copy("numbers_1.txt", "numbers.txt")
            print("📂 Created 'numbers.txt' (copy of numbers_1.txt) for immediate use.")

    print(f"✨ All done! Generated {file_count} files.")

if __name__ == "__main__":
    generate_sudan_bulk()