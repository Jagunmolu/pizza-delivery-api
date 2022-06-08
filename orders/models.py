from django.db import models
from django.contrib.auth import get_user_model



User = get_user_model()

class Orders(models.Model):

    SIZE = (
    ('SMALL', 'small'),
    ('MEDIUM', 'medium'),
    ('LARGE', 'large'),
    ('EXTRA_LARGE', 'extra_large'),
    )

    ORDER_STATUS = (
        ('PENDING', 'pending'),
        ('IN_TRANSIT', 'in_transit'),
        ('DELIVERED', 'delivered'),
    )
    
    customer=models.ForeignKey(User, on_delete=models.CASCADE)
    size=models.CharField(max_length=20, choices=SIZE, default=SIZE[0][0])
    order_status=models.CharField(max_length=20, choices=ORDER_STATUS, default=ORDER_STATUS[0][0])
    quantity=models.PositiveIntegerField(default=1)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'<Order {self.size} by {self.customer.id}'

    class Meta:
        verbose_name_plural = "Orders"
