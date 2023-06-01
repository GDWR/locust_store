from fastapi import APIRouter, HTTPException, Query
from sqlmodel import Session, select

from ..database import engine
from ..models import Product, Cart

router = APIRouter(prefix="/store")

carts = {}


@router.get("/products")
async def get_products(offset: int = 0, limit: int = Query(default=25, lte=1000)) -> list[Product]:
    with Session(engine) as session:
        results = session.exec(select(Product).offset(offset).limit(limit))

        return results.all()


@router.get("/products/{id}")
async def get_product_by_id(id: str) -> Product:
    with Session(engine) as session:
        product = session.exec(select(Product).where(Product.id == id)).one()

        if product:
            return product
        else:
            raise HTTPException(status_code=404, detail="product not found")


@router.post("/cart")
async def post_cart() -> Cart:
    cart = Cart()

    with Session(engine) as session:
        session.add(cart)
        session.commit()
        session.refresh(cart)

    return cart


@router.post("/cart/items")
async def post_cart_items(cart_id: str, product_id: str):
    # will raise 404 if it doesn't exist
    product = await get_product_by_id(product_id)

    with Session(engine) as session:
        cart = session.exec(select(Cart).where(Cart.id == cart_id)).one()

        cart.products.append(product)

        session.add(cart)
        session.commit()
