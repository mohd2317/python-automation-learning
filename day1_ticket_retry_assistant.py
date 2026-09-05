ticket_id = input("Enter Ticket ID: ")
current_status = input("Current Status: ")
retry_count = int(input("Retry: "))

if current_status == "Resolved":
    print(f"No retry is required for ticket id {ticket_id}")
elif retry_count > 0 :

    for retry_attempt in range(1, retry_count+1):
        print(f"Retry attempt {retry_attempt} for ticket {ticket_id}")
else:
    print(f"Ticket {ticket_id} has no retries remaining. Esclate for manual review.")    