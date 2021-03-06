class Property:
    """
    Represents property and works as a help for other classes
    """
    def __init__(self, square_feet='', beds='',
                 baths='', **kwargs):
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths

    def display(self):
        """
        Displays details
        """
        print("PROPERTY DETAILS")
        print("================")
        print("square footage: {}".format(self.square_feet))
        print("bedrooms: {}".format(self.num_bedrooms))
        print("bathrooms: {}".format(self.num_baths))

    def prompt_init():
        """
        Returns dictionary with inputted values
        """
        return dict(square__feet=input("Enter the square feet: "),
                    beds=input("Enter number of bedrooms: "),
                    baths=input("Enter number of baths:"))
    prompt_init = staticmethod(prompt_init)


class Apartment(Property):
    """
    Class represents Apartment and takes Property as superclass
    """
    valid_laundries = ("coin", "ensuite", "none")
    valid_balconies = ("yes", "no", "solarium")

    def __init__(self, balcony='', laundry='', **kwargs):
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        """
        Displays details
        """
        super().display()
        print("APARTEMENT DETAILS")
        print("laundry: %s" % self.laundry)
        print("has balcony: %s" % self.balcony)

    def prompt_init():
        """
        Static method for showing laundry and balconies
        Asking laundry facilities and presence of the balcony
        """
        parent_init = Property.prompt_init()
        laundry = ''
        while laundry.lower() not in \
                Apartment.valid_laundries:
            laundry = input("What laundry facilities does"
                            "the property have? ({})}".format(
                            ", ".join(Apartment.valid_laundries)))
        balcony = ''
        while balcony.lower() not in \
                Apartment.valid_balconies:
            laundry = input("Does the property have a balcony? "
                            "({})}".format(
                            ", ".join(Apartment.valid_balconies)))
        parent_init.update({
            "laundry": laundry,
            "balcony" : balcony
        })
        return parent_init
    prompt_init = staticmethod(prompt_init)


def get_valid_input(input_string, valid_options):
    """
    Validation function
    Independent of all other classes
    """
    input_string += " ({}) ".format(", ".join(valid_options))
    response = input(input_string)
    while response.lower() not in valid_options:
        response = input(input_string)
    return response


class House(Property):
    """
    Class representing House and takes Property as a superclass
    """
    valid_garage = ("attached", "detached", "none")
    valid_fenced = ("yes", "no")

    def __init__(self, num_stories='',
                 garage='', fenced='', **kwargs):
        super().__init__()
        self.garage = garage
        self.fenced = fenced
        self.num_stories = num_stories

    def display(self):
        """
        Displays details
        """
        super().display()
        print("HOUSE DETAILS")
        print("# of stories: {}".format(self.num_stories))
        print("garage: {}".format(self.garage))
        print("fenced yard".format(self.fenced))

    def prompt_init():
        """
        Static method asking about the yard, garage and number of stories
        Then representing that information to the user
        """
        parent_init = Property.prompt_init()
        fenced = get_valid_input("Is the yard fenced? ",
                                 House.valid_fenced)
        garage = get_valid_input("Is there a garage? ",
                                 House.valid_garage)
        num_stories = input("How many stories? ")

        parent_init.update({
            "fenced" : fenced,
            "garage": garage,
            "num_stories": num_stories
        })
        return parent_init
    prompt_init = staticmethod(prompt_init)


class Purchase(Property):
    """
    Represents class Purchase and takes Property as a superclass
    """
    def __init__(self, price='', taxes='', **kwargs):
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        """
        Displays details
        """
        super().display()
        print("PURCHASE DETAILS")
        print("selling price: {}".format(self.price))
        print("estimated taxes: {}".format(self.taxes))

    def prompt_init():
        """
        Static method for getting information about selling price and
        estimated taxes
        """
        return dict(
            price=input("What is the selling price? "),
            taxes=input("What are the estimated taxes? ")
        )
    prompt_init = staticmethod(prompt_init)


class Rental(Property):
    """
    Represents class Rental, which takes Property as a superclass
    """
    def __init__(self, furnished='', utilities='',
                 rent='', **kwargs):
        super().__init__(**kwargs)
        self.furnished = furnished
        self.utilities = utilities
        self.rent = rent

    def display(self):
        """
        Displays details
        """
        super().display()
        print("RENTAL DETAILS")
        print("rent: {}".format(self.rent))
        print("estimated utilities: {}".format(
            self.utilities))
        print("furnished: {}".format(self.furnished))

    def prompt_init():
        """
        Returns dictionary with inputted values representing monthly rent,
        utilities and if the property is furnished
        """
        return dict(
            rent=input("What is the monthly rent? "),
            utilities=input(
                "What are the estimated utilities? "),
            furnished=get_valid_input(
                "Is the property furnished? ",
                ("yes", "no")))
    prompt_init = staticmethod(prompt_init)


class HouseRental(Rental, House):
    """
    Represents House rental class, which has to super classes:
    Rental and House
    """
    def prompt_init():
        """
        Static method to add to the dictionary
        """
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)


class ApartmentRental(Rental, Apartment):
    """
    Represent Apartment rental class, which takes two super classes:
    rental and apartment
    """
    def prompt_init():
        """
        Static method to add to the existing dictionary
        """
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)


class ApartmentPurchase(Purchase, Apartment):
    """
    Represents Apartment purchase class, which takes two super classes:
    Purchase and Apartment
    """
    def prompt_init():
        """
        Static method to add to the dictionary
        """
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)


class HousePurchase(Purchase, House):
    """
    Represents House purchase class, which takes two super classes:
    Purchase and House
    """
    def prompt_init():
        """
        Static method to add to the dictionary
        """
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)


class Agent:
    """
    Represents class Agent, which allows you to do a payment job and choose
    type of property
    """
    def __init__(self):
        self.property_list = []

    def display_properties(self):
        """
        Dispalys details
        """
        for property in self.property_list:
            property.display()

    type_map = {
        ("house", "rental"): HouseRental,
        ("house", "purchase"): HousePurchase,
        ("apartment", "rental"): ApartmentRental,
        ("apartment", "purchase"): ApartmentPurchase
    }

    def add_property(self):
        """
        Add new information about a payment job and choose type of property
        """
        property_type = get_valid_input(
            "What type of property? ",
            ("house", "apartment")).lower()
        payment_type = get_valid_input(
            "What payment type? ",
            ("purchase", "rental")).lower()
        Agent.add_field_court(self)
        PropertyClass = self.type_map[
            (property_type, payment_type)]
        init_args = PropertyClass.prompt_init()
        self.property_list.append(PropertyClass(**init_args))

    def add_field_court(self):
        """
        Adding or not football field to the property
        """
        property_type = get_valid_input(
            "Do you need a football field",
            ("yes", "no")).lower()
        payment_type = get_valid_input(
            "Dou you need a tennis court ",
            ("yes", "no")).lower()





# print(HouseRental.prompt_init())
# print(Apartement.get_valid_input("what laundry", ("coin", "ensuite", "none")))
# print(Agent().add_property())
# print(Agent().display_properties())
