from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# many-to-many relationship

association_table = db.Table('association_table', db.Model.metadata,
                             db.Column('recipe_id', db.Integer,
                                       db.ForeignKey('recipe.id')),
                             db.Column('ingredient_id', db.Integer,
                                       db.ForeignKey('ingredient.id'))
                             )


class Recipe(db.Model):
    __tablename__ = 'recipe'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    instructions = db.Column(db.String, nullable=False)
    time = db.Column(db.Integer, nullable=False)
    reviews = db.relationship('Review', cascade='delete')
    ingredients = db.relationship(
        'Ingredient', secondary=association_table, back_populates='recipes')

    def __init__(self, **kwargs):
        self.name = kwargs.get('name', '')
        self.instructions = kwargs.get('instructions', '')
        self.time = kwargs.get('time', 30)

    def serialize_info(self):
        return{
            'id': self.id,
            'name': self.name,
            'instructions': self.instructions,
            'time': self.time
        }

    def serialize(self):
        return{
            'id': self.id,
            'name': self.name,
            'instructions': self.instructions,
            'time': self.time,
            'ingredients': [i.serialize_ing() for i in self.ingredients],
            'reviews': [r.serialize_review() for r in self.reviews]
        }


class Ingredient(db.Model):
    __tablename__ = 'ingredient'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    recipes = db.relationship(
        'Recipe', secondary=association_table, back_populates='ingredients')

    def __init__(self, **kwargs):
        self.name = kwargs.get('name', '')

    def serialize_ing(self):
        return{
            'id': self.id,
            'name': self.name
        }

    def serialize(self):
        return{
            'id': self.id,
            'name': self.name,
            'recipes': [r.serialize_info() for r in self.recipes]
        }


class Review(db.Model):
    __tablename__ = 'review'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey(
        'recipe.id'), nullable=False)

    def __init__(self, **kwargs):
        self.name = kwargs.get('name', '')
        self.rating = kwargs.get('rating', '')
        self.recipe_id = kwargs.get('recipe_id')

    def serialize_review(self):
        return {
            'id': self.id,
            'name': self.name,
            'rating': self.rating
        }

    def serialize(self):
        recipe = Recipe.query.filter_by(id=self.recipe_id).first()
        if recipe is not None:
            recipe = recipe.serialize_info()
        return{
            'id': self.id,
            'name': self.name,
            'rating': self.rating,
            'recipe': recipe
        }
