import sys
import hashlib
from datetime import datetime

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QFileDialog,
    QMessageBox,
    QGraphicsScene,
    QGraphicsItem,
    QGraphicsTextItem,
    QGraphicsPixmapItem,
)
from PySide6.QtGui import QFont, QPixmap, QImage
from PySide6.QtCore import Qt

from ui_mainwindow import Ui_MainWindow

# Usaremos pypdf para leer/escribir PDFs
from pypdf import PdfReader, PdfWriter


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # Cargamos lo diseñado en Qt Designer
        self.setupUi(self)

        # Estado
        self.ruta_pdf = None
        self.ruta_imagen = None

        # Configuramos la interfaz
        self._configurar_interfaz()
        # Conectamos señales
        self._conectar_senales()

    # ================== CONFIGURACIÓN INICIAL ==================

    def _configurar_interfaz(self):
        """Configura cosas iniciales de la ventana."""
        # Mensaje inicial en la barra de estado
        self.statusBar().showMessage("Listo: cargue un PDF para comenzar.")

        # Previsualización vacía
        self._actualizar_preview("Ningún PDF cargado.")

    def _conectar_senales(self):
        """Conecta botones y acciones de menú con funciones."""
        # Botón "Examinar..."
        self.btnExaminar.clicked.connect(self.on_examinar_pdf)

        # Botón "Seleccionar Imagen"
        self.btnSeleccionarImagen.clicked.connect(self.on_seleccionar_imagen)

        # Botón "Aplicar firma al PDF"
        self.btnFirmar.clicked.connect(self.on_firmar_pdf)

        # Menú Archivo
        self.actionAbrirPdf.triggered.connect(self.on_examinar_pdf)
        self.actionGuardarFirmado.triggered.connect(self.on_guardar_firmado)
        self.actionSalir.triggered.connect(self.close)

        # Menú Ayuda
        self.actionAcercaDe.triggered.connect(self.on_acerca_de)

    # ================== PREVISUALIZACIÓN ==================

    def _actualizar_preview(self, texto):
        """
        Muestra un texto en el QGraphicsView simulando una previsualización.
        """
        escena = QGraphicsScene(self)
        item_texto = QGraphicsTextItem(texto)
        fuente = QFont()
        fuente.setPointSize(12)
        item_texto.setFont(fuente)
        escena.addItem(item_texto)
        self.gvPreview.setScene(escena)

    # ================== LOGICA DE NEGOCIO ==================

    def _calcular_hash(self, ruta_archivo):
        """Calcula el hash SHA256 del archivo."""
        sha256_hash = hashlib.sha256()
        try:
            with open(ruta_archivo, "rb") as f:
                # Leer por bloques para no saturar memoria
                for byte_block in iter(lambda: f.read(4096), b""):
                    sha256_hash.update(byte_block)
            return sha256_hash.hexdigest()
        except Exception as e:
            print(f"Error calculando hash: {e}")
            return "Error"

    # ================== ACCIONES PRINCIPALES ==================

    def on_examinar_pdf(self):
        """Permite al usuario elegir un PDF desde el disco."""
        ruta, _ = QFileDialog.getOpenFileName(
            self,
            "Seleccionar PDF",
            "",
            "Archivos PDF (*.pdf);;Todos los archivos (*.*)",
        )

        if not ruta:
            return  # Usuario canceló

        self.ruta_pdf = ruta
        self.leRutaPdf.setText(ruta)

        # Calcular Hash
        hash_doc = self._calcular_hash(ruta)
        self.lblHash.setText(f"SHA256: {hash_doc}")

        # Previsualización simple
        nombre_archivo = ruta.split("/")[-1].split("\\")[-1]
        self._actualizar_preview(f"PDF cargado:\n{nombre_archivo}")

        self.statusBar().showMessage(f"PDF cargado: {nombre_archivo}", 3000)

    def on_seleccionar_imagen(self):
        """Selecciona una imagen para la firma."""
        ruta, _ = QFileDialog.getOpenFileName(
            self,
            "Seleccionar Imagen de Firma",
            "",
            "Imágenes (*.png *.jpg *.jpeg *.bmp);;Todos los archivos (*.*)",
        )

        if not ruta:
            return

        self.ruta_imagen = ruta
        
        # Mostrar preview en el label
        pixmap = QPixmap(ruta)
        if not pixmap.isNull():
            # Escalar para que quepa
            pixmap = pixmap.scaled(200, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.lblPreviewImagen.setPixmap(pixmap)
            self.lblPreviewImagen.setText("") # Borrar texto
        else:
            self.lblPreviewImagen.setText("Error al cargar imagen")

    def on_firmar_pdf(self):
        """
        Aplica la 'firma' al PDF.
        """
        if not self.ruta_pdf:
            QMessageBox.warning(self, "Aviso", "Primero debes cargar un PDF.")
            return

        # Determinar tipo de firma según tab activo
        idx_tab = self.tabWidget.currentIndex()
        
        datos_firma = {}
        
        if idx_tab == 0: # Texto
            firmante = self.leFirmante.text().strip()
            motivo = self.leMotivo.text().strip()

            if not firmante:
                QMessageBox.warning(self, "Aviso", "Introduce el nombre del firmante.")
                return
            if not motivo:
                QMessageBox.warning(self, "Aviso", "Introduce el motivo de la firma.")
                return
            
            datos_firma["tipo"] = "Texto"
            datos_firma["firmante"] = firmante
            datos_firma["motivo"] = motivo

        else: # Imagen
            if not self.ruta_imagen:
                QMessageBox.warning(self, "Aviso", "Selecciona una imagen para la firma.")
                return
            
            datos_firma["tipo"] = "Imagen"
            datos_firma["imagen_path"] = self.ruta_imagen

        # Pedimos dónde guardar el PDF firmado
        ruta_salida, _ = QFileDialog.getSaveFileName(
            self,
            "Guardar PDF firmado",
            "documento_firmado.pdf",
            "Archivos PDF (*.pdf);;Todos los archivos (*.*)",
        )

        if not ruta_salida:
            return

        try:
            self._firmar_pdf(self.ruta_pdf, ruta_salida, datos_firma)
        except Exception as e:
            QMessageBox.critical(
                self,
                "Error al firmar",
                f"Ocurrió un error al firmar el PDF:\n{e}",
            )
            return

        self.statusBar().showMessage(f"PDF firmado guardado en: {ruta_salida}", 5000)
        QMessageBox.information(
            self,
            "Firma completada",
            "El PDF se ha firmado correctamente.\n"
            f"Ruta de salida:\n{ruta_salida}",
        )

    def _firmar_pdf(self, ruta_entrada, ruta_salida, datos_firma):
        """
        Lógica de firma:
        - Copia el PDF de entrada a salida.
        - Añade metadatos de firma.
        """
        reader = PdfReader(ruta_entrada)
        writer = PdfWriter()

        # Copiamos todas las páginas tal cual
        for page in reader.pages:
            writer.add_page(page)

        # Fecha/hora de la "firma"
        fecha_firma = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Hash del documento original (ya calculado en UI, pero recalculamos por seguridad o consistencia)
        doc_hash = self._calcular_hash(ruta_entrada)

        # Metadatos
        nuevo_metadata = {
            "/SignedAt": fecha_firma,
            "/DocumentHash": doc_hash,
            "/SignatureType": datos_firma["tipo"],
        }
        
        if datos_firma["tipo"] == "Texto":
            nuevo_metadata["/SignedBy"] = datos_firma["firmante"]
            nuevo_metadata["/SignatureReason"] = datos_firma["motivo"]
        elif datos_firma["tipo"] == "Imagen":
            nuevo_metadata["/SignatureImage"] = datos_firma["imagen_path"]

        writer.add_metadata(nuevo_metadata)

        # Guardamos el nuevo PDF
        with open(ruta_salida, "wb") as f:
            writer.write(f)

    def on_guardar_firmado(self):
        QMessageBox.information(
            self,
            "Información",
            "Para guardar un PDF firmado, usa el botón 'Aplicar firma al PDF'.",
        )

    def on_acerca_de(self):
        """Muestra información sobre la aplicación."""
        QMessageBox.information(
            self,
            "Acerca de DocuSecure",
            "Aplicación de Firma Digital de Documentos\n"
            "Asignatura: Desarrollo de Interfaces (2º DAM)\n"
            "Tecnologías: PySide6 + pypdf + hashlib",
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
