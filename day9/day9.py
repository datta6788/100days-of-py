# dict={
#     'Hello': "namaskaram","python":"rakthapinjiroiiiii"
# }
# # print(dict["Hello"])
# # 
# print(dict['Hello'])
# dict['c']='cheruvu'
# print(dict['c'])
# # dict['Hello']='AAAAAAAGH'
# print(dict['Hello'])

# marks={
#     'A':'good',
#     'B':'fine',
#     'C':'dengey'
# }
# print(marks)

# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }

# student_grades ={}
# for scores in student_scores:
#     marks=student_scores[scores]
#     if marks>=91:
#         student_grades[scores]="Outstanding"
#     elif marks>=81:
#         student_grades[scores]="Exceeds Expectations"
#     elif marks>=71:
#         student_grades[scores]="Acceptable"
#     elif marks<=70:
#         student_grades[scores]="Fail"

# print(student_grades)

# travel={

#     'telangana':{'states':36,
#                  'states_visited': ['hyd','sangareddy','karimnagar']},
#     'ap':{"states":16,
#           'states_visited':['guntur','bapatla','cheerala']}

# }
# print(travel['telangana']['states_visited'][0])

# print(travel['telangana'][2])

# nested_list=['a','b',['c','d']]
# print(nested_list[2][1])

# print('I')
# print('\n'*100)
# print(input('type:'))
############################################################################################################################################
############################################################################################################################################
############################################################################################################################################

auction={}
print("BOA HANCOCK AUCTION")
def secret_auction():
    # auction={}
    name=input("what's your name? ")
    bid_amount=int(input("what's your bid? ₹"))
    auction[name]=bid_amount
    # print(auction)
bidding=True
while bidding:
    secret_auction()
    expl=input("is there anyone else who want to bid? Y/N:").lower()
    if expl=='y':
        print('\n'*50)
    else:bidding=False
bid_amount=[]
bidder_name=[]
for bidder in auction:
    bid_amount.append(auction[bidder])
    bidder_name.append(bidder)

# print(bid_amount)
# print(bidder_name)
max_amount=max(bid_amount)
max_amount_bidder=bidder_name[bid_amount.index(max_amount)]
# print(max_amount_bidder)
print(f"THE WINNER OF THE AUCTION IS {max_amount_bidder} WITH A BID OF ₹{max_amount}")
# print(bid_amount)

# print(auction)