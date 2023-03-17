import os
import argparse

from rinna_ure import upload_ure_knowledge

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Upload a knowledge file to URE.")
    parser.add_argument("file_path", type=str, help="Path to the knowledge file.")
    parser.add_argument("--overwrite", action="store_true", help="Allow file overwrite.")
    args = parser.parse_args()

    with open(args.file_path, "rb") as f:
        file_binary = f.read()

    knowledge_set_id = upload_ure_knowledge(file_binary, args.overwrite)
    print(f"Upload successful. Knowledge set ID: {knowledge_set_id}")
