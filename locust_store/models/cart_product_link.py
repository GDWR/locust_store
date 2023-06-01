from typing import Optional

from sqlmodel import Field, SQLModel


class CartProductLink(SQLModel, table=True):
    cart_id: Optional[int] = Field(default=None, foreign_key="cart.id", primary_key=True)
    product_id: Optional[int] = Field(default=None, foreign_key="product.id", primary_key=True)
