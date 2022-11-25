<template>
  <nav>
    <router-link to="/">Inicio</router-link> |
    <router-link to="/about">Registrate como Paciente</router-link>|
    <router-link to="/mostrarPacientes">Todos los Pacientes</router-link>|
    <router-link to="/medico">Medico</router-link>|
    <router-link to="/familiarDesignado">Familiares designado</router-link>
  </nav>
  <router-view/>
</template>

<style>



#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: rgb(41, 5, 247)
}

nav {
  padding: 20px;
}

nav a {
  font-weight: bold;
  color: #1e50c5;
}

nav a.router-link-exact-active {
  color: #1e50c5;
}


</style>
