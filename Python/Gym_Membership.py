import mysql.connector
from mysql.connector import Error

# Function to create a MySQL connection
def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='saurav2484',
            database='gym_management'
        )
        if connection.is_connected():
            print("Connected to MySQL database")
    except Error as e:
        print(f"Error: {e}")
    return connection

# Function to execute SQL queries
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()

# Function to display both members and memberships
def display_members_and_memberships(connection):
    # Display Members
    display_members(connection)

    # Display Memberships
    display_memberships(connection)

# Function to retrieve and display members
def display_members(connection):
    query = "SELECT * FROM Members"
    cursor = connection.cursor()
    cursor.execute(query)
    members = cursor.fetchall()
    cursor.close()

    if members:
        print("Members:")
        for member in members:
            print(member)
    else:
        print("No members found.")

# Function to display membership plans
def display_membership_plans(connection):
    query = "SELECT * FROM MembershipPlans"
    cursor = connection.cursor()
    cursor.execute(query)
    plans = cursor.fetchall()
    cursor.close()

    if plans:
        print("Membership Plans:")
        for plan in plans:
            # Explicitly access the price using the correct index
            print(f"PlanID: {plan[0]}, PlanName: {plan[1]}, Description: {plan[2]}, Duration: {plan[3]} months")
    else:
        print("No membership plans found.")


# Function to display memberships
def display_memberships(connection):
    query = "SELECT * FROM Memberships"
    cursor = connection.cursor()
    cursor.execute(query)
    memberships = cursor.fetchall()
    cursor.close()

    if memberships:
        print("Memberships:")
        for membership in memberships:
            print(membership)
    else:
        print("No memberships found.")

# Function to add a new member and membership
def add_member_and_membership(connection):
    print("\nEnter Member Details:")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    gender = input("Gender: ")
    dob = input("Date of Birth (YYYY-MM-DD): ")
    contact_number = input("Contact Number: ")
    email = input("Email: ")
    address = input("Address: ")

    query_member = f"INSERT INTO Members (FirstName, LastName, Gender, DateOfBirth, ContactNumber, Email, Address) VALUES " \
                   f"('{first_name}', '{last_name}', '{gender}', '{dob}', '{contact_number}', '{email}', '{address}')"
    execute_query(connection, query_member)
    print(f"{first_name} {last_name} added as a new member.")

    display_membership_plans(connection)
    plan_id = int(input("Enter the Plan ID: "))
    start_date = input("Enter the Start Date (YYYY-MM-DD): ")
    end_date = input("Enter the End Date (YYYY-MM-DD): ")
    renewal_date = input("Enter the Renewal Date (YYYY-MM-DD): ")

    query_membership = f"INSERT INTO Memberships (MemberID, PlanID, StartDate, EndDate, RenewalDate) " \
                       f"VALUES ((SELECT MAX(MemberID) FROM Members), {plan_id}, '{start_date}', '{end_date}', '{renewal_date}')"
    execute_query(connection, query_membership)
    print("Membership added.")

# Function to delete a member and their membership
def delete_member_and_membership(connection):
    display_members(connection)
    member_id = input("Enter the Member ID to delete: ")

    query_member = f"DELETE FROM Members WHERE MemberID = {member_id}"
    execute_query(connection, query_member)
    print(f"Member with ID {member_id} deleted.")

    query_membership = f"DELETE FROM Memberships WHERE MemberID = {member_id}"
    execute_query(connection, query_membership)
    print(f"Membership for Member ID {member_id} deleted.")

# Main function
def main():
    connection = create_connection()

    if connection:
        while True:
            print("\nMenu:")
            print("1. Display Members and Memberships")
            print("2. Display Membership Plans")
            print("3. Add Member and Membership")
            print("4. Delete Member and Membership")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                display_members_and_memberships(connection)
            elif choice == '2':
                display_membership_plans(connection)
                print("Price for Basic is 1400")
                print("Price for Premium is 3700")
            elif choice == '3':
                add_member_and_membership(connection)
            elif choice == '4':
                delete_member_and_membership(connection)
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

        connection.close()
        print("Connection closed.")

if __name__ == "__main__":
    main()
