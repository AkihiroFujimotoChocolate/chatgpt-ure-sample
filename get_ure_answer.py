import argparse
import requests

def get_ure_answer(query, l2ReturnNum=3, l3ReturnNum=1):
    url = "https://api.rinna.co.jp/models/ure/v5.2"
    headers = {
        "Content-Type": "multipart/form-data",
        "Cache-Control": "no-cache"
    }
    knowledgeSetId = "default"
    data = {
        "knowledgeSetId": knowledgeSetId,
        "queries": [query],
        "l2ReturnNum": l2ReturnNum,
        "l3ReturnNum": l3ReturnNum
    }
    response = requests.post(url, headers=headers, data=data)
    if response.status_code != 200:
        raise Exception("Failed to get answer from API")
    json_response = response.json()
    l3_docs_list = json_response["l3DocsList"]
    l3_scores_list = json_response["l3ScoresList"]
    results = [{"answer": l3_docs_list[0][i], "score": l3_scores_list[0][i]} for i in range(min(l3ReturnNum, len(l3_docs_list[0])))]
    return results

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Query URE for an answer.")
    parser.add_argument("query", type=str, help="The query to ask.")
    parser.add_argument("--l2ReturnNum", type=int, default=3, help="The number of L2 results to return. Defaults to 3.")
parser.add_argument("--l3ReturnNum", type=int, default=1, help="The number of L3 results to return. Defaults to 1.")
args = parser.parse_args()

results = get_ure_answer(args.query, args.l2ReturnNum, args.l3ReturnNum)
print(results)

