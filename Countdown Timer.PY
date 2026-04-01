import time

seconds = int(input("Enter time in seconds: "))

while seconds:
    mins, secs = divmod(seconds, 60)
    print(f"{mins}:{secs}", end="\r")
    time.sleep(1)
    seconds -= 1

print("Time's up!")