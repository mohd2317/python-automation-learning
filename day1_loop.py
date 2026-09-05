ticket_id = input("Enter ticket ID: ")
retry_count = int(input("Retry: "))

print(f"Starting retry process for ticket {ticket_id}")

for attempt_num in range(1, retry_count + 1):
    print(f"Retry attempt {attempt_num} for ticket {ticket_id}")

    # Mini Challenge
    if attempt_num == 3:
        print("Final retry attempt reached.")

print("Retry process completed.")