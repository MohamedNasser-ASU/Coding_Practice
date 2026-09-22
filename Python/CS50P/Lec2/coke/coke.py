def main():

    # 25, 10, 5

    due = 50
    while due > 0:
        print(f"Amount Due: {due}")
        coin = int(input("Insert Coin: "))
        if coin in (25, 10, 5):
            if coin > due or coin == due:
                print(f"Change Owed: {coin-due}")
                break
                # due -= coin
            else:
                due -= coin
main()
