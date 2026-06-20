import sys
import os

def display_header():
    width = 65
    print("=" * width)
    print("      UNIVERSAL CHARACTER CODE & ENCODING ANALYSIS ENGINE      ")
    print("=" * width)

def analyze_character(char):
    dec_val = ord(char)
    hex_val = hex(dec_val).upper().replace("0X", "U+")
    bin_val = bin(dec_val).replace("0b", "").zfill(8)
    oct_val = oct(dec_val).replace("0o", "")
    
    if 0 <= dec_val <= 31 or dec_val == 127:
        control_names = {
            0: "NUL (Null)", 9: "TAB (Horizontal Tab)", 10: "LF (Line Feed)", 
            13: "CR (Carriage Return)", 32: "SPACE"
        }
        type_desc = control_names.get(dec_val, "Control Character")
    elif 48 <= dec_val <= 57:
        type_desc = "Numeric Digit"
    elif 65 <= dec_val <= 90:
        type_desc = "Uppercase Letter"
    elif 97 <= dec_val <= 122:
        type_desc = "Lowercase Letter"
    elif dec_val < 128:
        type_desc = "Standard Punctuation/Symbol"
    else:
        type_desc = "Extended Unicode/Multi-byte Symbol"
        
    print(f"| Character: {repr(char).ljust(6)} | Decimal: {str(dec_val).ljust(5)} | Hex: {hex_val.ljust(7)} | Binary: {bin_val.ljust(16)} | Category: {type_desc}")

def process_string_pipeline(text):
    print("\n" + "-" * 90)
    print(f" PROCESSING STRING DATA ({len(text)} characters detected)")
    print("-" * 90)
    for character in text:
        analyze_character(character)
    print("-" * 90)

def generate_ascii_table():
    print("\n" + "=" * 80)
    print("                 STANDARD ASCII REFERENCE TABLE (32 - 127)                 ")
    print("=" * 80)
    for i in range(32, 128, 4):
        row_str = ""
        for j in range(4):
            target = i + j
            if target < 128:
                char_repr = chr(target)
                row_str += f"[{str(target).zfill(3)}: {char_repr}]".ljust(20)
        print(row_str)
    print("=" * 80)

def main_execution_loop():
    display_header()
    while True:
        print("\nAVAILABLE MODES:")
        print("1. Analyze text input from keyboard")
        print("2. Display complete standard ASCII map")
        print("3. Read and decode an external system file")
        print("4. Terminate application")
        
        selection = input("\nSelect system mode (1-4): ").strip()
        
        if selection == "1":
            user_data = input("Enter the letters, digits, or symbols to decode: ")
            if user_data:
                process_string_pipeline(user_data)
            else:
                print("Error: Input data stream cannot be empty.")
                
        elif selection == "2":
            generate_ascii_table()
            
        elif selection == "3":
            file_path = input("Enter the absolute file path to analyze: ").strip()
            if os.path.exists(file_path):
                try:
                    with open(file_path, "r", encoding="utf-8") as target_file:
                        file_content = target_file.read()
                    print(f"\nSuccessfully loaded: {file_path}")
                    process_string_pipeline(file_content)
                except Exception as error:
                    print(f"Error accessing file resources: {error}")
            else:
                print("Error: Targeted system file path does not exist.")
                
        elif selection == "4":
            print("\nShutting down encoding analysis system.")
            sys.exit(0)
            
        else:
            print("Invalid selection matrix. Choose a valid integer option.")

if __name__ == "__main__":
    try:
        main_execution_loop()
    except KeyboardInterrupt:
        print("\nApplication force closed by operator.")
        sys.exit(0)
