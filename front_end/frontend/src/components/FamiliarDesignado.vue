<template>
    <table align="left">
      <h1>Familiar Designado</h1>
      <tr>
        <th scope="col">ID</th>
        <th scope="col">NOMBRE FAMILIAR</th>
        <th scope="col">APELLIDO</th>
      </tr>
      <tr>
        <td>
          <input type="text" id="id" name="id" v-model="id">
        </td>
        <td>
          <input type="text" id="Nombre Familiar" name="Nombre Familiar" v-model="nombre">
        </td>
        <td>
          <input type="text" id="direccion" name="direccion" v-model="direccion">
        </td>  
      </tr>
      <tr>
        <button v-on:click="registrar()">CREAR</button>
      </tr>
      <br><br><br>
      <tr>
        <th scope="col">ID</th>
        <th scope="col">NOMBRE FAMILIAR</th>
        <th scope="col">DIRECCION</th>
      </tr>
      <tr v-for="i in Lista">
        <td>{{ i.id}}</td> 
        <td>{{ i.nombre}}</td> 
        <td>{{ i.direccion}}</td> 
      </tr>
    </table>    
  </template>
  