'use strict'

/** @type {import('@adonisjs/lucid/src/Schema')} */
const Schema = use('Schema')

class MascotasSchema extends Schema {
  up () {
    this.create('mascotas', (table) => {
      table.increments()
      table.string('nombre', 80)
      table.string('edad', 254)
      table.timestamps()
    })
  }

  down () {
    this.drop('mascotas')
  }
}

module.exports = MascotasSchema
