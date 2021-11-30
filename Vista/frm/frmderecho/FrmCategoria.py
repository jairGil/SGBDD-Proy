from PySide2.QtWidgets import QTabWidget, QWidget

from Controlador.DMLCategoria import DMLCategoria
from Vista.dlg.DlgAviso import DlgAviso
from Vista.frm.frmderecho.altas.AltaCategoria import AltaCategoria
from Vista.frm.frmderecho.bajas.BajaCategoria import BajaCategoria
from Vista.frm.frmderecho.cambios.CambioCategoria import CambioCategoria
from Vista.frm.frmderecho.consultas.Consulta import Consulta

from Modelo.Categoria import Categoria


class FrmCategoria(QTabWidget):
    __dlg_aviso: DlgAviso

    def __init__(self, parent: QWidget):
        super().__init__(parent=parent)
        self.conexion = self.parent().conexion
        self.dml = DMLCategoria(self.conexion)

        self.alta = AltaCategoria()
        self.baja = BajaCategoria()
        self.cambio = CambioCategoria()
        self.consulta = Consulta()

        self.setup_ui()
        self.agrega_items()
        self.agrega_acciones_btn()
        self.agrega_acciones_cmbx()

    def setup_ui(self):
        self.addTab(self.alta, "Alta")
        self.addTab(self.baja, "Baja")
        self.addTab(self.cambio, "Cambio")
        self.addTab(self.consulta, "Consulta")

    def agrega_items(self):
        # Obtener los datos de la BDD
        encabezados, datos_tabla = self.dml.consulta_tabla()
        datos = self.dml.consulta()
        self.cambio.cmbx_categoria_cambio.addItem("")
        self.baja.cmbx_categoria_baja.addItem("")
        # Si existen dtos y encabezados entonces:
        if datos and encabezados:
            # Agregar items a la tabla
            self.consulta.agrega_items(encabezados, datos_tabla)
            # Item en el indice 0 es la cabecera
            self.baja.cmbx_categoria_baja.setItemText(0, "Seleccione una opcion")
            self.cambio.cmbx_categoria_cambio.setItemText(0, "Seleccione una opcion")
            # Para cada registro en los datos
            for reg in datos:
                # Crear una nueva categoria
                cat = Categoria(reg[0], reg[1], reg[2])
                # Añadir el elemento en los combo boxes
                self.cambio.cmbx_categoria_cambio.addItem(str(cat), cat)
                self.baja.cmbx_categoria_baja.addItem(str(cat), cat)

    def agrega_acciones_cmbx(self):
        self.baja.cmbx_categoria_baja.currentTextChanged.connect(self.baja.agregar_datos)
        self.cambio.cmbx_categoria_cambio.currentIndexChanged.connect(self.cambio.agregar_datos)

    def agrega_acciones_btn(self):
        self.alta.btn_agregar_alta.clicked.connect(self.insertar_categoria_db)
        self.baja.btn_eliminar_baja.clicked.connect(self.eliminar_categoria_db)
        self.cambio.btn_modificar_cambio.clicked.connect(self.modificar_categoria_db)

    def insertar_categoria_db(self):
        # Obtener el contenido de los campos de texto
        nombre = self.alta.txt_categoria_alta.text()
        desc = self.alta.txt_descripcion_alta.text()
        # Si nombre y desc no estan vacias
        if nombre and desc:
            # Obtener el id segun su secuencia
            id = self.dml.obten_id()
            # Crear una nueva categoria
            cat = Categoria(id, nombre, desc)
            print(cat.id)
            # Agregarla a la BDD
            self.dml.alta(cat)
            # Actualizar los combo boxes
            self.baja.cmbx_categoria_baja.addItem(str(cat), cat)
            self.cambio.cmbx_categoria_cambio.addItem(str(cat), cat)
            # Mostrar el aviso
            self.__dlg_aviso = DlgAviso(self, "Registro agregado correctamente.")
            self.actualiza_tabla()
        elif not (nombre or desc):
            self.__dlg_aviso = DlgAviso(self, "ERROR: Los campos se encuentran vacios")
        elif not nombre:
            self.__dlg_aviso = DlgAviso(self, "ERROR: El campo categoria está vacío")
        else:
            self.__dlg_aviso = DlgAviso(self, "ERROR: El campo descripcion está vacío")

        self.alta.limpiar_campos()

    def eliminar_categoria_db(self):
        index = self.baja.cmbx_categoria_baja.currentIndex()
        if index != 0:
            id = int(self.baja.txt_id_baja.text())
            self.dml.baja(id)
            self.baja.cmbx_categoria_baja.removeItem(index)
            self.cambio.cmbx_categoria_cambio.removeItem(index)
            self.__dlg_aviso = DlgAviso(self, "Registro eliminado con exito.")
            self.actualiza_tabla()
        else:
            self.__dlg_aviso = DlgAviso(self, "Primero debe seleccionar un elemento del combo box")

    def modificar_categoria_db(self):
        index = self.cambio.cmbx_categoria_cambio.currentIndex()
        nombre = self.cambio.txt_nombre_cambio.text()
        descripcion = self.cambio.txt_descripcion_cambio.text()
        if index != 0:
            if nombre and descripcion:
                cat = self.cambio.cmbx_categoria_cambio.itemData(index)

                cat.nombre = nombre
                cat.descripcion = descripcion

                self.cambio.cmbx_categoria_cambio.setItemText(index, str(cat))
                self.cambio.cmbx_categoria_cambio.setItemData(index, cat)

                self.baja.cmbx_categoria_baja.setItemText(index, str(cat))
                self.baja.cmbx_categoria_baja.setItemData(index, cat)

                self.dml.cambio(cat)
                self.cambio.limpiar_campos()
                self.__dlg_aviso = DlgAviso(self, "Registro modificado correctamente")
                self.actualiza_tabla()
            else:
                if not(nombre or descripcion):
                    self.__dlg_aviso = DlgAviso(self, "ERROR: Los campos están vacíos")
                if not nombre:
                    self.__dlg_aviso = DlgAviso(self, "ERROR: El campo categoria está vacío")
                else:
                    self.__dlg_aviso = DlgAviso(self, "ERROR: El campo descripción está vacío")
        else:
            self.__dlg_aviso = DlgAviso(self, "ERROR: Seleccione un registro")

    def actualiza_tabla(self):
        encabezados, datos = self.dml.consulta_tabla()
        self.consulta.agrega_items(encabezados, datos)

    def remueve_items_cmbx(self):
        for i in range(1, self.cambio.cmbx_categoria_cambio.count()):
            self.cambio.cmbx_categoria_cambio.removeItem(i)
            self.baja.cmbx_categoria_baja.removeItem(i)


if __name__ == '__main__':
    import sys
    from PySide2.QtWidgets import QApplication

    app = QApplication(sys.argv)
    w = FrmCategoria(None)
    w.show()
    sys.exit(app.exec_())
