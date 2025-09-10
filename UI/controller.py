import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model



    def handleCreaGrafo(self, e):
        x = self._view.txtX.value
        self._model.creaGrafo(x)

    def aeroportiConnessi(self):
        pass
    def cercaItinerario(self):
        pass

