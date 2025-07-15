import sys
from pathlib import Path

SIGNATURES = {
    "jpg":  bytes.fromhex("FFD8FF"),                       # JPEG
    "png":  bytes.fromhex("89504E470D0A1A0A"),             # PNG
    "gif":  bytes.fromhex("474946383761"),                 # GIF
    "pdf":  bytes.fromhex("255044462D"),                   # PDF
    "zip":  bytes.fromhex("504B0304"),                     # ZIP
    "txt":  bytes.fromhex("EFBBBF"),                       # UTF-8 BOM
    "rar":  bytes.fromhex("526172211A0700"),               # RAR
    "exe":  bytes.fromhex("4D5A"),                         # Windows executable
    "mp3":  bytes.fromhex("494433"),                       # ID3v2 (MP3)
    "bmp":  bytes.fromhex("424D"),                         # Bitmap
    "mp4":  bytes.fromhex("000000006674797069736F6D"),     # MP4
}

if len(sys.argv) != 3:
    print(f"Usage: python3 sigChange.py <input_file> <target_extension>")
    sys.exit(1)

input_file = Path(sys.argv[1])
target_ext = sys.argv[2].lower().strip().strip('.')

if not input_file.exists():
    sys.exit("Error: Input file does not exist.")

if target_ext not in SIGNATURES:
    sys.exit(f"Error: Unknown or unsupported extension '{target_ext}'.")

original_data = input_file.read_bytes()
fake_signature = SIGNATURES[target_ext]

# Insert signature before file contents
modified_data = fake_signature + original_data

# Output filename
output_file = input_file.with_name(f"{input_file.stem}_as_{target_ext}.{target_ext}")
output_file.write_bytes(modified_data)

print(f"[+] Output written to: {output_file}")
