with open("../inputs/day21") as fp:
    lines = fp.read().splitlines()

food_dict = {}
safe_ingredient = set()
all_ingredients = []
for food in lines:
    ingredients, allergens = food.split(" (contains ")
    allergens = allergens[:-1]
    ingredients = ingredients.split(" ")
    all_ingredients.extend(ingredients)
    unique_in = set(ingredients)
    safe_ingredient=safe_ingredient.union(unique_in)
    allergens = allergens.split(", ")

    for allergen in allergens:
        if food_dict.get(allergen) is None:
            food_dict[allergen] = unique_in
        else:
            food_dict[allergen] = food_dict[allergen].intersection(unique_in)

safe_ingredient = safe_ingredient.difference(set(k for value in food_dict.values() for k in value))
safe_count = sum([ingredient in safe_ingredient for ingredient in all_ingredients])
print(f"Safe ingredients: {safe_count}")


while any([len(i) > 1 for i in food_dict.values()]):
    for a, i in food_dict.items():
        if len(i) == 1:
            alg = list(i)[0]
            for a2, i2 in food_dict.items():
                if a2 == a:
                    continue
                if len(i2) > 1:
                    if alg in i2:
                        food_dict[a2].remove(alg)


names = list(food_dict.keys())
names.sort()
print("My dangerous list: ", ",".join([",".join(food_dict[i]) for i in names]))