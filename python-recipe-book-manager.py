
import os

def get_recipe_name():
    # loop until a valid recipe name is entered
    while True:
        print()
        recipe_name = input("Enter the Recipe Name (or type 'back' to return): ").strip()
        
        # allow user to go back to previous menu
        if recipe_name.lower() == "back":
            return None
        
        # empty input check
        if recipe_name == "":
            print("The recipe name cannot be empty or contain only spaces.")
            continue
        
        # length validation (3 - 50 characters)
        if len(recipe_name) < 3 or len(recipe_name) > 50:
            print("The recipe name must be between 3 and 50 characters.")
            continue
        
        # ensure at least one letter exists
        if not any(character.isalpha() for character in recipe_name):
            print("The recipe name must contain at least one letter.")
            continue
        
        # validate allowed characters (letters, numbers, space, -, ')
        for character in recipe_name:
            if not (character.isalnum() or character in ["-", "'", " "]):
                print(f"Invalid Character ---> {character}")
                print("  The recipe name should contain only letters, numbers, spaces, hyphens(-) or apostrophes(').")
                break
        else:
            # all validations passed
            return recipe_name
        

    
def ask_to_continue(ingredients):
    # user decide whether to add another ingredient
    while True:
        print()
        choice = input("Do you want to add another ingredient? (yes/no): ").strip().lower()
        
        if choice == "no":
            return False
        
        elif choice == "yes":
            return True
        
        else:
            print("Please enter yes or no.")
            
                       

def get_ingredients():
    ingredients = []
    # allowed measurement units
    allowed_units = ["g", "kg", "ml", "l", "cup", "tbsp", "tsp", "piece"]
    
    print()
    print("Each recipe requires at least 3 ingredients, maximum 20.")
    print(" Valid units are: g, kg, ml, l, cup, tbsp, tsp, piece")

    while True:
        ingredient_input = input("Enter the ingredient as (ingredient name, quantity, unit): ")
        ingredient_parts_list = ingredient_input.split(",")
        
        # ensure correct input format (3 comma-separated values)
        if len(ingredient_parts_list) != 3:
            print("Invalid format! Please use: ingredient name, quantity, unit.")
            continue
        
        ingredient_name     = ingredient_parts_list[0].strip()
        ingredient_quantity = ingredient_parts_list[1].strip()
        ingredient_unit     = ingredient_parts_list[2].strip().lower()
        
        # ingredient name length check
        if len(ingredient_name) < 3 or len(ingredient_name) > 30:
            print("Ingredient name must be between 3 and 30 characters.")
            continue
        
        # must have at least one letter
        if not any(character.isalpha() for character in ingredient_name):
            print("Ingredient name must contain at least one letter.")
            continue
        
        # validate allowed characters in name
        invalid_char = list(set(char for char in ingredient_name if not (char.isalnum() or char in ["-", "'", " "])))
        if invalid_char:
            print("Invalid character in ingredient name: ({})".format(",".join(invalid_char)))
            continue
            
        
        # check if the same ingredient was already added
        allow_duplicate = True
        for ingredient in ingredients:
            if ingredient_name.lower() == ingredient[0].lower():
                while True:
                    print()
                    user_choice = input("  This ingredient already exists. Do you want to add it again? (yes/no): ").strip().lower()
                    
                    if user_choice == "yes":
                        allow_duplicate = True
                        break
                    elif user_choice == "no":
                        allow_duplicate = False
                        break
                    else:
                        print("Invalid input. Please enter yes or no.")
                break
                        
        if not allow_duplicate:
            # stop early if user declines duplicate and chooses to exit
            if not ask_to_continue(ingredients):
                return ingredients
            continue
        
        # quantity must be a positive number
        try:
            quantity_value = float(ingredient_quantity)
            if quantity_value <= 0:
                print("The quantity must be a positive number.")
                continue
        except ValueError:
            print("The quantity must be a number.")
            continue
        
        # validate measurement unit
        if ingredient_unit not in allowed_units:
            print("Invalid unit! Allowed units:", ", ".join(allowed_units))
            continue
        
        # store valid ingredient as a tuple
        ingredients.append((ingredient_name, quantity_value, ingredient_unit))
        print(f"\n  '{ingredient_name}' added!")
        
        # allow user to stop after minimum required ingredients
        if len(ingredients) >= 3:
            if not ask_to_continue(ingredients):
                return ingredients
                     
        # enforce maximum ingredient limit             
        if len(ingredients) == 20:
            print("You have reached the maximum of 20 ingredients.")
            return ingredients
    
    

