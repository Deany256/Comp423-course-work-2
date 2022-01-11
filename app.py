from converting_units import (
    convert_into_KMPH,
    convert_into_MPH,
    get_mode_of_dictionary,
    get_smallest_value,
    get_largest_value,
)

if __name__ == "__main__":
    MPH = {}
    KMPH = {}
    count = 0

    print("Swallow Speed Analysis: Ver 1.0")
    print("Numbers should be prefixed with either E or U")
    print("Press ENTER when finished")

    while True:
        response = input("Enter next Reading: ").upper()
        if response == "":
            break
        count = count + 1
        if response.find("U") != -1:
            data = response.replace("U", "")
            data = float(data)
            MPH.update({count: data})
            KMPH.update({count: convert_into_KMPH(data)})
            print(f"saving {data}MPH")
        elif response.find("E") != -1:
            data = response.replace("E", "")
            data = float(data)
            KMPH.update({count: data})
            MPH.update({count: convert_into_MPH(data)})
            print(f"saving {data}KM/H")
        else:
            print("please enter valid data")
    print()
    print("Results Summary")
    print()
    print(f"{count} Readings analysed")
    print(
        f"Minimum Speed: {get_smallest_value(MPH)} MPH, {get_smallest_value(KMPH)} KM/H"
    )
    print(f"Maximum Speed: {get_largest_value(MPH)} MPH,{get_largest_value(KMPH)} KM/H")
    print(
        f"Average Speed: {get_mode_of_dictionary(MPH)} MPH, {get_mode_of_dictionary(KMPH)} KM/H"
    )
