# Variável int
num = int(input('Digite um valor: '))
# Tabuada
x1 = num * 1
x2 = num * 2
x3 = num * 3
x4 = num * 4
x5 = num * 5
x6 = num * 6
x7 = num * 7
x8 = num * 8
x9 = num * 9
x10 = num * 10
# Cores
cor = {'fim': '\033[m',
       'branco': '\033[30m'}
print("""
{}{}{} x 0 = 0
{}{}{} x 1 = {}{}{}
{}{}{} x 2 = {}{}{}
{}{}{} x 3 = {}{}{}
{}{}{} x 4 = {}{}{}
{}{}{} x 5 = {}{}{}
{}{}{} x 6 = {}{}{}
{}{}{} x 7 = {}{}{}
{}{}{} x 8 = {}{}{}
{}{}{} x 9 = {}{}{}
{}{}{}x 10 = {}{}{}""".format(  # até 5
    # X0
    cor['branco'], num, cor['fim'],
    # X1
    cor['branco'], num, cor['fim'],
    cor['branco'], x1, cor['fim'],
    # X2
    cor['branco'], num, cor['fim'],
    cor['branco'], x2, cor['fim'],
    # X3
    cor['branco'], num, cor['fim'],
    cor['branco'], x3, cor['fim'],
    # X4
    cor['branco'], num, cor['fim'],
    cor['branco'], x4, cor['fim'],
    # X5
    cor['branco'], num, cor['fim'],
    cor['branco'], x5, cor['fim'],
    # X6
    cor['branco'], num, cor['fim'],
    cor['branco'], x6, cor['fim'],
    # X7
    cor['branco'], num, cor['fim'],
    cor['branco'], x7, cor['fim'],
    # X8
    cor['branco'], num, cor['fim'],
    cor['branco'], x8, cor['fim'],
    # X9
    cor['branco'], num, cor['fim'],
    cor['branco'], x9, cor['fim'],
    # X10
    cor['branco'], num, cor['fim'],
    cor['branco'], x10, cor['fim']
))
