import random
when=["A few years ago", "Yesterday",'Last Night','A long time ago','On 20th Jan']
who=['a rabbit','an elephent','a mouse','a dog','a cat']
name=['Abdo','Jesse','Adam','Jack','Greg']
residence=['Sydney','Melbourne','Brisbane','Tasmania','Perth']
went=[" the Shop",'Collage','School','Party','Work']
happened=['made good friends','Eats a Banana','Found a secert door',
'solved a case','wrote a book']

print(random.choice(when) + ', ' + random.choice(who) + ' that lived in ' + random.choice(residence) + ", went to " + random.choice(went) + ' and ' + random.choice(happened))
