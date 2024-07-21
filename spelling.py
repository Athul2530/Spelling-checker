from tkinter import *
from textblob import TextBlob


def check_spelling():
    input_text = spell_check.get("1.0", END).strip()

    # Process the text with TextBlob
    blob = TextBlob(input_text)
    corrected_text = str(blob.correct())

    # Clear previous output
    for widget in output_frame.winfo_children():
        widget.destroy()

    # Display the corrected text
    Label(output_frame, text="The Correct Spelling is:", font=("Helvetica", 24, "bold"), bg="#f8f9fa").pack(
        pady=(0, 10))
    Label(output_frame, text=corrected_text, font=("Helvetica", 30, "bold"), bg="#e9ecef", wraplength=700).pack(pady=10)


# Initialize the Tkinter window
window = Tk()
window.title("Spelling Checker")
window.geometry("900x700")
window.config(bg="#343a40")

# Heading
text_heading = Label(window, text="Spelling Checker", font=("Helvetica", 40, "bold"), bg="#343a40", fg="#f8f9fa")
text_heading.pack(pady=20)

# Text Entry
text_check = Label(window, text="Enter Your Text Below:", font=("Helvetica", 28), bg="#6c757d", fg="#f8f9fa")
text_check.pack(pady=(0, 10))

# Using Text widget for multi-line input
spell_check = Text(window, font=("Helvetica", 16), width=80, height=10, bg="#e9ecef", wrap=WORD, padx=10, pady=10)
spell_check.pack(pady=(0, 20))

# Check Button
check_button = Button(window, text="Check Spelling", font=("Helvetica", 24, "bold"), fg="#f8f9fa", bg="#007bff",
                      relief=FLAT, command=check_spelling)
check_button.pack(pady=20)

# Frame to display output
output_frame = Frame(window, bg="#343a40")
output_frame.pack(pady=20)

# Run the Tkinter event loop
window.mainloop()
