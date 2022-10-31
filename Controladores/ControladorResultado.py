from Modelos.Resultado import Resultado
from Modelos.Mesa import Mesa
from Modelos.Candidato import Candidato
from Repositorios.RepositorioResultado import RepositorioResultado
from Repositorios.RepositorioMesa import RepositorioMesa
from Repositorios.RepositorioCandidato import RepositorioCandidato

class ControladorResultado():
    def __init__(self):
        self.repositorioResultados = RepositorioResultado()
        self.repositorioMesas = RepositorioMesa()
        self.repositorioCandidatos = RepositorioCandidato()

    def index(self):
        return self.repositorioResultado.findAll()
    """
    Asignacion Mesa y candidato a Resultado
    """
    def create(self,infoResultado,id_mesa,id_candidato):
        nuevaResultado=Resultado(infoResultado)
        elMesa=Mesa(self.repositorioMesas.findById(id_mesa))
        laCandidato=Candidato(self.repositorioCandidatos.findById(id_candidato))
        nuevaResultado.mesa=elMesa
        nuevaResultado.candidato=laCandidato
        return self.repositorioResultado.save(nuevaResultado)

    def show(self,id):
        elResultado=Resultado(self.repositorioResultado.findById(id))
        return elResultado.__dict__
    """
    Modificación de inscripción (mesa y Candidato)
    """
    def update(self,id,infoResultado,id_mesa,id_candidato):
        laResultado=Resultado(self.repositorioResultado.findById(id))
        laResultado.año=infoResultado["año"]
        laResultado.semestre = infoResultado["semestre"]
        laResultado.notaFinal=infoResultado["nota_final"]
        elMesa = Mesa(self.repositorioMesas.findById(id_mesa))
        laCandidato = Candidato(self.repositorioCandidatos.findById(id_candidato))
        laResultado.mesa = elMesa
        laResultado.candidato = laCandidato
        return self.repositorioResultado.save(laResultado)

    def delete(self, id):
        return self.repositorioResultado.delete(id)

    "Obtener todos los inscritos en una Candidato"
    def listarInscritosEnCandidato(self,id_candidato):
        return self.repositorioResultado.getListadoInscritosEnCandidato(id_candidato)

    "Obtener notas mas altas por curso"
    def notasMasAltasPorCurso(self):
        return self.repositorioResultado.getMayorNotaPorCurso()

    "Obtener promedio de notas en candidato"
    def promedioNotasEnCandidato(self,id_candidato):
        return self.repositorioResultado.promedioNotasEnCandidato(id_candidato)