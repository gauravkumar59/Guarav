import mysql.connector as msc
from mysql.connector import Error
import streamlit as st


st.title("WELCOME TO STATE BANK OF INDIA ")

st.image(r'C:\\Users\\PC\\Desktop\\New_folder\\png-clipart-state-bank-of-india-thane-branch-banking-in-india-bank-blue-text-thumbnail-removebg-preview.png',width=200)


menu = st.sidebar.selectbox("MENU", ["CHECK BALANCE","AMOUNT TRANSFER"])



conn=msc.connect(
    host="localhost",
    user="root",
    password="root",
    database="transaction"
)   

# if conn.is_connected:
#     print("connected")

cur=conn.cursor()
try:
    def transaction_syestem(sender_acc_no,reciver_ac_no,transaction_amt):
        mtch_ac_no="select acc_num from transaction_table where acc_num= %s"
        matc_value=(sender_acc_no,)
        cur.execute(mtch_ac_no,matc_value)
        found=cur.fetchone()
        # print(found)
        if found:
            check_balance="select balance from transaction_table where acc_num= %s "
            chech_value=(sender_acc_no,)
            cur.execute(check_balance,chech_value)
            amt=cur.fetchone()[0]
            # print(amt)
            if amt>transaction_amt:
                minus_query="update transaction_table set balance=balance-%s where acc_num= %s  "   
                minus_value=(transaction_amt,sender_acc_no)
                cur.execute(minus_query,minus_value)
                conn.commit()
                plus_query="update transaction_table set balance=balance+%s where acc_num=%s  "   
                plus_value=(transaction_amt,reciver_ac_no)
                cur.execute(plus_query,plus_value)
                conn.commit()
            
                print("transaction suceessfull and your remainining balance is")
                
                chech_balnce="select * from transaction_table"
                cur.execute(chech_balnce)
                a=cur.fetchall()
                for i in a:
                    print(i)

            else:
                print("amount is less then for transaction amt ")
        else:
            print("this acc not valid")

   
except Exception as e :
    print(e)
            
except Error as e:
    print(e)


def check_balnce():
    ans = st.text_input("Enter Account number")
    if ans == '':  # Check if the input is empty
        st.warning("Please enter a valid account number.")
    else:
        try:
            ans = int(ans)  # Convert the input to an integer if it's not empty
            if st.button("submit"):
                amt_check = f"select balance from transaction_table where acc_num={ans}"
                cur.execute(amt_check)
                bal = (cur.fetchone())[0]
                st.success(f"Your balance is {bal}")
        except ValueError:
            st.error("Invalid account number. Please enter a valid integer.")



def main ():
    if menu=="CHECK BALANCE":
           check_balnce()
    elif menu=="AMOUNT TRANSFER":
        sender_acc_no = int(st.text_input("Enter Sender Account Number"))
        receiver_ac_no = int(st.text_input("Enter Receiver Account Number"))
        transaction_amte = int(st.text_input("Enter Transaction Amount"))
        if st.button("submitt"):
         
            transaction_syestem(sender_acc_no,receiver_ac_no,transaction_amte)
            st.success("Transaction sucessfull")

main()