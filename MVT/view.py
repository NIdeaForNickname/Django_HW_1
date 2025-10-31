from template import Templates

class RecipeView:
    def __init__(self, model):
        self.model = model

    def list_recipes(self):
        recipes = self.model.get_all()
        print(Templates.recipe_list(recipes))

    def show_recipe(self, recipe_id):
        recipe = self.model.get_by_id(recipe_id)
        if recipe:
            print(Templates.recipe_detail(recipe))
        else:
            print("Not found")

    def add_recipe(self, title, description, ingredients, instructions):
        self.model.add(title, description, ingredients, instructions)
        print("Recipe added")

    def edit_recipe(self, recipe_id, title, description, ingredients, instructions):
        self.model.edit_recipe(recipe_id, title, description, ingredients, instructions)
        print("Recipe updated")

    def delete_recipe(self, recipe_id):
        self.model.delete_recipe(recipe_id)
        print("Recipe deleted")
