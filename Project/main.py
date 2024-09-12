import customtkinter
from pick_up_currency import currency_names, available_conversions
from get_quotes import converter_currency

# Make and configure the window
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

window = customtkinter.CTk()
window.geometry('500x500')

dic_available_conversions = available_conversions()

# Create Button, labels, and other elements
title = customtkinter.CTkLabel(window, text='Currency Converter', font=('', 20))

text_currency_origin = customtkinter.CTkLabel(window, text='Select the currency of origin')
text_destination_currency = customtkinter.CTkLabel(window, text='Select the currency destination')

# Function to update the destination currencies based on selected origin currency
def load_target_coins(select_currency):
    if select_currency in dic_available_conversions:
        list_destination_currency = dic_available_conversions[select_currency]
        field_destination_currency.configure(values=list_destination_currency)
        field_destination_currency.set(list_destination_currency[0])
    else:
        field_destination_currency.configure(values=['No available currencies'])
        field_destination_currency.set('No available currencies')

# Create the origin currency dropdown menu
field_currency_origin = customtkinter.CTkOptionMenu(window, values=list(dic_available_conversions.keys()), command=load_target_coins)

# Initialize the destination currency dropdown menu with a placeholder
field_destination_currency = customtkinter.CTkOptionMenu(window, values=['Selecione uma moeda para converter'])
field_destination_currency.set('Selecione uma moeda para converter')

# Function to handle currency conversion
def handle_currency_conversion():
    currency_origin = field_currency_origin.get()
    destination_currency = field_destination_currency.get()
    if currency_origin and destination_currency and destination_currency != 'Selecione uma moeda para converter':
        quot = converter_currency(currency_origin, destination_currency)
        text_quot_currency.configure(text=f'1 {currency_origin} = {quot} {destination_currency}')
        print(f'The conversion rate from {currency_origin} to {destination_currency} is {quot}')
    else:
        print("Please select valid currencies.")

text_quot_currency = customtkinter.CTkLabel(window, text='')

button_converter = customtkinter.CTkButton(window, text='Convert', command=handle_currency_conversion)

currency_list = customtkinter.CTkScrollableFrame(window)

available_currencies = currency_names()
for currency_code in available_currencies:
    currency_name = available_currencies[currency_code]
    text_currency = customtkinter.CTkLabel(currency_list, text=f'{currency_code}: {currency_name}')
    text_currency.pack()

# Insert all elements on the screen
title.pack(padx=10, pady=10)
text_currency_origin.pack(padx=10, pady=10)
field_currency_origin.pack(padx=10)

text_destination_currency.pack(padx=10, pady=10)
field_destination_currency.pack(padx=10)

button_converter.pack(padx=10, pady=10)

text_quot_currency.pack(padx=10,pady=10)

currency_list.pack(padx=10, pady=10)

# Run the window
window.mainloop()
