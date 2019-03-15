class definePrice:
  a4p = 2.5
  a3p = 3.5
  
  def __init__(self, price, weight, format, vol):
    self.price = price
    self.weight = weight
    self.vol = vol
    self.format = format
    
  def letterPrice(self): 
    if ( self.format == 'a4' )
      return (a4p +1)*self.weight
    else
      return (a3p +1)*self.weight
    
  def boxPrice(self):
    return (0.25*self.vol)*self.weight
    
    
    
  class display:
    
    def __init__(self, dest, exp, weight, format, type, vol):
      self.dest = dest
      self.exp = exp
      self.weight = weight
      self.format = format
      self.type = type
      self.vol = vol
      
    def _print(self)
      if ( type == 'letter' )
        print('cout de la lettre', definePrice.letterPrice(self))
      else 
        print('cout du colis')
