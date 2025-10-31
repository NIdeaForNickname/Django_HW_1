import json


class Recipe:
    def __init__(self, id, title, description, ingredients, instructions):
        self.id = id
        self.title = title
        self.description = description
        self.ingredients = ingredients
        self.instructions = instructions


class RecipeRepo:
    FILE = "recipes.json"

    def __init__(self):
        self.recipes = []
        self.next_id = 1
        self.load()

    def load(self):
        with open(self.FILE, "r") as recipes_file:
            recipes = json.load(recipes_file)
            for recipe in recipes:
                recipe = Recipe(**recipe)
                self.recipes.append(recipe)
            if self.recipes:
                self.next_id = self.recipes[-1].id + 1

    def save(self):
        with open(self.FILE, "w") as recipes_file:
            json.dump([r.__dict__ for r in self.recipes], recipes_file)

    def add(self, title, description, ingredients, instructions):
        recipe = Recipe(self.next_id, title, description, ingredients, instructions)
        self.recipes.append(recipe)
        self.next_id += 1
        self.save()

    def delete(self, recipe_id):
        self.recipes = [x for x in self.recipes if x.id != recipe_id]
        self.save()

    def edit(self, recipe_id, title, description, ingredients, instructions):
        for r in self.recipes:
            if r.id == recipe_id:
                r.title = title
                r.description = description
                r.ingredients = ingredients
                r.instructions = instructions
                break
        self.save()

    def get_all(self):
        return list(self.recipes)

    def get_by_id(self, recipe_id):
        return next((x for x in self.recipes if x.id == recipe_id), None)
