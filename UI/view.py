import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.DARK
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.btn_hello = None
        self.txt_result = None
        self.txt_container = None
        self.txtX = None
        self.bottoneX = None
        self.row2 = None
        self.partenza=None
        self.inserisciPart=None
        self.btnP=None
        self.destinazione=None
        self.inserisciD=None
        self.tratte = None
        self.inserisceT = None
        self.btnI=None

    def load_interface(self):
        # title
        self._title = ft.Text("Esame turno c", color="blue", size=24)
        self._page.controls.append(self._title)

        self.p = ft.Text("", color="blue", size=12)
        self.txtX = ft.TextField(label="Numero compagnie minime X")
        self.bottoneX = ft.ElevatedButton(text="Analizza aeroporti", on_click= self._controller.handleCreaGrafo)
        self.row2 = ft.Row([self.p, self.txtX, self.bottoneX], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(self.row2)

        self.partenza = ft.Text("Aeroporto di partenza", color="blue", size=12)
        self.inserisciPart = ft.Dropdown(label="")
        self.btnP = ft.ElevatedButton(text="Aeroporti connessi", on_click=self._controller.aeroportiConnessi)
        row3= ft.Row([self.partenza, self.inserisciPart, self.btnP], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)

        self.destinazione= ft.Text("Aeroporto di destinazione", color="blue", size=12)
        self.inserisciD =  ft.Dropdown(label="")
        row4 = ft.Row([self.destinazione, self.inserisciD], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row4)

        self.tratte = ft.Text("Numero tratte massime", color="blue", size=12)
        self.inserisceT= ft.Dropdown(label="")
        self.btnI = ft.ElevatedButton(text="Cerca itinerario", on_click=self._controller.cercaItinerario)
        row5 = ft.Row([self.tratte, self.inserisceT, self.btnI], alignment=ft.MainAxisAlignment.CENTER)
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(row5)
        self._page.controls.append(self.txt_result)
        self.update_page()


    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
