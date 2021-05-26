'use strict'

/** @type {typeof import('@adonisjs/lucid/src/Lucid/Model')} */
const Model = use('Model')

class Mascota extends Model {
    static get table() { return 'mascotas' }
}

module.exports = Mascota
