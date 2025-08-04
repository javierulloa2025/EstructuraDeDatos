def run(values: list) -> int:
    # TODO
    max_value = values[0]
    for i in values:
        if i > max_value:
            max_value = i 
    return max_value


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
