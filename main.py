from math import floor


def lbtt_calculator(house_value):
    # Initialise values
    remaining_house_value = house_value
    lbtt_value = 0

    # Obtained from https://revenue.scot/taxes/land-buildings-transaction-tax/residential-property
    rates = [0, 0.02, 0.05, 0.1, 0.12]
    # Value above which corresponding rate applies
    brackets = [0, 145000, 250000, 325000, 750000]

    for count, bracket in enumerate(brackets):
        if remaining_house_value > 0:
            try:
                taxable_amount = min(
                    brackets[count+1]-bracket, remaining_house_value)
            except IndexError:
                taxable_amount = remaining_house_value
            lbtt_value += taxable_amount * rates[count]
            remaining_house_value -= taxable_amount
        else:
            break
    return floor(lbtt_value)


if __name__ == "__main__":
    house_value = float(input("How much is your house worth? £"))
    LBTT_value = "{:,.2f}".format(lbtt_calculator(house_value))
    print(f"You must pay LBTT of £{LBTT_value}")
