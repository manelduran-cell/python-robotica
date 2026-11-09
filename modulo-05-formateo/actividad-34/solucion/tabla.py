ultrasonidos = 40
infrarrojos = 12
luz = 7

barra = "#" * (ultrasonidos // 5)
print(f"Ultrasonidos: {ultrasonidos:.1f} cm {barra}")

barra = "#" * (infrarrojos // 5)
print(f"Infrarrojos: {infrarrojos:.1f} cm {barra}")

barra = "#" * (luz // 5)
print(f"Luz: {luz:.1f} cm {barra}")