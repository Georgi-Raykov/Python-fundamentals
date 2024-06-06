class Catalogue:

    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        current_list = [word for word in self.products if word[0] == first_letter]
        return current_list

    def __repr__(self):
        sorted_list = sorted(self.products)
        str_sorted_list = '\n'.join(sorted_list)
        return f"Items in the {self.name} catalogue:\n{str_sorted_list}"


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
