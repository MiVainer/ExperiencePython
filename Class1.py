from hero import *

myhero = Hero("Vurdalak", 5, "paladin")
mysuperhero = SuperHero("Sobaka", 10, "human", 10)

myhero.show_hero()
mysuperhero.show_hero()
mysuperhero.makemagic() #отнимает 10 от здоровья, изначально в классе superhero задано 100
mysuperhero.show_hero()
mysuperhero.makemagic()
mysuperhero.show_hero()