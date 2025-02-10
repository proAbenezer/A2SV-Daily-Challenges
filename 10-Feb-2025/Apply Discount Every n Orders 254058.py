# Problem: Apply Discount Every n Orders - https://leetcode.com/problems/apply-discount-every-n-orders/description/

class Cashier:
    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
      
        self.customer_count = 0
      
        self.discount_frequency = n
      
        self.discount_percentage = discount
         
        self.product_prices = {product: price for product, price in zip(products, prices)}

    def getBill(self, product: List[int], amount: List[int]) -> float:
        
        self.customer_count += 1
       
        is_discounted = self.customer_count % self.discount_frequency == 0
        
        total_bill = 0
      
         
        for prod, amt in zip(product, amount):
            
            total_price = self.product_prices[prod] * amt
          
          
            if is_discounted:
                total_price -= (self.discount_percentage * total_price) / 100
          
            
            total_bill += total_price
          
       
        return total_bill





# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)