def math_operations(*args, **kwargs):
    for i in range(len(args)):
        number = args[i]
        position = i % 4

        if position == 0:
            kwargs["a"] += number
        elif position == 1:
            kwargs["s"] -= number
        elif position == 2:
            if number != 0:
                kwargs["d"] /= number
        elif position == 3:
            kwargs["m"] *= number

    sorted_result = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))

    final_output = []
    for key, value in sorted_result:
        final_output.append(f"{key}: {value:.1f}")

    return "\n".join(final_output)