def get_cooking_time():
    while True:
        print()
        # enter time in HH:MM format
        cooking_time_input = input("Enter cooking time HH:MM (or type 'back' to return): ").strip()
        
        # handle back navigation
        if cooking_time_input.lower() == "back":
            return None
        
        parts = cooking_time_input.split(":")
        
        # ensure correct format (two parts separated by :)
        if len(parts) != 2:
            print("Invalid format! Time should be in HH:MM format. (Example: 02:45)")
            continue
        
        hours   = parts[0]
        minutes = parts[1]
        
        try:
            # convert the string to integer
            hours   = int(parts[0])
            minutes = int(parts[1])
        except ValueError:
            print("Hours and Minutes must be numbers.")
            continue
        
        # validate hour range (0 to 12)
        if not (0 <= hours <= 12):
           print("Hours must be between 0 and 12.")
           continue
        
        # validate minute range (0 to 59)
        if not (0 <= minutes <= 59):
            print("Minutes must be between 0 and 59.")
            continue
        
         # convert total time to minutes
        total_minutes = hours * 60 + minutes
        
        # minimum 5 minutes required
        if total_minutes < 5:
            print("Cooking time must be at least 00:05.")
            continue
        
        # maximum 12 hours (720 minutes)
        if total_minutes > 720:
            print("Cooking time must not exceed 12:00.")
            continue
         
        # return valid time in HH:MM format
        return f"{hours:02d}:{minutes:02d}"
    


# list of valid categories
allowed_category = ["BREAKFAST", "LUNCH", "DINNER", "DESSERT", "SNACK", "BEVERAGE"]

def get_category(category=None):
    
    while True:
        print()
        category_input = input("Choose category (BREAKFAST, LUNCH, DINNER, DESSERT, SNACK, BEVERAGE)\nor type 'back' to return: ").strip().upper()
        
        # allow user to go back 
        if category_input == "BACK":
            return None
        
        # check if input is in allowed list
        if category_input not in allowed_category:
            print("\n  Invalid category. Please choose from: BREAKFAST, LUNCH, DINNER, DESSERT, SNACK, BEVERAGE")
            continue
        
        return category_input
    
    

def tags_user():
    # store tags uniquely using a set
    tags = set()
    print()
    print("  Add tags one at a time. Type 'done' when you're finished.")
    print()
    
    while True:
        add_tag = input("Add a tag (or type 'done' to finish): ").strip()
        
        # stop input when user is done
        if add_tag.lower() == "done":
            break
        
        # prevent empty tags
        if add_tag == "":
            print("\n  Tag cannot be empty.")
            continue
        
        # sets ignore duplicates automatically
        tags.add(add_tag)
        print(f"  Tag '{add_tag}' added!")
        
    return tags



count_recipe  = 0
recipes_dict  = {}

