<template>
  
  <div>
    <h1 align="left">Registro de Medico:</h1>
    <img align="center" alt="Vue logo" src="../assets/prrsentacion.jpg">
  </div>
  <form    
    v-on:submit.prevent="registrarPaciente"
    style="width: 250px; margin:left;"
    class="row g-3 needs-validation"
  >
  <div align="left" style="margin-bottom: 100px">
    <div class="col-md-12">
      <label for="validationCustomCC" class="form-label">Ingrese Cedula Medico  </label>
      <input
        type="number"
        class="form-control"
        id="validationCustomCC"
        aria-describedby="inputGroupPrepend"
        v-model="paciente.id"
        required
      />
      <div class="valid-feedback"> . </div>

    </div>
    <div class="col-md-6">
      <label  for="validationCustom01" class="form-label">Nombre Medico   </label>
      <input
        type="text"
        class="form-control"
        id="validationCustom01"
        v-model="paciente.nombre"
        required
      />
      <div class="valid-feedback"> . </div>
    </div>
    <div class="col-md-6">
      <label for="validationCustom02" class="form-label">Apellidos  </label>
      <input
        type="text"
        class="form-control"
        id="validationCustom02"
        v-model="paciente.apellido"
        required
      />
      <div class="valid-feedback"> . </div>
    </div>

    <div class="col-md-6">
      <label for="validationCustom03" class="form-label">Teléfono   </label>
      <input
        type="number"
        class="form-control"
        id="validationCustom03"
        v-model="paciente.numTelefono"
        required
      />
      <div class="valid-feedback"> . </div>
    </div>
    <div class="col-md-6">
      <label for="validationCustom04" class="form-label">Género   </label>
      <select
        class="form-select"
        id="validationCustom04"
        v-model="paciente.genero"
        required
      >
        <option selected disabled value="">Seleccionar   </option>
        <option>Femenino</option>
        <option>Masculino</option>
      </select>
      <div class="invalid-feedback">Selecciona un genero por favor    </div>
      <div class="valid-feedback"> . </div>
    </div>
    <div class="col-md-12">
      <label for="validationCustom05" class="form-label">Especialidad   </label>
      <input
        type="text"
        class="form-control"
        id="validationCustom05"
        v-model="paciente.direccion"
        required
      />
      <div class="valid-feedback"> . </div>
    </div>
    <div class="col-md-6">
      <label for="validationCustom06" class="form-label">Registro   </label>
      <input
        type="text"
        class="form-control"
        id="validationCustom06"
        v-model="paciente.ciudad"
        required
      />
      
    </div>
    <div class="valid-feedback"> . </div>
    <div class="col-12">
      <button class="btn btn-primary" type="submit">Registrar   </button>
    </div>
  </div>
  </form>
</template>

<script>
import axios from "axios";

export default {
  name: "RegistrarPaciente",
  data: function () {
    return {
      paciente: {
        id: "",
        nombre: "",
        apellido: "",
        numTelefono: "",
        genero: "",
        direccion: "",
        ciudad: "",
        fechaNacimiento: null,
        latitud: "",
        longitud: "",
      },
    };
  },
  methods: {
    registrarPaciente: function () {
      //this.paciente.fechaNacimiento = this.paciente.fechaNacimiento + 'T00:00'
      axios
        .post("https://hathapp.herokuapp.com/pacientetodos/", this.paciente, {
          headeres: {},
        })
        .then((result) => {
          console.log("Paciente agregado");
          console.log(result);
          
          alert("Paciente creado exitosamente.");

        }).catch((error) => {
          console.log(error);

          alert("Paciente no creado.");
        });
    },
  },
};
</script>
  