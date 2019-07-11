print()
print(80*'-')
print('                               Torre de Hanói                               ')
print(80*'-')
print()
haste1 = [' [33333333]','  [222222]','   [1111]']
haste2 = []
haste3 = []



def haste(haste1,haste2,haste3):
        print(40*'@')
        print()
        print(40*'-')
        print(' 1 -Haste --> ')
        for l in haste1[::-1]:
            print(l)
        print(40*'-')
        print(' 2 -Haste --> ')
        for j in haste2[::-1]:
            print(j)
        print(40*'-')
        print(' 3 -Haste --> ')
        for k in haste3[::-1]:
            print(k)
        print(40*'-')
        print()
        print(40*'@')
        

jorge = [' [33333333]','  [222222]','   [1111]']
print()
haste(haste1,haste2,haste3)
print()


while haste3 != jorge:
        print(80*'-')
        i = str(input('Digite qual das hastes você quer mover(1,2 ou 3): '))
        print(80*'=')
        if i == '1':
                if len(haste1) == 0:
                        print()
                        print(80*'!')
                        print('Não é possivel mover, pois, não a peça nesta haste')
                        print(80*'!')
                        print()
                
                else:
                        w = str(input('Digite 2 para move-la para a segunda Haste,ou 3 para move-la para a terceira Haste: '))
                        if w == '2':
                                if len(haste1) != 0  and len(haste2) != 0:
                                        if haste1[-1] > haste2[-1]:
                                                print()
                                                print('Não é possivel colocar uma peça maior em cima de menor!! ')
                                                print()
                                        else:
                                                haste2.append(haste1.pop())
                                else:
                                        haste2.append(haste1.pop())
                                                
                        if w == '3':
                                if len(haste1) != 0 and len(haste3) != 0:
                                        if haste1[-1] > haste3[-1]:
                                                print()
                                                print('Não é possivel colocar uma peça maior em cima de menor!! ')
                                                print()
                                        else:
                                                haste3.append(haste1.pop())
                                else:
                                        haste3.append(haste1.pop())

                        
                        
                print()
                print(haste(haste1,haste2,haste3))
                print()
                
        elif i == '2':
                if len(haste2) == 0:
                        print()
                        print(80*'!')
                        print('Não é possivel mover, pois, não a peça nesta haste')
                        print(80*'!')
                        print()
                else:
                        q = str(input('Digite 1 para move-la para a primeira Haste,ou 3 para move-la para a terceira Haste: '))
                        if q == '1':
                                if len(haste1) != 0 and len(haste2) != 0:
                                        if haste2[-1] > haste1[-1]:
                                                print()
                                                print('Não é possivel colocar uma peça maior em cima de menor!! ')
                                                print()
                                        else:
                                                haste1.append(haste2.pop())
                                else:
                                        haste1.append(haste2.pop())
                                
                        if q == '3':
                                if len(haste3) != 0 and len(haste2) != 0:
                                        if haste2[-1] > haste3[-1]:
                                                print()
                                                print('Não é possivel colocar uma peça maior em cima de menor!! ')
                                                print()
                                        else:
                                                haste3.append(haste2.pop())
                                else:
                                        haste3.append(haste2.pop())
                        
                print()
                print(haste(haste1,haste2,haste3))
                print()
                
        
        
        
        elif i == '3':
                if len(haste3) == 0:
                        print()
                        print(80*'!')
                        print('Não é possivel mover, pois, não a peça nesta haste')
                        print(80*'!')
                        print()
                else:
                        p = str(input('Digite 2 para move-la para a segunda Haste,ou 1 para move-la para a primeira Haste: '))
                        if p == '2':
                                if len(haste2) != 0 and len(haste3) != 0:
                                        if haste3[-1] > haste2[-1]:
                                                print()
                                                print('Não é possivel colocar uma peça maior em cima de menor!! ')
                                                print()
                                        else:
                                                haste2.append(haste3.pop())
                                else:
                                        haste2.append(haste3.pop())
                        

                        if p == '1':
                                if len(haste1) != 0 and len(haste3) != 0:
                                        if haste3[-1] > haste1[-1]:
                                                print()
                                                print('Não é possivel colocar uma peça maior em cima de menor!! ')
                                                print()
                                        else:
                                                haste1.append(haste3.pop())
                                else:
                                        haste1.append(haste3.pop())
                                                
                       
                print()
                print(haste(haste1,haste2,haste3))
                print()
                        

print()
print('Fim..')
print()
print('Parabéns Você conseguiu!!: ')
print('Resultado:')
print(' 3 -Haste --> ')
for k in haste3[::-1]:
    print(k)