def validate_recipe_input():
    global count_recipe
    
    while True:
        print()
        print("  --- Adding a New Recipe ---")
        
        # get and validate recipe name
        name = get_recipe_name()
        if name is None:
            return
        
        # get ingredients list
        ingredients = get_ingredients()
        
        # select a category
        category = get_category()
        if category is None:
            return
        
        # get the cooking time
        cooking_time = get_cooking_time()
        if cooking_time is None:
            return
        
        # optional tags
        tags_call = tags_user()
        
        # display summary for user confirmation
        print("="*40)
        print("  Recipe Validated Successfully!")
        print("  Name       :", name)
        print("  Ingredients:", len(ingredients))
        print("  Category   :", category)
        print("  Cook Time  :", cooking_time)
        print("="*40)
        
        count_recipe += 1
        
        # generate formatted recipe ID (e.g., RCP001)
        recipe_id = f"RCP{count_recipe:03}"
        
        # store recipe details in global dictionary
        recipes_dict[recipe_id] = {
            "name":         name,
            "ingredients":  ingredients,
            "category":     category,
            "cooking_time": cooking_time,
            "tags":         tags_call
        }
        
        # auto save data to file immediately
        save_to_file()
        
        print()
        while True:
            add_another_recipe = input("Add another recipe? (yes/no): ").strip().lower()
            
            if add_another_recipe == "yes":
                break
            
            elif add_another_recipe == "no":
                return
            else:
                print("\n  Please enter yes or no.")



def save_to_file():
    try:
        # overwrite file and save all recipes
        with open("recipes.txt", "w") as f:
            
            for recipe_id, details in recipes_dict.items():
                f.write("===RECIPE===\n")
                f.write(f"ID:{recipe_id}\n")
                f.write(f"NAME:{details['name']}\n")
                f.write(f"CATEGORY:{details['category']}\n")
                f.write(f"TIME:{details['cooking_time']}\n")
                
                # convert ingredients list into a single string
                list_of_ingredients = "|".join(f"{parts[0]}, {parts[1]}, {parts[2]}" for parts in details["ingredients"])
                f.write(f"INGREDIENTS:{list_of_ingredients}\n")
                
                # convert tags set into comma-separated string
                list_of_tags = ",".join(details["tags"])
                f.write(f"TAGS:{list_of_tags}\n")
                
                f.write("===END===\n")
        print("\n  Recipes saved successfully to recipes.txt\n")
                
    except:
        # handle any error during file writing
        print("\n  Failed to save recipes.")
        


def loading_recipes_from_file():
    global recipes_dict, count_recipe
    
    # check if file exists before loading
    if not os.path.exists("recipes.txt"):
        print("\n  No saved recipes found. Starting fresh.\n")
        return
        
    try:
        with open("recipes.txt", "r") as file:
            current_recipe_dict = {}
            recipe_id = " "
            
            # read file line by line
            for l in file:
                l = l.strip()
                
                # start of a new recipe
                if l == "===RECIPE===":
                    current_recipe_dict = {}
                
                elif l.startswith("ID:"):
                    recipe_id = l.split(":", 1)[1]
                
                elif l.startswith("NAME:"):
                    current_recipe_dict["name"] = l.split(":", 1)[1]
                
                elif l.startswith("CATEGORY:"):
                    current_recipe_dict["category"] = l.split(":", 1)[1]
                
                elif l.startswith("TIME:"):
                    current_recipe_dict["cooking_time"] = l.split(":", 1)[1]
                
                elif l.startswith("INGREDIENTS:"):
                    ingredient_str = l.split(":", 1)[1]
                    ingredients_list = []
                    for ing in ingredient_str.split("|"):
                        try:
                            name, qty, unit = ing.split(",")
                            ingredients_list.append((name, float(qty), unit))
                        except:
                            continue  
                    current_recipe_dict["ingredients"] = ingredients_list
                
                elif l.startswith("TAGS:"):
                    tags_str = l.split(":", 1)[1]
                    current_recipe_dict["tags"] = set(tags_str.split(",")) if tags_str else set()
                
                elif l == "===END===":
                    # validate required fields before saving recipe
                    if not current_recipe_dict.get("name") or not current_recipe_dict.get("category") or not current_recipe_dict.get("cooking_time") or not current_recipe_dict.get("ingredients"):
                        print(f"\n  Recipe {recipe_id} skipped: missing data.")
                        continue
                    
                    # store reconstructed recipe
                    recipes_dict[recipe_id] = current_recipe_dict
                    
                    # update recipe counter to avoid ID duplication
                    num = int(recipe_id.replace("RCP", ""))
                    if num > count_recipe:
                        count_recipe = num
                        
        print(f"\n  Loaded {len(recipes_dict)} recipe(s) successfully.\n")
                        
    except Exception as e:
        # handle any unexpected file or parsing errors
        print("\n  Error loading recipes:", e)
            
        

