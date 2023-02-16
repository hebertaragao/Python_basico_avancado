#!Python3
def fatorial(n):
    return (n * fatorial(n - 1)) if n > 1 else 1


if __name__ == '__main__':
    n = 0
    print(f'{n}! = {fatorial(n)}')

    # 6 semanas em segundos é igual a 10!
    print(6 * 7 * 24 * 60 * 60)
