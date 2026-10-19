
stack1 = []
stack2 = []

def add_request():
    request = input("Enter web request: ")
    stack1.append(request)
    print("Request added successfully!")

def process_request():
    if not stack2:
        while stack1:
            stack2.append(stack1.pop())

    if not stack2:
        print("No requests to process.")
    else:
        print("Processing request:", stack2.pop())

def display_requests():
    requests = stack2[::-1] + stack1

    if not requests:
        print("No pending requests.")
    else:
        print("Pending requests:")
        for request in requests:
            print(request)

while True:
    print("\n--- Web Server Request System ---")
    print("1. Add Request")
    print("2. Process Request")
    print("3. Display Requests")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_request()
    elif choice == "2":
        process_request()
    elif choice == "3":
        display_requests()
    elif choice == "4":
        print("Web server stopped.")
        break
    else:
        print("Invalid choice. Try again.")
