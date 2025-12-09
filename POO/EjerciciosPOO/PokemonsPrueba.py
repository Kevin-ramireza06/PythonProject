from PokemnosModulos import Pokemon,PokemonLegendario,Equipo
#De esta forma separamos la clase pokemon, y dejmos en un solo fichero la clase, y en la otra la purewba, y
#con los imports, los usamos

#tambien podemos solamente importar el fichero, pero se vuelve mas tedisoo, pq toca usar el alias que tenga aqui para
# usar sus metodos
#import PokemnosModulos
#p5 = PokemnosModulos.Pokemon(77,"Eve", "tierra")

#Los imports en python es como si literalmente copiaras y pegaras el codigo del otro fichero en una linea

p1 = Pokemon(1,"Pikachu", "Electrico" )
p2 = Pokemon(2,"Venusaur", "Planta")
p3 = Pokemon(3,"Charizard", "Fuego" )

p1.setEvolucion(p2)

p1.mostrar()
p2.mostrar()

p2 = p2.evoluciona()
p1 = p1.evoluciona()

p1.mostrar()
p2.mostrar()
p3.mostrar()

print(p2.combate(p3))