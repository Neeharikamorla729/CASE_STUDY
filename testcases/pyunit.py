import pytest
from datetime import date
import dao
from dao import *
from entity import vehicle, customer, lease,  payment
from exception.carNotFound import  CarNotFoundException
from exception. customerNotFound import  CustomerNotFoundException
from exception.leaseNotFound import  LeaseNotFoundException


# Test case for creating a car
def test_create_car():
    from dao.listAllCars import listAllCars
    if listAllCars() is not None:
        print("car not created")
    else:
        print("car created")

def test_create_lease():
    from dao.listLeaseHistory import listLeaseHistory
    if listLeaseHistory() is not None:
        print("lease not created")
    else:
        print("lease created")



