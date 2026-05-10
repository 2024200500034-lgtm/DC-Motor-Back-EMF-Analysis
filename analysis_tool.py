import os
import subprocess
import sys

# অটোমেটিক লাইব্রেরি ইন্সটল করার হ্যাক
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    import pandas as pd
    import matplotlib.pyplot as plt
except ImportError:
    install('pandas')
    install('matplotlib')
    import pandas as pd
    import matplotlib.pyplot as plt

import streamlit as st

# বাকি অ্যাপ কোড এখান থেকে শুরু
st.title("🏎️ DC Motor Analysis Dashboard")
st.write("ম্যাম, এই টুলটি সরাসরি ল্যাব ডাটা থেকে গ্রাফ তৈরি করে।")

# ইনপুট সেকশন
v_supply = st.number_input("Supply Voltage (V)", value=9.0)
r_armature = st.number_input("Armature Resistance (Ra)", value=4.0)

# ডাটা এন্ট্রি টেবিল
st.subheader("⌨️ ডাটা ইনপুট দিন (নিচের টেবিলে ক্লিক করে মান লিখুন)")
input_data = pd.DataFrame({
    "Condition": ["No Load", "Small Fan", "Big Fan"],
    "Current_Ia": [0.20, 0.50, 1.10]
})

edited_df = st.data_editor(input_data, num_rows="dynamic")

# ক্যালকুলেশন
if not edited_df.empty:
    edited_df["Back_EMF_Eb"] = v_supply - (edited_df["Current_Ia"] * r_armature)
    
    st.write("### ফলাফল টেবিল:")
    st.dataframe(edited_df)

    # গ্রাফ তৈরি
    st.write("### গ্রাফ (Ia vs Eb):")
    fig, ax = plt.subplots()
    ax.plot(edited_df["Current_Ia"], edited_df["Back_EMF_Eb"], marker='o', color='red', label='Back EMF')
    ax.set_xlabel("Armature Current (Ia)")
    ax.set_ylabel("Back EMF (Eb)")
    ax.grid(True)
    st.pyplot(fig)
    
import tkinter as tk
from tkinter import messagebox

# ক্যালকুলেশন ফাংশন
def calculate_eb():
    try:
        V = float(entry_v.get())
        Ia = float(entry_ia.get())
        Ra = float(entry_ra.get())
        
        # সূত্র: Eb = V - (Ia * Ra)
        Eb = V - (Ia * Ra)
        # Efficiency: (Eb / V) * 100
        efficiency = (Eb / V) * 100 if V > 0 else 0
        
        lbl_eb_result.config(text=f"{Eb:.2f} V", fg="#007bff")
        lbl_eff_result.config(text=f"{efficiency:.2f} %", fg="#28a745")
        
    except ValueError:
        messagebox.showerror("Error", "দয়া করে সঠিক সংখ্যা ইনপুট দিন")

# GUI উইন্ডো তৈরি
window = tk.Tk()
window.title("DC Motor Analysis Tool")
window.geometry("400x450")
window.configure(bg="#f8f9fa")

# স্টাইলিং ও লেবেল
tk.Label(window, text="Back EMF & Efficiency Calculator", font=("Arial", 14, "bold"), bg="#f8f9fa").pack(pady=10)

tk.Label(window, text="Supply Voltage (V):", bg="#f8f9fa").pack()
entry_v = tk.Entry(window, font=("Arial", 12))
entry_v.pack(pady=5)

tk.Label(window, text="Armature Current (Ia):", bg="#f8f9fa").pack()
entry_ia = tk.Entry(window, font=("Arial", 12))
entry_ia.pack(pady=5)

tk.Label(window, text="Armature Resistance (Ra):", bg="#f8f9fa").pack()
entry_ra = tk.Entry(window, font=("Arial", 12))
entry_ra.pack(pady=5)

# বাটন
btn_calc = tk.Button(window, text="Calculate Now", command=calculate_eb, bg="#007bff", fg="white", font=("Arial", 12, "bold"), padx=20)
btn_calc.pack(pady=20)

# রেজাল্ট ডিসপ্লে
tk.Label(window, text="Back EMF (Eb):", font=("Arial", 12), bg="#f8f9fa").pack()
lbl_eb_result = tk.Label(window, text="0.00 V", font=("Arial", 16, "bold"), bg="#f8f9fa")
lbl_eb_result.pack()

tk.Label(window, text="Motor Efficiency:", font=("Arial", 12), bg="#f8f9fa").pack(pady=5)
lbl_eff_result = tk.Label(window, text="0.00 %", font=("Arial", 16, "bold"), bg="#f8f9fa")
lbl_eff_result.pack()

window.mainloop()
