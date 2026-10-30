customer_1 = {
    "customer_id": "C1002",
    "first_name": "James",
    "last_name": "Carter",
    "date_of_birth": "1978-07-25",
    "address": "456 Oak St, Chicago, IL 60601",
    "phone": "555-0102",
    "email": "james.carter@example.com",
    "account_type": "Savings",
    "account_number": "XXXX-1002",
    "balance": 18250.00,
    "credit_score": 785,
    "has_loan": False,
}
customer_2 = {
    "customer_id": "C1001",
    "first_name": "Maria",
    "last_name": "Lopez",
    "date_of_birth": "1985-03-12",
    "address": "123 Palm Ave, Miami, FL 33101",
    "phone": "555-0101",
    "email": "maria.lopez@example.com",
    "account_type": "Checking",
    "account_number": "XXXX-1001",
    "balance": 4520.75,
    "credit_score": 720,
    "has_loan": False,
}


customer_3 = {
    "customer_id": "C1003",
    "first_name": "Aisha",
    "last_name": "Khan",
    "date_of_birth": "1992-11-03",
    "address": "789 Pine Rd, Houston, TX 77002",
    "phone": "555-0103",
    "email": "aisha.khan@example.com",
    "account_type": "Checking",
    "account_number": "XXXX-1003",
    "balance": 932.40,
    "credit_score": 650,
    "has_loan": False,
}

customer_4 = {
    "customer_id": "C1004",
    "first_name": "David",
    "last_name": "Nguyen",
    "date_of_birth": "1969-01-30",
    "address": "321 Maple Dr, Los Angeles, CA 90012",
    "phone": "555-0104",
    "email": "david.nguyen@example.com",
    "account_type": "Savings",
    "account_number": "XXXX-1004",
    "balance": 56780.15,
    "credit_score": 790,
    "has_loan": True,
}

customer_5 = {
    "customer_id": "C1005",
    "first_name": "Emily",
    "last_name": "Brooks",
    "date_of_birth": "2001-05-18",
    "address": "654 Cedar Ln, New York, NY 10001",
    "phone": "555-0105",
    "email": "emily.brooks@example.com",
    "account_type": "Checking",
    "account_number": "XXXX-1005",
    "balance": 1275.60,
    "credit_score": 610,
    "has_loan": False,
}

customers = [customer_1, customer_2, customer_3, customer_4, customer_5]
print("\n")
for customer in customers:
    if customer["credit_score"]>=750 and customer["balance"]>=10000 and customer["has_loan"]==False:
        print(
            f"Hi {customer['first_name']}! You are welcome to apply for our platinum credit card, with a credit limit of up to $25,000.")
    elif customer["credit_score"]>=650 and customer["has_loan"]==False:
        customer["has_loan"]=True
        print(f"\n{customer['first_name']}, you are qualified to apply for a loan with our bank.")
print("\n")        
