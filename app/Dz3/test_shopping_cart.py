from shopping_cart import ShoppingCart


class TestShoppingCart:
    def test_init_empty(self):
        cart = ShoppingCart()
        assert cart.items == []

    def test_add_new_item(self):
        cart = ShoppingCart()
        cart.add_item("apple", 10, 2)
        assert cart.items == [{"name": "apple", "price": 10, "quantity": 2}]

    def test_add_existing_item(self):
        cart = ShoppingCart()
        cart.add_item("apple", 10, 2)
        cart.add_item("apple", 12, 3)
        assert cart.items == [{"name": "apple", "price": 12, "quantity": 5}]

    def test_add_multiple_items(self):
        cart = ShoppingCart()
        cart.add_item("apple", 10, 2)
        cart.add_item("bread", 20, 1)
        assert len(cart.items) == 2

    def test_remove_existing_item(self):
        cart = ShoppingCart()
        cart.add_item("apple", 10, 2)
        cart.add_item("bread", 20, 1)
        cart.remove_item("apple")
        assert cart.items == [{"name": "bread", "price": 20, "quantity": 1}]

    def test_remove_missing_item(self):
        cart = ShoppingCart()
        cart.add_item("apple", 10, 2)
        cart.remove_item("bread")
        assert cart.items == [{"name": "apple", "price": 10, "quantity": 2}]

    def test_get_total_empty(self):
        cart = ShoppingCart()
        assert cart.get_total() == 0

    def test_get_total(self):
        cart = ShoppingCart()
        cart.add_item("apple", 10, 2)
        cart.add_item("bread", 20, 3)
        assert cart.get_total() == 80

    def test_get_total_after_update_and_remove(self):
        cart = ShoppingCart()
        cart.add_item("apple", 10, 2)
        cart.add_item("apple", 15, 1)
        cart.add_item("bread", 20, 1)
        cart.remove_item("bread")
        assert cart.get_total() == 45