def export_single_recipe():
    # check if there are any recipes to export
    if not recipes_dict:
        print("\n  No saved recipes ready for export.")
        return
    
    print()
    print("  Available Recipes:")
    print("  " + "-"*36)
    # display available recipe IDs and names
    for recipes_id, details in recipes_dict.items():
        print("  ID:", recipes_id, "| Name:", details["name"])
    print()
    
    while True:
        recipe_id_export = input("Enter the Recipe ID to export (e.g. RCP001)\nor type 'back' to return: ").strip().upper()
        
        # allow user to exit the export process
        if recipe_id_export == "BACK":
            print()
            return
        
        # validate selected recipe ID
        if recipe_id_export not in recipes_dict:
            print("\n  Invalid recipe ID. Please try again.")
            continue
        else:
            break
    
    details = recipes_dict[recipe_id_export]
    
    try:
        # export selected recipe into a separate text file
        with open(f"{recipe_id_export}.txt", "w") as f:
            f.write(f"ID: {recipe_id_export}\n")
            f.write(f"Name: {details['name']}\n")
            f.write(f"Category: {details['category']}\n")
            f.write(f"Time: {details['cooking_time']}\n")
            f.write("Ingredients:\n")
            for ing in details["ingredients"]:
                f.write(f" - {ing[0]}: {ing[1]} {ing[2]}\n")
            f.write("Tags: " + ", ".join(details["tags"]) + "\n")
        print(f"\n  Recipe {recipe_id_export} exported successfully!\n")
    except Exception as e:
        print("\n  Error exporting recipe:", e)



