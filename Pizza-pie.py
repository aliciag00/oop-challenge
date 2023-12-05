class Topping:
    def __init__(self, name):
        self.name = name

class PizzaSize:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Pizza:
    def __init__(self):
        self.size = None
        self.toppings = [] # [] is an ampty list

    def set_size(self, size):
        self.size = size

    def add_topping(self, topping):
        self.toppings.append(topping) # append means to add toppings to the end of the list

    def display_order(self):
        print("\nYour pizza order:") # \n starts a new line
        print("Size:", self.size.name)
        print("Toppings:", ', '.join(topping.name for topping in self.toppings)) # shows a list goes over each topping in self.topping and gives a name
        # join method is used to concatenate the names into a single string with proper formatting
        self.display_pizza()

    def display_pizza(self):

        pizza_image = r"""
               _,--~~----~~--._
            ,/'  m%%%%%%=@%%m  `\.
           /' m%%o(_)%%o%%%%o%%m `\
         /' %%@=%o%%%o%%%o%(_)o%%% `\
        /  %o%%%%%=@%%%(_)%%o%%@=%%  \
       |  (_)%(_)%%o%%%o%%%%=@(_)%%%  |
       | %%o%(_)%%%%%o%(_)%%%o%%o%o%% |
       |  (_)%%=@%(_)%o%o%%(_)%o(_)%  |
        \ ~%%o%%%%%o%o%=@%%o%%@%%o%~ /
         \. ~o%%(_)%%%o%(_)%%(_)o~ ,/
           \_ ~o%=@%(_)%o%%(_)%~ _/
             `\_~~o%%%o%%%%%~~_/'
                `--..____,,--'

        """
        print(pizza_image)

class PizzaCustomizer:
    def __init__(self):
        self.available_sizes = [PizzaSize("Small", 8.99), PizzaSize("Medium", 10.99), PizzaSize("Large", 12.99)]
        self.available_toppings = [Topping("Pepperoni"), Topping("Ham"), Topping("Meatballs"),
                                   Topping("Sausage"), Topping("Bacon"), Topping("Extra cheese")]

    def customize_pizza(self):
        pizza = Pizza()

        print("Select pizza size:")
        for i, size in enumerate(self.available_sizes, start=1): # 
            print(f"{i}. {size.name} (${size.price:.2f})")

        size_choice = int(input("Enter the number corresponding to your choice: "))
        selected_size = self.available_sizes[size_choice - 1]
        pizza.set_size(selected_size)

        print("\nSelect pizza toppings (enter 'done' when finished):")
        while True:
            print("Available toppings:")
            for i, topping in enumerate(self.available_toppings, start=1):
                print(f"{i}. {topping.name}")

            topping_choice = input("Enter the number corresponding to your choice or 'done' to finish: ")
            if topping_choice.lower() == 'done':
                break

            topping_choice = int(topping_choice)
            selected_topping = self.available_toppings[topping_choice - 1]
            pizza.add_topping(selected_topping)

        return pizza


def main():
    print("Welcome to "
          """ 
:===\
::   \\  (_)
::   ::         ======     ======       //=====\\
:====:    ::         /          /      //       ||
::        ::       /          /        ||       ||
::        ::      /          /          \\      ||
::        ::     /======    /======      \\=====||

:===\                     :===\                              ||                             ||
::   \\                   ::   \\                            ||                             ||
::   ::                   ::   ::   //=====\\     || /===\   ||      /====\     || /===\    ||
:====:                    :====:   //       ||    ||/        ||     /      \    ||/         ||
::       \\    //         ::       ||       ||    ||         ||     |       |   ||          ||
::        \\  //          ::        \\      ||    ||         ||     \      /    ||         
::         \\//           ::         \\=====||    ||         ||      \====/     ||          (_)
            //
           //
        """)

    customizer = PizzaCustomizer()
    pizza_order = customizer.customize_pizza()
    pizza_order.display_order()


if __name__ == "__main__":
    main()

