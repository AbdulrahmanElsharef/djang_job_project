import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

import django
django.setup()


from faker import Faker
import random
import string
from board.models import *
from blog.models import *
from django.contrib.auth.models import User




# def seed_Category(n):
#     fake=Faker()
#     CAT=('Creative','Design','Marketing','Administration','Teaching' , 'Education','Engineering','Software','Web','Telemarketing')
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


# def seed_Candidates(n):
#     fake=Faker()
#     IMAGE=['1.png','2.png','3.png','4.png','5.png','6.png','7.png','8.png','9.png','10.png']
#     for _ in range(n):
#         Candidates.objects.create(
#         job=Job.objects.get(id=random.randint(1,499)),
#         name=fake.name(),
#         email= f"{fake.name()}_{str(random.randint(1975,2002))}@gmail.com".lower(),
#         image=f"Candidates/{IMAGE[random.randint(0,9)]}",
#         linkedin='https://www.linkedin.com/',
#         cv="Candidates/0911-learning-django.pdf",
#         cover=fake.text(max_nb_chars=1000),
#         )
#     print(f"{n} Candidates seed ")

# seed_Candidates(100)


# def seed_Post(n):
#     fake=Faker()
#     # IMAGE=['post_1.png','post_2.png','post_3.png','post_4.png','post_5.png','post_6.png','post_7.png','post_8.png','post_9.png','post_10.png']
#     for _ in range(n):
#         Post.objects.create(
#         # author=User.objects.get(id=1),
#         # title=f'{fake.name()} Post',
#         # subtitle=fake.text(max_nb_chars=150),
#         # article=fake.text(max_nb_chars=2500),
#         # image=f"posts/{IMAGE[random.randint(0,9)]}",
#         # category=Category.objects.get(id=random.randint(1,19)),
#         )
#     print(f"{n} Post seed ")

# seed_Post(100)


def seed_Review(n):
    fake=Faker()
    for _ in range(n):
        Review.objects.create(
            post=Post.objects.get(id=random.randint(1,99)),            
            author=User.objects.get(id=1),
            review=fake.text(max_nb_chars=300),
        )
    print(f"{n} Review seed ")
    
seed_Review(300)



