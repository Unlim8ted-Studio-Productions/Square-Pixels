import ctypes

# Get the window handle
hwnd = ctypes.windll.user32.GetForegroundWindow()

# Set the window shape
width, height = 800, 300  # Width and height of the window
rgn = ctypes.windll.gdi32.CreateEllipticRgn(0, 0, width, height)
ctypes.windll.user32.SetWindowRgn(hwnd, rgn, True)
