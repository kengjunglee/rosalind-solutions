def mortal_rabbit_pairs(n: int, m: int) -> list[int]:
    """
    Compute the number of rabbit pairs alive after n months when each pair
    lives for exactly m months.

    Rabbits become mature at age 2 and produce one new pair each month
    until they die at the end of their m-th month.

    Args:
        n: The number of months to simulate (>= 1).
        m: The lifespan of each rabbit pair in months (>= 1).

    Returns:
        A list where index i holds the number of rabbit pairs alive after month i.
    """
    fib: list[int] = [0]*(n+1)
    fib[1] = 1
    for i in range (2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
        if i == m+1:
            fib[i] -= 1
        
        elif i > m+1:
            fib[i] -= fib[i-m-1]
    return fib

def main() -> None:
    n = 80
    m = 20

    fib: list[int] = mortal_rabbit_pairs(n, m)
    print(fib)
    print(fib[n])

    # from custom_io import parse_two_ints, write_result
    # n, m = parse_two_ints(__file__)
    # fib = mortal_rabbit_pairs(n, m)
    # print(fib[n])
    # write_result(__file__, str(fib[n]))


if __name__ == "__main__":
    main()
