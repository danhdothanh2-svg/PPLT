# ================= PET CLASS =================
class Pet:
    def __init__(self, pet_id, name, species, price):
        self.__pet_id = pet_id
        self.__name = name
        self.__species = species
        self.__price = price

    def get_pet_id(self):
        return self.__pet_id

    def get_name(self):
        return self.__name

    def get_species(self):
        return self.__species

    def get_price(self):
        return self.__price

    def display_info(self):
        print(f"Pet ID : {self.__pet_id}")
        print(f"Name   : {self.__name}")
        print(f"Species: {self.__species}")
        print(f"Price  : ${self.__price}")
        print("----------------------------")


# ================= STORE SERVICE CLASS =================
class StoreService:
    def __init__(self):
        self.inventory = []
        self.revenue = 0.0

    def add_pet(self, pet):
        self.inventory.append(pet)
        print("Pet added successfully!")

    def view_inventory(self):
        if len(self.inventory) == 0:
            print("Inventory is empty.")
            return

        print("\n===== PET INVENTORY =====")

        for pet in self.inventory:
            pet.display_info()

    def sell_pet(self, pet_id):
        for pet in self.inventory:

            if pet.get_pet_id() == pet_id:
                self.inventory.remove(pet)

                self.revenue += pet.get_price()

                print(f"{pet.get_name()} sold successfully!")
                return

        print("Pet not found.")

    def view_revenue(self):
        print(f"Total Revenue: ${self.revenue}")


# ================= VIEWS LAYER =================
class ConsoleView:
    def __init__(self):
        self.store_service = StoreService()

    def run(self):

        while True:
            print("\n===== PET STORE MENU =====")
            print("1. Add a new pet")
            print("2. View inventory")
            print("3. Sell a pet")
            print("4. View total revenue")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                pet_id = input("Enter Pet ID: ")
                name = input("Enter Pet Name: ")
                species = input("Enter Species: ")
                price = float(input("Enter Price: "))
                pet = Pet(pet_id, name, species, price)
                self.store_service.add_pet(pet)
            elif choice == "2":
                self.store_service.view_inventory()
            elif choice == "3":
                pet_id = input("Enter Pet ID to sell: ")
                self.store_service.sell_pet(pet_id)
            elif choice == "4":
                self.store_service.view_revenue()
            elif choice == "5":
                print("Exiting program...")
                break
            else:
                print("Invalid choice. Please try again.")


# ================= MAIN PROGRAM =================
view = ConsoleView()
view.run()