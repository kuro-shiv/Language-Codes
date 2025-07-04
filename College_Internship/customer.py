class Customer_object:
    def Customer_details(self, customer_id, name, email):
        self.customer_id = customer_id
        self.customer_name = name
        self.customer_email = email

    def display_info(self):
        print(f"\nCustomer Name: {self.customer_name}")
        print(f"Customer ID: {self.customer_id}")
        print(f"Customer Email: {self.customer_email}")

    # take data input from user
    def get_data(self):
        customer_id = int(input("Enter Customer ID: "))
        name = input("Enter Customer Name: ")
        email = input("Enter Customer Email: ")

        # store data in object
        self.Customer_details(customer_id, name, email)


# create an object and take customer data
customer = Customer_object()

# perform operations
customer.get_data()
customer.display_info()



