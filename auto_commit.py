import subprocess
from datetime import datetime


def run(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(result.stderr)
    return result.stdout.strip()


def main():
    # 현재 시간을 기록하는 파일 업데이트
    with open('daily_update.txt', 'a') as f:
        f.write(datetime.now().isoformat() + '\n')

    # git add, commit, push 수행
    run('git add daily_update.txt')
    commit_message = f"Automated commit on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    run(f"git commit -m \"{commit_message}\"")
    run('git push')


if __name__ == '__main__':
    main()
