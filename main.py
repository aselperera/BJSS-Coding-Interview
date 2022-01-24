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
    slabs = [(750000, 0.12), (325000, 0.1),
             (250000, 0.05), (145000, 0.02), (0, 0)]

    for slab in slabs:
        if remaining_house_value > slab[0]:
            lbtt_value += (remaining_house_value - slab[0])*slab[1]
            remaining_house_value = slab[0]
        else:
            continue

    return floor(lbtt_value)  # Round down to the nearest £


if __name__ == "__main__":
    house_value = float(input("How much is your house worth? £"))
    LBTT_value = "{:,.2f}".format(lbtt_calculator(house_value))
    print(f"You must pay LBTT of £{LBTT_value}")