def recipe_book():
    
    # load existing recipes from file at program start
    loading_recipes_from_file()
    
    # welcome message
    print("========================================")
    print("     DIGITAL RECIPE BOOK MANAGER")
    print("========================================")
    print()
    
    while True:
        # main menu loop
        print("  1  - Add New Recipe")
        print("  2  - View All Recipes")   
        print("  3  - View Recipe by ID")
        print("  4  - Search by Ingredient")        
        print("  5  - Filter Recipes")           
        print("  6  - Edit Recipe")         
        print("  7  - Delete Recipe")       
        print("  8  - View Statistics")
        print("  9  - Save Recipes")
        print("  10 - Export Recipe")
        print("  11 - Exit")
        print()
        print("  ======================================")
        
        user_option = input("\n  Enter your choice (1-11): ").strip()
        print()
        
        # validate menu input
        if user_option not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]:
            print("  Invalid option. Please try again!\n")
            continue
        
        if user_option == "1":
            validate_recipe_input()
        
        
        elif user_option == "2":
            if not recipes_dict:
                print("  No recipes added yet!\n")
                continue
            
            # submenu for viewing recipes
            while True:
                print(f"\n  You currently have {len(recipes_dict)} recipe(s)")
                print("  ----------------------------------------")
                print("  1 - View a single recipe")
                print("  2 - Browse recipes by category")
                print("  3 - View all recipes")
                print("  4 - Go back to the main menu")
                print()
                
                chose_option = input("  Choose an option: ").strip()
                print()
                
                # view a single recipe by ID
                if chose_option == "1":
                    for recipe_id, details in recipes_dict.items():
                        print("  ID:", recipe_id, "| Name:", details["name"])
                    print()
                    
                    while True:
                        chose_recipe = input("Enter the Recipe ID (e.g. RCP001) or type 'back' to return: ").strip().upper()
                        
                        if chose_recipe == "BACK":
                            break
                        
                        if chose_recipe in recipes_dict:
                            details = recipes_dict[chose_recipe]
                            # display full recipe details
                            print("\n" + "="*40)
                            print("  Recipe ID  :", chose_recipe)
                            print("  Name       :", details["name"])
                            print("  Category   :", details["category"])
                            print("  Cook Time  :", details["cooking_time"])
                            print("  " + "-"*38)
                            print("  Ingredients:")
                            
                            for i, ing in enumerate(details["ingredients"], start=1):
                                print(f"    {i}. {ing[0]} - {ing[1]} {ing[2]}")
                                
                            print("  " + "-"*38)
                            print("  Tags:", ", ".join(details["tags"]))
                            print("="*40)
                            print()
                        else:
                            print("\n  Invalid recipe ID. Try again!\n")
                
                # browse recipes by category
                elif chose_option == "2":
                    while True:
                        print("  Valid categories: ", ", ".join(allowed_category))
                        print()
                        category_option = input("Enter category (or type 'back' to return): ").strip().upper()
                        print()
                        
                        if category_option == "BACK":
                            break
                        
                        if category_option not in allowed_category:
                            print("  Invalid category. Please try again.\n")
                            continue
                        
                        # filter recipes by selected category
                        use_category = {recipe_id: details for recipe_id, details in recipes_dict.items() if details["category"] == category_option}
                        
                        if not use_category:
                            print("  No recipes found in this category.\n")
                        else:
                            print(f"  Found {len(use_category)} {category_option} recipe(s):")
                            print("  " + "-"*38)
                            for recipe_id, details in use_category.items():
                                print(f"  {recipe_id} | {details['name']} | {details['category']} | {details['cooking_time']} | Tags: {', '.join(details['tags'])}")
                            print()
                
                # view all recipes summary
                elif chose_option == "3":
                    print("  All Recipes Summary:")
                    print("  " + "-"*38)
                    for recipe_id, details in recipes_dict.items():
                        print(f"  {recipe_id} | {details['name']} | {details['category']} | {details['cooking_time']} ")
                    print()
                
                # return to main menu
                elif chose_option == "4":
                    break
                else:
                    print("  Invalid option. Please try again!\n")
                    
        elif user_option == "3":
            view_recipe_by_id()
                    
        elif user_option == "4":
            search_by_ingredient()
        
        
        elif user_option == "5":
            filter_recipes()
            
        
        elif user_option == "6":
            edit_recipe()
        
        
        elif user_option == "7":
            delete_recipe()
        
        
        elif user_option == "8":
            show_statistics()
            
        elif user_option == "9":
            save_to_file()
        
        elif user_option == "10":
            export_single_recipe()
        
        
        elif user_option == "11":
            # save before exiting program
            print("  Saving your recipes before closing...")
            save_to_file()
            print("  Goodbye! Enjoy!\n")
            break
        
        

def view_recipe_by_id():
    # check if any recipes exist
    if not recipes_dict:
        print("  No recipes available.\n")
        return
    
    # display available recipe IDs and names
    print("  Available Recipes:")
    print("  " + "-"*36)
    for recipe_id, details in recipes_dict.items():
        print("  ID:", recipe_id, "| Name:", details["name"])
    print()

    while True:
        chosen = input("Enter Recipe ID (or type 'back' to return): ").strip().upper()
        print()
        
        # allow user to exit the view option
        if chosen == "BACK":
            return
        
        # validate recipe ID and display details
        if chosen in recipes_dict:
            details = recipes_dict[chosen]
            
            # display full recipe details
            print("="*40)
            print("  Recipe ID :", chosen)
            print("  Name      :", details["name"])
            print("  Category  :", details["category"])
            print("  Cook Time :", details["cooking_time"])
            print("  " + "-"*38)

            print("  Ingredients:")
            for i, ing in enumerate(details["ingredients"], start=1):
                print(f"    {i}. {ing[0]} - {ing[1]} {ing[2]}")

            print("  " + "-"*38)
            print("  Tags:", ", ".join(details["tags"]))
            print("="*40)
            print()
        else:
            print("  Invalid recipe ID. Please try again.\n")
        


