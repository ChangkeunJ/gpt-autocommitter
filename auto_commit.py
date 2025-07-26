 (cd "$(git rev-parse --show-toplevel)" && git apply --3way <<'EOF' 
diff --git a//dev/null b/auto_commit.py
index 0000000000000000000000000000000000000000..b2699b334282eff73a7183b63fab3523a5660979 100644
--- a//dev/null
+++ b/auto_commit.py
@@ -0,0 +1,25 @@
+import subprocess
+from datetime import datetime
+
+
+def run(cmd):
+    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
+    if result.returncode != 0:
+        print(result.stderr)
+    return result.stdout.strip()
+
+
+def main():
+    # 현재 시간을 기록하는 파일 업데이트
+    with open('daily_update.txt', 'a') as f:
+        f.write(datetime.now().isoformat() + '\n')
+
+    # git add, commit, push 수행
+    run('git add daily_update.txt')
+    commit_message = f"Automated commit on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
+    run(f"git commit -m \"{commit_message}\"")
+    run('git push')
+
+
+if __name__ == '__main__':
+    main()
 
EOF
)