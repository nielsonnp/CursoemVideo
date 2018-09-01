v_metro = float(input('Digite um valor em metros: '))

v_cm = v_metro*100
v_mm = v_metro*1000

print('A medida de {}m corresponde a {:.0f}cm e {:.0f}mm'.format(v_metro, v_cm, v_mm))