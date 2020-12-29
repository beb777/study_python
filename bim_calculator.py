def bim_calculator(name,height,weight):
    bim = weight/height **2
    if bim > 25:
           print('you are not under weight')
    else:
           print('you are under weight')
    return bim
name = input('enter your name :')
weight = float(input('enter your weight :'))
height = float(input('enter your height :'))
   
print(bim_calculator(name,height,weight))
