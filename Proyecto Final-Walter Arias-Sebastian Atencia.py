def clasificar_altura(altura):
    if 400 <= altura <= 800:
        return "sumamente apto"
    elif (0 < altura < 400) or (801 <= altura <= 999):
        return "moderadamente apto"
    elif 1000 <= altura <= 1200:
        return "marginalmente apto"
    else:
        return "no apto"

def clasificar_profundidad(profundidad):
    if profundidad > 100:
        return "sumamente apto"
    elif 50 <= profundidad <= 100:
        return "moderadamente apto"
    elif 25 <= profundidad < 50:
        return "marginalmente apto"
    else:
        return "no apto"

def peor_categoria(cat1, cat2):
    categorias = ["sumamente apto", "moderadamente apto", "marginalmente apto", "no apto"]
    return cat1 if categorias.index(cat1) > categorias.index(cat2) else cat2

def main():
    n = int(input("Ingrese el número de lecturas: "))
    alturas = []
    profundidades = []

    conteo = {
        "sumamente apto": 0,
        "moderadamente apto": 0,
        "marginalmente apto": 0,
        "no apto": 0
    }

    for i in range(n):
        print(f"\nLectura {i+1}:")
        altura = float(input("Altura (msnm): "))
        profundidad = float(input("Profundidad efectiva del suelo (cm): "))

        alturas.append(altura)
        profundidades.append(profundidad)

        cat_altura = clasificar_altura(altura)
        cat_profundidad = clasificar_profundidad(profundidad)

        if cat_altura == cat_profundidad:
            categoria = cat_altura
        else:
            categoria = peor_categoria(cat_altura, cat_profundidad)

        conteo[categoria] += 1

    promedio_altura = sum(alturas) / n
    promedio_profundidad = sum(profundidades) / n

    print("\n--- Resultados ---")
    print(f"Promedio de altura: {promedio_altura:.2f}")
    print(f"Promedio de profundidad efectiva del suelo: {promedio_profundidad:.2f}")

    for categoria in conteo:
        print(f"{categoria} {conteo[categoria]}")

if __name__ == "__main__":
    main()
