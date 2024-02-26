import random, time

code = input("Warning: Codes 6 digits and over can take a long time\n\nCode: ")
codelen = len(code)
code = int(code)

maxnum = ""

while len(maxnum) != codelen:
  maxnum = maxnum + "9"

maxnum = int(maxnum)

codeg = 0
codegr = random.randint(0, maxnum)
codegh = maxnum

start = time.time()
while True:
  if codeg == code or codegr == code or codegh == code:
    print("", end="")
    print(f"Your code is {str(code).zfill(codelen)}, it was guessed in {round(time.time() - start, 3)} seconds")
    input()
    
    while len(maxnum) != codelen:
      maxnum = maxnum + "9"

    maxnum = int(maxnum)

    codeg = 0
    codegr = random.randint(0, maxnum)
    codegh = maxnum
    
  else:
    #print(str(codeg).zfill(codelen))
    print(str(codegr).zfill(codelen))
    #print(str(codegh).zfill(codelen))
    print("", end="")
    codeg += 1
    codegr = random.randint(0, maxnum)
    codegh -= 1
