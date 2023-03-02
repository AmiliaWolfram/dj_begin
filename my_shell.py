(venv) C:\Users\User\Desktop\dj_begin>python manage.py shell
>>> from shop.models import Item, Purchase
>>> Item.objects.all()
<QuerySet []>
>>> i_1 = Item(name="Sofa", price="20000")
>>> i_1.save()
>>> i_1.id
1
>>> i_1.name
'Sofa'
>>> i_1.price
'20000'
>>> i_2 = Item(name="Table", price="15000")
>>> i_2.price
'15000'
>>> i_3 = Item(name="Chair", price="10000")
>>> i_2.save()
>>> i_2.price
'15000'
>>> i_3.save()
>>> i_4 = Item(name="Shells", price="7000")
>>> i_4.save()
>>> i_5 = Item(name="Window", price="9900")
>>> i_5.save()
>>> p_1 = Purchase(name="Erevan", age=22, item_id=1)
>>> p_1.name
'Erevan'
>>> p_1.age
22
>>> p_1.item
<Item: Item object (1)>
>>> p_1.item.name
'Sofa'
>>> p_2 = Purchase(name="Loren", age=32, item_id=2)
>>> p_1.save()
>>> p_2.save()
>>> p_3 = Purchase(name="Zain", age=42, item_id=3)
>>> p_3.save()
>>> p_4 = Purchase(name="Eliot", age=19, item_id=4)
>>> p_4.save()
>>> p_5 = Purchase(name="Liana", age=25, item_id=5)
>>> p_5.save()
