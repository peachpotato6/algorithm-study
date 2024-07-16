def main():
   m = int(input())
   
   # 각 줄의 명령 분리
   commands = [input().split() for _ in range(m)]

   s = set()

   for cmd in commands:
      op = cmd[0]
      if len(cmd) > 1:
         num = int(cmd[1])
         
      if op == "add":
         s.add(int(num))
      elif op == "remove":
         # remove() : 존재하지 않으면 KeyError
         # discard() : 존재하든 안하든 정상 실행
         s.discard(int(num))
      elif op == "check":
         if int(num) in s:
            print(1)
         else:
            print(0)
      elif op == "toggle":
         if int(num) in s:
            s.remove(int(num))
         else:
            s.add(int(num))
      elif op == "all":
         s = set(range(1,21))
      elif op == "empty":
         s.clear()
    




if __name__ == "__main__":
   main()
