const express = require('express')

const test = require('./test.json')

const app = express()

app.get('/ginias', (req, res) => {
    res.send(test)
})

app.get('/ginias/write/:send', (req, res) => {
    res.send('Message is : ' + req.params.send)
})

app.listen(8000, () => console.log('server running...'))
