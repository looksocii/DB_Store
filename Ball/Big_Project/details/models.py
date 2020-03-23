from django.db import models

# Create your models here.
class Account(models.Model):
    name = models.IntegerField()
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)


    '''
        ------- เหลือพวกช้อยด้วย ENUM -------------
    '''
    
    '''
    account_type = models.CharField(choices=[
        (AccountType.employee, _('employee')),
        (AccountType.customer, _('customer')),      
    ])
    '''
    def __str__(self):
        return self.name

class Employee(models.Model):
    emp_id = models.IntegerField(max_length=10, primary_key=True)
    emp_fname = models.CharField(max_length=255)
    emp_lname = models.CharField(max_length=255)
    entrance_date = models.DateField()
    leave_date = models.DateField()
    dep_id = models.IntegerField()
    dep_name = models.CharField(max_length=255)
    days_left = models.IntegerField()
    bonus = models.IntegerField()
    reimburse = models.IntegerField()
    account_acc_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    '''
    employee_type = models.CharField(choices=[
        (EmployeeType.accountant, _('accountant')),
        (EmployeeType.sale, _('sale')),      
    ])
    '''
    def __str__(self):
        return self.name

class Accountant(models.Model):
    phone = models.IntegerField(max_length=10)
    position = models.CharField(max_length=255)
    account_acc_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Customer(models.Model):
    cus_id = models.IntegerField(max_length=10, primary_key=True)
    contract_id = models.IntegerField()
    issue_date = models.DateField()
    expires_date = models.DateField()
    company_id = models.IntegerField()
    address_com = models.CharField(max_length=255)
    phone_com = models.IntegerField()
    other =models.TextField()
    account_acc_id = models.ForeignKey(Employee, on_delete=models.CASCADE)

class Sale(models.Model):
    phone = models.IntegerField(max_length=10)
    position = models.CharField(max_length=255)
    sale_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Cost(models.Model):
    cost_id = models.IntegerField(max_length=10, primary_key=True)
    electric_bill = models.IntegerField()
    water_bill = models.IntegerField()
    rent_fee = models.IntegerField()
    repair_fee = models.IntegerField()
    other_fee = models.IntegerField()
    cost_account_id = models.ForeignKey(Accountant, on_delete=models.CASCADE)

class Aperture(models.Model):
    aper_id = models.IntegerField(max_length=10, primary_key=True)
    aper_area = models.CharField(max_length=255)
    aper_loc = models.CharField(max_length=255)
    aper_pic = models.CharField(max_length=255)
    aper_price = models.IntegerField()
    customer_cus_id = models.ForeignKey(Customer, on_delete=models.CASCADE)

class Manager(models.Model):
    manag_fname = models.CharField(max_length=255)
    manag_lname = models.CharField(max_length=255)
    manag_phone = models.IntegerField()
    manag_level = models.IntegerField()
    customer_cus_id = models.ForeignKey(Customer, on_delete=models.CASCADE)

class Store(models.Model):
    store_id = models.IntegerField(primary_key=True) 
    store_name = models.CharField(max_length=255)
    manager_id = models.IntegerField()
    branch = models.CharField(max_length=255)
    phone = models.IntegerField()
    company_id = models.IntegerField(primary_key=True) 
    cost_total = models.IntegerField()
    loc_id = models.IntegerField()
    repaired = models.CharField(max_length=255)
    other_notes = models.TextField()
    manage_manag_id = models.ForeignKey(Manager, on_delete=models.CASCADE)
    customer_cus_id = models.ForeignKey(Customer, on_delete=models.CASCADE)

    





    
        