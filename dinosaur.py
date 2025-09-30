# Dinosaur Facts Program

# Dictionary of dinosaurs and their facts
dinosaurs = {
    "Tyrannosaurus Rex": {
        "Period": "Late Cretaceous",
        "Diet": "Carnivore",
        "Length": "40 feet",
        "Fact": "The T. Rex had the strongest bite of any land animal that ever lived!"
    },
    "Triceratops": {
        "Period": "Late Cretaceous",
        "Diet": "Herbivore",
        "Length": "30 feet",
        "Fact": "Triceratops had three horns and a huge bony frill to protect its neck."
    },
    "Velociraptor": {
        "Period": "Late Cretaceous",
        "Diet": "Carnivore",
        "Length": "6.8 feet",
        "Fact": "Velociraptors were feathered and hunted in packs."
    },
    "Brachiosaurus": {
        "Period": "Late Jurassic",
        "Diet": "Herbivore",
        "Length": "85 feet",
        "Fact": "Brachiosaurus had longer front legs than back legs and a very long neck."
    },
    "Stegosaurus": {
        "Period": "Late Jurassic",
        "Diet": "Herbivore",
        "Length": "30 feet",
        "Fact": "Stegosaurus had a small brain and large plates along its back."
    }
}

def show_menu():
    print("\n🦕 Welcome to the Dinosaur Facts Program!")
    print("Choose a dinosaur to learn more:")
    for i, dino in enumerate(dinosaurs.keys(), 1):
        print(f"{i}. {dino}")
    print("0. Exit")

def show_dinosaur_info(choice):
    dino_name = list(dinosaurs.keys())[choice - 1]
    dino_info = dinosaurs[dino_name]
    print(f"\n📘 {dino_name}")
    for key, value in dino_info.items():
        print(f"{key}: {value}")

# Main loop
while True:
    show_menu()
    try:
        user_choice = int(input("Enter your choice: "))
        if user_choice == 0:
            print("Goodbye! Keep exploring the prehistoric world! 🌍")
            break
        elif 1 <= user_choice <= len(dinosaurs):
            show_dinosaur_info(user_choice)
        else:
            print("Invalid choice. Please choose a number from the menu.")
    except ValueError:
        print("Please enter a valid number.")
