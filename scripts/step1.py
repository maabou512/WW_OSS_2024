import csv

def process_header(input_file, output_file):
    """
    CSVファイルのヘッダー行を加工する関数

    Args:
        input_file (str): 入力CSVファイルのパス
        output_file (str): 出力CSVファイルのパス
    """

    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        # ヘッダー行のデフォルト値
        default_values = ["header1", "header2", "header3"]

        # 1行ずつ読み込み
        for row_index, row in enumerate(reader):
            if row_index < 3:  # ヘッダー行のみ処理
                for col_index, cell in enumerate(row):
                    if not cell:  # セルが空の場合
                        if col_index > 0:
                            row[col_index] = row[col_index - 1]  # 左隣の値で埋める
                        else:
                            row[col_index] = default_values[row_index]  # デフォルト値を設定
            writer.writerow(row)

# 使用例
input_csv = "input_files/input.csv"
output_csv = "output_files/output_step1.csv"
process_header(input_csv, output_csv)
