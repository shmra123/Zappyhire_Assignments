from utils import add_district, get_district, modify_district, remove_district

def user_flow():
    while True:
        print("\nChoose an action:")
        print("1. Add")
        print("2. Get")
        print("3. Modify")
        print("4. Remove")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter the name of the district to add: ")
            add_district({'name': name})
        elif choice == '2':
            district_id = int(input("Enter the ID of the district to retrieve: "))
            district = get_district(district_id)
            if district:
                print("Retrieved district:", district)
            else:
                print("District not found.")
        elif choice == '3':
            district_id = int(input("Enter the ID of the district to modify: "))
            new_name = input("Enter the new name for the district: ")
            modify_district(district_id, new_name)
        elif choice == '4':
            district_id = int(input("Enter the ID of the district to remove: "))
            remove_district(district_id)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    user_flow()
