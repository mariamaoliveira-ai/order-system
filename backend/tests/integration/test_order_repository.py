import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base
from app.config import settings
from app.database.models import Order as OrderModel

@pytest.fixture
def dbSession():
    # Connects to your PostgreSQL Docker container
    engine = create_engine(settings.DATABASE_URL)
    
    # Create tables if they don't exist yet
    Base.metadata.create_all(bind=engine)
    
    TestingSessionLocal = sessionmaker(bind=engine)
    session = TestingSessionLocal()

    try:
        yield session
    finally:
        session.close()
        # Clean up database tables after every test run for complete test isolation
        with engine.connect() as conn:
            for table in reversed(Base.metadata.sorted_tables):
                conn.execute(table.delete())
            conn.commit()
        

def test_shouldSaveOrderInDatabase(dbSession):
    
    items = "1x Camiseta, 2x Calças"
    newOrder = OrderModel(
        items = items
    )
    
    dbSession.add(newOrder)
    dbSession.commit()
    dbSession.refresh(newOrder)
    
    assert newOrder.id is not None
    assert newOrder.items == items
    

def test_shouldLoadAllOrders(dbSession):
    items1 = "1x Camiseta, 2x Calças"
    newOrder1 = OrderModel(items=items1)
    
    items2 = "1x Camisetas"
    newOrder2 = OrderModel(items=items2)
    
    dbSession.add(newOrder1)
    dbSession.add(newOrder2)
    dbSession.commit()
    
    dbOrders = dbSession.query(OrderModel).all()

    assert len(dbOrders) == 2

    retrieved_items = [order.items for order in dbOrders]
    assert items1 in retrieved_items
    assert items2 in retrieved_items

    assert all(order.id is not None for order in dbOrders)
    

def test_shouldFindOrderById(dbSession):
    newOrder = OrderModel(items="1x Sapato")
    dbSession.add(newOrder)
    dbSession.commit()

    found_order = dbSession.query(OrderModel).filter_by(id=newOrder.id).first()

    assert found_order is not None
    assert found_order.items == "1x Sapato"


def test_shouldReturnNoneForMissingOrderId(dbSession):
    found_order = dbSession.query(OrderModel).filter_by(id=9999).first()

    assert found_order is None


def test_shouldDeleteOrder(dbSession):
    newOrder = OrderModel(items="1x Meia")
    dbSession.add(newOrder)
    dbSession.commit()

    dbSession.delete(newOrder)
    dbSession.commit()

    deleted_order = dbSession.query(OrderModel).filter_by(id=newOrder.id).first()
    assert deleted_order is None