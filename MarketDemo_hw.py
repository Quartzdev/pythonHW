import os

CATALOG_FILENAME = 'products.txt'

class Product:
    isin = ''
    title = ''
    price = 0.0
    count = 0

    def __init__(self, isin, title, price, count):
        self.isin = isin
        self.title = title
        self.price = price
        self.count = count

    def display_info(self):
        print(f'[ISIN: {self.isin}; title: {self.title};', end='')
        print(f'price: {self.price}; count: {self.count}]')

class MarketCatalog:
    catalog = []
def load_from_file(self):
    if not os.path.exists(CATALOG_FILENAME):
        return

    with open(CATALOG_FILENAME, encoding='utf-8') as file:
        for line in file:
            isin, title, price, count = line.split(';')
            add_product(Product (isin, title, float(price), int(count)))
            def add_product(self, product):
                self.catalog.append(product)


def save_catalog_to_file(self):
    with open(CATALOG_FILENAME, 'w', encoding='utf-8') as file:
        for product in product_catalog:
            file.write(';'.join([product.isin, product.title, str(product.price),str(product.count)]))


def create_product():
    isin = input('Enter the isin: ')
    title = input('Enter the title: ')
    price = float(input('Enter the price: '))
    count = int(input('Enter the count of product: '))

    return Product(isin, title, price, count)


def add_product(self, product):
    self.catalog.append(product)

def main():
    product_catalog = load_from_file()
    print(product_catalog)
    # product = create_product()
    # add_product(product_catalog, product)
    save_catalog_to_file(product_catalog)

    product = Product('2134124', 'Хлеб черный', 32.90, 2400)
    product.display_info()

class User(object):
    """docstring forUser."""
    login = ''
    password = ''
    name = ''
    secname = ''

    def __init__(self, login, password, name, secname, picture):

        self.login = login
        self.password = password
        self.name = name
        self.secname = secname
        self.picture = picture

    def log_in(login, password, name, secname):
        login = input('Enter your login')
        password = input('Enter your password')
        name = input('Enter your name')
        secname = input('Enter your secname')

        return User(login, password, name, secname)
    def main2 ():
        user_catalog = load_from_file()
        print(log_in)
        # product = create_product()
        # add_product(product_catalog, product)
        save_catalog_to_file(user_catalog)

        product = Product('ProductDesigner_Junior', 'fbMIEa', 'Rita', 'Quartzevskaya')
        product.display_info()


main()
