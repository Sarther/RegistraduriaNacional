from Repositorios.InterfaceRepositorio import InterfaceRepositorio
from Modelos.Resultado import Resultado

from bson import ObjectId

class RepositorioResultado(InterfaceRepositorio[Resultado]):
    def getListadoInscritosEnCandidato(self, id_candidato):
        theQuery = {"candidato.$id": ObjectId(id_candidato)}
        return self.query(theQuery)

    def getMayorNotaPorCurso(self):
        query1={
                "$group": {
                    "_id": "$candidato",
                    "max": {
                        "$max": "$nota_final"
                    },
                    "doc": {
                        "$first": "$$ROOT"
                    }
                }
            }
        pipeline=  [query1]
        return self.queryAggregation(pipeline)
    def promedioNotasEnCandidato(self,id_candidato):
        query1 = {
          "$match": {"candidato.$id": ObjectId(id_candidato)}
        }
        query2 = {
          "$group": {
            "_id": "$candidato",
            "promedio": {
              "$avg": "$nota_final"
            }
          }
        }
        pipeline = [query1,query2]
        return self.queryAggregation(pipeline)