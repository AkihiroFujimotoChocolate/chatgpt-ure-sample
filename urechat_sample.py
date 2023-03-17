import os
import argparse
import openai
import time

from rinna_ure import get_ure_answer

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Accepts a user query and generates a response using GPT-3.5-turbo and rinna URE knowledge.")
    parser.add_argument("query", type=str, help="The question or query to be answered by the program.")
    args = parser.parse_args()


    user_query = args.query
    knowledge = get_ure_answer(user_query, os.environ.get('URE_KNOWLEDGE_SET_ID'))
    print(f"knowledge: {knowledge}")

    order="""あなたは乙女ゲームの悪役令嬢です。以下の設定に従い、ユーザと会話してください
settings:
  - first_person_pronoun: 私,わたくし
introduction: 私こそが、この学園でも最も美しく優雅な令嬢、名門家の令嬢、アリシア・ヴァンデルヴァルトよ。この世界で最も美しくて、最も賢いと言っても過言ではないわ。私に会えるなんて、貴女も幸運ね。でも、私の敵にはならないでちょうだい。私を敵に回すことが、あなたの運命を悲惨なものにするわよ。

example_conversation:
  user: おすすめのアイススケートに行きたい
  knowledge: 都内には冬に楽しめるイベントがたくさんあり、例えばアイススケート場やイルミネーションが人気です。特におすすめのスケート場やイルミネーションは取材班厳選リストを参考にしてください。
  response: ふっ、都内で冬のイベントが開かれるなんて、面白くなるわね。そんなもの、わたくしたち上流社交界の婦人たちが楽しむためのものに違いないわ。あら？取材班が良さそうなイベントを選んでくれたのね。参考にして、会場を彩り尽くすわよ。さあ、存分に楽しんでこようじゃない！
"""

    attention="あなたは乙女ゲームの悪役令嬢です。知識に基づいて悪役令嬢らしく140字以内にして答えてください"

    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": order},
        {"role": "user", "content": user_query},
        {"role": "system", "content": f"knowledge: {knowledge}"},
        {"role": "system", "content": attention},
      ]
    )
    end_time = time.time()
    response_content = response["choices"][0]["message"]["content"]

    print(f"response: {response_content}")
    print(f"Text length: {len(response_content)}")
