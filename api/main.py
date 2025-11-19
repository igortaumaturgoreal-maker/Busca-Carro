from scraping.olx import buscar_olx
from scraping.webmotors import buscar_webmotors
from scraping.icarros import buscar_icarros
from scraping.mobiauto import buscar_mobiauto
from fipe.fipe_api import get_fipe
from utils.filtros import filtrar
from utils.planilha import registrar
from utils.notificacao import notificar

def handler(request):
    anuncios = []
    
    anuncios += buscar_olx()
    anuncios += buscar_webmotors()
    anuncios += buscar_icarros()
    anuncios += buscar_mobiauto()

    for a in anuncios:
        fipe = get_fipe(a["modelo"], a["ano"])
        diff = fipe - a["preco"]
        
        if filtrar(a, diff):
            registrar(a, fipe, diff)
            notificar(a, fipe, diff)

    return {"status": "ok"}
