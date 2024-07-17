bids = [int(x) for x in input("Enter All Bid : ").split(" ")]

if len(bids) < 2:
    print("not enough bidder")
    exit()
    
bids.sort()

if bids[-1] == bids[-2]:
    print("error : have more than one highest bid")
else:
    print(f"winner bid is {bids[-1]} need to pay {bids[-2]}")