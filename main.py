import tkinter as tk

def calculate_max_weight_lifted():
    weight_lifted = float(weight_lifted_entry.get())
    reps = int(reps_entry.get())
    
    one_rep_max = weight_lifted * (1 + reps / 30)
    result_label.config(text="Estimated one rep max: {:.2f} lbs".format(one_rep_max))

root = tk.Tk()
root.title("One Rep Max Calculator")

# Define style options
font_style = ("Arial", 14)
label_color = "#FFFFFF"
bg_color = "#002B49"
input_bg_color = "#fff"
button_color = "#4caf50"
button_hover_color = "#66bb6a"
result_bg_color = "#D22630"

# Set the default font
root.option_add("*Font", font_style)

# Set the background color
root.configure(bg=bg_color)

# Create a frame for the input fields
input_frame = tk.Frame(root, bg=bg_color)
input_frame.pack(pady=20)

weight_lifted_label = tk.Label(input_frame, text="Weight lifted (in lbs): ", bg=bg_color, fg=label_color)
weight_lifted_label.grid(row=0, column=0, padx=10, pady=10)

weight_lifted_entry = tk.Entry(input_frame, width=5, font=font_style, bg=input_bg_color)
weight_lifted_entry.grid(row=0, column=1, padx=10, pady=10)

reps_label = tk.Label(input_frame, text="Number of reps: ", bg=bg_color, fg=label_color)
reps_label.grid(row=1, column=0, padx=10, pady=10)

reps_entry = tk.Entry(input_frame, width=5, font=font_style, bg=input_bg_color)
reps_entry.grid(row=1, column=1, padx=10, pady=10)

# Create a frame for the calculate button
button_frame = tk.Frame(root, bg=bg_color)
button_frame.pack(pady=10)

calculate_button = tk.Button(button_frame, text="Calculate", bg=button_color, activebackground=button_hover_color,
                             command=calculate_max_weight_lifted, font=font_style)
calculate_button.pack(padx=10, pady=5)

# Create a frame for the result label
result_frame = tk.Frame(root, bg=result_bg_color)
result_frame.pack(pady=10)

result_label = tk.Label(result_frame, text="", bg=result_bg_color, fg=label_color, font=font_style)
result_label.pack(padx=10, pady=5)

root.mainloop()

