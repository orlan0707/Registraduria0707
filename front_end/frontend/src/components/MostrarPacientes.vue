<template>

    <table border="1px solid black" class="table" >
      <thead class="table-">
          <tr>
              <th scope="row">ID</th>
              <th scope="row">Nombres</th>
              <th scope="row">Apellidos</th>
              <th scope="row">Teléfono</th>
              <th scope="row">Género</th>
              <th scope="row">Dirección</th>
              <th scope="row">Ciudad</th>
              <th scope="row">Nacimiento</th>
              <th scope="row">Latitud</th>            
              <th scope="row">Longitud</th>
          </tr>
          
        <tr v-for="paciente in pacientes" :key="paciente.id">
          <th scope="row">{{paciente.id}}</th>
          <td>{{paciente.nombre}}</td>
          <td>{{paciente.apellido}}</td>
          <td>{{paciente.numTelefono}}</td>
          <td>{{paciente.genero}}</td>
          <td>{{paciente.direccion}}</td>
          <td>{{paciente.ciudad}}</td>
          <td>{{paciente.fechaNacimiento}}</td>
          <td>{{paciente.latitud}}</td>
          <td>{{paciente.longitud}}</td>
        </tr>
      </thead>
      <tbody>


      </tbody>
    </table>
  
  </template>
  
  <script>
  import axios from "axios";
  export default {
    name: "MostrarPacientes",
    data: function() {
      return {
        pacientes: []
      }
    },
    methods: {
      obtenerPacientes: function () {
        axios.get("https://hathapp.herokuapp.com/pacientetodos/", { 
          headers: {},
          }).then((result) => {
            this.pacientes = result.data;
          });
      },
    },
  
    created: function() {
      this.obtenerPacientes();
    },
  };
  </script>  

  <style>
    table {
     
      text-align: justify;
      padding: 20;
      border-style:double;
      border-color: black;
      border-radius: 0%;
      background-color: rgba(222, 221, 224, 0.758);
   
     
    }

    
    body {
     

    }
  </style>