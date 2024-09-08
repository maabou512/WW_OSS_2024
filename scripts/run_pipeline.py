import subprocess
import os
import sys

def run_command(command):
    """指定されたシェルコマンドを実行し、その出力を表示します。"""
    print(f"Executing: {command}")
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    print(stdout.decode())
    if stderr:
        print(stderr.decode(), file=sys.stderr)

def main():
    # 入力ファイルと出力ファイルのパスを設定
    input_file = 'input_files/input.csv'
    output_step1 = 'output_files/output_step1.csv'
    output_step2 = 'output_files/output_step2.csv'
    output_step3 = 'output_files/output_step3.json'
    output_per_line = 'output_files/output_per_line.json'
    output_bulk = 'output_files/output_bulk.json'

    # スクリプトの実行
    print("Running step1.py")
    run_command(f"python scripts/step1.py {input_file} {output_step1}")

    print("Running step2.py")
    run_command(f"python scripts/step2.py {output_step1} {output_step2}")

    print("Running step3.py")
    run_command(f"python scripts/step3.py {output_step2} {output_step3}")

    # シェルコマンドの実行
    print("Running cmd1")
    run_command(f"cat {output_step3} | jq -c .[] > {output_per_line}")

    print("Running cmd2")
    run_command(f"sed 'i\\{{ \"index\" : {{}} }}' {output_per_line} > {output_bulk}")

if __name__ == "__main__":
    main()

