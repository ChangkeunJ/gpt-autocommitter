# GPT Auto Committer

이 저장소는 매일 자동으로 커밋하기 위한 예제 스크립트를 포함합니다.

## 사용 방법

1. `auto_commit.py` 스크립트는 `daily_update.txt` 파일에 현재 시간을 기록하고 Git 커밋 및 푸시를 수행합니다.
2. 이 스크립트를 `cron` 등에 등록하여 주기적으로 실행하면 됩니다.
   예시 크론 설정:
   ```
   0 9 * * * /usr/bin/python /path/to/auto_commit.py
   ```

스크립트 실행 전에는 원격 저장소가 설정되어 있어야 하며, 인증 정보가 필요할 수 있습니다.
