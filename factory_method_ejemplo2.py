# Ejemplo 2 de Factory Method (ahora con diferentes tipos de notificaciones)

class Notificacion:
    def enviar(self, mensaje):
        pass

class NotificacionEmail(Notificacion):
    def enviar(self, mensaje):
        return "Enviando email: " + mensaje

class NotificacionSMS(Notificacion):
    def enviar(self, mensaje):
        return "Enviando SMS: " + mensaje

class NotificacionWhatsApp(Notificacion):
    def enviar(self, mensaje):
        return "Enviando WhatsApp: " + mensaje

class NotificacionFactory:
    @staticmethod
    def crear_notificacion(tipo):
        if tipo == "email":
            return NotificacionEmail()
        elif tipo == "sms":
            return NotificacionSMS()
        elif tipo == "whatsapp":
            return NotificacionWhatsApp()
        else:
            raise ValueError("Tipo de notificación no válido")

if __name__ == "__main__":
    notificacion1 = NotificacionFactory.crear_notificacion("email")
    notificacion2 = NotificacionFactory.crear_notificacion("sms")
    notificacion3 = NotificacionFactory.crear_notificacion("whatsapp")

    print(notificacion1.enviar("Su préstamo vence mañana."))
    print(notificacion2.enviar("Tiene un libro pendiente de devolver."))
    print(notificacion3.enviar("Ya puede recoger su reserva."))
