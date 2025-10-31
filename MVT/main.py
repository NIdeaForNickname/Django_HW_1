from model import RecipeRepo
from view import RecipeView

def main():
    model = RecipeRepo()
    view = RecipeView(model)

    while True:
        print("\n1. Show all recipes")
        print("2. View recipe by ID")
        print("3. Add Recipe")
        print("4. Change Recipe")
        print("5. Remove Recipe")

        choice = input("Action: ")

        if choice == '1':
            view.list_recipes()

        elif choice == '2':
            rid = int(input("ID: "))
            view.show_recipe(rid)

        elif choice == '3':
            title = input("Name: ")
            desc = input("Description: ")
            ingr = input("Ingredients: ")
            instr = input("Instructions: ")
            view.add_recipe(title, desc, ingr, instr)

        elif choice == '4':
            rid = int(input("ID: "))
            title = input("Name: ")
            desc = input("Description: ")
            ingr = input("Ingredients: ")
            instr = input("Instructions: ")
            view.edit_recipe(rid, title, desc, ingr, instr)

        elif choice == '5':
            rid = int(input("ID: "))
            view.delete_recipe(rid)


if __name__ == "__main__":
    main()
