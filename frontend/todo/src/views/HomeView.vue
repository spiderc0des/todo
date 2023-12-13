<template>
  <div class="home">
    <h1 class="title">ToDo App</h1>
    <div class="columns">
      <div class="column is-3 is-offset-3">
        <form v-on:submit.prevent="addTask">
          <div class="field">
            <div class="control">
              <input type="text" placeholder="Add new task" v-model="description">
            </div>
          </div>
          <div class="button-container">
            <button>Submit</button>
          </div>
        </form>
      </div>
    </div>
    <div class="columns">
      <div class="column is-6">
        <h2 class="subtitle">ToDo</h2>
        <div class="todo">
          <div class="card" v-for="task in todoTasks" :key="task.id">
            <div class="card-content"><li class="todo-li"> {{ task.description }} {{ task.time }} <i class="fas fa-edit" @click="edit(task.id, description)"></i></li></div>
            <footer class="card-footer">
              <button class="card-footer-item" @click="setStatus(task.id, 'done')">Done</button>
            </footer>
          </div>
        </div>
      </div>
      <div class="column is-6">
        <h2 class="subtitle">Completed</h2>
        <div class="done">
          <div class="card" v-for="task in doneTasks" :key="task.id">
            <div class="card-content"><li> {{ task.description }} {{ task.time }} <i class="fas fa-trash" @click="delet(task.id)"></i></li></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

// change the api value to ip:port on which the backend is running
const api = 'http://127.0.0.1:8000/'
export default {
  name: 'HomeView',
  data () {
    return {
      tasks: [],
      description: '',
      status: 'todo',
      time: ''
    }
  },
  computed: {
    todoTasks () {
      var todo = this.tasks.filter(task => task.status === 'todo')
      return todo
    },
    doneTasks () {
      return this.tasks.filter(task => task.status === 'done')
    }
  },
  mounted () {
    this.getTasks()
  },
  methods: {
    getTasks () {
      axios({
        method: 'get',
        url: api
      }).then(response => { this.tasks = response.data })
    },
    addTask () {
      if (this.description) {
        axios({
          method: 'post',
          url: api,
          data: {
            description: this.description,
            status: this.status
          }
        }).then((response) => {
          const newTask = {
            id: response.data.id,
            description: this.description,
            status: this.status
          }

          this.tasks.push(newTask)

          this.description = ''
          this.status = 'todo'
        }).catch((error) => {
          console.log(error)
        })
      }
    },
    setStatus (taskId, status) {
      const task = this.tasks.filter(task => task.id === taskId)[0]
      const description = task.description
      axios({
        method: 'put',
        url: `${api}/${taskId}/update/`,
        headers: {
          'Content-Type': 'application/json'
        },
        data: {
          status: status,
          description: description
        }
      }).then(() => {
        task.status = 'done'
      })
    },
    edit (taskId, description) {
      axios({
        method: 'put',
        url: `${api}/${taskId}/update/`,
        headers: {
          'Content-Type': 'application/json'
        },
        data: {
          description: description
        }
      }).then((response) => {
        this.getTasks()
      })
    },
    delet (taskId) {
      axios({
        method: 'delete',
        url: `${api}/${taskId}/delete/`,
        headers: {
          'Content-Type': 'application/json'
        }
      }).then(response => {
        this.getTasks()
      })
    }
  }
}

</script>

<style lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Red+Hat+Display:wght@300&family=Ubuntu:ital,wght@0,300;0,400;0,500;0,700;1,300;1,400;1,700&display=swap');
* {
  box-sizing: border-box;
  font-family: Ubuntu;
}
.select, select {
  width: 100%;
}
.card {
  margin-bottom: 20px;
}
.done {
  opacity: 0.3;
}

li {
  list-style-type: disc;
}

.todo-li {
  list-style: circle;
}

.fas {
  float: right;
}

 body {
  background-color: #38404B;
  min-height: 100vh;
  padding: 120px;
  padding-top: 0;
 }

 .title, .subtitle {
  color: #94ADCF;
 }

 input {
  position: relative;
  padding: 20px 30px;
  width: 578px;
  height: 59px;
  color: rgba(148, 173, 207, 0.70);
  font-size: 16px;
  font-style: normal;
  font-weight: 400;
  line-height: normal;
  border-radius: 16px;
  background: #38404B;
  box-shadow: 3px 3px 8px 0px rgba(46, 53, 62, 0.90) inset, -3px -3px 6px 0px rgba(66, 75, 88, 0.90) inset, 3px -3px 6px 0px rgba(46, 53, 62, 0.20) inset, -3px 3px 6px 0px rgba(46, 53, 62, 0.20) inset, -1px -1px 2px 0px rgba(46, 53, 62, 0.50), 1px 1px 2px 0px rgba(66, 75, 88, 0.30);
 }

 input::placeholder {
  color: rgba(148, 173, 207, 0.70);
  font-family: Ubuntu;
  font-size: 16px;
  font-style: normal;
  font-weight: 400;
  line-height: normal;
 }

 input:focus {
  border: 1px solid rgba(148, 173, 207, 0.70);
  outline: rgba(148, 173, 207, 0.70);

 }

 h2 {
  position: relative;
  color: #94ADCF;
  font-family: Ubuntu;
  font-size: 28px;
  font-style: normal;
  font-weight: 400;
  line-height: normal;
 }

 h1 {
  position: relative;
  color: #94ADCF;
  font-family: Ubuntu;
  font-size: 28px;
  font-style: normal;
  font-weight: 400;
  line-height: normal;
 }

 .button-container {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 578px;
 }

 button {
  background-color: #94ADCF;
  color: #38404B;
  width: 100px;
  height: 30px;
  font-family: Ubuntu;
  font-size: 20px;
  font-style: normal;
  font-weight: 400;
  line-height: normal;
  border-radius: 8px;
 }

 .card {
  width: 500px;
  color: #94ADCF;
  background-color: transparent;
  box-shadow: 3px 3px 8px 0px rgba(46, 53, 62, 0.90) inset, -3px -3px 6px 0px rgba(66, 75, 88, 0.90) inset, 3px -3px 6px 0px rgba(46, 53, 62, 0.20) inset, -3px 3px 6px 0px rgba(46, 53, 62, 0.20) inset, -1px -1px 2px 0px rgba(46, 53, 62, 0.50), 1px 1px 2px 0px rgba(66, 75, 88, 0.30);
  border: 1px solid rgba(148, 173, 207, 0.70);
  outline: rgba(148, 173, 207, 0.70);

 }

 i {
  opacity: 0.5;
 }

 i:hover {
  opacity: 1 ;
 }
</style>
