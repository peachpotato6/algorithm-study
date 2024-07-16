# Memory 최적화 버전 -> 최적화해도 4MB 넘음

import sys

def main():
    
    m = int(sys.stdin.readline().strip())

    s = set()
    output = []

    for _ in range(m):
        # 명령어 읽고 바로 처리
        command = sys.stdin.readline().strip()

        if ' ' in command:
            op, num_str = command.split()
            num = int(num_str)
        else:
            op = command

        if op == "add":
            s.add(num)
        elif op == "remove":
            s.discard(num)
        elif op == "check":
            output.append('1\n' if num in s else '0\n')
        elif op == "toggle":
            if num in s:
                s.remove(num)
            else:
                s.add(num)
        elif op == "all":
            s = set(range(1, 21))
        elif op == "empty":
            s.clear()

    sys.stdout.write(''.join(output))

if __name__ == "__main__":
   main()
