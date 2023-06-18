citas = [[1, 'Primera vez', 'BNS-150', 'Automóvil particular y vehículo de carga liviana (<3500kg)', 'Toyota', 'Forturner 4x4', 'Miguel Francisco Gonzalez', '01234567890123456789', 'josemiguel4484@gmail.com', 'Belén, Heredia', '09/06/2023 06:25 PM', 'PENDIENTE'], [], 
        [[2, 'Primera vez', 'BNS-150', 'Automóvil particular y vehículo de carga liviana (<3500kg)', 'Toyota', 'Forturner 4x4', 'Miguel Francisco Gonzalez', '01234567890123456789', 'josemiguel4484@gmail.com', 'Belén, Heredia', '09/06/2023 06:25 PM', 'PENDIENTE'], [], []]] 
"citas = [[1, 'Primera vez', 'BNS-150', 'Automóvil particular y vehículo de carga liviana (<3500kg)', 'Toyota', 'Forturner 4x4', 'Miguel Francisco Gonzalez', '01234567890123456789', 'josemiguel4484@gmail.com', 'Belén, Heredia', '09/06/2023 06:25 PM', 'PENDIENTE'], [], [[2, 'Primera vez', 'BNS-150', 'Automóvil particular y vehículo de carga liviana (<3500kg)', 'Toyota', 'Forturner 4x4', 'Miguel Francisco Gonzalez', '01234567890123456789', 'josemiguel4484@gmail.com', 'Belén, Heredia', '09/06/2023 06:25 PM', 'PENDIENTE'], [], []]]" 
def eliminar_cita (citas, numero_cita):
    return eliminar_cita_aux (citas, numero_cita)

def eliminar_cita_aux (citas, numero_cita):
    if citas == []:
        return []
    
    elif isinstance (citas [0], list):
        if not (citas [0] == []) and citas [0] [0] == numero_cita:
            return [[]] + eliminar_cita_aux (citas [1:], numero_cita)
        else:
            return [eliminar_cita_aux (citas [0], numero_cita)] + eliminar_cita_aux (citas [1:], numero_cita)
    else:
        return [citas [0]] + eliminar_cita_aux (citas [1:], numero_cita)
        
#print (eliminar_cita ([[1, 'Primera vez', 'BNS-150', 'Automóvil particular y vehículo de carga liviana (<3500kg)', 'Toyota', 'Forturner 4x4', 'Miguel Francisco Gonzalez', '01234567890123456789', 'josemiguel4484@gmail.com', 'Belén, Heredia', '09/06/2023 06:25 PM', 'PENDIENTE'], [], [[2, 'Primera vez', 'BNS-150', 'Automóvil particular y vehículo de carga liviana (<3500kg)', 'Toyota', 'Forturner 4x4', 'Miguel Francisco Gonzalez', '01234567890123456789', 'josemiguel4484@gmail.com', 'Belén, Heredia', '09/06/2023 06:25 PM', 'PENDIENTE'], [], []]], 2))

def modificar_estado_cita_cancelada (citas, numero_cita):
    return modificar_estado_cita_cancelada_aux (citas, numero_cita)

def modificar_estado_cita_cancelada_aux (citas, numero_cita):
    if citas == []:
        return []
    
    elif isinstance (citas [0], list):
        if not ((citas [0]) == []) and citas [0] [0] == numero_cita and citas [0] [-1] == "PENDIENTE":
            citas [0] [-1] = "CANCELADA"
        return [modificar_estado_cita_cancelada_aux (citas [0], numero_cita)] + modificar_estado_cita_cancelada_aux (citas [1:], numero_cita)

    else:
        return [citas [0]] + modificar_estado_cita_cancelada_aux (citas [1:], numero_cita)
    
print (modificar_estado_cita_cancelada ([[1, 'Primera vez', 'BNS-150', 'Automóvil particular y vehículo de carga liviana (<3500kg)', 'Toyota', 'Forturner 4x4', 'Miguel Francisco Gonzalez', '01234567890123456789', 'josemiguel4484@gmail.com', 'Belén, Heredia', '09/06/2023 06:25 PM', 'PENDIENTE'], [], 
            [[2, 'Primera vez', 'BNS-150', 'Automóvil particular y vehículo de carga liviana (<3500kg)', 'Toyota', 'Forturner 4x4', 'Miguel Francisco Gonzalez', '01234567890123456789', 'josemiguel4484@gmail.com', 'Belén, Heredia', '09/06/2023 06:25 PM', 'PENDIENTE'], [], []]], 2))

