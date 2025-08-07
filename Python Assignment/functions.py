def calculate_discount(price, discount_percent):
   if discount_percent >=20:
      a=(discount_percent/100) * price
      return(price-a)
   else:
        return price
   
 # Example usage 
print(calculate_discount(100, 20) )   