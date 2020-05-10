from flask import Flask, request
from db1 import db
import json
import dao
import os

app = Flask(__name__)
db_filename = "cooking.db"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///%s" % db_filename
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

db.init_app(app)
with app.app_context():
    db.create_all()


def success_response(data, code=200):
    return json.dumps({"success": True, "data": data}), code


def failure_response(message, code=404):
    return json.dumps({"success": False, "error": message}), code


# your routes here
@app.route('/')
def hello_world():
    return os.environ["SECRET_KEY"], 200


@app.route('/api/recipes/')  # GET all recipes
def get_recipes():
    return success_response(dao.get_all_recipes())


@app.route('/api/recipes/', methods=['POST'])  # POST a recipe
def create_recipe():
    body = json.loads(request.data)
    recipe = dao.create_recipe(
        name=body.get('name'),
        instructions=body.get('instructions'),
        time=body.get('time')
    )
    return success_response(recipe, 201)


@app.route('/api/recipes/<int:recipe_id>/')  # GET a recipe
def get_recipe(recipe_id):
    recipe = dao.get_recipe_by_id(recipe_id)
    if recipe is None:
        return failure_response("Recipe not found!")
    return success_response(recipe)


# DELETE a recipe
@app.route('/api/recipes/<int:recipe_id>/', methods=['DELETE'])
def delete_recipe(recipe_id):
    recipe = dao.delete_recipe_by_id(recipe_id)
    if recipe is None:
        return failure_response("Recipe not found!")
    return success_response(recipe)

# UPDATE a recipe
@app.route('/api/recipes/<int:recipe_id>/', methods=['POST'])
def update_recipe(recipe_id):
    body = json.loads(request.data)
    recipe = dao.update_recipe_by_id(recipe_id, body)
    if recipe is None:
        return failure_response("Recipe not found!")
    return success_response(recipe)

# ----------INGREDIENTS/USER------------------
@app.route('/api/ingredients/')  # GET all ingredients
def get_ingredients():
    return success_response(dao.get_all_ingredients())


@app.route('/api/ingredients/', methods=['POST'])  # POST an ingredient
def create_ingredient():
    body = json.loads(request.data)
    ing = dao.create_ingredient(
        name=body.get('name'),
    )
    return success_response(ing, 201)


@app.route('/api/ingredients/<int:ing_id>/')  # GET an ingredient
def get_ingredient(ing_id):
    ingredient = dao.get_ingredient_by_id(ing_id)
    if ingredient is None:
        return failure_response("Ingredient not found!")
    return success_response(ingredient)

# UPDATING recipe
# ADD a ingredient to a recipe
@app.route('/api/recipes/<int:recipe_id>/add/', methods=['POST'])
def add_ingredient(recipe_id):
    body = json.loads(request.data)
    # need to change the rest
    ing_id = body.get('ingredient_id')
    recipe, msg = dao.add_ingredient_to_recipe(recipe_id, ing_id)
    if recipe is None:
        return failure_response(msg)
    return success_response(recipe)


# DELETE an ingredient from a recipe
@app.route('/api/recipes/<int:recipe_id>/drop/', methods=['POST'])
def drop_ingredient(recipe_id):
    recipe = dao.get_recipe_by_id(recipe_id)
    if recipe is None:
        return failure_response("Recipe not found!")
    body = json.loads(request.data)
    ing_id = body.get('ingredient_id')
    ingredient, msg = dao.drop_ingredient_from_recipe(recipe_id, ing_id)
    if ingredient is None:
        return failure_response(msg)
    return success_response(ingredient)

# ---------------REVIEWS--------------


# CREATE a review
@app.route('/api/recipes/<int:recipe_id>/review/', methods=['POST'])
def create_review(recipe_id):
    recipe = dao.get_recipe_by_id(recipe_id)
    if recipe is None:
        return failure_response("Recipe not found!")
    body = json.loads(request.data)
    review = dao.create_review(
        body.get('name'),
        body.get('rating'),
        recipe_id
    )
    return success_response(review, 201)


@app.route('/api/reviews/<int:review_id>/')  # GET a review
def get_review(review_id):
    review = dao.get_review_by_id(review_id)
    if review is None:
        return failure_response("Review not found!")
    return success_response(review)


# DELETE a review
@app.route('/api/reviews/<int:review_id>/', methods=['DELETE'])
def delete_review(review_id):
    review = dao.delete_review_by_id(review_id)
    if review is None:
        return failure_response("Review not found!")
    return success_response(review)

# UPDATE a review
@app.route('/api/reviews/<int:review_id>/', methods=['POST'])
def update_review(review_id):
    body = json.loads(request.data)
    review = dao.update_review_by_id(review_id, body)
    if review is None:
        return failure_response("Review not found!")
    return success_response(review)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
