ticket_id = input("Enter ticket ID: ")
current_status = input("Current Status: ")
retry_count = int(input("retry"))

if current_status == "Resolved":
    print(f"Ticket {ticket_id} is already resolved. No retry required.")
elif retry_count > 0:
    print(f"Ticket {ticket_id} will be retried. Remaining retries: {retry_count}")
else:
    print(f"Ticket {ticket_id} has no retries remaining. Escalate for manual review")    