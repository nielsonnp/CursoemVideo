larg = float(input('Largura da parede em M: ' ))
alt = float(input('Altura da parede em M: ' ))
area = larg * alt
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(larg, alt, area))
tinta = area / 2
print('Para pintar essa parede, você precisará de {}L de tinta.'.format(tinta))