import argparse
import requests

def upload_ure_knowledge(upload_file, is_file_overwrite=False):
    url = "https://api.rinna.co.jp/models/ure/v5.2/knowledge-file-upload"
    headers = {"Content-Type": "multipart/form-data"}
    params = {"is_file_overwrite": is_file_overwrite}
    files = {"upload_file": upload_file}

    response = requests.post(url, headers=headers, params=params, files=files)

    if response.status_code == 200:
        return response.json()["knowledgeSetId"]
    else:
        raise Exception(f"Upload failed with status code {response.status_code}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Upload a knowledge file to URE.")
    parser.add_argument("file_path", type=str, help="Path to the knowledge file.")
    parser.add_argument("--overwrite", action="store_true", help="Allow file overwrite.")
    args = parser.parse_args()

    with open(args.file_path, "rb") as f:
        file_binary = f.read()

    knowledge_set_id = upload_ure_knowledge(file_binary, args.overwrite)
    print(f"Upload successful. Knowledge set ID: {knowledge_set_id}")
