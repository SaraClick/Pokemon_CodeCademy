class Pokemon:
  
  def __init__(self, name, level, type, is_knocked_out, max_health, health, max_level):
    self.name = name
    self.level = level
    self.type = type
    self.is_knocked_out = is_knocked_out
    self.max_health = max_health
    self.health = health
    self.max_level = max_level

  def __repr__(self):
    return """{name} is:
      Level: {level}
      Type: {type}
      Health: {health}""".format(name = self.name, level = self.level, type = self.type, health = self.health)
    
  def lose_health(self, damage):
    self.health -= damage
    if self.health <= 0:
      health = 0
      self.knock_out()
    else:
      print("{} health lost: {}".format(self.name, damage))
      print("{} now has {} health".format(self.name, self.health))

  def gain_health(self, gainedh):
    self.health += gainedh
    print("{} health gained: {}".format(self.name, gainedh))
    print("{} now has {} health".format(self.name, self.health))

  def knocked_out(self):
    if self.is_knocked_out:
      print("{} is already knocked out !".format(self.name))
    else:
      print("{} is now knocked out !".format(self.name))
    

  def attack(self, other_pokemon, damage):
    if self.is_knocked_out == True:
      print("You cannot attack, {} is knocked out".format(self.name))
      return
    elif self.type == "Fire" and other_pokemon == "Grass":
      damage *= other_pokemon.level
    elif self.type == "Fire" and other_pokemon == "Water":
      damage /= other_pokemon.level
    elif self.type == "Water" and other_pokemon == "Fire":
      damage *= other_pokemon.level    
    elif self.type == "Water" and other_pokemon == "Grass":
      damage /= other_pokemon.level
    elif self.type == "Grass" and other_pokemon == "Fire":
      damage /= other_pokemon.level
    elif self.type == "Grass" and other_pokemon == "Water":
      damage *= other_pokemon.level
      other_pokemon.lose_health(damage)
    print("{} attacked {} !!".format(self.name, other_pokemon.name))
    print("Your {} cuased {} damage on {} leaving him at {} health!!".format(self.name, damage, other_pokemon.name, other_pokemon.health))


  def gain_exp(self, exp):
    self.exp += exp
    print("{} experience gained! Your pokemon has now {} experience".format(exp, self.exp))
    if self.exp >= 5:
      self.level_up()
  
  def level_up(self):
    self.exp = 0
    if self.level <= self.max_level-1:
      self.level += 1
      self.max_health += 20
      print("{} leved up! {} is now level {} with maximum health of {}".format(self.name, self.name, self.level, self.max_health))
    else:
      print("{} is at maximum level!".format(self.name))


class Trainer:
  def __init__(self, name, pokemons, potions, current_pokemon):
    self.name = name
    self.pokemons = pokemons
    self.potions = potions
    self.current_pokemon = current_pokemon

  def __repr__(self):
    return "Trainer info. {name}, has pokemons: {pokemons}, has {potions} potions, current pokemon is {current_pokemon}.".format(name = self.name, pokemons = self.pokemons, potions = self.potions, current_pokemon = self.current_pokemon)
    
  def potion(self):
    if self.potions > 0:
      if self.current_pokemon.health < self.current_pokemon.max_health:
        self.current_pokemon.gain_health(1)
        self.potions -= 1
        print("{}: {} potions left".format(self.name, self.potions))
      else:
        print("{} is already at maximum health, potion not used!".format({self.current_pokemon}))
    else: 
      print("No potions left!")
    
  def attack_other(self, other_pokemon, damage):
    self.current_pokemon.attack(other_pokemon, damage)
  
  def switch_pokemon(self, pokemon):
    if pokemon.is_knocked_out == True:
      print("This pokemon is knocked out, chose another pokemon!")
    elif pokemon in self.pokemons:
      self.current_pokemon = pokemon
      print("{} has switched his pokemon to {}".format(self.name, self.current_pokemon))
  


  # The game (name, level, type, is_knocked_out, max_health,health):
pikachu = Pokemon("Pikachu", 3, "Fire", False, 50, 40, 10)
bulbasaur = Pokemon("Bulbasaur", 3, "Grass", False, 30, 20, 10)
squirtle = Pokemon("Squirtle", 3, "Water", False, 40, 30, 20)
charmander = Pokemon("Charmander", 3, "Fire", False, 60, 55, 15)

erika = Trainer('Erika', [pikachu], 2, pikachu)
ramos = Trainer('Ramos', [bulbasaur, squirtle], 2, bulbasaur)

print(pikachu)
print(bulbasaur)

pikachu.lose_health(1)
pikachu.gain_health(1)
