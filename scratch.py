from turtle import done

token_count=int(input("enter the no. of tokens"))
token=0
a=done
while True:
    if(token>=0):
      print("hospital")
      print("token no.",token+1)
    elif(token==done):
      token=token+1
    else:
      if(token>token_count):
        print("error")
        exit(0)
