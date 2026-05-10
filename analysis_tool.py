
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
