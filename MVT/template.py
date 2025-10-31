class Templates:
    @staticmethod
    def recipe_list(recipes):
        output = "- All Recipes "
        for r in recipes:
            output += f"ID: {r.id} - {r.title}"
        return output

    @staticmethod
    def recipe_detail(recipe):
        return f"""
- {recipe.title} 
Description: 
{recipe.description}

Ingredients:
{recipe.ingredients}

Instructions:
{recipe.instructions}
"""