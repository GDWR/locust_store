from typing import Optional

from sqlmodel import Field, SQLModel, Relationship

from .cart_product_link import CartProductLink
from .product import Product


class Cart(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    products: list[Product] = Relationship(back_populates="carts", link_model=CartProductLink)