def search_by_ingredient():
    # check if any recipes exist
    if not recipes_dict:
        print("  No recipes available.\n")
        return
    
    print()
    while True:
        search = input("Enter ingredient to search (or type 'back' to return): ").strip().lower()
        print()
        
        # allow user to exit search
        if search == "back":
            break
        
        found_count = 0
        
        # iterate through all recipes and their ingredients
        for recipe_id, details in recipes_dict.items():
            for ing in details["ingredients"]:
                # check if search term matches ingredient name
                if search in ing[0].lower():
                    # print header only once when first match is found
                    if found_count == 0:
                        print(f"  Recipes containing '{search}':")
                        print("  " + "-"*38)
                    
                    print(f"  {recipe_id} | {details['name']} | {details['category']}")
                    found_count += 1
                    break   # avoid duplicate matches within the same recipe
    
        if found_count == 0:
            print("  No recipes found with that ingredient.\n")
        else:
            print()
            


def filter_recipes():
    if not recipes_dict:
        # check if any recipes exist
        print("  No recipes available.\n")
        return
    
    print()
    print("  Leave any field blank to skip that filter.")
    print("  Type 'back' as the first answer to cancel.")
    print()
    
    min_time = input("  Enter minimum time (HH:MM) or press Enter to skip: ").strip()
    
    # allow user to exit at the beginning
    if min_time.lower() == "back":
        return
    
    max_time = input("  Enter maximum time (HH:MM) or press Enter to skip: ").strip()
    min_ing  = input("  Minimum number of ingredients (or Enter to skip): ").strip()
    max_ing  = input("  Maximum number of ingredients (or Enter to skip): ").strip()
    category = input("  Enter category (or press Enter to skip): ").strip().upper()
    print()
    
    found = 0
    
    for recipe_id, details in recipes_dict.items():
        show = True
        
        # apply category filter if provided
        if category != "":
            if details["category"] != category:
                show = False
        
        # apply ingredient count filters
        if min_ing != "":
            if len(details["ingredients"]) < int(min_ing):
                show = False
        
        if max_ing != "":
            if len(details["ingredients"]) > int(max_ing):
                show = False
        
        # helper function to convert HH:MM into total minutes
        def to_minutes(t):
            h, m = t.split(":")
            return int(h) * 60 + int(m)
        
        # apply cooking time filters
        if min_time != "":
            if to_minutes(details["cooking_time"]) < to_minutes(min_time):
                show = False
        
        if max_time != "":
            if to_minutes(details["cooking_time"]) > to_minutes(max_time):
                show = False
        
        # display recipe if it satisfies all conditions
        if show:
            if found == 0:
                print("  Filtered Recipes:")
                print("  " + "-"*38)
            
            print(f"  {recipe_id} | {details['name']} | {details['category']} | {details['cooking_time']}")
            found += 1
    
    if found == 0:
        print("  No recipes match your filters.")
    
    print()
        
        

