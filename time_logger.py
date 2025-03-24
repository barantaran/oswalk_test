import time

def start_time():
    """Start timing and return the start time"""
    start = time.time()
    return start

def stop_time(start_time):
    """Stop timing and print execution time"""
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution completed in: {execution_time:.4f} seconds")
    return execution_time
