
def __list_example() -> None:
    items_to_buy = ["Apple", "Orange", "Grapes", "Kiwi", "Watermelon"]

    # by '+' index
    # "Grapes"
    print("Grapes", items_to_buy[2])
    print("Orange", items_to_buy[1])
    print("Kiwi", items_to_buy[-1])

def __set_example() -> None:
    fruits = set()
    print(fruits, type(fruits))
    fruits.add('Apple')
    fruits.add('Grapes')
    fruits.add('Apple') # duplicate, won't be added
    fruits.add('Watermelon')
    print(fruits)

def all_examples() -> None:
    print("Data Structures\n")
    __list_example()
    __set_example()
    print("\nEnd of Data Structures")