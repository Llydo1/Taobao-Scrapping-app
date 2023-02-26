import sys
sys.path.insert(0, '..')
import PySimpleGUI as sg
from Controller.product_controller import ProductController
from Controller.store_controller import StoreController

options = ["Option 1", "Option 2", "Option 3", "Option 4", "Exit"]

layout = [
    [sg.Text("Select an option:")],
    [sg.Listbox(values=options, size=(30, 6), key="-OPTIONS-")],
    [sg.Button("Ok"), sg.Button("Exit")],
]

def main():
    window = sg.Window("Menu", layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Exit":
            break
        elif event == "Ok":
            selected_option = values["-OPTIONS-"][0]
            if selected_option == "Exit":
                break
            elif selected_option == "Option 1":
                controller = StoreController()
                selected_option = controller.scrap_store(window)
                if selected_option is not None:
                    sg.popup("Scraped store successfully!", "ID: " + selected_option[0], "Item URL list: " + str(selected_option[1]))
                else:
                    sg.popup_error("Scraping store failed!")
    window.close()

if __name__ == "__main__":
    main()
