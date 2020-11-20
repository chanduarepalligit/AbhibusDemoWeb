# Greatest common divisor of both numbers
def common(a, b):
    if b == 0:
        return a
    else:
        return common(b, a % b)


print(common(11, 22))