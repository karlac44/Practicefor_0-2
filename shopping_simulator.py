
def main():
    print("🛍️ Welcome to the Girly Shop 🛍️")
    print("Everything is cute and affordable 💕\n")

    # Get shopping items
    total = shop()

    # Show final total
    print("\n💄 Your total is: $", total)
    print("✨ Thanks for shopping bestie ✨")


# 🛒 Shopping function
def shop():
    # Dictionary of items and prices
    items = {
        "lipstick": 10,
        "dress": 25,
        "handbag": 30,
        "perfume": 20
    }

    total = 0  # Keep track of total cost

    # Show available items
    print("Available items:")
    for item in items:
        print("-", item, "($", items[item], ")")

    # Keep shopping until user is done
    while True:
        choice = input("\nWhat do you want to buy? (type 'done' to finish): ").lower()

        # If user is done shopping
        if choice == "done":
            break

        # If item exists in the shop
        elif choice in items:
            total += items[choice]  # Add price to total
            print("💕 Added", choice, "to your cart!")

        # If item does not exist
        else:
            print("❌ Sorry bestie, we don't have that item.")

    return total  # Send total back to main()



main()
