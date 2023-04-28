import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

import django
django.setup()


from faker import Faker
import random
from board.models import *
from blog.models import *
from django.contrib.auth.models import User




# def seed_Category(n):
#     fake=Faker()
#     CAT=('Creative','Design','Marketing','Administration','Teaching' , 'Education','Engineering','Software','Web','Telemarketing')
#     # images=['2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpeg','9.jpg','10.jpg','11.png','12.png','13.jpeg','14jpeg']
#     for _ in range(n):
#         Category.objects.create(
#             name=CAT[random.randint(0,9)],
#         )
#     print(f"{n} Category seed ")
# seed_Category(20)


# def seed_Job_Company(n):
#     fake=Faker()
#     COMP=('Amazon','Apple'
#     'Microsoft'
#     ,'Google',
#     'Facebook',
#     'Tesla',
#     'Coca-Cola',
#     "McDonald's",
#     'Toyota',
#     'Samsung',
#     'Nike',
#     'Procter & Gamble',
#     'IBM',
#     'Intel',
#     'General Electric',
#     'PepsiCo',
#     'Visa',
#     'Mastercard',
#     'JPMorgan Chase',)
#     ICON=['1.svg','1.svg','3.svg','4.svg','5.svg']
#     for _ in range(n):
#         Job_Company.objects.create(
#         name=COMP[random.randint(0,18)],
#         icon=ICON[random.randint(0,4)],
#         Fb_link='https://www.facebook.com/',
#         Gm_link='https://www.gmail.com/',
#         Tw_link='https://www.twiter.com/',
#         Yb_link='https://www.youtub.com/',
#         )
#     print(f"{n} Job_Company seed ")
# seed_Job_Company(50)



# def seed_job(n):
#     fake=Faker()
#     IMAGE=['1.svg','1.svg','3.svg','4.svg','5.svg']
#     JOB_TYPE=['Full_Time','Part_Time','Remotely']
#     for _ in range(n):
#         Job.objects.create(
#             author=User.objects.get(id=1),
#             title=f'{fake.name()} JOB',
#             image=IMAGE[random.randint(0,4)],
#             location=fake.address(),
#             company=Job_Company.objects.get(id=random.randint(1,49)),
#             category=Category.objects.get(id=random.randint(1,23)),
#             job_type=JOB_TYPE[random.randint(0,2)],
#             vacancy=random.randint(1,10),
#             salary=random.randint(5000,25000),
#             description=fake.text(max_nb_chars=1000),
#             Qualification=fake.text(max_nb_chars=1000),
#             Responsibility=fake.text(max_nb_chars=1000),
#             Benefits=fake.text(max_nb_chars=1000),
#         )
#     print(f"{n} JOB seed ")

# seed_job(500)

# def seed_ProductImage(n):
#     fake=Faker()
#     images=['2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpeg','9.jpg','10.jpg','11.png','12.png','13.jpeg','14jpeg']
#     for _ in range(n):
#         ProductImage.objects.create(
#             product=Product.objects.get(id=random.randint(1,999)),
#             image=f"product_images/{images[random.randint(1,12)]}"
#         )
#     print(f"{n} Images seed ")


# def seed_ProductReview(n):
#     fake=Faker()
#     for _ in range(n):
#         ProductReview.objects.create(
#             user=User.objects.get(id=1),
#             product=Product.objects.get(id=random.randint(1,999)),
#             rate=random.randint(0,5),
#             review=fake.text(max_nb_chars=500),
#         )
#     print(f"{n} Review seed ")



# seed_brand(100)
# seed_product(1000)
# seed_ProductImage(5000)