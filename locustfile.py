import random

from locust import HttpUser, task


class StoreUser(HttpUser):
    product_ids: list[str]

    @task
    def get_all_products(self):
        self.client.get(
            f"/store/products?page={random.randint(0, 10)}&limit={random.randint(25, 100)}",
            name="/store/products"
        )

    @task
    def get_product_by_id(self):
        product_id = random.choice(self.products)
        self.client.get(f"/store/products/{product_id}", name="/store/products/:id")

    @task
    def crate_cart_add_items(self):
        response = self.client.post("/store/cart")
        cart_id = response.json()["id"]
        product_id = random.choice(self.products)
        self.client.post(f"/store/cart/items?cart_id={cart_id}&product_id={product_id}", name="/store/cart/items")

    def on_start(self):
        response = self.client.get("/store/products?limit=1000", name=None)
        self.products = list(o['id'] for o in response.json())
