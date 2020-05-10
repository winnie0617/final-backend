# Final Project

## Submission Details

>Names: Jessica Feng (jyf5), Winnie Chow (wc459)
>
>Date: 5/8/2020
>
> Github Repo: https://github.com/winniechow0617/final-backend
>
> Public server IP: http://34.75.155.213/
>
> Project Overview: This application allows users to create recipes, as well as to add ingredients and reviews to the recipes.

## Api Specification


### Get all recipes
> **GET** /api/recipes/
> ```
> Response 
> {
>   "success": true,
>   "data": [
>       {
>           "id": 1,
>           "name": "Scrambled eggs",
>           "instructions": "Beat eggs, milk, salt and pour into frying pen."
>           "time": 20,
>           "ingredients": [<SERIALIZED INGREDIENT WITHOUT RECEIPT FIELD>, ...],
>           "reviews": [<SERIALIZED REVIEW WITHOUT RECEIPT FIELD>, ...]
>       },
>       {
>           "id": 2,
>           "name": "Sushi",
>           "instructions": "Spread the seaweed with a layer of rice."
>           "time": 30,
>           "ingredients": [<SERIALIZED INGREDIENT WITHOUT RECEIPT FIELD>, ...]
>           "reviews": [<SERIALIZED REVIEW WITHOUT RECEIPT FIELD>, ...]
>       }
>       ...
>   ]
> }
> ```

### Create a recipe
> **POST** /api/recipes/
> ```
> Request 
> {
>   "name": <USER INPUT>,
>   "instructions": <USER INPUT>,
>   "time": <USER INPUT>,
> }
>
> Response
> {
>   "success": true,
>   "data": {
>       "id": <ID>,
>       "name": <USER INPUT>,
>       "instructions": <USER INPUT>,
>       "time": <USER INPUT>,
>       "ingredients": [],
>       "reviews": []
>   }
> }
> ```

### Get a specific recipe
> **GET** /api/recipes/{id}/
> ```
> Response
> {
>   "success": true,
>   "data": {
>       "id": <ID>,
>       "name": <USER INPUT FOR NAME>,
>       "instructions": <USER INPUT FOR INSTRUCTIONS>,
>       "time": <USER INPUT FOR TIME>,
>       "ingredients": [<SERIALIZED INGREDIENT WITHOUT RECEIPT FIELD>, ...]
>       "reviews": [<SERIALIZED REVIEW WITHOUT RECEIPT FIELD>, ...]
>   }
> }
> ```

## Delete a specific recipe
> **DELETE** /api/recipes/{id}/
> ```
> Response
> {
>   "success": true,
>   "data": {
>       "id": <ID>,
>       "name": <USER INPUT FOR NAME>,
>       "instructions": <USER INPUT FOR INSTRUCTIONS>,
>       "time": <USER INPUT FOR TIME>,
>       "ingredients": [<SERIALIZED INGREDIENT WITHOUT RECEIPT FIELD>, ...]
>       "reviews": [<SERIALIZED REVIEW WITHOUT RECEIPT FIELD>, ...]
>   }
> }
> ```

### Update a recipe
> **POST** /api/recipes/{id}/
> ```
> Request 
> {
>   "name": <USER INPUT>,
>   "instructions": <USER INPUT>,
>   "time": <USER INPUT>,
> }
>
> Response
> {
>   "success": true,
>   "data": {
>       "id": <ID>,
>       "name": <USER INPUT>,
>       "instructions": <USER INPUT>,
>       "time": <USER INPUT>,
>       "ingredients": [<SERIALIZED INGREDIENT WITHOUT RECEIPT FIELD>, ...]
>       "reviews": [<SERIALIZED REVIEW WITHOUT RECEIPT FIELD>, ...]
>   }
> }
> ```

### Get all ingredients
> **GET** /api/ingredients/
> ```
> Response 
> {
>   "success": true,
>   "data": [
>       {
>           "id": 1,
>           "name": "Egg",
>           "recipes": [<SERIALIZED RECIPE WITHOUT INGREDIENT FIELD>, ...]
>       },
>       {
>           "id": 2,
>           "name": "Chicken",
>           "recipes": [<SERIALIZED RECIPE WITHOUT INGREDIENT FIELD>, ...]
>       }
>       ...
>   ]
> }
> ```

### Create an ingredient
> **POST** /api/ingredients/
> ```
> Request 
> {
>   "name": <USER INPUT>,
> }
>
>Response
> {
>   "success": true,
>   "data": {
>       "id": <ID>,
>       "name": <USER INPUT>,
>       "recipes": []
>   }
> }
> ```

### Get a specific ingredient
> **GET** /api/ingredients/{id}/
> ```
> Response
> {
>   "success": true,
>   "data": {
>       "id": <ID>,
>       "name": <USER INPUT FOR NAME>,
>       "recipes": [<SERIALIZED RECIPE WITHOUT INGREDIENT FIELD>, ...]
>   }
> }
> ```

### Add an ingredient to a recipe
> **POST** /api/recipes/{id}/ingredients/add/
> ```
> Request 
> {
>   "ingredient_id": <USER INPUT>,
> }
>
>Response
> {
>   "success": true,
>   "data": <SERIALIZED RECIPE>
>   }
> }
> ```

## Drop an ingredient from a recipe
> **DELETE** /api/recipes/{id}/ingredients/drop/
> ```
> Response
> {
>   "success": true,
>   "data": {
>       "id": <ID>,
>       "name": <USER INPUT FOR NAME>,
>       "recipes": [<SERIALIZED RECIPE WITHOUT INGREDIENT FIELD>, ...]
>   }
> }

### Create a review
> **POST** /api/recipes/{id}/review/
> ```
> Request 
> {
>   "name": <USER INPUT>,
>   "rating": <USER INPUT>
> }
>
>Response
> {
>   "success": true,
>   "data": {
>       "id": <ID>,
>       "name": <USER INPUT FOR NAME>,
>       "rating": <USER INPUT FOR REGION>,
>       "recipe": <RECIPE>
>   }
> }
> ```

### Get a specific review
> **GET** /api/reviews/{id}/
> ```
> Response
> {
>   "success": true,
>   "data": {
>       "id": <ID>,
>       "name": <USER INPUT FOR NAME>,
>       "rating": <USER INPUT FOR REGION>,
>       "recipe": <RECIPE>
>   }
> }
> ```

### Delete a specific review
> **DELETE** /api/reviews/{id}/
> ```
> Response
> {
>   "success": true,
>   "data": {
>       "id": <ID>,
>       "name": <USER INPUT FOR NAME>,
>       "instructions": <USER INPUT FOR INSTRUCTIONS>,
>       "time": <USER INPUT FOR TIME>,
>       "ingredients": [<SERIALIZED INGREDIENT WITHOUT RECEIPT FIELD>, ...]
>       "reviews": [<SERIALIZED REVIEW WITHOUT RECEIPT FIELD>, ...]
>   }
> }
> ```

### Update a review
> **POST** /api/reviews/{id}/
> ```
> Request 
> {
>   "name": <USER INPUT>,
>   "rating": <USER INPUT>
> }
>
>Response
> {
>   "success": true,
>   "data": {
>       "id": <ID>,
>       "name": <USER INPUT FOR NAME>,
>       "rating": <USER INPUT FOR REGION>,
>       "recipe": <RECIPE>
>   }
> }
> ```