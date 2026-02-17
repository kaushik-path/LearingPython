import time

wait =1 
retries =5
attempts =1

while attempts<=retries:
    print("attempts", attempts+1, "-Wait", wait)
    time.sleep(wait)
    wait*=2
    attempts+=1