from custom_io import parse_two_ints, write_result
def rabbit_pairs(n: int, k: int) -> list[int]:
    """
    Compute the number of rabbit pairs after each month up to n, with litter size k.

    This follows a modified Fibonacci recurrence: F(n) = F(n-1) + k * F(n-2),
    where each mature pair produces k pairs of offspring per generation.

    Args:
        n: The number of months (>= 1).
        k: The number of offspring pairs produced per mature pair.

    Returns:
        A list where index i holds the number of rabbit pairs after month i.
    month pairs
    0      0
    1.     1
    2.     1
    3      4: 1+1*3
    4.     7: 4+1*3 
    5.     19:7+4*3
    n.     F(n) = F(n-1)+F(n-2)*k, n>=2
    """
    p = [0]*(n+1)

    for i in range(n+1):
        if i == 1:
            p[i] = 1
        elif i >= 2:
            p[i] = p[i-1]+k*p[i-2]
    return p



def main() -> None:
    n = 5
    k = 3

    fib: list[int] = rabbit_pairs(n, k)
    print(fib)
    print(fib[n])

    
    n, k = parse_two_ints(__file__)
    fib = rabbit_pairs(n, k)
    print(fib[n])
    write_result(__file__, str(fib[n]))
    


if __name__ == "__main__":
    main()
