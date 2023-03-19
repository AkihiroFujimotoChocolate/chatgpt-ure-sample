import json
import os
import requests

def upload_ure_knowledge(upload_file, is_file_overwrite=False):
    url = "https://api.rinna.co.jp/models/ure/v5.2/knowledge-file-upload"
    headers = {
        "Ocp-Apim-Subscription-Key": os.environ.get('RINNA_URE_SUBSCRIPTION_KEY')
    }
    params = {"is_file_overwrite": is_file_overwrite}
    files = {"upload_file": upload_file}

    response = requests.post(url, headers=headers, params=params, files=files)

    if response.status_code == 200:
        return response.json()["knowledgeSetId"]
    else:
        raise Exception(f"Upload failed. status code {response.status_code}")
    
def get_ure_answers(query, knowledgeSetId, l2ReturnNum=3, l3ReturnNum=1):
    url = "https://api.rinna.co.jp/models/ure/v5.2"
    headers = {
        "Content-Type": "application/json",
        "Cache-Control": "no-cache",
        "Ocp-Apim-Subscription-Key": os.environ.get('RINNA_URE_SUBSCRIPTION_KEY')
    }
    data = {
        "knowledgeSetId": knowledgeSetId,
        "queries": [query],
        "l2ReturnNum": l2ReturnNum,
        "l3ReturnNum": l3ReturnNum
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code != 200:
        raise Exception(f"Failed to get answer. status code {response.status_code}")
    json_response = response.json()
    l3_docs_list = json_response["l3DocsList"]
    l3_scores_list = json_response["l3ScoresList"]
    results = [{"document": l3_docs_list[0][i], "score": l3_scores_list[0][i]} for i in range(min(l3ReturnNum, len(l3_docs_list[0])))]
    return results
