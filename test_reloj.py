from reloj import RelojDigital

def test_crear_reloj_digital():
    #preparo el rest, cofniciones inciales
    reloj = RelojDigital(0,0,0)
    
    #compruebor resultado esperado
    
    assert reloj.horas == 0
    assert reloj.minutos == 0
    assert reloj.segundos == 0
    assert reloj.info() == "00:00:00"
    
def test_crear_reloj_digital_con_hora_buena():
    
    reloj = RelojDigital(22,45,3)
    
    assert reloj.horas == 22
    assert reloj.minutos == 45
    assert reloj.segundos == 3
    assert reloj.info() == "22:45:03"
    
def test_crear_reloj_digital_con_horas_de_mas():
    
    reloj = RelojDigital(22,45,3)
    
    assert reloj.horas == 22
    assert reloj.minutos == 45
    assert reloj.segundos == 3
    assert reloj.info() == "22:45:03"
    
def test_crear_reloj_digital_sumando_min_seg_de_mas():
    
    reloj = RelojDigital(35, 63, 75)
    
    reloj.avanzar_tiempo()
        
    assert reloj.horas == 12
    assert reloj.minutos == 4
    assert reloj.segundos == 16
    assert reloj.info() == "12:04:16"

        
def test_crear_reloj_digital_sumando_un_seg():
        
    reloj = RelojDigital(12,4,59)
    
    reloj.tic()
        
    assert reloj.horas == 12
    assert reloj.minutos == 5
    assert reloj.segundos == 00
    assert reloj.info() == "12:05:00"    