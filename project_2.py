import os
class Stock():
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ADD STOCK <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<   
 def add_stock(self, name, quantity, price, retail_price, freepack):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.retail_price = retail_price
        self.freepack = freepack
      # Adding The Stock As A Dictionary
        stock_list = {
        "Product Name ":self.name,
        "Quantity " :self.quantity,
        "Buying Price ":self.price,
        "Retail Price ":self.retail_price,
        "FreePacks ":self.freepack}
      # Write The Content Or Details To The File
        with open("products.txt","a") as file_product:
            file_product.write(f" {stock_list} \n ")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> SEARCH STOCK <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
 def search_stock(self):
    with open("products.txt", "r") as f:
        while f:
         content = f.readline()
         if self.name in content.lower():
            print("Yes It's In The Stock \n")
            print(content)
   
        print("Search Done \n")
# >>>>>>>>>>>>>>>>>>>>>>>>> DETAILS CHANGE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#  def change_details(self):
        

  


product = Stock()
# product.add_stock("Lays Salt 30rs", 7, 610, 760, 6)
product.name = "hello"
product.search_stock()
# product.change_details()



