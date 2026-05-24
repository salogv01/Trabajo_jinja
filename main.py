from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates



app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def Peliculas(request: Request):
    return templates.TemplateResponse(request=request, name="pelicula.html", context={"pelicula": "Interestelar", "director": "Christopher Nolan", "anio": 2014, "nombre": "Salomé"})


colores = ["Red", "Blue", "Green", "Yellow", "Black"]

@app.get("/colores")
async def Colores(request: Request):
    return templates.TemplateResponse(request=request, name="colores.html", context={"colores": colores, "nombre": "Salomé"})

equipos = {

    "Nacional" : {
        "color": "#A8E6A3",
        "jugadores": [
        "David Ospina",
        "Andrés Felipe Román",
        "Jorman Campuzano",
        "Andrés Sarmiento",
        "Eduard Bello"
        ]
    },

    "Independiente Medellín" : {
        "color": "#FFB3B3",
        "jugadores": [
        "Eder Chaux",
        "José Ortiz",
        "Kevin Mantilla",
        "Frank Fabra",
        "Baldomero Perlaza"
        ]
    },

    "Junior" : {
        "color": "#A7C7E7",
        "jugadores": [
        "Mauro Silveira",
        "Mauro Silveira",
        "Juan David Ríos",
        "Jannenson Sarmiento",
        "Bryan Castrillón"
        ]
    }
}

@app.get("/equipos")
async def mostrar_equipos(request: Request):
    return templates.TemplateResponse(request=request, name="equipos.html", context={"equipos": equipos, "nombre": "Salomé"})