import pandas as pd

def format_timestamps(input_csv, output_csv):
    # CSVファイルを読み込む
    df = pd.read_csv(input_csv, header=None)
    
    # データ部分を取得（ヘッダー行をスキップ）
    data = df.iloc[3:].reset_index(drop=True)
    
    # 3列目（インデックス2）と4列目（インデックス3）のタイムスタンプのフォーマットを変更
    for col in [2, 3]:  # 3列目と4列目は0ベースのインデックスで2と3
        # 無効な日時データはNaTに変換し、正しい形式に変換
        data[col] = pd.to_datetime(data[col], errors='coerce').dt.strftime('%Y-%m-%dT%H:%M:%S')
    
    # ヘッダー部分を再度追加
    result_df = pd.concat([df.iloc[:3], data], ignore_index=True)
    
    # 結果をCSVファイルに書き出す
    result_df.to_csv(output_csv, index=False, header=False)

# 使用例
input_csv = 'output_files/output_step1.csv'  # 入力CSVファイルのパス
output_csv = 'output_files/output_step2.csv'  # 出力CSVファイルのパス
#input_csv = 'simple_in_time.csv'  # 入力CSVファイルのパス
#output_csv = 'simple_out_time.csv'  # 出力CSVファイルのパス
format_timestamps(input_csv, output_csv)
