a = int(input('組數為:'))
# a=3
for i in range(0,a):
    aa=input('第'+str(i+1)+'組為:').split(' ')
    # aa=[str(i+2),str(i+4)]
    print('第'+str(i+1)+'組應收費用為:',(int(aa[0])*250+int(aa[1])*175))