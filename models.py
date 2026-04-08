from database import Base
from sqlalchemy import Column, Integer, Boolean, Text, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_utils.types import ChoiceType

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(25), unique=True)
    email = Column(String(65), unique=True)
    password = Column(Text, nullable=True)
    is_staff = Column(Boolean, default=False)
    is_active = Column(Boolean, default=False)
    orders = relationship('Order', back_populates='user')


    def __repr__(self):
        return f"<User: {self.username}>"
    
class Order(Base):
    ORDER_STATUSES = (
        ('PENDING', 'pending'),
        ('IN-TRANSIT', 'in-transit'),
        ('DELIVERED', 'delivered')
    )

    FOOD_CATEGORIES = (
        ('SANDWICHES', 'sandwiches'),
        ('PASTAS', 'pastas'),
        ('SOUPS', 'soups'),
        ('PIZZAS', 'pizzas'),
        ('DRINKS', 'drinks')
    )

    SANDWICH_SIZES = (
        ('SMALL', 'small'),
        ('REGULAR', 'regular')
    )

    PIZZA_SIZES = (
        ('SMALL', 'small'),
        ('MEDIUM', 'medium'),
        ('LARGE', 'large')
    )

    DRINK_SIZES = (
        ('SMALL', 'small'),
        ('MEDIUM', 'medium'),
        ('LARGE', 'large')
    )


    __tablename__='orders'
    id = Column(Integer, primary_key=True)
    quantity = Column(Integer, nullable=False)
    order_status = Column(ChoiceType(choices=ORDER_STATUSES), default="PENDING")
    food_categories = Column(ChoiceType(choices=FOOD_CATEGORIES), default="SANDWICHES")
    sandwich_sizes = Column(ChoiceType(choices=SANDWICH_SIZES), default="SMALL")
    pizza_sizes = Column(ChoiceType(PIZZA_SIZES), default="SMALL")
    drink_sizes = Column(ChoiceType(choices=DRINK_SIZES), default="SMALL")
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', back_populates='orders')

    def __repr__(self):
        return f"<Order: {self.id}>"

