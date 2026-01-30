import mysql.connector
import time as t

print("Program started...")

try:
    print("Trying to connect...")

    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="itsmeVEDANT@098",
        database="atm_system",   
        port=3306,
        auth_plugin="mysql_native_password",
        use_pure=True,
        connection_timeout=5
    )

    print("Connection object created")

    if conn.is_connected():
        print("Connected Successfully")
    else:
        print("Not Connected")

except Exception as e:
    print("ERROR:", e)


def bill():

    cur = conn.cursor()

    order_id = int(input("Enter Order ID: "))
    product_name = input("Enter Product Name: ")
    price = float(input("Enter Price: "))
    quantity = int(input("Enter Quantity: "))

    amount = price * quantity

    sql = """INSERT INTO Products 
             (order_Id, product_Name, price, quantity, Amount) 
             VALUES (%s, %s, %s, %s, %s)"""

    values = (order_id, product_name, price, quantity, amount)

    cur.execute(sql, values)
    conn.commit()

    print("✅ Data inserted successfully!")
    print("Total Amount:", amount)

    filename = f"order_{order_id}.txt"
    with open(filename, "w") as f:
        f.write(f"""Order Id: {order_id}
Product Name: {product_name}
Price: {price}
Quantity: {quantity}
Total Amount: {amount}
Time: {t.ctime()}
""")

    cur.close()




bill()


conn.close()
print("Database connection closed.")
