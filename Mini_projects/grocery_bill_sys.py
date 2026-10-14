def add_item(cart,name,quantity,price):
    cart.append({"name":name,"quantity":quantity,"price":price})
    return cart
def calculate_total(cart):
    subtotal=sum(item["quantity"]*item["price"]for item in cart)
    return subtotal
def calculate_gst(subtotal):
    gst=subtotal*0.05 #5%GST
    final_total=subtotal+gst
    return gst,final_total

#print_bill(cart, subtotal, gst, final_total

def print_bill(cart,subtotal,gst,final_total):
    print("\n HOJA SUPER MARKET")
    print("-----Customer bill-----")
    for item in cart:
        total_item=item["quantity"]*item["price"]
        print(f"{item['name']}({item['quantity']} x ${item['price']})....${total_item:.2f}")
    print("----------------------------")
    print(f"subtotal...........${subtotal:.2f}")
    print(f"GST (5%)...............${gst:.2f}")
    print(f"final_total............${final_total:.2f}")
    
def main():
    cart=[]
    while True:
        name=input("Enter item name(or done to finish):")
        if name.lower()=="done":
            break
        quantity=int(input("Enter quantity:"))
        price=float(input("Enter piece per item: "))
        add_item(cart,name,quantity,price)
        
    sub_total=calculate_total(cart)
    gst,final_total=calculate_gst(sub_total)
    print_bill(cart,sub_total,gst,final_total)       
    
if __name__=="__main__":
        main()
    