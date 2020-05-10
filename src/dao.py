from db1 import db

from db1 import db, Recipe, Ingredient, Review


def get_all_recipes():
    return [r.serialize() for r in Recipe.query.all()]


def create_recipe(name, instructions, time):
    new_recipe = Recipe(
        name=name,
        instructions=instructions,
        time=time
    )
    db.session.add(new_recipe)
    db.session.commit()
    return new_recipe.serialize()


def get_recipe_by_id(recipe_id):
    recipe = Recipe.query.filter_by(id=recipe_id).first()
    if recipe is None:
        return None
    return recipe.serialize()


def delete_recipe_by_id(recipe_id):
    recipe = Recipe.query.filter_by(id=recipe_id).first()
    if recipe is None:
        return None
    db.session.delete(recipe)
    db.session.commit()
    return recipe.serialize()


def update_recipe_by_id(recipe_id, body):
    recipe = Recipe.query.filter_by(id=recipe_id).first()
    if recipe is None:
        return None
    recipe.name = body.get('name', recipe.name)
    recipe.instructions = body.get('instructions', recipe.instructions)
    recipe.time = body.get('time', recipe.time)
    db.session.commit()
    return recipe.serialize()


def get_all_ingredients():
    return [i.serialize() for i in Ingredient.query.all()]


def create_ingredient(name):
    new_ing = Ingredient(
        name=name
    )
    db.session.add(new_ing)
    db.session.commit()
    return new_ing.serialize()


def get_ingredient_by_id(ing_id):
    ingredient = Ingredient.query.filter_by(id=ing_id).first()
    if ingredient is None:
        return None
    return ingredient.serialize()


def delete_ingredient_by_id(ing_id):
    ingredient = Ingredient.query.filter_by(id=ing_id).first()
    if ingredient is None:
        return None
    db.session.delete(ingredient)
    db.session.commit()
    return ingredient.serialize()

# add ingredient to a recipe


def add_ingredient_to_recipe(recipe_id, ingredient_id):
    ingredient = Ingredient.query.filter_by(id=ingredient_id).first()
    msg = "Success!"
    if ingredient is None:
        msg = "Ingredient not found!"
        return None, msg
    recipe = Recipe.query.filter_by(id=recipe_id).first()
    if recipe is None:
        msg = "Recipe not found!"
        return None, msg
    recipe.ingredients.append(ingredient)
    db.session.commit()
    return recipe.serialize(), msg


def drop_ingredient_from_recipe(recipe_id, ingredient_id):
    ingredient = Ingredient.query.filter_by(id=ingredient_id).first()
    msg = "Success!"
    if ingredient is None:
        msg = "Ingredient not found!"
        return None, msg
    recipe = Recipe.query.filter_by(id=recipe_id).first()
    if recipe is None:
        msg = "Recipe not found!"
        return recipe, msg
    try:
        recipe.ingredients.remove(ingredient)
    except ValueError:
        msg = "Ingredient has not been added to this recipe"
    db.session.commit()
    return ingredient.serialize(), msg


# def get_assignment_by_id(assignment_id):
#     assignment = Assignment.query.filter_by(id=assignment_id).first()
#     if assignment is None:
#         return None
#     return assignment.serialize()

def create_review(name, rating, recipe_id):
    recipe = Recipe.query.filter_by(id=recipe_id).first()
    if recipe is None:
        return None
    review = Review.query.filter_by(name=name).first()
    if review is not None:
        return review.serialize()
    new_review = Review(
        name=name,
        rating=rating,
        recipe_id=recipe_id
    )
    db.session.add(new_review)
    db.session.commit()
    return new_review.serialize()


def get_review_by_id(review_id):
    review = Review.query.filter_by(id=review_id).first()
    if review is None:
        return None
    return review.serialize()


def delete_review_by_id(review_id):
    review = Review.query.filter_by(id=review_id).first()
    if review is None:
        return None
    db.session.delete(review)
    db.session.commit()
    return review.serialize()


def update_review_by_id(review_id, body):
    review = Review.query.filter_by(id=review_id).first()
    if review is None:
        return None
    review.name = body.get('name', review.name)
    review.rating = body.get('rating', review.rating)
    db.session.commit()
    return review.serialize()

