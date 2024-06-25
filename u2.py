import keyboard
import pyperclip

# Global list to store clipboard contents
clipboard_list = []

def save_clipboard():
    """Save the current clipboard content to the global list."""
    content = pyperclip.paste().strip()
    clipboard_list.append(content)
    print(f"Saved: {content}")

def copy_list_to_clipboard(numbered=False):
    """Copy the contents of the list to the clipboard, optionally with numbered bullets."""
    if numbered:
        content = "\n".join(f"{i+1}. {item}" for i, item in enumerate(clipboard_list))
    else:
        content = "\n".join(clipboard_list)
    pyperclip.copy(content)
    print("All items copied to clipboard")

def clear_list():
    """Clear the global list."""
    clipboard_list.clear()
    print("List cleared")

# Set hotkeys
keyboard.add_hotkey('ctrl+space', save_clipboard)
keyboard.add_hotkey('ctrl+f1', lambda: copy_list_to_clipboard(numbered=False))
keyboard.add_hotkey('ctrl+f2', clear_list)
keyboard.add_hotkey('ctrl+f3', lambda: copy_list_to_clipboard(numbered=True))

print("Hotkeys set up: 'Ctrl+Space' to save clipboard, 'Ctrl+F1' to copy list to clipboard, 'Ctrl+F2' to clear list, 'Ctrl+F3' to copy numbered list to clipboard.")
print("Press 'Esc' to exit.")

# Keep the script running
keyboard.wait('esc')
