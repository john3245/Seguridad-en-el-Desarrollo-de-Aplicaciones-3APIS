'use strict'
const Mascota = use('App/Models/Mascota')

class MascotaController {


    async register({ response, request }) {
        const pet = new Mascota()
        const {nombre,edad} = request.all()

        pet.nombre = nombre
        pet.edad = edad
        

        await pet.save()
        return response.status(201).send({ message: "La mascota se registro con exito" })
    }

    async all({ response }) {
        const data = await Mascota.all()

        return response.status(200).json(data)
    }
}

module.exports = MascotaController
