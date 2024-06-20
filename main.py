import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont, ImageTk

class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Watermark App")

        self.create_widgets()

    def create_widgets(self):
        # Frame to hold buttons
        frame_buttons = tk.Frame(self.root, padx=10, pady=10)
        frame_buttons.pack()

        # Button to select image file
        self.btn_select_image = tk.Button(frame_buttons, text="Select Image", command=self.select_image)
        self.btn_select_image.pack(side=tk.LEFT)

        # Button to add watermark
        self.btn_add_watermark = tk.Button(frame_buttons, text="Add Watermark", command=self.add_watermark, state=tk.DISABLED)
        self.btn_add_watermark.pack(side=tk.LEFT, padx=(10, 0))

        # Canvas to display image
        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.pack(pady=10)

    def select_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
        if file_path:
            self.image = Image.open(file_path)
            self.display_image()

            # Enable add watermark button
            self.btn_add_watermark.config(state=tk.NORMAL)

    def display_image(self):
        # Resize image to fit canvas
        self.image.thumbnail((400, 400))
        self.photo = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

    def add_watermark(self):
        # Create a copy of the image
        image_with_watermark = self.image.copy()

        # Add watermark
        draw = ImageDraw.Draw(image_with_watermark)
        font = ImageFont.load_default()
        text = "Your Watermark Text"

        # Calculate text size and position
        text_width, text_height = draw.textbbox((0, 0), text, font=font)[:2]
        x = (image_with_watermark.width - text_width) / 2
        y = (image_with_watermark.height - text_height) / 2

        # Draw text on the image
        draw.text((x, y), text, font=font, fill=(255, 255, 255, 128))

        # Save or display the image with watermark
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if save_path:
            image_with_watermark.save(save_path)
            messagebox.showinfo("Success", "Watermark added and saved successfully.")


if __name__ == "__main__":
    root = tk.Tk()
    app = WatermarkApp(root)
    root.mainloop()

