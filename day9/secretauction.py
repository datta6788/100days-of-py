auction={}
print("WELCOME TO THE SECRET AUCTION")
def secret_auction():
    # auction={}
    name=input("what's your name? ").upper()
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
max_amount=max(bid_amount)
max_amount_bidder=bidder_name[bid_amount.index(max_amount)]
print(f"THE WINNER OF THE AUCTION IS {max_amount_bidder} WITH A BID OF ₹{max_amount}")
