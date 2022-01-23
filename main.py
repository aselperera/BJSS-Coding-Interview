from math import floor


def lbtt_calculator(house_value):
    """Returns the LBTT for a given property price, subject to the following conditions:
    - The buyer of the property currently owns a property and lives in it as their main residence,
        i.e. they are not a first-time buyer
    - The property is for residential purposes only, i.e. non-commercial
    - The buyer does not own any other properties
    - The buyer will not own multiple properties upon purchase of this property,
        i.e. they will sell their existing property concurrently

    Note: the LBTT rates and bands here are for purchases made from 1 April 2021 onwards

    Args:
        house_value (float): Price of a property in £

    Returns:
        lbtt_value (float): LBTT payable on property, rounded down to the nearest £
    """

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
                # Catches the case where value > £750,000
                taxable_amount = remaining_house_value
            lbtt_value += taxable_amount * rates[count]
            remaining_house_value -= taxable_amount
        else:
            break
    return floor(lbtt_value)  # Round down to the nearest £


if __name__ == "__main__":
    house_value = float(input("How much is your house worth? £"))
    LBTT_value = "{:,.2f}".format(lbtt_calculator(house_value))
    print(f"You must pay LBTT of £{LBTT_value}")
