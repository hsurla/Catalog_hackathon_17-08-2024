#list of virtual products available
virtual_products = [
    {"type": "shirt", "size": "M", "color": "blue"},
    {"type": "shirt", "size": "L", "color": "white"},
    {"type": "shirt", "size": "S", "color": "black"},
    {"type": "pants", "size": "32", "color": "black"},
    {"type": "pants", "size": "34", "color": "gray"},
    {"type": "pants", "size": "30", "color": "navy"},
    {"type": "jacket", "size": "L", "color": "red"},
    {"type": "jacket", "size": "M", "color": "green"},
    {"type": "jacket", "size": "S", "color": "blue"},
    {"type": "dress", "size": "M", "color": "green"},
    {"type": "dress", "size": "L", "color": "red"},
    {"type": "dress", "size": "S", "color": "black"},
    {"type": "shoes", "size": "9", "color": "brown"},
    {"type": "shoes", "size": "10", "color": "black"},
    {"type": "shoes", "size": "8", "color": "white"},
    {"type": "hat", "size": "M", "color": "white"},
    {"type": "hat", "size": "L", "color": "black"},
    {"type": "hat", "size": "S", "color": "red"},
    {"type": "skirt", "size": "S", "color": "pink"},
    {"type": "skirt", "size": "M", "color": "blue"},
    {"type": "skirt", "size": "L", "color": "yellow"},
    {"type": "t-shirt", "size": "L", "color": "yellow"},
    {"type": "t-shirt", "size": "M", "color": "white"},
    {"type": "t-shirt", "size": "S", "color": "green"},
    {"type": "jeans", "size": "32", "color": "blue"},
    {"type": "jeans", "size": "34", "color": "black"},
    {"type": "jeans", "size": "30", "color": "gray"},
    {"type": "sneakers", "size": "9", "color": "white"},
    {"type": "sneakers", "size": "10", "color": "black"},
    {"type": "sneakers", "size": "8", "color": "red"},
    {"type": "coat", "size": "M", "color": "brown"},
    {"type": "coat", "size": "L", "color": "gray"},
    {"type": "coat", "size": "S", "color": "black"}
]

def try_on_item(user_measurements, item):
    #size matching based on user measurements
    if item["type"] in ["shirt", "t-shirt", "jacket", "dress", "coat"]:
        if user_measurements["waist"] == 32 and item["size"] == "M":
            return f"Item '{item['color']} {item['type']}' fits perfectly on the user."
        elif user_measurements["waist"] <= 34 and item["size"] == "L":
            return f"Item '{item['color']} {item['type']}' fits perfectly on the user."
        elif user_measurements["waist"] < 30 and item["size"] == "S":
            return f"Item '{item['color']} {item['type']}' fits perfectly on the user."
        else:
            return f"Item '{item['color']} {item['type']}' does not fit well."
    elif item["type"] in ["pants", "jeans", "skirt"]:
        if user_measurements["waist"] == 32 and item["size"] == "32":
            return f"Item '{item['color']} {item['type']}' fits perfectly on the user."
        elif user_measurements["waist"] <= 34 and item["size"] == "34":
            return f"Item '{item['color']} {item['type']}' fits perfectly on the user."
        elif user_measurements["waist"] < 30 and item["size"] == "30":
            return f"Item '{item['color']} {item['type']}' fits perfectly on the user."
        else:
            return f"Item '{item['color']} {item['type']}' does not fit well."
    elif item["type"] in ["shoes", "sneakers"]:
        if str(user_measurements["shoe_size"]) == item["size"]:
            return f"Item '{item['color']} {item['type']}' fits perfectly on the user."
        else:
            return f"Item '{item['color']} {item['type']}' does not fit well."
    elif item["type"] == "hat":
        return f"Item '{item['color']} {item['type']}' fits perfectly on the user."

#predict the recommended size based on user measurements
def predict_size(user_measurements):
    if user_measurements["waist"] < 30:
        return "S"
    elif 30 <= user_measurements["waist"] <= 34:
        return "M"
    else:
        return "L"

#start the AR shopping experience
def start_shopping():
    print("Welcome to the AR Shopping Experience!")
    user_height = int(input("Enter your height (in cm): "))
    user_waist = int(input("Enter your waist size: "))
    user_shoe_size = int(input("Enter your shoe size: "))
    
    selected_items = []
    
    while True:
        # Show available products
        print("\nAvailable products:")
        for i, product in enumerate(virtual_products, start=1):
            print(f"{i}. {product['color'].capitalize()} {product['type'].capitalize()} (Size: {product['size']})")
        
        choice = int(input("Choose a product by entering its number (or 0 to finish): "))
        
        if choice == 0:
            break
        
        # Add the selected product to the list
        selected_item = virtual_products[choice - 1]
        selected_items.append(selected_item)
        print(f"{selected_item['color'].capitalize()} {selected_item['type'].capitalize()} added to your selection.\n")
    
    # Process each selected item
    print("\nResults of the virtual try-on:")
    for item in selected_items:
        result = try_on_item({"height": user_height, "waist": user_waist, "shoe_size": user_shoe_size}, item)
        print(result)
    
    # Predict and display the recommended size
    recommended_size = predict_size({"height": user_height, "waist": user_waist})
    print(f"\nRecommended size for the user: {recommended_size}")

# Run the shopping experience
start_shopping()

