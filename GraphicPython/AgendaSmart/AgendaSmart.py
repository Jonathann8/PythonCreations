import PySimpleGUI as sg

# Função para criar a janela principal
def create_main_window(contact_list):
    layout = [
        [sg.Text('AgendaSmart', font=('Arial', 20), justification='center', background_color='#000000', text_color='#FFA500')],
        [sg.Listbox(values=contact_list, size=(40, 10), key='-CONTACT_LIST-', enable_events=True, background_color='#000000', text_color='#FFA500')],
        [sg.Button('Adicionar', button_color=('#FFA500', '#000000')), sg.Button('Editar', button_color=('#FFA500', '#000000')), sg.Button('Excluir', button_color=('#FFA500', '#000000')), sg.Button('Fechar', button_color=('#FFA500', '#000000'))],
        [sg.Text('AgendaSmart Version 1.0', font=('Arial', 10), justification='center', background_color='#000000', text_color='#FFA500')]
    ]
    return sg.Window('AgendaSmart', layout, size=(400, 300), background_color='#000000', finalize=True)

# Função para criar a janela de edição
def create_edit_window(contact=None):
    layout = [
        [sg.Text('Nome:', size=(15, 1), background_color='#000000', text_color='#FFA500'), sg.InputText(default_text=contact['name'] if contact else '', key='-NAME-')],
        [sg.Text('Telefone:', size=(15, 1), background_color='#000000', text_color='#FFA500'), sg.InputText(default_text=contact['phone'] if contact else '', key='-PHONE-')],
        [sg.Text('Email:', size=(15, 1), background_color='#000000', text_color='#FFA500'), sg.InputText(default_text=contact['email'] if contact else '', key='-EMAIL-')],
        [sg.Button('Salvar', button_color=('#FFA500', '#000000')), sg.Button('Cancelar', button_color=('#FFA500', '#000000'))]
    ]
    return sg.Window('Editar Contato', layout, size=(300, 200), background_color='#000000', finalize=True)

# Função para criar a janela de visualização
def create_view_window(contact):
    layout = [
        [sg.Text('Nome:', size=(15, 1), background_color='#000000', text_color='#FFA500'), sg.Text(contact['name'], size=(25, 1), key='-VIEW_NAME-')],
        [sg.Text('Telefone:', size=(15, 1), background_color='#000000', text_color='#FFA500'), sg.Text(contact['phone'], size=(25, 1), key='-VIEW_PHONE-')],
        [sg.Text('Email:', size=(15, 1), background_color='#000000', text_color='#FFA500'), sg.Text(contact['email'], size=(25, 1), key='-VIEW_EMAIL-')],
        [sg.Button('Fechar', button_color=('#FFA500', '#000000'))]
    ]
    return sg.Window('Visualizar Contato', layout, size=(300, 150), background_color='#000000', finalize=True)

# Função principal
def main():
    contacts = []
    contact_list = []
    main_window = create_main_window(contact_list)
    
    while True:
        event, values = main_window.read()
        
        if event == sg.WIN_CLOSED or event == 'Fechar':
            break
        
        if event == 'Adicionar':
            edit_window = create_edit_window()
            while True:
                e, v = edit_window.read()
                if e == sg.WIN_CLOSED or e == 'Cancelar':
                    break
                if e == 'Salvar':
                    name = v['-NAME-'].strip()
                    phone = v['-PHONE-'].strip()
                    email = v['-EMAIL-'].strip()
                    if name:
                        contacts.append({'name': name, 'phone': phone, 'email': email})
                        contact_list.append(name)
                        main_window['-CONTACT_LIST-'].update(contact_list)
                        edit_window.close()
                        break
        
        if event == 'Editar':
            selected_contact = values['-CONTACT_LIST-']
            if selected_contact:
                contact_name = selected_contact[0]
                contact = next(c for c in contacts if c['name'] == contact_name)
                edit_window = create_edit_window(contact)
                while True:
                    e, v = edit_window.read()
                    if e == sg.WIN_CLOSED or e == 'Cancelar':
                        break
                    if e == 'Salvar':
                        contact['name'] = v['-NAME-'].strip()
                        contact['phone'] = v['-PHONE-'].strip()
                        contact['email'] = v['-EMAIL-'].strip()
                        contact_list = [c['name'] for c in contacts]
                        main_window['-CONTACT_LIST-'].update(contact_list)
                        edit_window.close()
                        break

        if event == 'Excluir':
            selected_contact = values['-CONTACT_LIST-']
            if selected_contact:
                contact_name = selected_contact[0]
                contacts = [c for c in contacts if c['name'] != contact_name]
                contact_list = [c['name'] for c in contacts]
                main_window['-CONTACT_LIST-'].update(contact_list)
        
        if event == '-CONTACT_LIST-':
            selected_contact = values['-CONTACT_LIST-']
            if selected_contact:
                contact_name = selected_contact[0]
                contact = next(c for c in contacts if c['name'] == contact_name)
                view_window = create_view_window(contact)
                while True:
                    e, v = view_window.read()
                    if e == sg.WIN_CLOSED or e == 'Fechar':
                        view_window.close()
                        break

    main_window.close()

if __name__ == "__main__":
    main()