def edit_recipe():
    #  check if any recipes exist
    if not recipes_dict:
        print("  No recipes available.\n")
        return
    
    # display available recipes
    print("  Available Recipes:")
    print("  " + "-"*36)
    for recipe_id, details in recipes_dict.items():
        print("  ID:", recipe_id, "| Name:", details["name"])
    print()
    
    while True:
        recipe_id = input("Enter recipe ID to edit (or type 'back' to return): ").strip().upper()
        print()
        
        # allow user to exit
        if recipe_id == "BACK":
            return
        
        # validate recipe ID
        if recipe_id not in recipes_dict:
            print("  Invalid recipe ID. Please try again.\n")
            continue
        
        # edit options menu
        print("  What would you like to change?")
        print("  1 - Change Name")
        print("  2 - Change Category")
        print("  3 - Change Cooking Time")
        print("  4 - Back to main menu")
        print()
        
        
        while True:
            
            choice = input("  Choose what to edit: ").strip()
            print()
        
            # update name
            if choice == "1":
                new_name = get_recipe_name()
                if new_name is None:
                    break
                recipes_dict[recipe_id]["name"] = new_name
            
            # update category
            elif choice == "2":
                new_category = get_category()
                if new_category is None:
                    break
                recipes_dict[recipe_id]["category"] = new_category
            
            # update cooking time
            elif choice == "3":
                new_time = get_cooking_time()
                if new_time is None:
                    break
                recipes_dict[recipe_id]["cooking_time"] = new_time
            
            # return to main menu
            elif choice == "4":
                return
            
            else:
                print("  Invalid choice. Please try again.\n")
                continue
            
            # save changes after update
            print("  Recipe updated successfully!\n")
            save_to_file()
            break
        
        break
    


def delete_recipe():
    # check if any recipes exist
    if not recipes_dict:
        print("  No recipes available.\n")
        return
    
    # display available recipes
    print("  Available Recipes:")
    print("  " + "-"*36)
    for recipe_id, details in recipes_dict.items():
        print("  ID:", recipe_id, "| Name:", details["name"])
    print()
        
    while True:
        recipe_id = input("Enter recipe ID to delete (or type 'back' to return): ").strip().upper()
        print()
        
        # allow user to exit
        if recipe_id == "BACK":
            return
        
        # validate recipe ID
        if recipe_id not in recipes_dict:
            print("  Invalid recipe ID. Please try again.\n")
            continue
        else:
            break
        
    # confirm deletion before removing data
    while True:
        confirm = input(f"  Are you sure you want to delete '{recipes_dict[recipe_id]['name']}'? (yes/no): ").strip().lower()
        print()
        
        if confirm == "yes":
            # remove recipe from dictionary
            del recipes_dict[recipe_id]
            print("  Recipe deleted successfully.\n")
            save_to_file()
            break
        elif confirm == "no":
            print("  Deletion cancelled.\n")
            break
        else:
            print("  Please enter yes or no.\n")
            continue
        


def show_statistics():
    if not recipes_dict:
        # check if any recipes exist
        print("  No recipes available.\n")
        return
    
    print("\n  ========== RECIPE SUMMARY ==========")
    print("  Total Recipes:", len(recipes_dict))
    
    # initialize category counters
    category_count = {}
    for cat in allowed_category:
        category_count[cat] = 0
    
    # count recipes per category
    for details in recipes_dict.values():
        category_count[details["category"]] += 1
    
    print("\n  Recipes by Category:")
    for cat in allowed_category:
        print("  ", cat + ":", category_count[cat])
    
    # count frequency of each ingredient across all recipes
    ingredient_count = {}
    
    for details in recipes_dict.values():
        for ing in details["ingredients"]:
            name = ing[0]
            if name in ingredient_count:
                ingredient_count[name] += 1
            else:
                ingredient_count[name] = 1
    
    print("\n  Most Used Ingredients (Top 3):")
    
    # sort ingredients by frequency in descending order
    sorted_items = sorted(ingredient_count.items(), key=lambda x: x[1], reverse=True)
    
    for i in range(min(3, len(sorted_items))):
        print("  ", i+1, "-", sorted_items[i][0], "-", sorted_items[i][1], "recipe(s)")
    
    # calculate average number of ingredients per recipe
    total_ing = 0
    for details in recipes_dict.values():
        total_ing += len(details["ingredients"])
    
    avg = total_ing / len(recipes_dict)
    print("\n  Average Ingredients per Recipe:", round(avg, 2))
    
    print("  ====================================\n")


# start the application
recipe_book()
