import re
import streamlit as st

#page styling
st.set_pageconfig(page_title= "Password Strenght Checker By Roshni Mahesh", page_icon ="🔑", layout ="Centered")
#Custom css
st.markdown("""
<style>
            .main {text-align: center;}
            .stTextInput {width: 60% ! important; margin:auto;}
            .stButton button {width:50%; background-color #4CAF50; color:white; font-size:18px;}
            .stButton button:hover {background-color: #45a049;}
<style>
""", unsafe_allow_html=True)

#page title and description
st.title("🔐 Password Strenght Generation")
st.write ("Enter your password below to check its security level.🔍")

#function to check password strenght
def check_password_strenght(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1 #increase score by 1
    else:
        feedback.append("❌ password should be **alteast 8 Charaters Long**")

    if re.search(r"[A-Z]" , password) and re.search (r"[a-z]", password):
            score +=1
    else :
        feedback.append("❌ password should be **Both uppercase (A-Z) and lowercase letters(a-z)**.")

        if re.search (r"\d", password):
         score +=1
        else:
         feedback.append("❌ password should be **alteast one number (0-9)**.")

#special character
    if re.search(r"[!@#$%^&*]", password):
     score +=1
    else:
        feedback.append("❌ password should be **alteast one special character (!@#$%^&*)**.")

#display password strenght results
    if score == 4 :
     st.sucess("✅ **Strong Password** your password is secure.")
    elif score ==3 :
     st.info("⚠️ **Moderate Password** -Consider improving security by adding more feature")
    else:
     st.error("❌ **Week password** -follow the suggestion below to strenght it.")

#Feedback
    if feedback:
       with st.expander ("🔍**Improve your Password**"):
          for item in feedback:
             st.write(item)
password =st.text_input ("Enter Your Password:" , type= "password", help = "Ensure your password is strong 🔐" )

#Button Working
if st.button ("check strenght"):
   if password:
      check_password_strenght(password)
else:
   st.warning ("⚠️ Please enter password first!") #show warnig if password is empty
      





                        




