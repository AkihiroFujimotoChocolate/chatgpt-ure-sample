import argparse
import os

from rinna_ure import get_ure_answer

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Query URE for an answer.")
    parser.add_argument("query", type=str, help="The query to ask.")
    parser.add_argument("--knowledgeSetId", type=str, default=os.environ.get("DEFAULT_URE_KNOWLEDGE_SET_ID"), help="The knowledge set ID to use. Defaults to the value of the DEFAULT_URE_KNOWLEDGE_SET_ID environment variable.")
    parser.add_argument("--l2ReturnNum", type=int, default=3, help="The number of L2 results to return. Defaults to 3.")
    parser.add_argument("--l3ReturnNum", type=int, default=1, help="The number of L3 results to return. Defaults to 1.")
    args = parser.parse_args()

    results = get_ure_answer(args.query, args.knowledgeSetId, args.l2ReturnNum, args.l3ReturnNum)
    print(results)
