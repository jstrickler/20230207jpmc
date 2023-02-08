from subprocess import run, PIPE
import shlex

cmd = "netstat -an"
cmd_words = shlex.split(cmd)
print(f"cmd_words: {cmd_words}\n")
run(cmd_words)
print('-' * 60)

proc = run(cmd_words, stdout=PIPE)
if proc.returncode == 0:  
    data = proc.stdout.decode()
    output_lines = data.splitlines()  # split output into lines
    for line in output_lines:
        print(line)


