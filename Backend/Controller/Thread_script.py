import threading


count = 0

def worker():
    """Thread worker function"""
    global count 
    for i in range(1000):
       count += 1
       print(count)

# Create threads
t1 = threading.Thread(target=worker)
t2 = threading.Thread(target=worker)

# Start threads
t1.start()
t2.start()

# Wait for threads to complete
t1.join()
t2.join()
