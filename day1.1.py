ticket_id = input("Enter ticket ID: ")
assigned_to = input("Assigned to: ")
# retry_count = input("Enter retry count: ")
retry_count = int(input("enter retry count: "))
environment = input("Enter environment: ")

print(f"Ticket {ticket_id} is assigned to {assigned_to} and will retry {retry_count} time(s). environment is {environment}")