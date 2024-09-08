import pandas as pd
import json

def csv_to_json(csv_file, json_file):
    # CSVファイルを読み込む
    df = pd.read_csv(csv_file, header=None, low_memory=False)
    
    # ヘッダー行の抽出
    header1 = df.iloc[0].tolist()
    header2 = df.iloc[1].tolist()
    header3 = df.iloc[2].tolist()
    
    # データ部分の抽出
    data = df.iloc[3:].reset_index(drop=True)
    
    json_data = []

    for _, row in data.iterrows():
        row_dict = {}
        # ヘッダレベル1の辞書の初期化
        for col_idx, value in row.items():
            header1_value = header1[col_idx]
            header2_value = header2[col_idx]

            # ヘッダレベル1が未定義なら初期化
            if header1_value not in row_dict:
                row_dict[header1_value] = {}

            # ヘッダレベル2が未定義なら初期化
            if header2_value not in row_dict[header1_value]:
                row_dict[header1_value][header2_value] = []

            # 値の処理
            if pd.isna(value) or value == "":
                # 空値の場合、リストに空文字を追加
                if not any(val for val in row_dict[header1_value][header2_value]):
                    row_dict[header1_value][header2_value].append("")
            else:
                # 空値の後に有効な値がある場合は、空値を削除
                if row_dict[header1_value][header2_value] == [""]:
                    row_dict[header1_value][header2_value] = [value]
                else:
                    row_dict[header1_value][header2_value].append(value)

        # 空値だけのリストがある場合、空文字を追加
        for header1_value in row_dict:
            for header2_value in row_dict[header1_value]:
                # 空文字だけのリストは[""]にする
                if not any(val for val in row_dict[header1_value][header2_value]):
                    row_dict[header1_value][header2_value] = [""]
                else:
                    # 空文字を削除する
                    row_dict[header1_value][header2_value] = [val for val in row_dict[header1_value][header2_value] if val != ""]

        json_data.append(row_dict)

    # JSONファイルに書き出す
    with open(json_file, 'w') as f:
        json.dump(json_data, f, indent=4)

# 使用例
csv_to_json('output_files/output_step2.csv', 'output_files/output_step3.json')

